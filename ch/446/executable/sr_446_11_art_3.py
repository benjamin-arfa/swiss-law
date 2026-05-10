"""SR 446.11 Art. 3

Generated from: ch/446/de/446.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesamte_finanzmittel_kjf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamte fuer die Kinder- und Jugendfoerderung zur Verfuegung stehende Finanzmittel"
    reference = "SR 446.11 Art. 3"


class anteil_betriebsstruktur_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Prozentualer Anteil fuer Betriebsstruktur und Aus-/Weiterbildung (75-90%)"
    reference = "SR 446.11 Art. 3 Abs. 1 Bst. a"


class anteil_modellvorhaben_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Prozentualer Anteil fuer Modellvorhaben und Partizipationsprojekte (10-25%)"
    reference = "SR 446.11 Art. 3 Abs. 1 Bst. b"


class finanzmittel_betriebsstruktur_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mindestbetrag fuer Betriebsstruktur und Aus-/Weiterbildung (75%)"
    reference = "SR 446.11 Art. 3 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return person('gesamte_finanzmittel_kjf', period) * 0.75


class finanzmittel_betriebsstruktur_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstbetrag fuer Betriebsstruktur und Aus-/Weiterbildung (90%)"
    reference = "SR 446.11 Art. 3 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return person('gesamte_finanzmittel_kjf', period) * 0.90


class finanzmittel_modellvorhaben_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mindestbetrag fuer Modellvorhaben und Partizipationsprojekte (10%)"
    reference = "SR 446.11 Art. 3 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        return person('gesamte_finanzmittel_kjf', period) * 0.10


class finanzmittel_modellvorhaben_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstbetrag fuer Modellvorhaben und Partizipationsprojekte (25%)"
    reference = "SR 446.11 Art. 3 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        return person('gesamte_finanzmittel_kjf', period) * 0.25


class finanzmittel_aufteilung_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist die Aufteilung der Finanzmittel gemaess Art. 3 gueltig"
    reference = "SR 446.11 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        anteil_bs = person('anteil_betriebsstruktur_prozent', period)
        anteil_mv = person('anteil_modellvorhaben_prozent', period)
        bs_ok = (anteil_bs >= 75) * (anteil_bs <= 90)
        mv_ok = (anteil_mv >= 10) * (anteil_mv <= 25)
        summe_ok = (anteil_bs + anteil_mv) == 100
        return bs_ok * mv_ok * summe_ok
