from setuptools import setup

setup(
    name='bigacme-dummy-plugin',
    version='1.0.1',
    description="Dummy plugin for bigacme",
    url='https://github.com/magnuswatn/bigacme-dummy-plugin',
    author="Magnus Watn",
    py_modules=['bigacme_dummy_plugin'],
    include_package_data=True,
    install_requires=[
        'bigacme'
        ],
    entry_points={
        'bigacme.plugins': [
            'dummy = bigacme_dummy_plugin:DummyPlugin',
        ],
    }
)
