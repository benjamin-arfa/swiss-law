"""SR 614.0 Art. 9

Generated from: ch/614/de/614.0.md

Art. 9: Dokumentation - Die BK stellt der EFK alle Beschlüsse der
Bundesversammlung und des Bundesrates zu, welche den Finanzhaushalt
des Bundes betreffen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bk_stellt_efk_beschluesse_zu(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "BK stellt der EFK alle Beschlüsse der Bundesversammlung und des "
        "Bundesrates zu, die den Finanzhaushalt betreffen (Art. 9 Abs. 1)"
    )
    reference = "SR 614.0 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        ist_bk = person('ist_bundeskanzlei', period)
        betrifft_finanzhaushalt = person('beschluss_betrifft_finanzhaushalt', period)
        return ist_bk * betrifft_finanzhaushalt


class ist_bundeskanzlei(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entität ist die Bundeskanzlei (BK)"
    reference = "SR 614.0 Art. 9 Abs. 1"


class beschluss_betrifft_finanzhaushalt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beschluss betrifft den Finanzhaushalt des Bundes"
    reference = "SR 614.0 Art. 9"


class departemente_uebermitteln_weisungen_efk(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Departemente bringen der EFK Weisungen und Verfügungen zur "
        "Kenntnis, die auf Grund der Beschlüsse erlassen werden (Art. 9 Abs. 2)"
    )
    reference = "SR 614.0 Art. 9 Abs. 2"


class efk_anspruch_auf_unterlagen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Auf Verlangen händigen die Departemente und Dienststellen der EFK "
        "alle Unterlagen zu Rechtsgeschäften aus, die den Finanzhaushalt "
        "betreffen können (Art. 9 Abs. 3)"
    )
    reference = "SR 614.0 Art. 9 Abs. 3"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)
