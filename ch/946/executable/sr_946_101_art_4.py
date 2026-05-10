"""SR 946.101 Art. 4

Generated from: ch/946/de/946.101.md

Maximaler Deckungssatz:
- Abs. 1: Allgemein max. 95% des versicherten Betrags.
- Abs. 2: Fabrikationskreditversicherung max. 80%, in Ausnahmefaellen bis 95%.
- Abs. 3: Bondgarantie max. 90%, in Ausnahmefaellen bis zum vollen Garantiebetrag.
- Abs. 4: Versicherungsnehmerin kann keine Deckungsprozente zukaufen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class versicherter_betrag_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherter Betrag (CHF)"
    reference = "SR 946.101 Art. 4"


class ist_fabrikationskreditversicherung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Fabrikationskreditversicherung handelt"
    reference = "SR 946.101 Art. 4 Abs. 2"


class ist_bondgarantie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Bondgarantie handelt"
    reference = "SR 946.101 Art. 4 Abs. 3"


class serv_ausnahmefall_erhoehung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein begruendeter Ausnahmefall fuer erhoehten Deckungssatz vorliegt"
    reference = "SR 946.101 Art. 4 Abs. 2-3"


class serv_maximaler_deckungssatz_pct(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler Deckungssatz der SERV-Versicherung (%)"
    reference = "SR 946.101 Art. 4"

    def formula(person, period, parameters):
        import numpy as np
        ist_fabrikat = person('ist_fabrikationskreditversicherung', period)
        ist_bond = person('ist_bondgarantie', period)
        ausnahme = person('serv_ausnahmefall_erhoehung', period)

        p = parameters(period).sr_946_101
        max_allgemein = p.max_deckungssatz_allgemein_pct
        max_fabrikat = p.max_deckungssatz_fabrikationskredit_pct
        max_fabrikat_ausnahme = p.max_deckungssatz_fabrikationskredit_ausnahme_pct
        max_bond = p.max_deckungssatz_bondgarantie_pct
        max_bond_ausnahme = p.max_deckungssatz_bondgarantie_ausnahme_pct

        # Fabrikationskreditversicherung: 80%, Ausnahme 95%
        result_fabrikat = np.where(ausnahme, max_fabrikat_ausnahme, max_fabrikat)
        # Bondgarantie: 90%, Ausnahme 100%
        result_bond = np.where(ausnahme, max_bond_ausnahme, max_bond)
        # Default: 95%
        result = np.where(ist_fabrikat, result_fabrikat,
                 np.where(ist_bond, result_bond, max_allgemein))
        return result


class serv_maximale_deckung_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Deckungssumme der SERV-Versicherung (CHF)"
    reference = "SR 946.101 Art. 4"

    def formula(person, period, parameters):
        betrag = person('versicherter_betrag_chf', period)
        satz = person('serv_maximaler_deckungssatz_pct', period)
        return betrag * satz / 100
