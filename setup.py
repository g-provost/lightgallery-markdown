from setuptools import setup

setup(
    name='lightgallery',
    version='0.1.2',
    author='Gauthier Provost',
    author_email='gauthier@kobol.io',
    description='Markdown extension to wrap images in lightbox/lightgallery',
    py_modules=['lightgallery'],
    install_requires = ['markdown>=3.0'],
    classifiers=['Topic :: Text Processing :: Markup :: HTML'],
    license='MIT License',
)
