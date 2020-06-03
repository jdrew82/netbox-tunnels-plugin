# Netbox Tunnels Plugin

<!-- Build status with linky to the builds for ease of access. -->
[![Build Status](https://travis-ci.com/jdrew82/netbox-tunnels-plugin.svg?token=XHesDxGFcPtaq1Q3URi5&branch=master)](https://travis-ci.com/jdrew82/netbox-tunnels-plugin)

<!-- PyPI version badge. -->
[![PyPI version](https://badge.fury.io/py/netbox-tunnels-plugin.svg)](https://badge.fury.io/py/netbox-tunnels-plugin)

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+NOTE: Please be aware that this plugin is still a work in progress and should not be used for production work at this time!+
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

A plugin for [NetBox](https://github.com/netbox-community/netbox) to support documentation of network tunneling
 protocols, ie IPsec, GRE, L2TP, etc.

## Installation

The plugin is available as a Python package in pypi and can be installed with pip
```shell
pip install netbox-tunnels-plugin
```

Once installed, the plugin needs to be enabled in your `configuration.py`
```python
# In your configuration.py
PLUGINS = ["netbox-tunnels-plugin"]

# PLUGINS_CONFIG = {
#   "netbox-tunnels-plugin": {
#     ADD YOUR SETTINGS HERE
#   }
# }
```

## Contributing

Pull requests are welcomed and automatically built and tested against multiple version of Python and multiple version of NetBox through TravisCI.

The project is packaged with a light development environment based on `docker-compose` to help with the local development of the project and to run the tests within TravisCI.

The project is following Network to Code software development guideline and is leveraging:
- Black, Pylint, Bandit and pydocstyle for Python linting and formatting.
- Django unit test to ensure the plugin is working properly.

### CLI Helper Commands

The project is coming with a CLI helper based on [invoke](http://www.pyinvoke.org/) to help setup the development environment. The commands are listed below in 3 categories `dev environment`, `utility` and `testing`. 

Each command can be executed with `invoke <command>`. All commands support the arguments `--netbox-ver` and `--python-ver` if you want to manually define the version of Python and NetBox to use. Each command also has its own help `invoke <command> --help`

#### Local dev environment
```
  build            Build all docker images.
  debug            Start NetBox and its dependencies in debug mode.
  destroy          Destroy all containers and volumes.
  start            Start NetBox and its dependencies in detached mode.
  stop             Stop NetBox and its dependencies.
```

#### Utility 
```
  cli              Launch a bash shell inside the running NetBox container.
  create-user      Create a new user in django (default: admin), will prompt for password.
  makemigrations   Run Make Migration in Django.
  nbshell          Launch a nbshell session.
```
#### Testing 

```
  tests            Run all tests for this plugin.
  pylint           Run pylint code analysis.
  pydocstyle       Run pydocstyle to validate docstring formatting adheres to NTC defined standards.
  bandit           Run bandit to validate basic static code security analysis.
  black            Run black to check that Python files adhere to its style standards.
  unittest         Run Django unit tests for the plugin.
```
