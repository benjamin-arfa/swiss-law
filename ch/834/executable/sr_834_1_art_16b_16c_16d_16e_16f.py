"""SR 834.1 Art. 16b-16f

Generated from: ch/834/de/834.1.md

Mutterschaftsentschaedigung:
- Art. 16b: Anspruchsberechtigte (9 Monate versichert, 5 Monate erwerbstaetig)
- Art. 16c: Dauer: 98 aufeinanderfolgende Tage, Verlaengerung bei Hospitalisierung
  des Neugeborenen um max 56 Tage.
- Art. 16d: Ende des Anspruchs am 98. Tag oder bei Wiederaufnahme Erwerbstaetigkeit.
- Art. 16e: Taggeld = 80% des durchschnittlichen Erwerbseinkommens.
- Art. 16f: Hoechstbetrag 220 CHF/Tag (Stand 2025).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import DAY, MONTH


class eo_mutter_9_monate_versichert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Mutter war 9 Monate vor Niederkunft obligatorisch AHV-versichert"
    reference = "SR 834.1 Art. 16b Abs. 1 Bst. a"


class eo_mutter_5_monate_erwerbstaetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Mutter war in den 9 Monaten vor Niederkunft mindestens 5 Monate erwerbstaetig"
    reference = "SR 834.1 Art. 16b Abs. 1 Bst. b"


class eo_mutter_ist_arbeitnehmerin_oder_selbstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Mutter ist bei Niederkunft Arbeitnehmerin, Selbstaendigerwerbende oder mitarbeitend"
    reference = "SR 834.1 Art. 16b Abs. 1 Bst. c"


class eo_mutterschaft_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Mutterschaftsentschaedigung nach Art. 16b EOG"
    reference = "SR 834.1 Art. 16b"

    def formula_2005(person, period, parameters):
        versichert = person('eo_mutter_9_monate_versichert', period)
        erwerbstaetig = person('eo_mutter_5_monate_erwerbstaetig', period)
        status = person('eo_mutter_ist_arbeitnehmerin_oder_selbstaendig', period)
        return versichert * erwerbstaetig * status


class eo_mutterschaft_tage_bezogen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Tage Mutterschaftsentschaedigung bereits bezogen"
    reference = "SR 834.1 Art. 16c"


class eo_neugeborenes_hospitalisiert_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Tage Hospitalisierung des Neugeborenen (mind. 14 Tage ununterbrochen)"
    reference = "SR 834.1 Art. 16c Abs. 3"


class eo_mutter_hat_erwerbstaetigkeit_wiederaufgenommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Mutter hat Erwerbstaetigkeit wiederaufgenommen (Art. 16d Abs. 3 EOG)"
    reference = "SR 834.1 Art. 16d Abs. 3"


class eo_mutterschaft_maximale_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Anzahl Tage Mutterschaftsentschaedigung"
    reference = "SR 834.1 Art. 16c"

    def formula_2021(person, period, parameters):
        import numpy as np

        hosp_tage = person('eo_neugeborenes_hospitalisiert_tage', period)
        p = parameters(period).sr834_1

        basis_tage = p.mutterschaft_dauer_tage  # 98
        max_verlaengerung = p.mutterschaft_max_verlaengerung_tage  # 56

        verlaengerung = np.where(
            hosp_tage >= 14,
            np.minimum(hosp_tage, max_verlaengerung),
            0
        )

        return basis_tage + verlaengerung


class eo_mutterschaft_anspruch_laufend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Laufender Anspruch auf Mutterschaftsentschaedigung (nicht erloschen)"
    reference = "SR 834.1 Art. 16d"

    def formula_2005(person, period, parameters):
        anspruch = person('eo_mutterschaft_anspruch', period)
        tage_bezogen = person('eo_mutterschaft_tage_bezogen', period)
        max_tage = person('eo_mutterschaft_maximale_tage', period)
        wiederaufgenommen = person('eo_mutter_hat_erwerbstaetigkeit_wiederaufgenommen', period)

        return anspruch * (tage_bezogen < max_tage) * not_(wiederaufgenommen)


class eo_mutterschaft_taggeld(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Mutterschaftsentschaedigung Taggeld (CHF)"
    reference = "SR 834.1 Art. 16e-16f"

    def formula_2005(person, period, parameters):
        import numpy as np

        anspruch = person('eo_mutterschaft_anspruch_laufend', period)
        einkommen = person('eo_vordienstliches_erwerbseinkommen_taeglich', period)

        p = parameters(period).sr834_1
        anteil = p.mutterschaft_taggeld_anteil  # 0.80
        hoechstbetrag = p.mutterschaft_hoechstbetrag  # 220

        taggeld = np.minimum(einkommen * anteil, hoechstbetrag)

        return np.where(anspruch, taggeld, 0.0)
