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
