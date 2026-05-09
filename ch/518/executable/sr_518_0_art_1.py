"""SR 518.0 Art. 1

Generated from: ch/518/de/518.0.md

Anwendung der Genfer Abkommen in der Armee: Das Eidg. Militaerdepartement
wird beauftragt, im Einvernehmen mit dem Eidg. Finanz- und Zolldepartement
die notwendigen Massnahmen zu treffen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class genfer_abkommen_massnahmen_friedenszeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Massnahmen zur Anwendung der Genfer Abkommen zum Schutze der Kriegsopfer in der Armee (Friedenszeit)"
    reference = "SR 518.0 Art. 1"

    def formula(person, period, parameters):
        # Art. 1: Structural/institutional provision - the military department
        # is tasked with implementing Geneva Convention measures in peacetime.
        # Applies universally within scope of military law.
        return True
