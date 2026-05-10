"""SR 614.0 Art. 7

Generated from: ch/614/de/614.0.md

Art. 7: Begutachtung und Beratung - Der EFK obliegt die Mitarbeit an
Vorschriften über den Kontroll- und Revisionsdienst, das Buchhaltungswesen,
den Zahlungsverkehr und die Führung von Inventaren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class efk_mitarbeit_kontrollvorschriften(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK arbeitet mit an Vorschriften über Kontroll- und Revisionsdienst, "
        "Buchhaltungswesen, Zahlungsverkehr und Inventare (Art. 7 Abs. 1)"
    )
    reference = "SR 614.0 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_begutachtet_finanzaufsichtsfragen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK begutachtet alle Fragen, welche die Finanzaufsicht "
        "betreffen (Art. 7 Abs. 1)"
    )
    reference = "SR 614.0 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_beizug_voranschlag_staatsrechnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK kann zu den Verhandlungen der vorberatenden Organe über den "
        "Voranschlag und die Staatsrechnung beigezogen werden (Art. 7 Abs. 2)"
    )
    reference = "SR 614.0 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)
