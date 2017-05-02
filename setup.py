from setuptools import find_packages
from setuptools import setup


setup(
    name='jinja2_precommit_hook',
    description='Some out-of-the-box hooks for pre-commit.',
    url='https://github.com/arehmandev/jinja2-lint/pre-commit-hooks',
    version='1.0',

    author='Abdul Rehman',
    author_email='arehmandev@outlook.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    entry_points={
        'console_scripts': [
            'j2_lint_test = pre_commit_hooks.j2_lint_test:j2_lint_test',
        ],
    },
)
