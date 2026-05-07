"""SR 514.544.2 Art. 5

Generated from: ch/514/de/514.544.2.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)
Organisation = build_entity(key='organisation', plural='organisations', label='An organisation')


class videoueberwachung_speicherdauer_tage(Variable):
    value_type = int
    entity = Organisation
    definition_period = YEAR
    label = "Tatsaechliche Speicherdauer der Videoueberwachung in Tagen"


class videoueberwachung_speicherdauer_konform(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "Speicherdauer der Videoueberwachung konform (Art. 5 Abs. 2 SR 514.544.2)"
    reference = "SR 514.544.2 Art. 5"

    def formula(organisation, period, parameters):
        dauer = organisation('videoueberwachung_speicherdauer_tage', period)
        # Mindestens 5 und hoechstens 30 Tage
        return (dauer >= 5) * (dauer <= 30)


class waffenhandlung_hat_videoueberwachung(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "Geschaeftsraeume und Eingangsbereiche mit Videoueberwachung ausgestattet (Art. 5 Abs. 1 SR 514.544.2)"
    reference = "SR 514.544.2 Art. 5"
