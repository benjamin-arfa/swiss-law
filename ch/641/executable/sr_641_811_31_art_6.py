"""SR 641.811.31 Art. 6

Generated from: ch/641/de/641.811.31.md

Vehicles subject to flat-rate levy: applications for both domestic and foreign
vehicles per vehicle and levy period, filed after the period ends.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_fahrzeug_pauschale_abgabe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Fahrzeug der pauschalen Abgabeerhebung unterliegt"
    reference = "SR 641.811.31 Art. 6"


class gesuch_nach_abgabeperiode(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Rueckerstattungsgesuch nach Ablauf der Abgabeperiode eingereicht wird"
    reference = "SR 641.811.31 Art. 6"
