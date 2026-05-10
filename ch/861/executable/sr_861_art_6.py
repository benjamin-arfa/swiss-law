"""SR 861 Art. 6

Generated from: ch/de/861.md

Application procedure: applications to BSV; timing requirements
for different types of institutions and projects.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class gesuch_bei_bsv_eingereicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gesuch beim Bundesamt fuer Sozialversicherungen (BSV) eingereicht wurde"
    reference = "SR 861 Art. 6 Abs. 1"


class gesuch_kita_vor_betriebsaufnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gesuch vor Betriebsaufnahme oder Angebotserhoeung eingereicht wurde"
    reference = "SR 861 Art. 6 Abs. 2"


class gesuch_tagesfamilien_vor_massnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gesuch vor Beginn der Massnahme eingereicht wurde"
    reference = "SR 861 Art. 6 Abs. 3"


class gesuch_innovation_vor_projektbeginn(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gesuch vor Beginn des Innovationsprojekts eingereicht wurde"
    reference = "SR 861 Art. 6 Abs. 4"


class gesuch_subventionserhoehung_vor_erhoehung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gesuch vor der Erhoehung der kantonalen und kommunalen Subventionen eingereicht wurde"
    reference = "SR 861 Art. 6 Abs. 5"


class gesuch_abstimmungsprojekt_vor_beginn(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gesuch vor Beginn des Abstimmungsprojekts eingereicht wurde"
    reference = "SR 861 Art. 6 Abs. 6"
