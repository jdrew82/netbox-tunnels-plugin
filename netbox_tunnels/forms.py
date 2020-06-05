"""Forms for tunnel creation.

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

from django import forms

from utilities.forms import BootstrapMixin
from dcim.models import Device
from extras.forms import CustomFieldModelCSVForm

from .models import Tunnel
from .choices import TunnelStatusChoices, TunnelTypeChoices

BLANK_CHOICE = (("", "---------"),)


class TunnelCreationForm(BootstrapMixin, forms.ModelForm):
    """Form for creating a new tunnel."""

    name = forms.CharField(required=True, label="Name", help_text="Name of tunnel")

    status = forms.ChoiceField(choices=BLANK_CHOICE + TunnelStatusChoices.CHOICES, required=False)

    tunnel_type = forms.ChoiceField(
        choices=TunnelTypeChoices.CHOICES,
        required=True,
        label="Tunnel type",
        help_text="Tunnel type. This must be specified.",
    )

    src_address = forms.CharField(required=True, label="Source IP address", help_text="IP address of the source device")

    dst_address = forms.CharField(required=True, label="Peer IP address", help_text="IP address of the peer device")

    psk = forms.CharField(
        required=False, label="Pre-shared Key", widget=forms.PasswordInput, help_text="Pre-shared key"
    )

    class Meta:
        """Class to define what is used to create a new network tunnel."""

        model = Tunnel
        fields = [
            "name",
            "status",
            "tunnel_type",
            "src_address",
            "dst_address",
            "psk",
        ]


class TunnelFilterForm(BootstrapMixin, forms.ModelForm):
    """Form for filtering Tunnel instances."""

    device = forms.ModelChoiceField(queryset=Device.objects.all(), required=False)

    status = forms.ChoiceField(choices=BLANK_CHOICE + TunnelStatusChoices.CHOICES, required=False)

    q = forms.CharField(required=False, label="Search")

    class Meta:
        """Class to define what is used for filtering tunnels with the search box."""

        model = Tunnel
        fields = [
            "src_address",
            "dst_address",
            "psk",
            "tunnel_type",
        ]


class TunnelCreationCSVForm(CustomFieldModelCSVForm):
    """Form for entering CSV to bulk-import Tunnel entries."""

    src_address = forms.CharField(required=True, help_text="IP Address of the source device")
    dst_address = forms.CharField(required=True, help_text="IP Address of the peer device")
    tunnel_type = forms.CharField(required=True, help_text="Specified tunnel type.")
    psk = forms.CharField(required=True, help_text="Pre-shared key")

    class Meta:
        """Class to define what is used for bulk import of tunnels form using CSV."""

        model = Tunnel
        fields = Tunnel.csv_headers

    def save(self, commit=True, **kwargs):
        """Save the model, and add it and the associated PSK."""
        model = super().save(commit=commit, **kwargs)
        # if commit:
        #     credentials = Credentials(self.data.get("psk"))
        return model
