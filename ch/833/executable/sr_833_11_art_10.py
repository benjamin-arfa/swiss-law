"""SR 833.11 Art. 10

Generated from: ch/833/de/833.11.md

Art. 10: Koordination mit Leistungen der Truppe, Sanität, Zivilschutz, Zivildienst und EO:
1. During military service: troop medical service takes priority over MV
2. Civilian treatment ordered by troop/civil protection/civil service doctors: paid by MV
3. Examination/prophylactic costs during service: paid by MV
4. While entitled to pay/pocket money/EO compensation: daily allowance from MV is deferred
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mvv_anspruch_truppenarzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person hat Behandlungsanspruch gegenüber dem Truppenarztdienst"
    reference = "SR 833.11 Art. 10 Abs. 1"


class mvv_behandlung_durch_zivile_medizinalperson(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Behandlung durch zivile Medizinalperson/Anstalt (veranlasst durch Truppenarzt oder Notfall)"
    reference = "SR 833.11 Art. 10 Abs. 2"


class mvv_bezieht_sold_oder_eo(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person bezieht Sold, Taschengeld oder EO-Entschädigung"
    reference = "SR 833.11 Art. 10 Abs. 4"


class mvv_taggeld_aufgeschoben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Taggeld-Anspruch der Militärversicherung ist aufgeschoben"
    reference = "SR 833.11 Art. 10 Abs. 4"

    def formula(person, period, parameters):
        bezieht_sold = person('mvv_bezieht_sold_oder_eo', period)
        return bezieht_sold


class mvv_behandlungskosten_mv_verguetet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Behandlungskosten werden von der Militärversicherung vergütet"
    reference = "SR 833.11 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        truppenarzt_vorrang = person('mvv_anspruch_truppenarzt', period)
        zivil_behandlung = person('mvv_behandlung_durch_zivile_medizinalperson', period)
        # MV pays if: troop doctor ordered civilian treatment, or not during active service
        return zivil_behandlung + (1 - truppenarzt_vorrang) > 0
