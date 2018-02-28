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
META = CONTEXT['cookiecutter'].get('_meta', False)


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


def do_meta_generation():
    """Make a copy of the template directory inside itself."""
    dir_name = '{% raw %}{{cookiecutter.repository_name}}{% endraw %}'
    shutil.copytree(dir_name, os.path.join(dir_name, dir_name))


def print_context():
    """Simply print the context in a pretty manner."""
    print("""
    You have succesfully created `{{ cookiecutter.repository_name }}`
    with these cookiecutter parameters:

    {% for key, value in cookiecutter.items()|sort %}
      {{ "{0:28}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
    {%- endfor %}
    """)


if META in TRUE_VALUES:
    do_meta_generation()

render_license()
print_context()
