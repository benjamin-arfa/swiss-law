"""SR 834.1 Art. 16a

Generated from: ch/834/de/834.1.md

Hoechstbetrag der Gesamtentschaedigung:
- Abs. 1: 275 CHF pro Tag (Stand 2025).
- Abs. 2: Bundesrat kann nach je 2 Jahren anpassen bei >= 12% Lohnaenderung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH

# This article defines the parameter only; see parameters/sr_834_1.yaml
# The parameter eo_hoechstbetrag_gesamtentschaedigung is used by other articles.
# No separate variable needed — the parameter is referenced directly.
