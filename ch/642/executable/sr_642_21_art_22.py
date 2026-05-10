"""SR 642.21 Art. 22 - Anspruch natuerlicher Personen (Refund for Natural Persons)

Generated from: ch/642/de/642.21.md

Art. 22: Natural persons are entitled to a refund of the withholding tax
if they had domicile in Switzerland at the time the taxable benefit
became due.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vstg_wohnsitz_inland_bei_faelligkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die natuerliche Person bei Faelligkeit der steuerbaren Leistung Wohnsitz im Inland hatte"
    reference = "SR 642.21 Art. 22 Abs. 1"


class vstg_rueckerstattungsanspruch_natuerliche_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf Rueckerstattung der Verrechnungssteuer (natuerliche Person)"
    reference = "SR 642.21 Art. 22 Abs. 1"

    def formula(person, period, parameters):
        return person('vstg_wohnsitz_inland_bei_faelligkeit', period)
