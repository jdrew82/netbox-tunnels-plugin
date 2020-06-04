"""Django urlpatterns declaration for netbox_tunnels plugin.

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
from django.urls import path

from .views import (
    ListTunnelView,
    CreateTunnelView,
    BulkDeleteTunnelView,
    BulkImportTunnelView,
)

urlpatterns = [
    path("", ListTunnelView.as_view(), name="tunnels_list"),
    path("add/", CreateTunnelView.as_view(), name="tunnel_creation"),
    path("delete/", BulkDeleteTunnelView.as_view(), name="tunnels_bulk_delete"),
    path("import/", BulkImportTunnelView.as_view(), name="tunnels_import"),
]
