import contextlib
import glob
import os

from jinja2 import FileSystemLoader, Environment

class AccessMethodMixin(object):
    pass

API_DIR = os.path.abspath(__file__).replace('access_methods.py', '')


def generate_access_methods(path_to_endpoint_docs):

    with work_in(path_to_endpoint_docs):
        for file_name in glob.glob('*.rst'):
            with open(file_name) as f:
                rows = f.readlines()

            methods = []
            docs = []
            block = False
            internal = False
            for row in rows:

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
                    block = True
                    docstring = row
                    methods.append(create_method_from_row(row))
                    continue
                if block:
                    if row.startswith(('------', '.. ebapiview')):
                        continue
                    docstring += '\n{0}'.format(row)
            docstring = docstring.replace('\n\n', '\n')
            docs.append(docstring)

            # for doc in docs:
            #     print(doc)
            for method in methods:
                print(method)

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
    method_path = '/'
    argument_count = 0
    for element in [x for x in elements.split('/') if len(x)]:
        if element.startswith(':'):
            method_path += '{%s}/' % argument_count
            argument_count += 1
        else:
            method_path += '{0}'.format(element.replace('\n', ''))
    if not method_path.endswith("/"):
        return method_path + '/'
    return method_path


def create_method_from_row(row):
    # POST /users/:id/contact_lists/:contact_list_id/contacts/
    data = {
        'method_name': get_method_name_from_row(row),
        'arguments': get_args_from_row(row),
        'docstring': '',
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

