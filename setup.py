#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__dir__ = os.path.dirname(__file__)


def read_requirements(filename):
    """
    Parse a requirements file.

    It doesn't support any vcs+ dependency.

    :return: list of str for each package
    """
    data = []
    filename = os.path.join(__dir__, filename)
    with open(filename) as requirements:
        required = requirements.read().splitlines()
        for line in required:
            if not line or line.startswith('#') or line.__contains__('#egg='):
                continue
            data.append(line)

    return data


def get_version(*file_paths):
    """Retrieves the version from openhub_django/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("openhub_django", "__init__.py")


if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
required = read_requirements('requirements.txt')
test_required = read_requirements('requirements_test.txt')

if __name__ == '__main__':
    setup(
        name='openhub-django',
        version=version,
        description="""Integrate openhub APIs with Django""",
        long_description=readme + '\n\n' + history,
        author='Shrikrishna Singh',
        author_email='krishnasingh.ss30@gmail.com',
        url='https://github.com/sks444/openhub-django',
        packages=[
            'openhub_django',
        ],
        include_package_data=True,
        install_requires=required,
        tests_require=test_required,
        license="MIT",
        zip_safe=False,
        keywords='openhub-django',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Framework :: Django :: 1.11',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
    )
