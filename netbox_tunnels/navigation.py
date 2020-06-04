"""Plugin additions to the NetBox navigation menu.

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

from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link="plugins:netbox_tunnels:tunnels_list",
        link_text="Tunnels",
        permissions=["netbox_tunnels.view_tunnels"],
        buttons=(
            # Link to the plugins view to add a tunnel if user has "add_tunnels" permission.
            PluginMenuButton(
                link="plugins:netbox_tunnels:tunnel_creation",
                title="Add a new tunnel",
                icon_class="fa fa-plus",
                color=ButtonColorChoices.GREEN,
                permissions=["netbox_tunnels.add_tunnels"],
            ),
            # Links to the plugins view to bulk import tunnels if user has the "add_tunnels" permission.
            PluginMenuButton(
                link="plugins:netbox_tunnels:tunnels_import",
                title="Bulk import tunnels",
                icon_class="fa fa-download",
                color=ButtonColorChoices.BLUE,
                permissions=["netbox_tunnels.add_tunnels"],
            ),
        ),
    ),
)
