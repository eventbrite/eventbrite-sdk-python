import contextlib
import datetime
import glob
import os
import re

from jinja2 import FileSystemLoader, Environment

API_DIR = os.path.abspath(__file__).replace('generate_access_methods.py', '')


def generate_access_methods(path_to_endpoint_docs):

    with work_in(path_to_endpoint_docs):
        all_methods = []
        docstrings = []
        for file_name in glob.glob('*.rst'):
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
                if row.endswith('.. end-internal'):
                    internal = False
                    continue
                if internal:
                    continue

                # create methods
                if row.startswith(('GET', 'POST', 'DELETE')):
                    methods.append(create_method_from_row(row))
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

    with open('access_methods.py', 'w') as f:
        data = {"now": datetime.datetime.now()}
        base = render_from_template('.', 'access_methods_base.jinja', **data)
        f.write(base)
        for method, docstring in contents:
            method = method.replace("**docstring**", docstring)
            f.write('\n')
            f.write(method)


def make_docstring_from_row(row):
    docstring = row.strip()
    if re.match(r"(\w|\*|\.|\`|\|\:')", docstring):
        docstring = "        " + docstring
        # docstring = "{0: >8}".format(docstring)
    return '\n' + docstring


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
    elements = row.split('/')
    prefix = elements[0].strip().lower()
    method_pieces = [x.strip() for x in elements[1:] if not x.startswith(':')]
    method_pieces = [x for x in method_pieces if len(x)]
    method_pieces.insert(0, prefix)
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


def create_method_from_row(row):
    # POST /users/:id/contact_lists/:contact_list_id/contacts/
    data = {
        'method_name': get_method_name_from_row(row),
        'arguments': get_args_from_row(row),
        'method_type': row.split(' ')[0].lower().strip(),
        'method_path': get_method_path_from_row(row),
    }
    return render_from_template('.', 'access_methods.jinja', **data)


def render_from_template(directory, template_name, **kwargs):
    with work_in(API_DIR):
        loader = FileSystemLoader(directory)
        env = Environment(loader=loader)
        template = env.get_template(template_name)
    return template.render(**kwargs)


if __name__ == '__main__':
    path = '/Users/danny/eventbrite/core/django/src/www/eventbrite/ebapi/docs/endpoints'
    generate_access_methods(path)

