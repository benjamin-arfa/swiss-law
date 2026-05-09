"""SR 836.11 Art. 3

Generated from: ch/836/de/836.11.md

Art. 3: Unterstellte selbstaendigerwerbende Landwirte.
Abs. 1: Betriebsleiter und mitarbeitende Familienglieder (nicht Arbeitnehmer).
Abs. 2: Hauptberuflich: vorwiegend im eigenen Betrieb taetig, bestreitet
        daraus ueberwiegend den Familienunterhalt.
Abs. 3: Nebenberuflich: nicht hauptberuflich, aber mind. 2000 CHF/Jahr
        Betriebseinkommen oder Taetigkeit entspricht einer Grossvieheinheit.
Abs. 4: Aelpler: mind. 2 Monate ununterbrochen eine Alp selbstaendig bewirtschaftet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_betriebsleiter_landwirtschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Betriebsleiter eines landwirtschaftlichen Betriebes"
    reference = "SR 836.11 Art. 3 Abs. 1"


class ist_mitarbeitendes_familienglied(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist mitarbeitendes Familienglied (nicht als Arbeitnehmer anerkannt)"
    reference = "SR 836.11 Art. 3 Abs. 1"


class vorwiegend_im_landw_betrieb_taetig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist im Verlaufe des Jahres vorwiegend im landw. Betrieb taetig"
    reference = "SR 836.11 Art. 3 Abs. 2"


class familienunterhalt_ueberwiegend_aus_betrieb(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Familienunterhalt wird ueberwiegend aus Betriebsertrag bestritten"
    reference = "SR 836.11 Art. 3 Abs. 2"


class jaehrliches_betriebseinkommen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Jaehrliches Einkommen aus landwirtschaftlichem Betrieb"
    reference = "SR 836.11 Art. 3 Abs. 3"


class landw_taetigkeit_entspricht_gve(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Landwirtschaftliche Taetigkeit entspricht dem Halten einer Grossvieheinheit"
    reference = "SR 836.11 Art. 3 Abs. 3"


class monate_alp_bewirtschaftung(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Monate ununterbrochener selbstaendiger Alpbewirtschaftung"
    reference = "SR 836.11 Art. 3 Abs. 4"


class ist_hauptberuflich_landwirt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person gilt als hauptberuflich selbstaendigerwerbender Landwirt (Art. 3 Abs. 2)"
    reference = "SR 836.11 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        betriebsleiter = person('ist_betriebsleiter_landwirtschaft', period)
        familienglied = person('ist_mitarbeitendes_familienglied', period)
        vorwiegend = person('vorwiegend_im_landw_betrieb_taetig', period)
        unterhalt = person('familienunterhalt_ueberwiegend_aus_betrieb', period)
        # Betriebsleiter oder mitarbeitendes Familienglied
        ist_selbstaendig = (betriebsleiter + familienglied) > 0
        return ist_selbstaendig * vorwiegend * unterhalt


class ist_nebenberuflich_landwirt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person gilt als nebenberuflich selbstaendigerwerbender Landwirt (Art. 3 Abs. 3)"
    reference = "SR 836.11 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        hauptberuflich = person('ist_hauptberuflich_landwirt', period)
        einkommen = person('jaehrliches_betriebseinkommen', period)
        gve = person('landw_taetigkeit_entspricht_gve', period)
        # Nicht hauptberuflich, aber mind. 2000 CHF oder eine GVE
        return (1 - hauptberuflich) * ((einkommen >= 2000) + gve > 0)


class ist_aelpler(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person gilt als Aelpler (Art. 3 Abs. 4)"
    reference = "SR 836.11 Art. 3 Abs. 4"

    def formula(person, period, parameters):
        monate = person('monate_alp_bewirtschaftung', period)
        # Mindestens 2 Monate ununterbrochene Alpbewirtschaftung
        return monate >= 2
