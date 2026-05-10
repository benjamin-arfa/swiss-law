"""SR 614.0 Art. 14

Generated from: ch/614/de/614.0.md

Art. 14: Berichterstattung und Umsetzung - Die EFK verfasst über jede
abgeschlossene Prüfung einen Bericht und stellt ihn der Finanzdelegation zu.
Regelung der Veröffentlichung und Umsetzung von Empfehlungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class efk_verfasst_pruefbericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK verfasst über jede abgeschlossene Prüfung einen Bericht "
        "(Art. 14 Abs. 1)"
    )
    reference = "SR 614.0 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_bericht_an_finanzdelegation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK stellt Prüfbericht und Akten der Finanzdelegation der "
        "eidgenössischen Räte zu (Art. 14 Abs. 1)"
    )
    reference = "SR 614.0 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_kann_bericht_veroeffentlichen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK kann Prüfbericht zusammen mit Stellungnahme der geprüften "
        "Stelle veröffentlichen, nachdem die Finanzdelegation ihn behandelt "
        "hat (Art. 14 Abs. 2)"
    )
    reference = "SR 614.0 Art. 14 Abs. 2"

    def formula(person, period, parameters):
        ist_efk = person('ist_eidgenoessische_finanzkontrolle', period)
        finanzdelegation_hat_behandelt = person('finanzdelegation_hat_bericht_behandelt', period)
        return ist_efk * finanzdelegation_hat_behandelt


class finanzdelegation_hat_bericht_behandelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Finanzdelegation hat den Prüfbericht der EFK behandelt"
    reference = "SR 614.0 Art. 14 Abs. 2"


class geprueft_stelle_meldet_umsetzung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Geprüfte Stellen teilen der EFK jährlich mit, wie weit die "
        "Empfehlungen der höchsten Wichtigkeitsstufe umgesetzt "
        "sind (Art. 14 Abs. 2bis)"
    )
    reference = "SR 614.0 Art. 14 Abs. 2bis"


class efk_jahresbericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK unterbreitet der Finanzdelegation und dem Bundesrat jährlich "
        "einen Bericht über Revisionstätigkeit, Feststellungen und "
        "Umsetzungspendenzen (Art. 14 Abs. 3)"
    )
    reference = "SR 614.0 Art. 14 Abs. 3"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_meldet_nicht_umgesetzte_empfehlungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK unterrichtet den Departementsvorsteher, wenn Empfehlungen der "
        "höchsten Wichtigkeitsstufe nicht innert Frist umgesetzt "
        "werden (Art. 14 Abs. 3bis)"
    )
    reference = "SR 614.0 Art. 14 Abs. 3bis"

    def formula(person, period, parameters):
        ist_efk = person('ist_eidgenoessische_finanzkontrolle', period)
        empfehlung_nicht_umgesetzt = person('empfehlung_hoechster_stufe_nicht_fristgerecht', period)
        return ist_efk * empfehlung_nicht_umgesetzt


class empfehlung_hoechster_stufe_nicht_fristgerecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Empfehlungen der höchsten Wichtigkeitsstufe wurden nicht innert Frist umgesetzt"
    reference = "SR 614.0 Art. 14 Abs. 3bis"
