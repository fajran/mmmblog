from setuptools import setup, find_packages

setup(
    name = "mmmblog",
    version = "1.0",
    url = 'http://kambing.ui.ac.id/',
    license = 'BSD',
    description = 'Microblog',
    author = 'Fajran Iman Rusadi',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools', 'staticgenerator', 'Markdown'],
)

