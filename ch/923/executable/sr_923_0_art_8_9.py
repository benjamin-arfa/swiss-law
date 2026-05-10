"""SR 923.0 Art. 8 & 9

Generated from: ch/923/de/923.0.md

Art. 8: Bewilligung für technische Eingriffe - Permit for technical interventions:
- Interventions in waters/hydrology/course or banks/bed need a fisheries permit
  if they may affect fisheries interests
- Enumerated list of activities requiring a permit (water power, regulation,
  constructions, excavation, etc.)
- Extended/restored installations count as new installations

Art. 9: Massnahmen für Neuanlagen - Measures for new installations:
- Authorities prescribe measures for: a. favorable conditions (min flow, profile,
  substrate, shelter, temperature, velocity); b. free fish migration; c. natural
  reproduction; d. preventing injury/killing by installations
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bgf_technischer_eingriff_in_gewaesser(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Es handelt sich um einen technischen Eingriff in Gewässer/Wasserhaushalt/Ufer/Grund"
    reference = "SR 923.0 Art. 8 Abs. 1"


class bgf_eingriff_betrifft_fischerei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Eingriff kann die Interessen der Fischerei berühren"
    reference = "SR 923.0 Art. 8 Abs. 1"


class bgf_eingriff_typ(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Typ des technischen Eingriffs (1=Wasserkraft, 2=Seeregulierung, 3=Verbauung, 4=künstliches Fliessgewässer, 5=Leitungen, 6=Reinigung, 7=Kies/Sand, 8=Wasserentnahme, 9=Wassereinleitung, 10=Entwässerung, 11=Verkehr, 12=Fischzuchtanlage, 0=anderer)"
    reference = "SR 923.0 Art. 8 Abs. 3"


class bgf_ist_erweiterung_oder_instandsetzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anlage wird erweitert oder wieder instand gestellt (gilt als Neuanlage)"
    reference = "SR 923.0 Art. 8 Abs. 5"


class bgf_fischereirechtliche_bewilligung_noetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fischereirechtliche Bewilligung ist erforderlich"
    reference = "SR 923.0 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        eingriff = person('bgf_technischer_eingriff_in_gewaesser', period)
        betrifft = person('bgf_eingriff_betrifft_fischerei', period)
        return eingriff * betrifft


class bgf_massnahme_mindestabfluss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme für Mindestabflussmengen bei Wasserentnahmen vorgeschrieben"
    reference = "SR 923.0 Art. 9 Abs. 1 Bst. a Ziff. 1"


class bgf_massnahme_fischwanderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme zur Sicherstellung der freien Fischwanderung vorgeschrieben"
    reference = "SR 923.0 Art. 9 Abs. 1 Bst. b"


class bgf_massnahme_fortpflanzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme zur Ermöglichung natürlicher Fortpflanzung vorgeschrieben"
    reference = "SR 923.0 Art. 9 Abs. 1 Bst. c"


class bgf_massnahme_schutz_vor_anlagen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme zum Schutz vor Tötung/Verletzung durch Anlagen/Maschinen vorgeschrieben"
    reference = "SR 923.0 Art. 9 Abs. 1 Bst. d"
