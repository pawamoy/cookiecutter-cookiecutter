# {{ cookiecutter.project_name }}

<!-- badge list -->
{{ cookiecutter.project_description }}

<!-- logo -->

- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Features](#features)
- [License {{ cookiecutter.copyright_license }}](LICENSE)
- [Requirements](#requirements)
- [Usage](#usage)
- [Credits](#credits)

## Features
- All licenses from [choosealicense.com](https://choosealicense.com/appendix/)

## Requirements
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/)
- [cookiecutter](https://github.com/audreyr/cookiecutter)

## Usage
```shell-session
cookiecutter {% if cookiecutter.repository_provider == 'github.com' %}gh:{% elif cookiecutter.repository_provider == 'gitlab.com' %}gl:{% elif cookiecutter.repository_provider == 'bitbucket.org' %}bb:{% else %}https://{{ cookiecutter.repository_provider }}/{% endif %}{{ cookiecutter.repository_namespace }}/{{ cookiecutter.repository_name }}
```

{% if cookiecutter._meta|default(False) -%}
If you want to create a generator of cookiecutter-generators (so meta),
pass `_meta=true`
option on the command line:

```shell-session
cookiecutter {% if cookiecutter.repository_provider == 'github.com' %}gh:{% elif cookiecutter.repository_provider == 'gitlab.com' %}gl:{% elif cookiecutter.repository_provider == 'bitbucket.org' %}bb:{% else %}https://{{ cookiecutter.repository_provider }}/{% endif %}{{ cookiecutter.repository_namespace }}/{{ cookiecutter.repository_name }} _meta=true
```

Any *"true-ish"* value (true, yes, 1) will *enable* the meta generation.

Linux users, to ease your development of a [double-]meta-cookiecutter, let me
remind you that you can use hardlinks instead of distinct copies. To set this
up, use the following shell snippet:

```bash
cd '{% raw %}{{cookiecutter.repository_name}}/{{cookiecutter.repository_name}}{% endraw %}'
rm -rf *
for file_or_dir in ../*; do
  ln "${file_or_dir}" . 2>/dev/null || ln -s "${file_or_dir}" .
done

# avoid recursive copy error by cookiecutter
rm '{% raw %}{{cookiecutter.repository_name}}{% endraw %}'
```

Once your cookiecutter is generated, you should of course update the README
and cookiecutter parameters (in `cookiecutter.json`) accordingly, as well as
add, delete or modify contents in the `{% raw %}{{cookiecutter.repository_name}}{% endraw %}`
directory.
{%- endif %}

## Credits
This cookiecutter was created with [cookiecutter-cookiecutter](https://github.com/Pawamoy/cookiecutter-cookiecutter).
