from setuptools import setup
from os import path

# Read the content of the README.md file as long_description
root_directory = path.abspath(path.dirname(__file__))
with open(path.join(root_directory, 'README.md'), encoding='utf-8') as readme_file:
    readme_content = readme_file.read()

# Package Definition
setup(
    name='lightgallery',
    version='0.5',
    author='Gauthier Provost',
    author_email='gauthier@kobol.io',
    description='Markdown extension to wrap images in lightbox/lightgallery',
    long_description=readme_content,
    long_description_content_type='text/markdown; charset=UTF-8; variant=GFM',
    py_modules=['lightgallery'],
    install_requires = ['markdown>=3.0'],
    classifiers=['Topic :: Text Processing :: Markup :: HTML'],
    license='MIT License',
    url='https://github.com/g-provost/lightgallery-markdown',
    project_urls={
        'Source': 'https://github.com/g-provost/lightgallery-markdown',
        'Documentation': 'https://github.com/g-provost/lightgallery-markdown',
        'Tracker': 'https://github.com/g-provost/lightgallery-markdown/issues'
    }
)
