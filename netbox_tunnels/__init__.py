"""Plugin declaration for netbox_tunnels.

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

__version__ = "0.3.6"

from extras.plugins import PluginConfig


class TunnelsConfig(PluginConfig):
    """This class defines attributes for the NetBox Tunnels Plugin."""

    name = "netbox_tunnels"
    verbose_name = "Network Tunnels"
    version = __version__
    description = "Network Tunnels"
    base_url = "netbox_tunnels"
    author = "Justin Drew"
    author_email = "jdrew82@users.noreply.github.com"
    min_version = "2.8.3"
    required_settings = []
    # default_settings = {}
    # caching_config = {}


config = TunnelsConfig  # pylint:disable=invalid-name
