"""SR 915.8 Art. 1

Generated from: ch/915/de/915.8.md

FKINV - Art. 1: Voraussetzungen fuer die Gewaehrung von Finanzhilfen
fuer Kompetenz- und Innovationsnetzwerke in der Land- und Ernaehrungswirtschaft.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fkinv_taetig_in_pflanzenzuechtung_tierzucht_tiergesundheit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Netzwerk ist in Pflanzenzuechtung, Tierzucht oder Tiergesundheit "
        "taetig (Art. 1 Abs. 1 lit. a)"
    )
    reference = "SR 915.8 Art. 1 Abs. 1 lit. a"


class fkinv_foerdert_wissensaustausch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Netzwerk foerdert den Austausch von Wissen und Innovationen durch "
        "Vernetzung und Umsetzung von Technologien (Art. 1 Abs. 1 lit. b)"
    )
    reference = "SR 915.8 Art. 1 Abs. 1 lit. b"


class fkinv_wirkung_gesamtschweizerisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Netzwerk erzeugt Wirkung von gesamtschweizerischer Bedeutung (Art. 1 Abs. 1 lit. c)"
    reference = "SR 915.8 Art. 1 Abs. 1 lit. c"


class fkinv_sitz_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Netzwerk hat Sitz in der Schweiz (Art. 1 Abs. 1 lit. d)"
    reference = "SR 915.8 Art. 1 Abs. 1 lit. d"


class fkinv_nicht_gewinnorientierte_organisation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Organisation mit Rechtspersoenlichkeit, die nicht gewinnorientiert "
        "mit Forschungseinrichtungen und Wirtschaft zusammenarbeitet (Art. 1 Abs. 1 lit. e)"
    )
    reference = "SR 915.8 Art. 1 Abs. 1 lit. e"


class fkinv_finanzhilfe_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Voraussetzungen fuer Finanzhilfen nach Art. 1 Abs. 1 sind erfuellt"
    reference = "SR 915.8 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        taetig = person('fkinv_taetig_in_pflanzenzuechtung_tierzucht_tiergesundheit', period)
        wissen = person('fkinv_foerdert_wissensaustausch', period)
        wirkung = person('fkinv_wirkung_gesamtschweizerisch', period)
        sitz = person('fkinv_sitz_in_schweiz', period)
        org = person('fkinv_nicht_gewinnorientierte_organisation', period)
        return taetig * wissen * wirkung * sitz * org


class fkinv_netzwerk_im_aufbau(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Kompetenz- und Innovationsnetzwerk ist im Aufbau und verfuegt noch "
        "ueber keine Rechtspersoenlichkeit (Art. 1 Abs. 2)"
    )
    reference = "SR 915.8 Art. 1 Abs. 2"


class fkinv_aufbau_beitraege_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Beitraege koennen an Netzwerk im Aufbau ausgerichtet werden, "
        "wenn Gesuchsteller verantwortlich und ggf. Vereinbarung vorliegt (Art. 1 Abs. 2)"
    )
    reference = "SR 915.8 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        im_aufbau = person('fkinv_netzwerk_im_aufbau', period)
        taetig = person('fkinv_taetig_in_pflanzenzuechtung_tierzucht_tiergesundheit', period)
        wissen = person('fkinv_foerdert_wissensaustausch', period)
        wirkung = person('fkinv_wirkung_gesamtschweizerisch', period)
        sitz = person('fkinv_sitz_in_schweiz', period)
        return im_aufbau * taetig * wissen * wirkung * sitz
