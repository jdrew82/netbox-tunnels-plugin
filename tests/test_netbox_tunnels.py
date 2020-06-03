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
