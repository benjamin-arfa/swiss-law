"""AG 290.100 § 6

Generated from: ch/ag/de/290.100.md

§ 6 Organisation: The Anwaltskommission is the supervisory authority over
lawyers. It is composed of 2 senior judges, 2 registered lawyers, and
1 additional person with a lawyer's certificate, plus substitutes.
Term of office is 4 years, beginning 24 months after that of the Grosse Rat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ag_anwaltskommission_mitglieder_oberrichter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Oberrichter in der Anwaltskommission"
    reference = "AG 290.100 § 6 Abs. 2"


class ag_anwaltskommission_mitglieder_anwaelte(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Anwaelte in der Anwaltskommission"
    reference = "AG 290.100 § 6 Abs. 2"


class ag_anwaltskommission_beschlussfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anwaltskommission ist beschlussfaehig (AG 290.100 § 6 Abs. 4)"
    reference = "AG 290.100 § 6 Abs. 4"
