from setuptools import setup

setup(
    name='snipsfakeweather',
    version='1.1.1.2',
    description='Fake weather forescasts skill for Snips',
    author='Michael Fester',
    author_email='michael.fester@gmail.com',
    url='https://github.com/snipsco/snips-skill-fakeweather',
    download_url='',
    license='MIT',
    install_requires=[],
    setup_requires=['green'],
    keywords=['snips'],
    packages=['snipsfakeweather'],
    package_data={'snipsfakeweather': ['Snipsspec']},
    include_package_data=True,
)
