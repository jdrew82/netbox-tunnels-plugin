"""Django views for network tunnels.

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
import logging
from django.contrib.auth.mixins import PermissionRequiredMixin
from utilities.views import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

from .filters import TunnelFilter
from .forms import TunnelCreationForm, TunnelCreationCSVForm
from .models import Tunnel

log.setLevel(logging.DEBUG)


class TunnelListView(PermissionRequiredMixin, ObjectListView):
    """View for listing all Tunnels."""

    def get(self, request):
        tunnels = Tunnel.objects.all()
        return render(request, "netbox_tunnels/tunnels_list.html", {"tunnels": tunnels,})

    permission_required = "netbox_tunnels.view_tunnels"
    # queryset = Tunnels.objects.all().order_by("-id")
    filterset = TunnelFilter
    # template_name = "netbox_tunnels/tunnels_list.html"


class TunnelCreateView(PermissionRequiredMixin, ObjectEditView):
    """View for creating a new Tunnels."""

    permission_required = "netbox_tunnels.tunnels_creation"
    model = Tunnel
    queryset = Tunnel.objects.all()
    model_form = TunnelCreationForm
    template_name = "netbox_tunnels/tunnels_creation.html"
    default_return_url = "plugins:netbox_tunnels:tunnels_list"


class TunnelBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    """View for deleting one or more Tunnels."""
    
    permission_required = "netbox_tunnels.delete_tunnels"
    queryset = Tunnel.objects.filter()
    default_return_url = "plugins:netbox_tunnels:tunnels_list"

 
class TunnelFeedBulkImportView(PermissionRequiredMixin, BulkImportView):
    """View for bulk-importing a CSV file to create Tunnels."""
    
    permission_required = "netbox_tunnels.add_tunnels"
    model_form = TunnelCreationCSVForm
    default_return_url = "plugins:netbox_tunnels:tunnels_list"