"""SR 944.3 Art. 1

Generated from: ch/944/de/944.3.md

Pauschalreise: Definition of a package travel contract.
A combination of at least 2 services (transport, accommodation, other
tourist services) at a total price, lasting >24 hours or including overnight.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pauschalreise_hat_befoerderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Reise Befoerderung beinhaltet"
    reference = "SR 944.3 Art. 1 Abs. 1 Bst. a"
    default_value = False


class pauschalreise_hat_unterbringung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Reise Unterbringung beinhaltet"
    reference = "SR 944.3 Art. 1 Abs. 1 Bst. b"
    default_value = False


class pauschalreise_hat_andere_dienstleistung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Reise andere touristische Dienstleistungen beinhaltet"
    reference = "SR 944.3 Art. 1 Abs. 1 Bst. c"
    default_value = False


class pauschalreise_gesamtpreis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verbindung zu einem Gesamtpreis angeboten wird"
    reference = "SR 944.3 Art. 1 Abs. 1"
    default_value = False


class pauschalreise_dauer_ueber_24h_oder_uebernachtung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Reise laenger als 24 Stunden dauert oder eine Uebernachtung einschliesst"
    reference = "SR 944.3 Art. 1 Abs. 1"
    default_value = False


class ist_pauschalreise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Pauschalreise im Sinne von SR 944.3 handelt"
    reference = "SR 944.3 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        befoerderung = person('pauschalreise_hat_befoerderung', period)
        unterbringung = person('pauschalreise_hat_unterbringung', period)
        andere = person('pauschalreise_hat_andere_dienstleistung', period)
        gesamtpreis = person('pauschalreise_gesamtpreis', period)
        dauer = person('pauschalreise_dauer_ueber_24h_oder_uebernachtung', period)

        # Mindestens 2 von 3 Dienstleistungen muessen kombiniert sein
        anzahl_dienstleistungen = (
            befoerderung.astype(int) +
            unterbringung.astype(int) +
            andere.astype(int)
        )
        return (anzahl_dienstleistungen >= 2) * gesamtpreis * dauer
