"""Tunnel Django model.

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

from django.db import models
from ipam.models import Device
from .choices import TunnelStatusChoices, TunnelTypeChoices


class Tunnel(models.Model):
    """Tunnel model."""

    tunnel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    status = models.CharField(
        max_length=30, choices=TunnelStatusChoices, default=TunnelStatusChoices.STATUS_PENDING_CONFIGURATION
    )
    tunnel_type = models.CharField(max_length=30, choices=TunnelTypeChoices, default=TunnelTypeChoices.IPSEC_TUNNEL)
    src_address = models.CharField(verbose_name="Source Address", max_length=28, blank=True)
    dst_address = models.CharField(verbose_name="Dest Address", max_length=28, blank=True)
    psk = models.CharField(verbose_name="Pre-shared Key", max_length=100, blank=True)

    csv_headers = [
        "name",
        "status",
        "tunnel_type",
        "src_address",
        "dst_address",
        "psk",
    ]

    class Meta:
        """Class to define what will be used to set order based on. Will be using the unique tunnel ID for this purpose."""

        ordering = ["tunnel_id"]

    def __str__(self):
        """Class to define what identifies the Tunnel object. Will be using name for this."""
        return self.name


class TunnelDevice(models.Model):
    """Tunnel to Device relationship."""

    tunnel = models.ForeignKey(to=Tunnel, on_delete=models.CASCADE, related_name="device")
    device = models.OneToOneField(to=Device, on_delete=models.CASCADE, related_name="device_of")

    class Meta:
        """Class to define what will be used to set order based on. Will be using the unique tunnel for this purpose."""

        ordering = ["tunnel"]
