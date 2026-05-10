"""SR 442.1 Art. 9

Generated from: ch/442/de/442.1.md

Soziale Sicherheit der Kulturschaffenden: Der Bund und Pro Helvetia ueberweisen
einen prozentualen Anteil ihrer Finanzhilfen an die Pensionskasse oder eine
andere Vorsorgeform. Der Bundesrat legt den Anteil fest.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class finanzhilfe_kulturschaffende(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Finanzhilfe fuer Kulturschaffende (CHF)"
    reference = "SR 442.1 Art. 9"


class anteil_soziale_sicherheit_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prozentualer Anteil fuer soziale Sicherheit (vom Bundesrat festgelegt)"
    reference = "SR 442.1 Art. 9 Abs. 2"
    default_value = 12.0  # Festgelegt in SR 442.11 Art. 2a Abs. 3


class beitrag_soziale_sicherheit_kulturschaffende(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Beitrag an Pensionskasse oder andere Vorsorgeform fuer Kulturschaffende"
    reference = "SR 442.1 Art. 9"

    def formula(person, period, parameters):
        finanzhilfe = person('finanzhilfe_kulturschaffende', period)
        anteil = person('anteil_soziale_sicherheit_prozent', period)
        return finanzhilfe * anteil / 100
