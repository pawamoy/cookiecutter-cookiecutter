import os
import shutil

from jinja2 import Environment, FileSystemLoader


def get_context():
    """As hooks are executed rendered, it will return a context dict."""
    context = {"cookiecutter": {
    {%- for key, value in cookiecutter.items()|sort %}
        "{{ key }}": {{ "{0!r}".format(value) }},
    {% endfor -%}
    } }
    return context


TRUE_VALUES = (True, 'true', 'yes', '1', 1)
CONTEXT = get_context()
META = CONTEXT['cookiecutter'].get('_meta', False) in TRUE_VALUES
TEMPLATE_DIR = '{% raw %}{{cookiecutter.repository_name}}{% endraw %}'


def render_license():
    """Render the selected license in the LICENSE file."""
    target_file = 'LICENSE'
    source_template = '{{ cookiecutter.copyright_license }}'.replace(
        '"', '').replace("'", '').replace('/', '-').replace(' ', '_')
    env = Environment(loader=FileSystemLoader('licenses'),
                      keep_trailing_newline=True)
    template = env.get_template(source_template)
    rendered = template.render(CONTEXT)
    with open(target_file, 'w') as write_stream:
        write_stream.write(rendered)
    shutil.rmtree('licenses')


def do_meta_generation():
    """Make a copy of the template directory inside itself."""
    shutil.copytree(TEMPLATE_DIR, os.path.join(TEMPLATE_DIR, TEMPLATE_DIR))


def remove_meta_content():
    """Remove hooks directory as well as cookiecutter.json."""
    try:
        shutil.rmtree(os.path.join(TEMPLATE_DIR, 'hooks'))
        os.remove(os.path.join(TEMPLATE_DIR, 'cookiecutter.json'))
    except FileNotFoundError:
        pass


def print_context():
    """Simply print the context in a pretty manner."""
    print("""
    You have succesfully created `{{ cookiecutter.repository_name }}`
    with these cookiecutter parameters:

    {% for key, value in cookiecutter.items()|sort %}
      {{ "{0:28}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
    {%- endfor %}
    """)


if META:
    do_meta_generation()
else:
    remove_meta_content()

render_license()
print_context()
