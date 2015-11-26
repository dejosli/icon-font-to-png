# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

# Convert description from markdown to reStructuredText
try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description = ''


# Requirements based on Python verison
if sys.version_info >= (3, 0):
    # Python 3
    install_requires = ['pillow>=3.0.0',
                        'tinycss>=0.3',
                        'six>=1.10.0']
else:
    # Python 2
    install_requires = ['pillow>=2.8.1',
                        'tinycss>=0.3',
                        'six>=1.10.0']

setup(
    name='icon_font_to_png',
    url='https://github.com/Pythonity/icon-font-to-png',
    version='0.1.3',
    license='MIT',
    author='Pythonity',
    author_email=' pythonity@pythonity.com',
    description='Python script for exporting icons from icon font '
                '(e.g. Font Awesome, Octicons) as PNG images.',
    long_description=description,
    packages=['icon_font_to_png'],
    tests_require=['tox'],
    cmdclass={'test': Tox},
    install_requires=install_requires,
    extras_require={
        'testing': ['pytest'],
    },
    scripts=['bin/font-awesome-to-png', 'bin/icon-font-to-png'],
    keywords='icon font export',
)
