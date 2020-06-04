"""Tables for Tunnels.

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
import django_tables2 as tables
from utilities.tables import BaseTable, ToggleColumn
from .models import Tunnel


class TunnelTable(BaseTable):
    """Table for displaying configured Tunnel instances."""

    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        """Class to define what is used for tunnl_lists.html template to show configured tunnels."""

        model = Tunnel
        fields = [
            "pk",
            "name",
            "status",
            "tunnel_type",
            "src_address",
            "dst_address",
        ]


class TunnelBulkTable(BaseTable):
    """Table for displaying Tunnel imports."""

    pk = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        """Class to define what is used for bulk import of tunnels."""

        model = Tunnel
        fields = (
            "pk",
            "name",
            "status",
            "tunnel_type",
            "src_address",
            "dst_address",
        )
