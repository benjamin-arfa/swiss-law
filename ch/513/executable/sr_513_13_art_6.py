"""SR 513.13 Art. 6

Generated from: ch/513/de/513.13.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_militaerdienstpflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist militaerdienstpflichtig"


class verfuegt_ueber_erforderliche_kenntnisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person verfuegt ueber erforderliche Kenntnisse"


class einteilung_stab_einsatzunterstuetzung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einteilung in den Stab Einsatzunterstuetzung Landesregierung moeglich (Art. 6 SR 513.13)"
    reference = "SR 513.13 Art. 6"

    def formula(person, period, parameters):
        # Militaerdienstpflichtige Personen mit erforderlichen Kenntnissen
        # koennen eingeteilt werden
        dienstpflichtig = person('ist_militaerdienstpflichtig', period)
        kenntnisse = person('verfuegt_ueber_erforderliche_kenntnisse', period)
        return dienstpflichtig * kenntnisse
