"""SR 351.6 Art. 21

Generated from: ch/351/de/351.6.md
Release from transfer detention - deadline rules.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tage_seit_festnahme(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Tage seit der Festnahme"
    reference = "SR 351.6 Art. 21 Abs. 1"


class ueberstellungsersuchen_eingegangen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ueberstellungsersuchen und Unterlagen sind bei Zentralstelle eingegangen"
    reference = "SR 351.6 Art. 21 Abs. 1"


class person_bereits_in_haft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person befand sich bereits in Haft vor der Ueberstellungshaft"
    reference = "SR 351.6 Art. 21 Abs. 2"


class ueberstellungshaft_aufzuheben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ueberstellungshaft muss aufgehoben werden"
    reference = "SR 351.6 Art. 21"

    def formula(person, period):
        tage = person('tage_seit_festnahme', period)
        ersuchen = person('ueberstellungsersuchen_eingegangen', period)
        # Spaetestens 60 Tage nach Festnahme muss die Haft aufgehoben werden
        # wenn das Ersuchen nicht eingegangen ist
        frist_abgelaufen = tage >= 60
        return frist_abgelaufen * not_(ersuchen)
