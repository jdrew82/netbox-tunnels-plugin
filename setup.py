import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
readme = ""
if os.path.exists('README.md'):
    with open('README.md', 'r') as f:
        readme = f.read()

setup(
    name='netbox-tunnels-plugin',
    version='0.2.2',
    description='A plugin for NetBox to support documentation of network tunneling protocols, ie IPsec, GRE, L2TP, etc.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/jdrew82/netbox-tunnels-plugin',
    author='Justin Drew',
    license='Apache v2.0',
    package_data={
        '': ['LICENSE'],
    },
    install_requires=[],
    min_version='2.8.3',
    packages=find_packages(),
    include_package_data=True
)
