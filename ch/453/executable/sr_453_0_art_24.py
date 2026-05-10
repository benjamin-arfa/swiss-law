"""SR 453.0 Art. 24

Generated from: ch/453/de/453.0.md
Anerkennung wissenschaftlicher Einrichtungen - Voraussetzungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_allgemein_zugaenglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einrichtung ist allgemein zugaenglich und nach wissenschaftlichen Grundsaetzen geleitet"
    reference = "SR 453.0 Art. 24 Abs. 1 Bst. a"


class hat_staendige_sammlung_cites(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einrichtung hat staendige Sammlung von CITES-Exemplaren"
    reference = "SR 453.0 Art. 24 Abs. 2 Bst. a"


class sammlung_dient_forschung_lehre(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sammlung dient Forschungs- oder Lehrzwecken und ist zugaenglich"
    reference = "SR 453.0 Art. 24 Abs. 2 Bst. b"


class rechtmaessigkeit_nachgewiesen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rechtmaessigkeit des Verkehrs auf Etiketten/Katalogen nachgewiesen"
    reference = "SR 453.0 Art. 24 Abs. 2 Bst. c"


class anerkennung_wissenschaftliche_einrichtung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzungen fuer Anerkennung als wissenschaftliche Einrichtung erfuellt"
    reference = "SR 453.0 Art. 24 Abs. 2"

    def formula(person, period, parameters):
        sammlung = person('hat_staendige_sammlung_cites', period)
        forschung = person('sammlung_dient_forschung_lehre', period)
        nachweis = person('rechtmaessigkeit_nachgewiesen', period)
        return sammlung * forschung * nachweis
