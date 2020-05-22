from django.db import models
from ipam.models import Device
from .choices import TunnelStatusChoices


class VirtualCircuit(models.Model):
    """Tunnel model."""

    tunnel_id = models.PositiveSmallIntegerField(
        primary_key=True,
        verbose_name='ID'
    )
    name = models.CharField(
        max_length=64
    )
    status = models.CharField(
        max_length=30,
        choices=TunnelStatusChoices,
        default=TunnelStatusChoices.STATUS_PENDING_CONFIGURATION
    )
    context = models.CharField(
        max_length=100,
        blank=True
    )

    class Meta:
        ordering = ['tunnel_id']

    def __str__(self):
        return self.name


class TunnelDevice(models.Model):
    """Tunnel to Device relationship."""

    tunnel = models.ForeignKey(
        to=Tunnel,
        on_delete=models.CASCADE,
        related_name='device'
    )
    device = models.OneToOneField(
        to=Device,
        on_delete=models.CASCADE,
        related_name='device_of'
    )

    class Meta:
        ordering = ['tunnel']
