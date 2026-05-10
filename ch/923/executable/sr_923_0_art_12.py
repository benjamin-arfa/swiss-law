"""SR 923.0 Art. 12

Generated from: ch/923/de/923.0.md

Art. 12: Finanzhilfen - Financial aid:
1. The Confederation may grant financial aid for:
   a. Measures to improve living conditions and restore habitats (Art. 7 Abs. 2)
   b. Research on species diversity/stocks and their habitats
   c. Public information about aquatic flora and fauna
2. Federal aid: max 40% of costs, based on significance of measures
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bgf_massnahme_lebensraum_verbesserung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme dient der Verbesserung der Lebensbedingungen oder Wiederherstellung von Lebensräumen"
    reference = "SR 923.0 Art. 12 Abs. 1 Bst. a"


class bgf_massnahme_forschung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme betrifft Forschungsarbeiten über Artenvielfalt/Bestände/Lebensräume"
    reference = "SR 923.0 Art. 12 Abs. 1 Bst. b"


class bgf_massnahme_information(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme dient der Information der Bevölkerung über Gewässer-Fauna/Flora"
    reference = "SR 923.0 Art. 12 Abs. 1 Bst. c"


class bgf_finanzhilfe_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf Finanzhilfe des Bundes nach Art. 12"
    reference = "SR 923.0 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        lebensraum = person('bgf_massnahme_lebensraum_verbesserung', period)
        forschung = person('bgf_massnahme_forschung', period)
        information = person('bgf_massnahme_information', period)
        return (lebensraum + forschung + information) > 0


class bgf_massnahme_kosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten der Massnahme nach Art. 12 (CHF)"
    reference = "SR 923.0 Art. 12 Abs. 2"


class bgf_finanzhilfe_max_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler Betrag der Finanzhilfe des Bundes (CHF)"
    reference = "SR 923.0 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        berechtigt = person('bgf_finanzhilfe_berechtigt', period)
        kosten = person('bgf_massnahme_kosten', period)
        # Maximum 40% of costs
        return berechtigt * kosten * 0.4
