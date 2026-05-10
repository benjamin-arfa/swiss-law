"""SR 143.13 Art. 4

Generated from: ch/143/de/143.13.md

Swiss representations abroad: if technically unable to issue Pass 2010
at time of entry into force, registered persons may apply at another
issuing authority abroad. Provisional passports and ID cards can be
applied for at all issuing authorities abroad.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vertretung_technisch_bereit_pass_2010(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die schweizerische Vertretung im Ausland technisch in der Lage ist Pass 2010 auszustellen"
    reference = "SR 143.13 Art. 4 Abs. 1"


class kann_pass_2010_bei_anderer_behoerde_beantragen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person den Pass 2010 bei einer anderen ausstellenden Behoerde im Ausland beantragen kann"
    reference = "SR 143.13 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return not_(person('vertretung_technisch_bereit_pass_2010', period))


class provisorischer_pass_bei_allen_behoerden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob provisorische Paesse und Identitaetskarten bei allen ausstellenden Behoerden im Ausland beantragt werden koennen"
    reference = "SR 143.13 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        return True
