import contextlib
import datetime
import glob
import os
import re

import bs4
import click
from jinja2 import FileSystemLoader, Environment

API_DIR = os.path.abspath(__file__).replace('generate_access_methods.py', '')


@click.command(help="This generates the access_methods module.")
@click.option(
    '-p', '--path',
    help='Path to endpoint docs',
    type=click.Path(exists=True, file_okay=False))
def generate_access_methods(path):

    with work_in(path):
        all_methods = []
        docstrings = []
        with click.progressbar(glob.glob('*.rst')) as file_names:
            for file_name in file_names:
                with open(file_name) as f:
                    rows = f.readlines()

                methods = []
                internal = False
                docstring = []
                docstring = ""
                block = False
                for idx, row in enumerate(rows):
                    # Hide internal methods
                    if row.startswith('.. start-internal'):
                        internal = True
                        continue
                    if row.startswith('.. end-internal'):
                        internal = False
                        continue
                    if internal:
                        continue

                    # create methods
                    if row.startswith(('GET', 'POST', 'DELETE')):
                        method = create_method_from_row(
                            row=row,
                            path=path,
                            file_name=file_name,
                            method_count=len(methods) + 1
                        )
                        methods.append(method)
                        block = True
                        if docstring:
                            docstring = docstring.replace('\n\n', '\n')
                            docstrings.append(docstring)
                        docstring = row
                        continue

                    # Skip some formatting
                    if row.startswith(('------', '.. ebapiview')):
                        continue

                    # Only add docstrings once methods begin to be descripted
                    if block:
                        docstring += make_docstring_from_row(row)

                # Add last docstring for a file
                docstrings.append(docstring)
                # Add methods for file to the list of all methods
                all_methods += methods

    # Remove any empty docstrings
    docstrings = [x for x in docstrings if len(x.strip())]

    # Combined all_methods list and docstrings list into tuple pairs
    contents = zip(all_methods, docstrings)

    with open("access_methods.py", 'w') as f:
        data = {"now": datetime.datetime.now()}
        base = render_from_template(
            './jinja2', 'access_methods_base.jinja', **data)
        f.write(base)
        for method, docstring in contents:
            docstring = docstring.replace('\n\n\n', '\n')
            docstring = docstring.replace('\n\n', '\n')
            docstring = docstring.replace('\n\n        :param', '\n        :param')  # noqa
            method = method.replace("**docstring**", docstring)
            f.write('\n')
            f.write(method)


def make_docstring_from_row(row):
    docstring = row.strip()
    punctuation = ('w', '*', '.', '`', ':', "'", '(')
    if re.match(r'\w+', docstring) or docstring.startswith(punctuation):
        docstring = "        " + docstring
    # if ':param' in docstring:
    #     docstring = '\n{0}'.format(docstring)
    # if docstring.strip().endswith('.'):
    #     docstring = '{0}\n'.format(docstring)
    return '\n{0}'.format(docstring)


@contextlib.contextmanager
def work_in(dirname=None):
    '''
    Context manager version of os.chdir. When exited, returns to the working
    directory prior to entering.
    '''
    curdir = os.getcwd()
    try:
        if dirname is not None:
            os.chdir(dirname)
        yield
    finally:
        os.chdir(curdir)


def get_method_name_from_row(row):
    row = row.strip()
    if row.endswith(':id/') or row.endswith('_id/'):
        row = row.replace(':id', '')
        row = row.replace("attendees", "attendee")
        row = row.replace("categories", "category")
        row = row.replace("classes", "class")
        row = row.replace("codes", "code")
        row = row.replace("contact_lists", "contact_list")
        row = row.replace("contacts", "contact")
        row = row.replace("events", "event")
        row = row.replace("orders", "order")
        row = row.replace("organizers", "organizers")
        row = row.replace("users", "user")
        row = row.replace("webhooks", "webhook")
        row = row.replace("formats", "format")
    elements = row.split('/')
    prefix = elements[0].strip().lower()
    method_pieces = [x.strip() for x in elements[1:] if not x.startswith(':')]
    method_pieces = [x for x in method_pieces if len(x)]
    method_pieces.insert(0, prefix)

    if len(method_pieces) > 2:
        # fix stuff broken from the first pass
        method_pieces[1] = method_pieces[1].replace("events", "event")
        method_pieces[1] = method_pieces[1].replace("users", "user")

    return '_'.join(method_pieces)


def get_args_from_row(row):
    elements = row.split('/')
    return [x[1:] for x in elements[1:] if x.startswith(':')]


def get_method_path_from_row(row):
    # POST /users/:id/contact_lists/:contact_list_id/contacts/
    # /users/{0}/contact_lists/{1}/contacts/
    elements = row.split(' ')[1]
    method_path_list = []
    argument_count = 0
    for element in [x for x in elements.split('/') if len(x)]:
        if element.startswith(':'):
            method_path_list.append('{%s}/' % argument_count)
            argument_count += 1
        else:
            method_path_list.append('{0}'.format(element.replace('\n', '')))
    return "/" + os.path.join(*method_path_list)


def get_params_from_page(path, file_name, method_count):
    """ This function accesses the rendered content.
        We must do this because how the params are not defined in the docs,
            but rather the rendered HTML
    """
    # open the rendered file.
    file_name = file_name.replace(".rst", "")
    file_path = "{0}/../_build/html/endpoints/{1}/index.html".format(
        path, file_name)
    soup = bs4.BeautifulSoup(open(file_path))

    # Pull out the relevant section
    section = soup.find_all('div', class_='section')[method_count]

    # get the tbody of the params table
    tbody = section.find('tbody')
    params = []
    if tbody is not None:
        for row in tbody.find_all('tr'):
            name, param_type, required, description = row.find_all('td')
            required = required.text == 'Yes'
            param = dict(
                name=name.text,
                type=param_type.text,
                required=required,
                description=description.text
            )
            params.append(param)
    params = sorted(params, key=lambda k: not k['required'])
    return params


def create_method_from_row(row, path, file_name, method_count):
    # POST /users/:id/contact_lists/:contact_list_id/contacts
    # params = get_params_from_page(path, file_name, method_count)
    data = {
        'method_name': get_method_name_from_row(row),
        'arguments': get_args_from_row(row),
        'method_type': row.split(' ')[0].lower().strip(),
        'method_path': get_method_path_from_row(row),
        'params': []  # params
    }
    return render_from_template('./jinja2', 'access_methods.jinja', **data)


def render_from_template(directory, template_name, **kwargs):
    with work_in(API_DIR):
        loader = FileSystemLoader(directory)
        env = Environment(loader=loader)
        template = env.get_template(template_name)
    return template.render(**kwargs)


if __name__ == '__main__':
    generate_access_methods()
