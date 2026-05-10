"""SR 614.0 Art. 15

Generated from: ch/614/de/614.0.md

Art. 15: Dienstlicher Verkehr - Die EFK verkehrt direkt mit den
Finanzkommissionen, der Finanzdelegation, dem Bundesrat, den
Verwaltungseinheiten und den eidgenössischen Gerichten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class efk_direkter_verkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK verkehrt direkt mit Finanzkommissionen, Finanzdelegation, "
        "Bundesrat, Verwaltungseinheiten und eidgenössischen "
        "Gerichten (Art. 15 Abs. 1)"
    )
    reference = "SR 614.0 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_informiert_efd_vorsteher(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK bringt dem EFD-Vorsteher alle Gegenstände zur Kenntnis, "
        "über die sie mit anderen Departementvorstehern oder dem "
        "Bundesrat verkehrt (Art. 15 Abs. 2)"
    )
    reference = "SR 614.0 Art. 15 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_meldet_besondere_vorkommnisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK unterrichtet bei besonderen Vorkommnissen oder Mängeln von "
        "grundsätzlicher oder erheblicher finanzieller Bedeutung den "
        "zuständigen Departementsvorsteher und den EFD-Vorsteher "
        "(Art. 15 Abs. 3)"
    )
    reference = "SR 614.0 Art. 15 Abs. 3"

    def formula(person, period, parameters):
        ist_efk = person('ist_eidgenoessische_finanzkontrolle', period)
        besonderes_vorkommnis = person('besonderes_vorkommnis_festgestellt', period)
        mangel_grundsaetzlich = person('mangel_von_grundsaetzlicher_bedeutung', period)
        mangel_finanziell = person('mangel_von_erheblicher_finanzieller_bedeutung', period)
        return ist_efk * (besonderes_vorkommnis + mangel_grundsaetzlich + mangel_finanziell)


class besonderes_vorkommnis_festgestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ein besonderes Vorkommnis wurde festgestellt"
    reference = "SR 614.0 Art. 15 Abs. 3"
