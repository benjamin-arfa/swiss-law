"""SR 420.1 Art. 19

Generated from: ch/420/de/420.1.md

Foerderung von Innovationsprojekten - Kostenbeteiligung Umsetzungspartner 40-60 Prozent.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class direkte_gesamtprojektkosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Direkte Gesamtprojektkosten des Innovationsprojekts"
    reference = "SR 420.1 Art. 19 Abs. 2 Bst. d"


class eigenleistung_umsetzungspartner(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Eigenleistungen oder Leistungen des Umsetzungspartners an Forschungspartner"
    reference = "SR 420.1 Art. 19 Abs. 2 Bst. d"


class beteiligungsquote_umsetzungspartner(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Beteiligungsquote des Umsetzungspartners an direkten Gesamtprojektkosten"
    reference = "SR 420.1 Art. 19 Abs. 2 Bst. d"

    def formula(person, period, parameters):
        kosten = person('direkte_gesamtprojektkosten', period)
        eigenleistung = person('eigenleistung_umsetzungspartner', period)
        return where(kosten > 0, eigenleistung / kosten, 0)


class wirkungsvolle_umsetzung_erwartet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wirkungsvolle Umsetzung der Forschungsresultate kann erwartet werden"
    reference = "SR 420.1 Art. 19 Abs. 2 Bst. b"


class projekt_ohne_foerderung_nicht_realisierbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Projekt kann ohne Bundesfoerderung voraussichtlich nicht realisiert werden"
    reference = "SR 420.1 Art. 19 Abs. 2 Bst. c"


class projekt_traegt_zur_ausbildung_bei(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Projekt traegt zur praxisorientierten Ausbildung des wissenschaftlichen Nachwuchses bei"
    reference = "SR 420.1 Art. 19 Abs. 2 Bst. e"


class ausnahme_geringere_beteiligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einzelfall-Ausnahme fuer geringere Beteiligung als 40 Prozent (Art. 19 Abs. 2bis)"
    reference = "SR 420.1 Art. 19 Abs. 2bis"


class ausnahme_hoehere_beteiligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einzelfall-Ausnahme fuer hoehere Beteiligung als 60 Prozent (Art. 19 Abs. 2ter)"
    reference = "SR 420.1 Art. 19 Abs. 2ter"


class beteiligung_umsetzungspartner_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beteiligung des Umsetzungspartners ist zulaessig (40-60% oder Ausnahme)"
    reference = "SR 420.1 Art. 19 Abs. 2 Bst. d"

    def formula(person, period, parameters):
        quote = person('beteiligungsquote_umsetzungspartner', period)
        ausnahme_tiefer = person('ausnahme_geringere_beteiligung', period)
        ausnahme_hoeher = person('ausnahme_hoehere_beteiligung', period)

        im_regelbereich = (quote >= 0.40) * (quote <= 0.60)
        unter_40_mit_ausnahme = (quote < 0.40) * ausnahme_tiefer
        ueber_60_mit_ausnahme = (quote > 0.60) * ausnahme_hoeher

        return im_regelbereich + unter_40_mit_ausnahme + ueber_60_mit_ausnahme


class innovationsprojekt_foerderbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Innovationsprojekt erfuellt die Foerdervoraussetzungen nach Art. 19 Abs. 2"
    reference = "SR 420.1 Art. 19 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('wirkungsvolle_umsetzung_erwartet', period) *
            person('projekt_ohne_foerderung_nicht_realisierbar', period) *
            person('beteiligung_umsetzungspartner_zulaessig', period) *
            person('projekt_traegt_zur_ausbildung_bei', period)
        )
