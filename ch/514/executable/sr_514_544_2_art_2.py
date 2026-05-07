"""SR 514.544.2 Art. 2

Generated from: ch/514/de/514.544.2.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)
Organisation = build_entity(key='organisation', plural='organisations', label='An organisation')


class waffenhandlung_widerstandsklasse(Variable):
    value_type = str
    entity = Organisation
    definition_period = YEAR
    label = "Widerstandsklasse der Tueren/Fenster der Waffenhandlung"


class waffenhandlung_einbruchsicherung_konform(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "Einbruchsicherung entspricht mindestens RC 3 (Art. 2 Abs. 1 SR 514.544.2)"
    reference = "SR 514.544.2 Art. 2"

    # Tueren, Fenster und andere Oeffnungen muessen mindestens der
    # Widerstandsklasse RC 3 nach SN EN 1627 entsprechen.
    # Input variable - compliance must be assessed externally.


class waffenhandlung_hat_einbruchmeldeanlage(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "Geschaeftsraeume mit Einbruchmeldeanlage Sicherheitsgrad 2 ausgestattet (Art. 2 Abs. 4 SR 514.544.2)"
    reference = "SR 514.544.2 Art. 2"
