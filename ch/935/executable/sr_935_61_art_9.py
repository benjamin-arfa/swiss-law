"""SR 935.61 Art. 9

Generated from: ch/935/de/935.61.md

Art. 9: Löschung des Registereintrags
- Anwältinnen und Anwälte, die eine der Voraussetzungen für den Registereintrag
  nicht mehr erfüllen, werden im Register gelöscht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class anwalt_registereintrag_zu_loeschen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Registereintrag ist zu löschen, da Voraussetzungen "
        "nicht mehr erfüllt (Art. 9 BGFA)"
    )
    reference = "SR 935.61 Art. 9"

    def formula(person, period, parameters):
        fachlich = person('fachliche_voraussetzungen_anwaltspatent', period)
        persoenlich = person('persoenliche_voraussetzungen_registereintrag', period)
        eingetragen = person('anwalt_in_kantonalem_register_eingetragen', period)
        # Löschung wenn eingetragen aber Voraussetzungen nicht mehr erfüllt
        voraussetzungen_erfuellt = fachlich * persoenlich
        return eingetragen * (1 - voraussetzungen_erfuellt)
