"""SR 672.933.21 Art. 4 — Rechte der betroffenen Person

Art. 4: Die ESTV eröffnet die Verfügung auch der betroffenen Person (sofern
nicht Geheimhaltung verlangt). Die Person kann sich am Verfahren beteiligen
und Einsicht in die Akten nehmen.

Generated from: ch/672/de/672.933.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class geheimhaltung_verlangt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Im Ersuchen wird ausdrücklich Geheimhaltung verlangt (SR 672.933.21 Art. 4 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_4"
    default_value = False


class betroffene_person_erhaelt_eroeffnung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Betroffene Person erhält Eröffnung der Verfügung und Kopie des Ersuchens (SR 672.933.21 Art. 4 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_4"

    def formula(person, period, parameters):
        # Art. 4 Abs. 1: Eröffnung an betroffene Person, sofern nicht Geheimhaltung verlangt.
        return person('verfuegung_herausgabe_3_monate', period) * (1 - person('geheimhaltung_verlangt', period))


class akteneinsicht_betroffene_person(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Betroffene Person kann sich beteiligen und Akteneinsicht nehmen (SR 672.933.21 Art. 4 Abs. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_4"

    def formula(person, period, parameters):
        return person('betroffene_person_erhaelt_eroeffnung', period)


class verwendung_fuer_ch_steuerrecht_nach_rechtskraft(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dokumente dürfen erst nach Rechtskraft für CH-Steuerrecht verwendet werden (SR 672.933.21 Art. 4 Abs. 4)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_4"
    default_value = True
