"""SR 837.0 Art. 23

Generated from: ch/837/de/837.0.md

Art. 23: Versicherter Verdienst (Insured income)

Abs. 1: The insured income is the relevant salary under AHV legislation
normally earned during a measurement period from one or more employment
relationships. The maximum insured income corresponds to that of mandatory
accident insurance (currently CHF 148,200/year as of 2024).
The income is not insured if it does not reach a minimum threshold.

Abs. 2: For persons exempt from contribution requirements, the Federal
Council sets flat-rate insured income amounts.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alv_versicherter_verdienst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherter Verdienst (massgebender AHV-Lohn im Bemessungszeitraum)"
    reference = "SR 837.0 Art. 23 Abs. 1"


class alv_verdienst_ueber_mindestgrenze(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherter Verdienst erreicht Mindestgrenze"
    reference = "SR 837.0 Art. 23 Abs. 1"

    def formula(person, period, parameters):
        verdienst = person('alv_versicherter_verdienst', period)
        # Minimum threshold: CHF 500/month = CHF 6,000/year (as per AVIV Art. 40)
        mindestgrenze = 6000.0
        return verdienst >= mindestgrenze


class alv_versicherter_verdienst_begrenzt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherter Verdienst begrenzt auf Hoechstbetrag UVG (Art. 23 Abs. 1)"
    reference = "SR 837.0 Art. 23 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        verdienst = person('alv_versicherter_verdienst', period)
        # Maximum insured income = UVG maximum (CHF 148,200 as of 2024)
        hoechstbetrag = 148200.0
        return np.minimum(verdienst, hoechstbetrag)
