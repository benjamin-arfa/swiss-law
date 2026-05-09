"""SR 832.112.31 Art. 3

Generated from: ch/832/de/832.112.31.md

Art. 3: Kostenuebernahme (Psychotherapie)
Die Versicherung uebernimmt die Kosten fuer hoechstens 40 Abklaerungs-
und Therapiesitzungen. Artikel 3b bleibt vorbehalten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class klv_psychotherapie_sitzungen_absolviert(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl absolvierter Psychotherapie-Sitzungen im laufenden Behandlungszyklus"
    reference = "SR 832.112.31 Art. 3"


class klv_psychotherapie_max_sitzungen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Anzahl Psychotherapie-Sitzungen ohne Vertrauensarzt-Bericht"
    reference = "SR 832.112.31 Art. 3"

    def formula(person, period, parameters):
        # Art. 3: Die Versicherung uebernimmt hoechstens 40 Sitzungen
        return 40


class klv_psychotherapie_kostenuebernahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kostenuebernahme fuer Psychotherapie durch OKP (innerhalb 40 Sitzungen)"
    reference = "SR 832.112.31 Art. 3"

    def formula(person, period, parameters):
        sitzungen = person('klv_psychotherapie_sitzungen_absolviert', period.this_year)
        max_sitzungen = person('klv_psychotherapie_max_sitzungen', period.this_year)
        return sitzungen < max_sitzungen
