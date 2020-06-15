"""Setup file for netbox-tunnels plugin.

(c) 2020 Justin Drew
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = ""

if os.path.exists("README.md"):
    with open("README.md", "r") as f:
        README = f.read()

setup(
    name="netbox-tunnels-plugin",
    version="0.3.6",
    description="A plugin for NetBox to support documentation of network tunneling protocols, ie IPsec, GRE, L2TP, etc.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jdrew82/netbox-tunnels-plugin",
    author="Justin Drew",
    license="Apache v2.0",
    package_data={"": ["LICENSE"],},
    install_requires=[],
    min_version="2.8.3",
    packages=find_packages(),
    include_package_data=True,
)
