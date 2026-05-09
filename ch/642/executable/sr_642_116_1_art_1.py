"""SR 642.116.1 Art. 1

Generated from: ch/642/de/642.116.1.md

Art. 1: Measures (Massnahmen)

Defines the catalogue of measures for rational energy use and renewable
energy that qualify as deductible investments equal to maintenance costs:

a. Measures reducing energy losses of the building envelope
   (insulation, windows, sealing, unheated vestibules, shutters)
b. Measures for rational energy use in building systems
   (heating replacement, water heaters, district heating, heat pumps,
    CHP, renewables, controls, pipe insulation, metering, chimney
    renovation, heat recovery)
c. Costs for energy analyses and energy concepts
d. Costs for replacing high-consumption household appliances included
   in building value

This is a definitional/catalogue article. Variables model eligibility.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class liegenschaft_massnahme_gebaeudehulle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme zur Verminderung der Energieverluste der Gebaeudehuelle (Art. 1 Bst. a)"
    reference = "SR 642.116.1 Art. 1 Bst. a"


class liegenschaft_massnahme_haustechnik(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme zur rationellen Energienutzung bei haustechnischen Anlagen (Art. 1 Bst. b)"
    reference = "SR 642.116.1 Art. 1 Bst. b"


class liegenschaft_massnahme_energieanalyse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten fuer energietechnische Analysen und Energiekonzepte (Art. 1 Bst. c)"
    reference = "SR 642.116.1 Art. 1 Bst. c"


class liegenschaft_massnahme_geraeteersatz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ersatz von Haushaltgeraeten mit grossem Stromverbrauch im Gebaeudewert (Art. 1 Bst. d)"
    reference = "SR 642.116.1 Art. 1 Bst. d"


class liegenschaft_energiespar_massnahme_qualifiziert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme qualifiziert als abziehbare Energiespar-/Umweltschutzinvestition"
    reference = "SR 642.116.1 Art. 1"

    def formula(person, period, parameters):
        hulle = person('liegenschaft_massnahme_gebaeudehulle', period)
        haustechnik = person('liegenschaft_massnahme_haustechnik', period)
        analyse = person('liegenschaft_massnahme_energieanalyse', period)
        geraete = person('liegenschaft_massnahme_geraeteersatz', period)
        return hulle + haustechnik + analyse + geraete
