from setuptools import setup
import ast
import os
import re


def _read(fn):
    path = os.path.join(os.path.dirname(__file__), fn)

    return open(path).read()


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('flickr2markdown/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='flickr2markdown',
    version=version,
    url='https://github.com/xsteadfastx/flickr2markdown',
    license='MIT',
    author='Marvin Steadfast',
    author_email='marvin@xsteadfastx.org',
    description='A tool to get a number of flickr uploads or '
                'single pictures and create markdown strings out of them',
    long_description=_read('README.rst'),
    packages=['flickr2markdown'],
    platforms='any',
    install_requires=[
        'Click',
        'requests'
    ],
    keywords=['markdown', 'flickr'],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        'console_scripts': [
            'flickr2markdown = flickr2markdown.ui:main'
        ]
    }
)
