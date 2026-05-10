"""SR 821.421 Art. 11

Generated from: ch/821/de/821.421.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vermittlungsvorschlag_aufgestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Einigungsstelle hat einen Vermittlungsvorschlag unter Ausschluss "
        "der Parteien aufgestellt (keine direkte Verstaendigung erzielt)"
    )
    reference = "SR 821.421 Art. 11 Abs. 1"


class stimmabgabe_pflicht_einigungsstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Mitglieder der Einigungsstelle sind zur Stimmabgabe verpflichtet "
        "(absolute Mehrheit entscheidet, Stichentscheid des Obmanns)"
    )
    reference = "SR 821.421 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_mitglied_einigungsstelle', period)


class ist_mitglied_einigungsstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Mitglied der Einigungsstelle"
    reference = "SR 821.421 Art. 11 Abs. 2"
