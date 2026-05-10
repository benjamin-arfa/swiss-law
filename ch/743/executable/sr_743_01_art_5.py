"""SR 743.01 Art. 5

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Erfuellung der grundlegenden Anforderungen.
Konformitaetsvermutung bei Einhaltung technischer Normen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class seilbahn_technische_normen_eingehalten(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Seilbahn den technischen Normen entspricht"
    reference = "SR 743.01 Art. 5 Abs. 2"


class seilbahn_grundlegende_anforderungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die grundlegenden Anforderungen als erfuellt gelten (Konformitaetsvermutung)"
    reference = "SR 743.01 Art. 5"

    def formula(organisation, period, parameters):
        normen = organisation('seilbahn_technische_normen_eingehalten', period)
        anderer_nachweis = organisation('seilbahn_anderer_nachweis_grundlegende_anforderungen', period)
        return normen + anderer_nachweis > 0


class seilbahn_anderer_nachweis_grundlegende_anforderungen(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die grundlegenden Anforderungen auf andere Weise nachgewiesen wurden"
    reference = "SR 743.01 Art. 5 Abs. 3"
