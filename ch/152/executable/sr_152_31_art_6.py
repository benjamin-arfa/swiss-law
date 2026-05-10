"""SR 152.31 Art. 6

Generated from: ch/152/de/152.31.md

Balancing interests between privacy protection and public interest in access.
Access may exceptionally be granted after weighing public interest against
third-party privacy rights.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class oeffentliches_interesse_an_zugang(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein oeffentliches Interesse am Zugang zum Dokument besteht"
    reference = "SR 152.31 Art. 6 Abs. 1"


class privatsphaere_dritter_betroffen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Recht einer Drittperson auf Schutz ihrer Privatsphaere betroffen ist"
    reference = "SR 152.31 Art. 6 Abs. 1"


class besonderes_informationsinteresse_oeffentlichkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein besonderes Informationsinteresse der Oeffentlichkeit besteht (wichtige Vorkommnisse)"
    reference = "SR 152.31 Art. 6 Abs. 2 Bst. a"


class zugang_dient_schutz_oeffentlicher_interessen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Zugang dem Schutz spezifischer oeffentlicher Interessen dient"
    reference = "SR 152.31 Art. 6 Abs. 2 Bst. b"


class betroffene_person_hat_beziehung_zu_behoerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die betroffene Person in einer Beziehung zur Behoerde steht aus der ihr bedeutende Vorteile erwachsen"
    reference = "SR 152.31 Art. 6 Abs. 2 Bst. c"


class oeffentliches_interesse_ueberwiegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das oeffentliche Interesse am Zugang ueberwiegt"
    reference = "SR 152.31 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('besonderes_informationsinteresse_oeffentlichkeit', period) +
            person('zugang_dient_schutz_oeffentlicher_interessen', period) +
            person('betroffene_person_hat_beziehung_zu_behoerde', period)
        ) > 0


class zugang_ausnahmsweise_gewaehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Zugang ausnahmsweise nach Interessenabwaegung gewaehrt wird"
    reference = "SR 152.31 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('privatsphaere_dritter_betroffen', period) *
            person('oeffentliches_interesse_ueberwiegt', period)
        )
