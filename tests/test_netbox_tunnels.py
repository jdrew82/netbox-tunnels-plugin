"""Tests for validating netbox_tunnels plugin.

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
from django.contrib.auth.models import User, Permission
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from dcim.models import Site

from netbox_tunnels.models import Tunnel


class ListTunnelViewTestCase(TestCase):
    """Test the ListTunnelView view."""

    def setUp(self):
        """Create a user and baseline data for testing."""
        self.user = User.objects.create(username="testuser")
        self.client = Client()
        self.client.force_login(self.user)

        self.url = reverse("plugins:netbox_tunnels:tunnels_list")

        self.site1 = Site.objects.create(name="USA", slug="usa")
        self.tunnel1 = Tunnel.objects.create(ip_address="1.1.1.1", site=self.site1)
        self.tunnel2 = Tunnel.objects.create(ip_address="2.2.2.2", site=self.site1)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_list_tunnel_anonymous(self):
        """Verify that configured Tunnels can be listed without logging in if permissions are exempted."""
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "netbox_tunnels/tunnels_list.html")

    @override_settings(EXEMPT_VIEW_PERMISSIONS=[])
    def test_list_tunnel(self):
        """Verify that configured Tunnels can be listed by a user with appropriate permissions."""
        # Attempt to access without permissions
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

        # Add permission
        self.user.user_permissions.add(
            Permission.objects.get(content_type__app_label="netbox_tunnels", codename="view_tunnels")
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "netbox_tunnels/tunnels_list.html")
