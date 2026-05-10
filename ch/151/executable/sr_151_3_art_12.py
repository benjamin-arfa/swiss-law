"""SR 151.3 Art. 12

Generated from: ch/151/de/151.3.md

Besondere Faelle: Kostenschwellen fuer die Pflicht zur Beseitigung
von Benachteiligungen bei Bauten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gebaeudeversicherungswert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebaeudeversicherungswert des Gebaeudes"
    reference = "SR 151.3 Art. 12 Abs. 1"


class erneuerungskosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Erneuerungskosten des Gebaeudes/der Anlage"
    reference = "SR 151.3 Art. 12 Abs. 1"


class anpassungskosten_behinderte(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten der behindertengerechten Anpassung"
    reference = "SR 151.3 Art. 12 Abs. 1"


class anpassung_ueber_schwelle_versicherungswert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anpassungskosten 5% des Gebaeudeversicherungswerts uebersteigen"
    reference = "SR 151.3 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        kosten = person('anpassungskosten_behinderte', period)
        versicherungswert = person('gebaeudeversicherungswert', period)
        return kosten > versicherungswert * 0.05


class anpassung_ueber_schwelle_erneuerung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anpassungskosten 20% der Erneuerungskosten uebersteigen"
    reference = "SR 151.3 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        kosten = person('anpassungskosten_behinderte', period)
        erneuerung = person('erneuerungskosten', period)
        return kosten > erneuerung * 0.20


class anpassungspflicht_entfaellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Anpassungspflicht wegen Kostenuebersteigung entfaellt"
    reference = "SR 151.3 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        ueber_versicherung = person('anpassung_ueber_schwelle_versicherungswert', period)
        ueber_erneuerung = person('anpassung_ueber_schwelle_erneuerung', period)
        return ueber_versicherung + ueber_erneuerung > 0
