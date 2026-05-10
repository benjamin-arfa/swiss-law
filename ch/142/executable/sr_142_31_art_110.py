"""SR 142.31 Art. 110 - Delais de procedure (Procedural Deadlines)

Generated from: ch/142/fr/142.31.md

Procedural deadlines in asylum proceedings:
- Supplementary deadline to cure appeal defects: 7 days (general)
- Supplementary deadline for non-entry decisions: 3 days
- Evidence deadline (Switzerland): 7 days
- Evidence deadline (abroad): 30 days
- Expert opinions: 30 days
- Extension possible if prevented by illness/accident
- Airport procedure (refusal of entry): max 2 working days
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lasi_type_decision(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Type de decision: 0=general, 1=non-entree, 2=art23/40, 3=art111b, 4=aeroport"
    reference = "SR 142.31 Art. 110"


class lasi_moyens_preuve_en_suisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les moyens de preuve se trouvent en Suisse"
    reference = "SR 142.31 Art. 110 al. 2"


class lasi_delai_regularisation_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai supplementaire pour regulariser le recours (jours)"
    reference = "SR 142.31 Art. 110 al. 1"

    def formula(person, period, parameters):
        type_dec = person('lasi_type_decision', period)

        # General: 7 days; non-entry/art23+40/art111b: 3 days
        return select(
            [type_dec == 0, type_dec == 1, type_dec == 2, type_dec == 3, type_dec == 4],
            [7, 3, 3, 3, 2]
        )


class lasi_delai_moyens_preuve_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai pour fournir les moyens de preuve (jours)"
    reference = "SR 142.31 Art. 110 al. 2"

    def formula(person, period, parameters):
        en_suisse = person('lasi_moyens_preuve_en_suisse', period)
        # Suisse: 7 jours, etranger: 30 jours
        return where(en_suisse, 7, 30)


class lasi_delai_expertise_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai pour fournir une expertise (30 jours)"
    reference = "SR 142.31 Art. 110 al. 2"

    def formula(person, period, parameters):
        return person('lasi_type_decision', period) * 0 + 30
