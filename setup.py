from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='confile',
    version='1.2',
    url='https://github.com/777nancy/confile',
    author='777nancy',
    author_email='ys.5.mil.7@gmail.com',
    description='confile: config file reader',
    packages=find_packages(),
    install_requires=[
        "PyYAML >= 5.3.1"
    ],
    license='MIT License',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    python_requires='>=3.6',
)
