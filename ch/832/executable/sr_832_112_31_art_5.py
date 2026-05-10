"""SR 832.112.31 Art. 5

Generated from: ch/832/de/832.112.31.md

Art. 5: Physiotherapie
- Abs. 1ter: Med. Trainingstherapie beginnt mit Einfuehrung und ist max.
  3 Monate nach der Einfuehrung abgeschlossen.
- Abs. 2: Je aerztliche Anordnung hoechstens 9 Sitzungen; erste Behandlung
  innert 5 Wochen seit aerztlicher Anordnung.
- Abs. 3: Fuer weitere Sitzungen ist eine neue aerztliche Anordnung noetig.
- Abs. 4: Nach 36 Sitzungen: Bericht an Vertrauensarzt erforderlich.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class klv_physiotherapie_sitzungen_pro_anordnung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Physiotherapie-Sitzungen unter aktueller aerztlicher Anordnung"
    reference = "SR 832.112.31 Art. 5 Abs. 2"


class klv_physiotherapie_sitzungen_gesamt(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtanzahl Physiotherapie-Sitzungen im laufenden Behandlungszyklus"
    reference = "SR 832.112.31 Art. 5 Abs. 4"


class klv_physiotherapie_max_sitzungen_pro_anordnung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Sitzungen je aerztliche Anordnung (Physiotherapie)"
    reference = "SR 832.112.31 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        # Art. 5 Abs. 2: hoechstens 9 Sitzungen je Anordnung
        return 9


class klv_physiotherapie_schwelle_vertrauensarzt(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Schwelle fuer Vertrauensarzt-Bericht (Physiotherapie)"
    reference = "SR 832.112.31 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        # Art. 5 Abs. 4: Nach 36 Sitzungen ist ein Bericht erforderlich
        return 36


class klv_physiotherapie_neue_anordnung_noetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Neue aerztliche Anordnung fuer weitere Physiotherapie noetig"
    reference = "SR 832.112.31 Art. 5 Abs. 2-3"

    def formula(person, period, parameters):
        sitzungen = person('klv_physiotherapie_sitzungen_pro_anordnung', period)
        max_sitzungen = person('klv_physiotherapie_max_sitzungen_pro_anordnung', period)
        return sitzungen >= max_sitzungen


class klv_physiotherapie_vertrauensarzt_noetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vertrauensarzt-Bericht fuer Fortsetzung der Physiotherapie noetig"
    reference = "SR 832.112.31 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        sitzungen_gesamt = person('klv_physiotherapie_sitzungen_gesamt', period.this_year)
        schwelle = person('klv_physiotherapie_schwelle_vertrauensarzt', period.this_year)
        return sitzungen_gesamt >= schwelle


class klv_physiotherapie_frist_erste_behandlung_wochen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer erste Behandlung nach aerztlicher Anordnung (Wochen)"
    reference = "SR 832.112.31 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        # Art. 5 Abs. 2: innert 5 Wochen
        return 5


class klv_trainingstherapie_max_dauer_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Dauer der medizinischen Trainingstherapie nach Einfuehrung (Monate)"
    reference = "SR 832.112.31 Art. 5 Abs. 1ter"

    def formula(person, period, parameters):
        # Art. 5 Abs. 1ter: maximal 3 Monate nach Einfuehrung
        return 3
