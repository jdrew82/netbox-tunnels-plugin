"""ChoiceSet classes for device tunnel.

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

from utilities.choices import ChoiceSet


class TunnelStatusChoices(ChoiceSet):
    """List of possible status for a Tunnel."""

    STATUS_PENDING_CONFIGURATION = "pending-configuration"
    STATUS_CONFIGURED = "configured"
    STATUS_PENDING_DELETION = "pending-deletion"

    CHOICES = (
        (STATUS_PENDING_CONFIGURATION, "Pending Configuration"),
        (STATUS_CONFIGURED, "Configured"),
        (STATUS_PENDING_DELETION, "Pending Deletion"),
    )


class TunnelTypeChoices(ChoiceSet):
    """List of possible types of Tunnels."""

    IPSEC_TUNNEL = "ipsec-tunnel"
    GRE_TUNNEL = "gre-tunnel"
    L2TP_TUNNEL = "l2tp-tunnel"
    PPTP_TUNNEL = "pptp-tunnel"
    CIPE_TUNNEL = "cipe-tunnel"

    CHOICES = (
        (IPSEC_TUNNEL, "IPSec Tunnel"),
        (GRE_TUNNEL, "GRE Tunnel"),
        (L2TP_TUNNEL, "L2TP Tunnel"),
        (PPTP_TUNNEL, "PPTP Tunnel"),
        (CIPE_TUNNEL, "CIPE Tunnel"),
    )
