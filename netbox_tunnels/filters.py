"""Filtering logic for Tunnel instances.

(c) 2020 Network To Code
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

import django_filters
from django.db.models import Q

from dcim.models import Site, DeviceRole, Platform
from utilities.filters import NameSlugSearchFilterSet

from .models import Tunnel


class TunnelFilter(NameSlugSearchFilterSet):
    """Filter capabilities for OnboardingTask instances."""

    q = django_filters.CharFilter(method="search", label="Search",)

    tunnel_id = django_filters.ModelMultipleChoiceFilter(queryset=Tunnel.objects.all(), label="Tunnel (ID)",)

    name = django_filters.ModelMultipleChoiceFilter(
        field_name="name__slug", queryset=Tunnel.objects.all(), to_field_name="slug", label="Tunnel Name (slug)",
    )

    status = django_filters.ModelMultipleChoiceFilter(
        field_name="status__slug", queryset=Tunnel.objects.all(), to_field_name="slug", label="Tunnel Status (slug)",
    )

    context = django_filters.ModelMultipleChoiceFilter(
        field_name="context__slug", queryset=Tunnel.objects.all(), to_field_name="slug", label="Tunnel Context (slug)",
    )

    class Meta:  # noqa: D106 "Missing docstring in public nested class"
        model = Tunnel
        fields = ["tunnel_id", "name", "status", "context"]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(tunnel_id__icontains=value)
            | Q(ip_address__icontains=value)
            | Q(platform__name__icontains=value)
            | Q(device__icontains=value)
            | Q(status__icontains=value)
            | Q(message__icontains=value)
        )
        return queryset.filter(qs_filter)