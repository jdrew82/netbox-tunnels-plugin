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
from django_rq import get_queue

from utilities.forms import BootstrapMixin
from dcim.models import Site, Platform, DeviceRole, DeviceType
from extras.forms import CustomFieldModelCSVForm

from .models import Tunnel
from .choices import TunnelStatusChoices
from .utils.credentials import Credentials

BLANK_CHOICE = (("", "---------"),)


class TunnelCreationForm(BootstrapMixin, forms.ModelForm):
    """Form for creating a new tunnel."""

    src_address = forms.CharField(required=True, label="Source IP address", help_text="IP address of the source device")

    dst_address = forms.CharField(required=True, label="Peer IP address", help_text="IP address of the peer device")

    psk = forms.CharField(required=True,
                                     widget=forms.PasswordInput,
                                     help_text="Pre-shared key (will not be stored in database)")

    tunnel_type = forms.ModelChoiceField(
        queryset=DeviceType.objects.all(),
        required=True,
        to_field_name="slug",
        help_text="Tunnel type. This must be specified.",
    )

    class Meta:  # noqa: D106 "Missing docstring in public nested class"
        model = OnboardingTask
        fields = [
            "src_address",
            "dst_address",
            "psk",
            "tunnel_type",
        ]

    def save(self, commit=True, **kwargs):
        """Save the model, and add it and the associated PSK."""
        model = super().save(commit=commit, **kwargs)
        if commit:
            credentials = Credentials(self.data.get("psk"))
        return model


class TunnelCreationCSVForm(CustomFieldModelCSVForm):
    """Form for entering CSV to bulk-import Tunnel entries."""

    src_address = forms.CharField(required=True, help_text="IP Address of the source device")
    dst_address = forms.CharField(required=True, help_text="IP Address of the peer device")
    psk = forms.CharField(required=True, help_text="Pre-shared key, will not be stored in database")
    tunnel_type = forms.CharField(required=True, help_text="Specified tunnel type.")

    class Meta:  # noqa: D106 "Missing docstring in public nested class"
        model = Tunnel
        fields = Tunnel.csv_headers

    def save(self, commit=True, **kwargs):
        """Save the model, and add it and the associated PSK."""
        model = super().save(commit=commit, **kwargs)
        if commit:
            credentials = Credentials(self.data.get("psk"))
        return model
