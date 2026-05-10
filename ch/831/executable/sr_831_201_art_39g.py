"""SR 831.201 Art. 39g

Generated from: ch/831/de/831.201.md

Berechnung des Assistenzbeitrages:
- Abs. 1: IV-Stelle berechnet den monatlichen und jaehrlichen Assistenzbeitrag
- Abs. 2a: Annual = 12 x monthly (default)
- Abs. 2b: Annual = 11 x monthly if:
  1. the insured person lives in the same household as their spouse,
     registered partner, de facto partner, or direct-line relative, AND
  2. that person is of legal age and does not receive a helplessness allowance
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_assistenzbeitrag_monatlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Monatlicher Assistenzbeitrag in Franken"
    reference = "SR 831.201 Art. 39g Abs. 1"


class iv_lebt_mit_volljaehriger_person_ohne_he(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Lebt im selben Haushalt mit Ehepartner/Partner/Verwandtem, "
        "der volljaehrig ist und keine Hilflosenentschaedigung bezieht"
    )
    reference = "SR 831.201 Art. 39g Abs. 2 Bst. b"


class iv_assistenzbeitrag_jaehrlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher Assistenzbeitrag in Franken"
    reference = "SR 831.201 Art. 39g Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        monatlich = person('iv_assistenzbeitrag_monatlich', period.first_month)
        lebt_mit = person('iv_lebt_mit_volljaehriger_person_ohne_he', period.first_month)

        # 12x if alone/independent; 11x if living with qualifying person
        faktor = np.where(lebt_mit, 11, 12)
        return monatlich * faktor
