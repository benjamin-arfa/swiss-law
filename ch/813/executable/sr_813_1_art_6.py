"""SR 813.1 Art. 6

Generated from: ch/813/de/813.1.md

Inverkehrbringen: Herstellerin darf nach Selbstkontrolle ohne behoerdliche
Zustimmung in Verkehr bringen. Ausnahmen: neue Stoffe (Anmeldung), Biozid-
produkte und Pflanzenschutzmittel (Zulassung).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_neuer_stoff(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um einen neuen Stoff handelt (anmeldepflichtig nach Art. 9)"
    reference = "SR 813.1 Art. 6 Bst. a"


class ist_biozidprodukt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um ein Biozidprodukt handelt (zulassungspflichtig nach Art. 10)"
    reference = "SR 813.1 Art. 6 Bst. b"


class ist_pflanzenschutzmittel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um ein Pflanzenschutzmittel handelt (zulassungspflichtig nach Art. 11)"
    reference = "SR 813.1 Art. 6 Bst. b"


class benoetigt_anmeldung_oder_zulassung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob fuer das Inverkehrbringen eine Anmeldung oder Zulassung erforderlich ist"
    reference = "SR 813.1 Art. 6"

    def formula(person, period, parameters):
        neuer_stoff = person('ist_neuer_stoff', period)
        biozid = person('ist_biozidprodukt', period)
        pflanzenschutz = person('ist_pflanzenschutzmittel', period)
        return neuer_stoff + biozid + pflanzenschutz > 0


class darf_ohne_zustimmung_in_verkehr_bringen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Herstellerin Stoffe ohne behoerdliche Zustimmung in Verkehr bringen darf"
    reference = "SR 813.1 Art. 6"

    def formula(person, period, parameters):
        selbstkontrolle = person('hat_selbstkontrolle_durchgefuehrt', period)
        braucht_zulassung = person('benoetigt_anmeldung_oder_zulassung', period)
        return selbstkontrolle * (1 - braucht_zulassung)
