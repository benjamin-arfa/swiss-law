"""SR 834.1 Art. 16t-16w

Generated from: ch/834/de/834.1.md

Adoptionsentschaedigung:
- Art. 16t: Anspruchsberechtigte (Kind unter 4 Jahren, 9 Monate versichert,
  5 Monate erwerbstaetig). Keine Stiefkindadoption.
- Art. 16u: Rahmenfrist 1 Jahr ab Aufnahme des Kindes.
- Art. 16v: Max 14 Taggelder (7/Woche oder 5+2-Regel).
- Art. 16w: Taggeld = 80% Einkommen, Hoechstbetrag wie Art. 16f.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eo_adoption_kind_unter_4_jahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Adoptiertes Kind ist weniger als 4 Jahre alt"
    reference = "SR 834.1 Art. 16t Abs. 1 Bst. a"


class eo_adoption_9_monate_versichert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "9 Monate AHV-versichert und 5 Monate erwerbstaetig vor Aufnahme des Kindes"
    reference = "SR 834.1 Art. 16t Abs. 1 Bst. b"


class eo_adoption_erwerbsstatus(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bei Aufnahme Arbeitnehmer, Selbstaendiger oder mitarbeitend"
    reference = "SR 834.1 Art. 16t Abs. 1 Bst. c"


class eo_adoption_ist_stiefkindadoption(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Adoption ist Stiefkindadoption nach Art. 264c Abs. 1 ZGB"
    reference = "SR 834.1 Art. 16t Abs. 5"


class eo_adoption_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Adoptionsentschaedigung nach Art. 16t EOG"
    reference = "SR 834.1 Art. 16t"

    def formula_2023(person, period, parameters):
        kind_unter_4 = person('eo_adoption_kind_unter_4_jahren', period)
        versichert = person('eo_adoption_9_monate_versichert', period)
        status = person('eo_adoption_erwerbsstatus', period)
        stiefkind = person('eo_adoption_ist_stiefkindadoption', period)

        return kind_unter_4 * versichert * status * not_(stiefkind)


class eo_adoption_monate_seit_aufnahme(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Monate seit Aufnahme des Adoptivkindes"
    reference = "SR 834.1 Art. 16u"


class eo_adoption_taggelder_bezogen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Adoptions-Taggelder bereits bezogen"
    reference = "SR 834.1 Art. 16v"


class eo_adoption_anspruch_laufend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Laufender Anspruch auf Adoptionsentschaedigung"
    reference = "SR 834.1 Art. 16u"

    def formula_2023(person, period, parameters):
        anspruch = person('eo_adoption_anspruch', period)
        monate = person('eo_adoption_monate_seit_aufnahme', period)
        bezogen = person('eo_adoption_taggelder_bezogen', period)

        p = parameters(period).sr834_1
        rahmenfrist = p.adoption_rahmenfrist_monate  # 12
        max_taggelder = p.adoption_max_taggelder  # 14

        return anspruch * (monate <= rahmenfrist) * (bezogen < max_taggelder)


class eo_adoption_taggeld(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Adoptionsentschaedigung Taggeld (CHF)"
    reference = "SR 834.1 Art. 16w"

    def formula_2023(person, period, parameters):
        import numpy as np

        anspruch = person('eo_adoption_anspruch_laufend', period)
        einkommen = person('eo_vordienstliches_erwerbseinkommen_taeglich', period)

        p = parameters(period).sr834_1
        anteil = p.mutterschaft_taggeld_anteil  # 0.80
        hoechstbetrag = p.mutterschaft_hoechstbetrag  # Art. 16f

        taggeld = np.minimum(einkommen * anteil, hoechstbetrag)

        return np.where(anspruch, taggeld, 0.0)
