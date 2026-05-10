"""SR 441.11 Art. 7

Generated from: ch/441/de/441.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sprachgemeinschaft(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Sprachgemeinschaft der Person (de, fr, it, rm)"
    reference = "SR 441.11, Art. 7"


class vertretung_deutsch_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimale Bandbreite für Vertretung Deutsch in Bundesverwaltung"
    reference = "SR 441.11, Art. 7 Abs. 1 lit. a"

    def formula(self, period, parameters):
        return 0.665


class vertretung_deutsch_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Bandbreite für Vertretung Deutsch in Bundesverwaltung"
    reference = "SR 441.11, Art. 7 Abs. 1 lit. a"

    def formula(self, period, parameters):
        return 0.685


class vertretung_franzoesisch_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimale Bandbreite für Vertretung Französisch in Bundesverwaltung"
    reference = "SR 441.11, Art. 7 Abs. 1 lit. b"

    def formula(self, period, parameters):
        return 0.225


class vertretung_franzoesisch_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Bandbreite für Vertretung Französisch in Bundesverwaltung"
    reference = "SR 441.11, Art. 7 Abs. 1 lit. b"

    def formula(self, period, parameters):
        return 0.245


class vertretung_italienisch_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimale Bandbreite für Vertretung Italienisch in Bundesverwaltung"
    reference = "SR 441.11, Art. 7 Abs. 1 lit. c"

    def formula(self, period, parameters):
        return 0.075


class vertretung_italienisch_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Bandbreite für Vertretung Italienisch in Bundesverwaltung"
    reference = "SR 441.11, Art. 7 Abs. 1 lit. c"

    def formula(self, period, parameters):
        return 0.085


class vertretung_raetoromanisch_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimale Bandbreite für Vertretung Rätoromanisch in Bundesverwaltung"
    reference = "SR 441.11, Art. 7 Abs. 1 lit. d"

    def formula(self, period, parameters):
        return 0.005


class vertretung_raetoromanisch_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Bandbreite für Vertretung Rätoromanisch in Bundesverwaltung"
    reference = "SR 441.11, Art. 7 Abs. 1 lit. d"

    def formula(self, period, parameters):
        return 0.010


class anteil_sprachgemeinschaft(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Aktueller Anteil der Sprachgemeinschaft in der Verwaltungseinheit"
    reference = "SR 441.11, Art. 7"


class sprachgemeinschaft_in_bandbreite(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vertretung der Sprachgemeinschaft liegt innerhalb der Bandbreite nach Art. 7"
    reference = "SR 441.11, Art. 7 Abs. 1"

    def formula(self, period, parameters):
        sprache = self.person('sprachgemeinschaft', period)
        anteil = self.person('anteil_sprachgemeinschaft', period)

        # Check if within range for each language
        de_ok = (sprache == 'de') * (anteil >= 0.665) * (anteil <= 0.685)
        fr_ok = (sprache == 'fr') * (anteil >= 0.225) * (anteil <= 0.245)
        it_ok = (sprache == 'it') * (anteil >= 0.075) * (anteil <= 0.085)
        rm_ok = (sprache == 'rm') * (anteil >= 0.005) * (anteil <= 0.010)

        return de_ok + fr_ok + it_ok + rm_ok


class vorrang_untervertretene_sprachgemeinschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorrangige Einstellung bei untervertretener Sprachgemeinschaft und gleichwertiger Qualifikation"
    reference = "SR 441.11, Art. 7 Abs. 3"

    def formula(self, period, parameters):
        in_bandbreite = self.person('sprachgemeinschaft_in_bandbreite', period)
        gleichwertige_qualifikation = self.person('gleichwertige_qualifikation', period)
        return not_(in_bandbreite) * gleichwertige_qualifikation


class gleichwertige_qualifikation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gleichwertige Qualifikation bei Stellenbesetzung"
    reference = "SR 441.11, Art. 7 Abs. 3"
