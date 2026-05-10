"""AG 290.100 § 15

Generated from: ch/ag/de/290.100.md

§ 15 Zulassung zur Pruefung: Admission to bar exams requires:
a) legal capacity and no criminal convictions incompatible with the profession
   (unless deleted from criminal register)
b) completed law degree (Lizentiat or Master)
c) sufficient practical experience
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ag_handlungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Handlungsfaehig (AG 290.100 § 15 Abs. 1 Bst. a)"
    reference = "AG 290.100 § 15 Abs. 1 Bst. a"


class ag_keine_unvereinbare_strafregistereintraege(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Keine mit dem Anwaltsberuf unvereinbare Strafregistereintraege (AG 290.100 § 15 Abs. 1 Bst. a)"
    reference = "AG 290.100 § 15 Abs. 1 Bst. a"


class ag_rechtsstudium_abgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Rechtsstudium abgeschlossen - Lizentiat oder Master (AG 290.100 § 15 Abs. 1 Bst. b)"
    reference = "AG 290.100 § 15 Abs. 1 Bst. b"


class ag_hinreichend_praktisch_taetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hinreichend praktisch taetig gewesen (AG 290.100 § 15 Abs. 1 Bst. c)"
    reference = "AG 290.100 § 15 Abs. 1 Bst. c"


class ag_zulassung_anwaltspruefung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zulassung zur Anwaltspruefung (AG 290.100 § 15)"
    reference = "AG 290.100 § 15 Abs. 1"

    def formula(person, period, parameters):
        handlungsfaehig = person('ag_handlungsfaehig', period)
        kein_strafregister = person('ag_keine_unvereinbare_strafregistereintraege', period)
        studium = person('ag_rechtsstudium_abgeschlossen', period)
        praxis = person('ag_hinreichend_praktisch_taetig', period)
        return handlungsfaehig * kein_strafregister * studium * praxis
