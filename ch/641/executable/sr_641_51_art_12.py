"""SR 641.51 Art. 12

Generated from: ch/641/de/641.51.md

Steuerbefreiung bei der Automobilsteuer:
1. Von der Steuer befreit sind:
   a. zollfreie Automobile
   b. voruebergehend eingefuehrte Automobile
   c. im Inland hergestellte, direkt ins Ausland gelieferte Automobile
   d. aufgrund internationaler Abkommen steuerfreie Automobile
   e. der Schwerverkehrsabgabe unterliegende Automobile
2. Der Bundesrat kann Elektro-Automobile ganz oder teilweise befreien.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class astg_ist_zollfrei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Automobil aufgrund besonderer Umstaende zollfrei ist"
    reference = "SR 641.51 Art. 12 Abs. 1 Bst. a"


class astg_zollpflicht_aufgehoben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Pflicht zur Bezahlung der Zollabgaben aufgehoben wurde"
    reference = "SR 641.51 Art. 12 Abs. 1 Bst. b"


class astg_direkt_ins_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das im Inland hergestellte Automobil direkt ins Ausland geliefert wird"
    reference = "SR 641.51 Art. 12 Abs. 1 Bst. c"


class astg_international_steuerfrei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Automobil aufgrund internationaler Abkommen steuerfrei ist"
    reference = "SR 641.51 Art. 12 Abs. 1 Bst. d"


class astg_unterliegt_schwerverkehrsabgabe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Automobil der Schwerverkehrsabgabe unterliegt"
    reference = "SR 641.51 Art. 12 Abs. 1 Bst. e"


class astg_ist_elektroautomobil(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um ein Elektro-Automobil handelt"
    reference = "SR 641.51 Art. 12 Abs. 2"


class astg_steuerbefreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Automobil von der Automobilsteuer befreit ist"
    reference = "SR 641.51 Art. 12"

    def formula(person, period, parameters):
        zollfrei = person('astg_ist_zollfrei', period)
        zoll_aufgehoben = person('astg_zollpflicht_aufgehoben', period)
        direkt_ausland = person('astg_direkt_ins_ausland', period)
        international = person('astg_international_steuerfrei', period)
        schwerverkehr = person('astg_unterliegt_schwerverkehrsabgabe', period)
        elektro = person('astg_ist_elektroautomobil', period)
        elektro_befreit = parameters(period).sr_641_51.elektroautomobil_befreit

        return (
            zollfrei
            + zoll_aufgehoben
            + direkt_ausland
            + international
            + schwerverkehr
            + (elektro * elektro_befreit)
        ) > 0
