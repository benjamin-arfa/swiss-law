"""SR 282.11 Art. 18 - Ausweis und Vertretung

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vertreter_hat_schriftliche_vollmacht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vertreter hat eine schriftliche Vollmacht"
    reference = "SR 282.11 Art. 18 Abs. 2"


class vertretung_beruht_auf_gesetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Vertretung beruht auf Gesetz"
    reference = "SR 282.11 Art. 18 Abs. 2"


class vertreter_ist_organ_der_schuldnerin(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vertreter ist ein Organ der Schuldnerin"
    reference = "SR 282.11 Art. 18 Abs. 3"


class vertretung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Vertretung in der Glaeubigerversammlung ist zulaessig"
    reference = "SR 282.11 Art. 18"

    def formula(self, period, parameters):
        vollmacht = self('vertreter_hat_schriftliche_vollmacht', period)
        gesetzlich = self('vertretung_beruht_auf_gesetz', period)
        organ = self('vertreter_ist_organ_der_schuldnerin', period)
        # Vertretung nur mit Vollmacht oder gesetzlicher Grundlage, nie durch Organe der Schuldnerin
        return (vollmacht + gesetzlich > 0) * (1 - organ)
