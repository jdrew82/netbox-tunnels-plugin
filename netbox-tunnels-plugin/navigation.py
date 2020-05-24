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
        link='plugins:netbox_tunnels_plugin:list_tunnels',
        link_text='Tunnels',
        permissions=[],
        buttons=(
            # Link to the admin view to add a tunnel if user has "add_tunnels" permission.
            PluginMenuButton(
                link='admin:netbox_tunnels_plugin_tunnels_add',
                title='Add a new tunnel',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_tunnels_plugin.add_tunnels']
            ),
            # Links to the admin view to assign a tunnel to a device if user has the "add_tunnels"
            # permission.
            PluginMenuButton(
                link='admin:netbox_tunnels_plugin_tunnels_add',
                title='Assign a tunnel to a device',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.BLUE,
                permissions=['netbox_tunnels_plugin.add_tunnels']
            ),
        )
    ),
)