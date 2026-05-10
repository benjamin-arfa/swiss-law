"""SR 832.112.31 Art. 6

Generated from: ch/832/de/832.112.31.md

Art. 6: Ergotherapie
- Abs. 2: Je aerztliche Anordnung hoechstens 9 Sitzungen; erste Behandlung
  innert 8 Wochen seit aerztlicher Anordnung.
- Abs. 3: Fuer weitere Sitzungen neue aerztliche Anordnung erforderlich.
- Abs. 4: Nach 36 Sitzungen Bericht an Vertrauensarzt noetig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class klv_ergotherapie_sitzungen_pro_anordnung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Ergotherapie-Sitzungen unter aktueller aerztlicher Anordnung"
    reference = "SR 832.112.31 Art. 6 Abs. 2"


class klv_ergotherapie_sitzungen_gesamt(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtanzahl Ergotherapie-Sitzungen im laufenden Behandlungszyklus"
    reference = "SR 832.112.31 Art. 6 Abs. 4"


class klv_ergotherapie_max_sitzungen_pro_anordnung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Sitzungen je aerztliche Anordnung (Ergotherapie)"
    reference = "SR 832.112.31 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        # Art. 6 Abs. 2: hoechstens 9 Sitzungen je Anordnung
        return 9


class klv_ergotherapie_frist_erste_behandlung_wochen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer erste Behandlung nach aerztlicher Anordnung (Wochen)"
    reference = "SR 832.112.31 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        # Art. 6 Abs. 2: innert 8 Wochen
        return 8


class klv_ergotherapie_schwelle_vertrauensarzt(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Schwelle fuer Vertrauensarzt-Bericht (Ergotherapie)"
    reference = "SR 832.112.31 Art. 6 Abs. 4"

    def formula(person, period, parameters):
        # Art. 6 Abs. 4: Nach 36 Sitzungen
        return 36


class klv_ergotherapie_neue_anordnung_noetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Neue aerztliche Anordnung fuer weitere Ergotherapie noetig"
    reference = "SR 832.112.31 Art. 6 Abs. 2-3"

    def formula(person, period, parameters):
        sitzungen = person('klv_ergotherapie_sitzungen_pro_anordnung', period)
        max_sitzungen = person('klv_ergotherapie_max_sitzungen_pro_anordnung', period)
        return sitzungen >= max_sitzungen


class klv_ergotherapie_vertrauensarzt_noetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vertrauensarzt-Bericht fuer Fortsetzung der Ergotherapie noetig"
    reference = "SR 832.112.31 Art. 6 Abs. 4"

    def formula(person, period, parameters):
        sitzungen_gesamt = person('klv_ergotherapie_sitzungen_gesamt', period.this_year)
        schwelle = person('klv_ergotherapie_schwelle_vertrauensarzt', period.this_year)
        return sitzungen_gesamt >= schwelle
