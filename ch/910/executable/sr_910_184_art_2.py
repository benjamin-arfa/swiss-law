"""SR 910.184 Art. 2

Generated from: ch/910/de/910.184.md

Liste anerkannter Zertifizierungsstellen und Kontrollbehoerden:
Die nach Art. 23a Abs. 2 Bio-Verordnung anerkannten Stellen
sind in Anhang 2 aufgefuehrt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zertifizierungsstelle_anerkannt_bio(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zertifizierungsstelle oder Kontrollbehoerde nach Art. 23a Abs. 2 Bio-Verordnung anerkannt ist"
    reference = "SR 910.184 Art. 2"
