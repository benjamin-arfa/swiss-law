"""SR 371 Art. 5 - Tateinheit mit anderen Straftaten (Concurrence with Other Offences)

Generated from: ch/de/371.md
If the conviction also covered other offences, the annulment extends to those
if they appear subordinate upon overall assessment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class weitere_straftaten_untergeordnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Weitere Straftaten bei Tateinheit erscheinen bei Gesamtwuerdigung als untergeordnet"
    reference = "SR 371 Art. 5"
    default_value = False


class aufhebung_erfasst_weitere_straftaten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aufhebung erfasst auch weitere Straftaten bei Tateinheit"
    reference = "SR 371 Art. 5"

    def formula(person, period, parameters):
        ist_helfer = person('gilt_als_fluechtlingshelfer', period)
        untergeordnet = person('weitere_straftaten_untergeordnet', period)
        return ist_helfer * untergeordnet
