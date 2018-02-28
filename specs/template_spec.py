# -*- coding: utf-8 -*-
import sys
import os
import filecmp
import re
from expects import *
from testfixtures import TempDirectory
from cookiecutter.config import get_config
from datetime import datetime

modules = [
    os.path.dirname(__file__),
    os.path.dirname(__file__) + '/support'
]
for module in modules:
    if module not in sys.path:
        sys.path.append(module)

from support.runner import Runner
from support.settings import SettingObject


def check_template_variables(subject, vars):
    """
    check a given subject contains some template variables
    :param subject: the subject to be checked for the presence of
                    template variables
    :param vars: list of template variables to look for in subject
    """
    for var in vars:
        expect(subject).to(match(r'\{\{cookiecutter\.' + var + '\}\}'))

# defaults
MAIN_DIR = os.path.realpath(os.path.dirname(__file__) + '/..')
DEFAULT_PROJECT = 'Dummy Project'
DEFAULT_PROJECT_DIR = 'dummy-project'


with description('Cookiecutter Template'):
    with after.all:
        TempDirectory.cleanup_all()

    with before.each:
        self.tempdir = TempDirectory()
        self.output_dir = self.tempdir.path
        self.project_dir = self.output_dir + '/' + DEFAULT_PROJECT_DIR
        self.settings = SettingObject(
            {"project_name": DEFAULT_PROJECT}, self.output_dir)
        self.runner = Runner(self.settings)

    with after.each:
        self.tempdir.cleanup()

    with context('file content'):

        with it('fills the LICENSE file with the year, the full name and the email address'):
            config = get_config(SettingObject.CONFIG_FILE)
            self.runner.run()
            f = open(self.project_dir + '/LICENSE', 'r')
            actual = f.read()

            expect(actual).to(contain(config['default_context']['author_fullname']))
            expect(actual).to(contain(datetime.now().strftime("%Y")))

        with it('fills the README.md project name, project description, project directory name and author username'):
            config = get_config(SettingObject.CONFIG_FILE)
            expected_description = 'My dummy project short description'
            self.settings.extra_context["project_description"] = expected_description
            self.runner.run()
            f = open(self.project_dir + '/README.md', 'r')
            actual = f.read()

            expect(actual).to(contain(DEFAULT_PROJECT))
            expect(actual).to(contain(DEFAULT_PROJECT_DIR))
            expect(actual).to(contain(expected_description))
            expect(actual).to(
                contain(config['default_context']['author_username'])
            )

    with context('existing files and directories'):
        with it('creates a CHANGELOG.md file'):
            expected = self.project_dir + "/CHANGELOG.md"
            self.runner.run()

            expect(os.path.exists(expected)).to(be_true)

        with it('creates the main cookiecutter.json file without rendering'):
            expected = "\"repository_name\": \"{{ cookiecutter.project_name.lower().replace('_', '-').replace(' ', '-') }}\","
            self.runner.run()
            f = open(self.project_dir + '/cookiecutter.json', 'r')

            expect(f.read()).to(contain(expected))

        with it('creates the main {{cookiecutter.repository_name}} directory without rendering'):
            expected = self.project_dir + "/{{cookiecutter.repository_name}}"
            self.runner.run()

            expect(os.path.exists(expected)).to(be_true)

        with context('the post hook should be available in the generated template'):

            with it('copies the hook file'):
                source = (MAIN_DIR + "/hooks/post_gen_project.py")
                expected = self.project_dir + "/hooks/post_gen_project.py"
                self.runner.run()

                expect(os.path.exists(expected)).to(be_true)

            with it('reverts template expansion'):
                self.runner.run()
                f = open(self.project_dir + "/hooks/post_gen_project.py", 'r')
                actual = f.read()

                expect(actual).not_to(contain(DEFAULT_PROJECT))
                expect(actual).not_to(contain(DEFAULT_PROJECT_DIR))

            with it('reverts template expansion even for one word project name in lower case '):
                lc_project_name = 'dummy'
                project_dir = self.project_dir[0:self.project_dir.rfind('-')]
                self.settings.extra_context['project_name'] = lc_project_name
                self.runner.run()
                f = open(project_dir + "/hooks/post_gen_project.py", 'r')
                actual = f.read()

                expect(actual).not_to(contain(lc_project_name))
                expect(actual).not_to(contain(DEFAULT_PROJECT_DIR))
