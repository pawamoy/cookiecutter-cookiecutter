# Cookiecutter-Cookiecutter

<!-- badge list -->
The cookiecutter that generated itself.

<!-- logo -->

- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Features](#features)
- [License ISC License](LICENSE)
- [Requirements](#requirements)
- [Usage](#usage)
- [Credits](#credits)

## Features
- All licenses from [choosealicense.com](https://choosealicense.com/appendix/)
- Standard fields that every open source project uses:
  - project name
  - project description
  - author full name
  - author email
  - author username (on given provider)
  - repository provider (github/gitlab/bitbucket)
  - repository namespace (user/organization/group)
  - repository name
  - package use name (when using in code)
  - package installation name (when installing through package manager)
  - package cli name (when using on the command line)
  - copyright holder
  - copyright holder email
  - copyright date
  - copyright license
- Only essential files:
  - changelog
  - code of conduct
  - contributing
  - readme

## Requirements
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/)
- [cookiecutter](https://github.com/audreyr/cookiecutter)

## Usage
```shell-session
cookiecutter gh:Pawamoy/cookiecutter-cookiecutter
```

If you want to create a generator of cookiecutter-generators (so meta),
pass `_meta=true` option on the command line:

```shell-session
cookiecutter gh:Pawamoy/cookiecutter-cookiecutter _meta=true
```

Any *"true-ish"* value (true, yes, 1) will *enable* the meta generation.

Linux users, to ease your development of a [double-]meta-cookiecutter, let me
remind you that you can use hardlinks instead of distinct copies. To set this
up, use the following shell snippet:

```bash
cd '{{cookiecutter.repository_name}}/{{cookiecutter.repository_name}}'
rm -rf *
for file_or_dir in ../*; do
  ln "${file_or_dir}" . 2>/dev/null || ln -s "${file_or_dir}" .
done

# avoid recursive copy error by cookiecutter
rm '{{cookiecutter.repository_name}}'
```

Once your cookiecutter is generated, you should of course update the README
and cookiecutter parameters (in `cookiecutter.json`) accordingly, as well as
add, delete or modify contents in the `{{cookiecutter.repository_name}}`
directory.

## Credits
This cookiecutter was created with [cookiecutter-cookiecutter](https://github.com/Pawamoy/cookiecutter-cookiecutter).
