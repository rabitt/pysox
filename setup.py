""" Setup script for sox. """
from setuptools import setup



with open("README.md") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name='sox',
        description='Python wrapper around SoX.',
        author='Rachel Bittner',
        author_email='rachel.bittner@nyu.edu',
        url='https://github.com/rabitt/pysox',
        download_url='https://github.com/rabitt/pysox/releases',
        packages=['sox'],
        package_data={'sox': []},
        long_description=long_description,
        long_description_content_type="text/markdown",
        keywords='audio effects SoX',
        license='BSD-3-Clause',
        install_requires=[
            'numpy >= 1.9.0',
            'typing-extensions >=  3.7.4.2 '
        ],
        extras_require={
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'soundfile >= 0.11.0',
            ],
            'docs': [
                'sphinx==1.2.3',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
        }
    )
