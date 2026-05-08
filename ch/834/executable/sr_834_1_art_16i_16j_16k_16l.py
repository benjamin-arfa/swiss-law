"""SR 834.1 Art. 16i-16l

Generated from: ch/834/de/834.1.md

Entschaedigung des andern Elternteils (Vaterschafts-/Elternurlaub):
- Art. 16i: Anspruchsberechtigte (rechtl. anderer Elternteil, 9 Monate
  versichert, 5 Monate erwerbstaetig, Arbeitnehmer/Selbstaendiger).
- Art. 16j: Rahmenfrist 6 Monate ab Geburt.
- Art. 16k: Max 14 Taggelder (7/Woche oder 5+2-Regel bei tageweisem Bezug).
- Art. 16l: Taggeld = 80% Einkommen, max wie Mutterschaft (Art. 16f).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class eo_anderer_elternteil_ist_rechtlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist rechtlicher anderer Elternteil bei Geburt oder wird es innert 6 Monaten"
    reference = "SR 834.1 Art. 16i Abs. 1 Bst. a"


class eo_anderer_elternteil_9_monate_versichert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anderer Elternteil war 9 Monate vor Geburt obligatorisch AHV-versichert"
    reference = "SR 834.1 Art. 16i Abs. 1 Bst. b"


class eo_anderer_elternteil_5_monate_erwerbstaetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anderer Elternteil war 5 Monate erwerbstaetig in den 9 Monaten vor Geburt"
    reference = "SR 834.1 Art. 16i Abs. 1 Bst. c"


class eo_anderer_elternteil_erwerbsstatus(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anderer Elternteil ist bei Geburt Arbeitnehmer, Selbstaendiger oder mitarbeitend"
    reference = "SR 834.1 Art. 16i Abs. 1 Bst. d"


class eo_anderer_elternteil_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Entschaedigung des andern Elternteils nach Art. 16i EOG"
    reference = "SR 834.1 Art. 16i"

    def formula_2021(person, period, parameters):
        rechtlich = person('eo_anderer_elternteil_ist_rechtlich', period)
        versichert = person('eo_anderer_elternteil_9_monate_versichert', period)
        erwerbstaetig = person('eo_anderer_elternteil_5_monate_erwerbstaetig', period)
        status = person('eo_anderer_elternteil_erwerbsstatus', period)
        return rechtlich * versichert * erwerbstaetig * status


class eo_anderer_elternteil_monate_seit_geburt(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Monate seit Geburt des Kindes"
    reference = "SR 834.1 Art. 16j"


class eo_anderer_elternteil_taggelder_bezogen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Taggelder anderer Elternteil bereits bezogen"
    reference = "SR 834.1 Art. 16k"


class eo_anderer_elternteil_anspruch_laufend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Laufender Anspruch auf Entschaedigung anderer Elternteil"
    reference = "SR 834.1 Art. 16j"

    def formula_2021(person, period, parameters):
        anspruch = person('eo_anderer_elternteil_anspruch', period)
        monate = person('eo_anderer_elternteil_monate_seit_geburt', period)
        bezogen = person('eo_anderer_elternteil_taggelder_bezogen', period)

        p = parameters(period).sr834_1

        rahmenfrist_monate = p.anderer_elternteil_rahmenfrist_monate  # 6
        max_taggelder = p.anderer_elternteil_max_taggelder  # 14

        in_rahmenfrist = monate <= rahmenfrist_monate
        nicht_ausgeschoepft = bezogen < max_taggelder

        return anspruch * in_rahmenfrist * nicht_ausgeschoepft


class eo_anderer_elternteil_taggeld(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taggeld Entschaedigung anderer Elternteil (CHF)"
    reference = "SR 834.1 Art. 16l"

    def formula_2021(person, period, parameters):
        import numpy as np

        anspruch = person('eo_anderer_elternteil_anspruch_laufend', period)
        einkommen = person('eo_vordienstliches_erwerbseinkommen_taeglich', period)

        p = parameters(period).sr834_1
        anteil = p.mutterschaft_taggeld_anteil  # 0.80 (Art. 16l -> Art. 16e)
        hoechstbetrag = p.mutterschaft_hoechstbetrag  # Art. 16l -> Art. 16f

        taggeld = np.minimum(einkommen * anteil, hoechstbetrag)

        return np.where(anspruch, taggeld, 0.0)
