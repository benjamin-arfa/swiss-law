"""SR 831.201 Art. 27bis

Generated from: ch/831/de/831.201.md

Bemessung des Invaliditaetsgrades von Teilerwerbstaetigen:
The disability degree of part-time workers is calculated by combining:
a. disability degree in employment (weighted by employment rate)
b. disability degree in household tasks (weighted by remaining time)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_beschaeftigungsgrad_ohne_invaliditaet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Beschaeftigungsgrad den die Person ohne Invaliditaet haette (0-100%)"
    reference = "SR 831.201 Art. 27bis Abs. 2 Bst. c"


class iv_einkommen_ohne_invaliditaet_100(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkommen ohne Invaliditaet hochgerechnet auf 100% Beschaeftigung"
    reference = "SR 831.201 Art. 27bis Abs. 2 Bst. a"


class iv_einkommen_mit_invaliditaet_100(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkommen mit Invaliditaet basierend auf 100% Beschaeftigung, angepasst an Leistungsfaehigkeit"
    reference = "SR 831.201 Art. 27bis Abs. 2 Bst. b"


class iv_einschraenkung_aufgabenbereich_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prozentualer Anteil der Einschraenkung im Aufgabenbereich (Haushalt)"
    reference = "SR 831.201 Art. 27bis Abs. 3 Bst. a"


class iv_invaliditaetsgrad_teilerwerbstaetige(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Invaliditaetsgrad von Teilerwerbstaetigen (gemischte Methode)"
    reference = "SR 831.201 Art. 27bis"

    def formula(person, period, parameters):
        import numpy as np
        bg = person('iv_beschaeftigungsgrad_ohne_invaliditaet', period) / 100.0
        e_ohne = person('iv_einkommen_ohne_invaliditaet_100', period)
        e_mit = person('iv_einkommen_mit_invaliditaet_100', period)
        einschraenkung = person('iv_einschraenkung_aufgabenbereich_prozent', period)

        # Abs. 2: Disability degree in employment
        # c. weighted by employment rate the person would have had
        erwerbseinbusse = np.where(
            e_ohne > 0,
            (e_ohne - e_mit) / e_ohne * 100.0,
            0.0
        )
        iv_grad_erwerb = erwerbseinbusse * bg

        # Abs. 3: Disability degree in household/task domain
        # b. weighted by (1 - employment rate)
        iv_grad_aufgaben = einschraenkung * (1 - bg)

        # Abs. 1: Sum of both components
        return iv_grad_erwerb + iv_grad_aufgaben
