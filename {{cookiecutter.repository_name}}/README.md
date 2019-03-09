# {{ cookiecutter.project_name }}

<!-- badge list -->
{{ cookiecutter.project_description }}

<!-- logo -->

- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Features](#features)
- [License: {{ cookiecutter.copyright_license }}](LICENSE)
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

## Credits
This cookiecutter was created with [cookiecutter-cookiecutter](https://github.com/pawamoy/cookiecutter-cookiecutter).
