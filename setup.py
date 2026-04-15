from setuptools import setup

# https://packaging.python.org/distributing/#packaging-your-project

def readme():
    with open('README.rst') as f:
        return f.read()
setup(
    name = 'novaterm-apt-repo',
    version = '0.5',
    license='Apache License 2.0',
    description = 'Script to create NovaTerm apt repositories',
    long_description = readme(),
    author = 'Fredrik Fornwall',
    author_email = 'fredrik@fornwall.net',
    url = 'https://github.com/novaterm/novaterm-apt-repo',
    scripts = ['novaterm-apt-repo'],
    classifiers = (
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3'
    )
)
