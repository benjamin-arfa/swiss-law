"""SR 360.2 Art. 22

Generated from: ch/360/de/360.2.md

Aufbewahrungsdauer: Verschiedene Fristen fuer NES-Daten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nes_daten_unterkategorie(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "NES-Unterkategorie der Daten (standard, ga_pr, text_bild_ton, unverjaehrbar)"
    reference = "SR 360.2 Art. 22"
    default_value = "standard"


class nes_aufbewahrungsdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsdauer der NES-Daten in Jahren"
    reference = "SR 360.2 Art. 22"

    def formula(person, period, parameters):
        kategorie = person('nes_daten_unterkategorie', period)
        # Abs. 1: Standard = 10 Jahre nach letztem Eintrag
        # Abs. 6: GA/PR ohne Verknuepfung = 3 Jahre
        # Abs. 7: Text/Bild/Ton ohne Verknuepfung = 10 Jahre
        # Abs. 8: Unverjaehrbare Straftaten = 80 Jahre
        standard = where(kategorie == 'standard', 10, 0)
        ga_pr = where(kategorie == 'ga_pr', 3, 0)
        text_bild = where(kategorie == 'text_bild_ton', 10, 0)
        unverjaehrbar = where(kategorie == 'unverjaehrbar', 80, 0)
        return standard + ga_pr + text_bild + unverjaehrbar
