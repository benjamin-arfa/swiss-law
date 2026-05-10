"""SR 956.1 Art. 1-4

Generated from: ch/956/de/956.1.md

FINMAG - Gegenstand und Ziele:
- Bund schafft Behörde (FINMA) für Finanzmarktaufsicht
- Beaufsichtigt nach diversen Finanzmarktgesetzen
- Ziel: Schutz von Gläubigern, Anlegern, Versicherten
- Schutz der Funktionsfähigkeit der Finanzmärkte
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class benoetigt_finma_bewilligung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine FINMA-Bewilligung, Anerkennung, Zulassung oder Registrierung benötigt wird"
    reference = "SR 956.1 Art. 3 Bst. a"


class ist_kollektive_kapitalanlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine kollektive Kapitalanlage mit Bewilligung/Genehmigung handelt"
    reference = "SR 956.1 Art. 3 Bst. b"


class unterliegt_finanzmarktaufsicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person/Institution der Finanzmarktaufsicht untersteht"
    reference = "SR 956.1 Art. 3"

    def formula(person, period, parameters):
        return (
            person('benoetigt_finma_bewilligung', period) +
            person('ist_kollektive_kapitalanlage', period)
        )
