from setuptools import setup

setup(
    name='snipsfakeweather',
    version='0.1.3',
    description='Fake weather forescasts skill for Snips',
    author='Michael Fester',
    author_email='michael.fester@gmail.com',
    url='https://github.com/snipsco/snips-skill-fakeweather',
    download_url='',
    license='MIT',
    install_requires=['enum'],
    test_suite="tests",
    keywords=['snips'],
    packages=[
        'snipsfakeweather'
    ]
)
