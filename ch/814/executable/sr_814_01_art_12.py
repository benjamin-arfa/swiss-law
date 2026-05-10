"""SR 814.01 Art. 12

Generated from: ch/fr/814/814.01.md

Art. 12: Limitations d'emissions (Emissionsbegrenzungen)
- Abs. 1: Emissions limited by:
  a. emission limit values
  b. construction/equipment requirements
  c. traffic/operation requirements
  d. thermal insulation requirements
  e. fuel specifications
- Abs. 2: Limitations in ordinances or individual decisions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class usg_emissionsgrenzwert_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Emissionsgrenzwerte eingehalten werden"
    reference = "SR 814.01 Art. 12 Abs. 1 Bst. a"


class usg_bau_und_ausruestungsvorschriften_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Bau- und Ausruestungsvorschriften erfuellt sind"
    reference = "SR 814.01 Art. 12 Abs. 1 Bst. b"


class usg_verkehrs_und_betriebsvorschriften_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Verkehrs- und Betriebsvorschriften eingehalten werden"
    reference = "SR 814.01 Art. 12 Abs. 1 Bst. c"


class usg_emissionsbegrenzung_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob alle Emissionsbegrenzungen eingehalten werden"
    reference = "SR 814.01 Art. 12"

    def formula(person, period, parameters):
        grenzwert = person('usg_emissionsgrenzwert_eingehalten', period)
        bau = person('usg_bau_und_ausruestungsvorschriften_erfuellt', period)
        verkehr = person('usg_verkehrs_und_betriebsvorschriften_erfuellt', period)
        return grenzwert * bau * verkehr
