"""SR 418.0 Art. 4

Generated from: ch/418/de/418.0.md

Voraussetzungen fuer die Anerkennung der allgemeinbildenden Sekundarstufe II.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sekundarstufe_ii_genuegend_schueler(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sekundarstufe II weist genuegend Schueler fuer langfristigen Fortbestand auf"
    reference = "SR 418.0 Art. 4 Bst. a"


class sekundarstufe_ii_zweite_landessprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sekundarstufe II bietet zweite CH-Landessprache an"
    reference = "SR 418.0 Art. 4 Bst. b"


class sekundarstufe_ii_anerkannter_abschluss(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sekundarstufe II fuehrt zu anerkanntem Abschluss (Matur, IB, FMS)"
    reference = "SR 418.0 Art. 4 Bst. c"


class sekundarstufe_ii_gastland_anerkennung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Abschluss im Gastland als Sek-II-Abschluss anerkannt"
    reference = "SR 418.0 Art. 4 Bst. d"


class sekundarstufe_ii_beitragsberechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sekundarstufe II als beitragsberechtigt anerkannt"
    reference = "SR 418.0 Art. 4"

    def formula(person, period, parameters):
        return (
            person('sekundarstufe_ii_genuegend_schueler', period) *
            person('sekundarstufe_ii_zweite_landessprache', period) *
            person('sekundarstufe_ii_anerkannter_abschluss', period) *
            person('sekundarstufe_ii_gastland_anerkennung', period)
        )
