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


def render_template(source, target):
    """Utility function to render a source template in a target file."""
    env = Environment(loader=FileSystemLoader('.'), keep_trailing_newline=True)
    template = env.get_template(source)
    context = get_context()
    rendered = template.render(context)
    with open(target, 'w') as stream:
        stream.write(rendered)


def render_license():
    """Render the selected license in the LICENSE file."""
    target = 'LICENSE'
    source = os.path.join(
        'licenses',
        '{{ cookiecutter.copyright_license }}'
            .replace('"', '')
            .replace("'", '')
            .replace('/', '-')
            .replace(' ', '_'))

    render_template(source, target)
    shutil.rmtree('licenses')


def render_subreadme():
    """Run a rendering pass on the sub-README to include credits."""
    template_dir = '{% raw %}{{cookiecutter.repository_name}}{% endraw %}'
    source = os.path.join(template_dir, 'README.md')
    target = source
    render_template(source, target)


render_license()
render_subreadme()
