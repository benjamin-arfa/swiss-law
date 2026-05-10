"""SR 614.0 Art. 10

Generated from: ch/614/de/614.0.md

Art. 10: Auskunft, Amtshilfe und Datenzugriff - Die EFK ist berechtigt,
Auskunft zu verlangen und Akteneinsicht zu nehmen, ungeachtet einer
allfälligen Geheimhaltungspflicht. Das Post- und Telegraphengeheimnis
bleibt gewährleistet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class efk_recht_auf_auskunft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK ist berechtigt, Auskunft zu verlangen und Akten einzusehen, "
        "ungeachtet Geheimhaltungspflicht (Art. 10 Abs. 1)"
    )
    reference = "SR 614.0 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        # Art. 10 Abs. 1: Berechtigt, ungeachtet Geheimhaltungspflicht
        # Ausnahme: Post- und Telegraphengeheimnis bleibt gewährleistet
        return person('ist_eidgenoessische_finanzkontrolle', period)


class pflicht_zur_unterstuetzung_efk(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Wer der Aufsicht der EFK unterstellt ist, muss ihr jede Unterstützung "
        "bei der Durchführung ihrer Aufgabe gewähren (Art. 10 Abs. 2)"
    )
    reference = "SR 614.0 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        return person('untersteht_efk_finanzaufsicht', period)


class efk_datenzugriffsrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Verwaltungseinheiten räumen der EFK Recht auf Datenzugriff im "
        "Abrufverfahren ein (Art. 10 Abs. 3)"
    )
    reference = "SR 614.0 Art. 10 Abs. 3"

    def formula(person, period, parameters):
        # Art. 10 Abs. 3: Zugriffsrecht erstreckt sich bei Bedarf auch auf
        # besonders schützenswerte Personendaten.
        # Daten nur bis Abschluss Revisionsverfahren speichern.
        return person('ist_zentrale_bundesverwaltung', period)
