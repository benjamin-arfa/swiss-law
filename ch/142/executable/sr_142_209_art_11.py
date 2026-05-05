"""SR 142.209 Art. 11

Generated from: ch/142/de/142.209.md

Gebuehren fuer Arbeitgeber: Bemessung nach Art. 2 und 4.
Arbeitsmarktliche Gebuehren sind vom Arbeitgeber zu tragen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_arbeitgeber_gebuehrenpflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Arbeitgeber fuer arbeitsmarktliche Verfuegungen gebuehrenpflichtig ist"
    reference = "SR 142.209 Art. 11 Abs. 2"
