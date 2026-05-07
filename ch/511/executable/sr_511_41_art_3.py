"""SR 511.41 Art. 3 – Zuteilung

Generated from: ch/511/de/511.41.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class hat_information_erhalten_und_verstanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat Information nach Art. 2 erhalten und verstanden"
    reference = "SR 511.41 Art. 3 Abs. 1 lit. a"
    default_value = False


class ist_einverstanden_mit_zuteilung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist mit der Zuteilung der Funktion einverstanden"
    reference = "SR 511.41 Art. 3 Abs. 1 lit. b"
    default_value = False


class freiwillige_nicht_ausreichend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anzahl geeigneter Freiwilliger reicht nicht aus (Art. 3 Abs. 2)"
    reference = "SR 511.41 Art. 3 Abs. 2"
    default_value = False


class zuteilung_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuteilung einer Funktion mit Rückerstattungspflicht ist gültig"
    reference = "SR 511.41 Art. 3"

    def formula(person, period, parameters):
        info = person('hat_information_erhalten_und_verstanden', period)
        einverstanden = person('ist_einverstanden_mit_zuteilung', period)
        mangel = person('freiwillige_nicht_ausreichend', period)

        # Abs. 1: gültig wenn informiert UND einverstanden
        # Abs. 2: auch ohne Einwilligung, wenn Freiwillige nicht ausreichen
        return (info * einverstanden) + mangel
