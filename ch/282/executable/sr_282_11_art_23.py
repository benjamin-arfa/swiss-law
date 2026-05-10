"""SR 282.11 Art. 23 - Genehmigung der Beschluesse

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class beschluss_erfuellt_gesetzliche_voraussetzungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beschluss erfuellt die gesetzlichen Voraussetzungen"
    reference = "SR 282.11 Art. 23 Abs. 2"


class beschluss_wahrt_gemeinsame_interessen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beschluss wahrt die gemeinsamen Interessen der Obligationaere genuegend"
    reference = "SR 282.11 Art. 23 Abs. 2"


class beschluss_auf_redliche_weise_zustande_gekommen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beschluss ist auf redliche Weise zustande gekommen"
    reference = "SR 282.11 Art. 23 Abs. 2"


# Computed variables

class genehmigung_darf_erteilt_werden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Genehmigung des Beschlusses darf erteilt werden"
    reference = "SR 282.11 Art. 23 Abs. 2"

    def formula(self, period, parameters):
        voraussetzungen = self('beschluss_erfuellt_gesetzliche_voraussetzungen', period)
        interessen = self('beschluss_wahrt_gemeinsame_interessen', period)
        redlich = self('beschluss_auf_redliche_weise_zustande_gekommen', period)
        return voraussetzungen * interessen * redlich
