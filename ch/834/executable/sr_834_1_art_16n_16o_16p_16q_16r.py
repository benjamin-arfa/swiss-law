"""SR 834.1 Art. 16n-16r

Generated from: ch/834/de/834.1.md

Betreuungsentschaedigung (Betreuung schwer kranker/verletzter Kinder):
- Art. 16n: Anspruchsberechtigte Eltern eines minderjaehrigen Kindes mit
  schwerer gesundheitlicher Beeintraechtigung.
- Art. 16o: Definition gesundheitlich schwer beeintraechtigtes Kind.
- Art. 16p: Rahmenfrist 18 Monate, max 98 Taggelder.
- Art. 16q: Pro 5 Taggelder zusaetzlich 2 Taggelder.
  Beide Eltern erwerbstaetig: je max Haelfte.
- Art. 16r: Taggeld = 80% Einkommen, Hoechstbetrag wie Art. 16f.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class eo_kind_gesundheitlich_schwer_beeintraechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Minderjaehriges Kind ist gesundheitlich schwer beeintraechtigt (Art. 16o EOG)"
    reference = "SR 834.1 Art. 16o"


class eo_betreuung_erwerbstaetigkeit_unterbrochen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Erwerbstaetigkeit fuer Betreuung des Kindes unterbrochen"
    reference = "SR 834.1 Art. 16n Abs. 1 Bst. a"


class eo_betreuung_ist_arbeitnehmer_oder_selbstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Elternteil ist bei Unterbrechung Arbeitnehmer, Selbstaendiger oder mitarbeitend"
    reference = "SR 834.1 Art. 16n Abs. 1 Bst. b"


class eo_betreuung_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Betreuungsentschaedigung nach Art. 16n EOG"
    reference = "SR 834.1 Art. 16n"

    def formula_2021(person, period, parameters):
        kind_beeintraechtigt = person('eo_kind_gesundheitlich_schwer_beeintraechtigt', period)
        unterbrochen = person('eo_betreuung_erwerbstaetigkeit_unterbrochen', period)
        status = person('eo_betreuung_ist_arbeitnehmer_oder_selbstaendig', period)
        return kind_beeintraechtigt * unterbrochen * status


class eo_betreuung_taggelder_bezogen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Betreuungs-Taggelder bereits bezogen"
    reference = "SR 834.1 Art. 16q"


class eo_betreuung_monate_seit_erstem_bezug(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Monate seit erstem Bezug der Betreuungsentschaedigung"
    reference = "SR 834.1 Art. 16p"


class eo_beide_eltern_erwerbstaetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Beide Elternteile sind erwerbstaetig"
    reference = "SR 834.1 Art. 16q Abs. 4"


class eo_betreuung_anspruch_laufend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Laufender Anspruch auf Betreuungsentschaedigung"
    reference = "SR 834.1 Art. 16p"

    def formula_2021(person, period, parameters):
        anspruch = person('eo_betreuung_anspruch', period)
        monate = person('eo_betreuung_monate_seit_erstem_bezug', period)
        bezogen = person('eo_betreuung_taggelder_bezogen', period)

        p = parameters(period).sr834_1

        rahmenfrist = p.betreuung_rahmenfrist_monate  # 18
        max_taggelder = p.betreuung_max_taggelder  # 98

        return anspruch * (monate <= rahmenfrist) * (bezogen < max_taggelder)


class eo_betreuung_max_taggelder_elternteil(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Betreuungs-Taggelder fuer diesen Elternteil"
    reference = "SR 834.1 Art. 16q Abs. 4"

    def formula_2021(person, period, parameters):
        import numpy as np

        beide_erwerbstaetig = person('eo_beide_eltern_erwerbstaetig', period)
        p = parameters(period).sr834_1
        max_tg = p.betreuung_max_taggelder  # 98

        return np.where(beide_erwerbstaetig, max_tg // 2, max_tg)


class eo_betreuung_taggeld(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betreuungsentschaedigung Taggeld (CHF)"
    reference = "SR 834.1 Art. 16r"

    def formula_2021(person, period, parameters):
        import numpy as np

        anspruch = person('eo_betreuung_anspruch_laufend', period)
        einkommen = person('eo_vordienstliches_erwerbseinkommen_taeglich', period)

        p = parameters(period).sr834_1
        anteil = p.mutterschaft_taggeld_anteil  # 0.80
        hoechstbetrag = p.mutterschaft_hoechstbetrag  # Art. 16f

        taggeld = np.minimum(einkommen * anteil, hoechstbetrag)

        return np.where(anspruch, taggeld, 0.0)
