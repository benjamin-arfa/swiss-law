"""SR 916.402 Art. 2 – Grundsätze (Veterinärwesen)

Generated from: ch/916/de/916.402.md

Personen mit Funktionen im öffentlichen Veterinärwesen müssen über ein
eidgenössisches Diplom verfügen. Personen nach Art. 1 Bst. b-f müssen
spätestens 3 Jahre nach Aufnahme der Funktion über das Diplom verfügen.
Mindestbeschäftigungsgrad: 30%.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

FRIST_DIPLOM_JAHRE = 3
MINDEST_BESCHAEFTIGUNGSGRAD = 0.30  # 30%


class hat_eidg_diplom_veterinaerwesen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Verfügt über eidgenössisches Diplom im Veterinärwesen"
    reference = "SR 916.402 Art. 2 Abs. 1"


class funktion_veterinaerwesen(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Funktion im öffentlichen Veterinärwesen (a-f nach Art. 1)"
    reference = "SR 916.402 Art. 1"


class funktionsaufnahme_datum_jahre_seit(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Jahre seit Aufnahme der Funktion"
    reference = "SR 916.402 Art. 2 Abs. 1"


class beschaeftigungsgrad(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Beschäftigungsgrad (0-1)"
    reference = "SR 916.402 Art. 2 Abs. 5"


class interessenkonflikt_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person übt andere Tätigkeiten aus, die zu Interessenkonflikt führen können"
    reference = "SR 916.402 Art. 2 Abs. 4"


class erfuellt_grundsaetze_veterinaerwesen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Erfüllt Grundsätze nach Art. 2 für das öffentliche Veterinärwesen"
    reference = "SR 916.402 Art. 2"

    def formula(person, period, parameters):
        import numpy as np
        hat_diplom = person('hat_eidg_diplom_veterinaerwesen', period)
        funktion = person('funktion_veterinaerwesen', period.this_year)
        jahre_seit = person('funktionsaufnahme_datum_jahre_seit', period.this_year)
        grad = person('beschaeftigungsgrad', period.this_year)
        konflikt = person('interessenkonflikt_vorhanden', period.this_year)

        # Abs. 1: Kantonstierärzte (a) brauchen Diplom sofort,
        # andere (b-f) haben 3 Jahre Frist
        ist_kantonstierarzt = funktion == 'a'
        diplom_ok = np.where(
            ist_kantonstierarzt,
            hat_diplom,
            hat_diplom + (jahre_seit < FRIST_DIPLOM_JAHRE)
        )

        # Abs. 4: Keine Interessenkonflikte
        # Abs. 5: Mindestbeschäftigungsgrad 30% für Funktionen b und c
        ist_b_oder_c = (funktion == 'b') + (funktion == 'c')
        grad_ok = not_(ist_b_oder_c) + (ist_b_oder_c * (grad >= MINDEST_BESCHAEFTIGUNGSGRAD))

        return diplom_ok * not_(konflikt) * grad_ok
