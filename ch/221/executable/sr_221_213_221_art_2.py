"""SR 221.213.221 Art. 2 – Elemente des Pachtzinses (Gewerbe)

Generated from: ch/221/de/221.213.221.md

Der höchstzulässige Pachtzins für Gewerbe setzt sich aus der Verzinsung
des Ertragswertes und der Abgeltung der Verpächterlasten zusammen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hoechstzulaessiger_pachtzins_gewerbe(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Höchstzulässiger Pachtzins für landwirtschaftliche Gewerbe (CHF)"
    reference = "SR 221.213.221 Art. 2"

    def formula(person, period, parameters):
        verzinsung = person('verzinsung_gewerbe', period)
        verpaechterlasten = person('abgeltung_verpaechterlasten_total', period)
        return verzinsung + verpaechterlasten
