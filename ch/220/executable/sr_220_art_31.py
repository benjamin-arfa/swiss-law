"""SR 220 Art. 31

Generated from: ch/de/220.md

Aufhebung des Mangels durch Genehmigung: Wenn der durch Irrtum, Taeuschung
oder Furcht beeinflusste Teil nicht binnen Jahresfrist eroeffnet, dass er
den Vertrag nicht halte, so gilt der Vertrag als genehmigt. Fristbeginn:
bei Irrtum/Taeuschung mit Entdeckung, bei Furcht mit deren Beseitigung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vertrag_wegen_irrtum_anfechtbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Vertrag wegen Irrtum anfechtbar ist"
    reference = "SR 220 Art. 23-27"


class vertrag_wegen_taeuschung_anfechtbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Vertrag wegen absichtlicher Taeuschung anfechtbar ist"
    reference = "SR 220 Art. 28"


class vertrag_wegen_furcht_anfechtbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Vertrag wegen Furchterregung anfechtbar ist"
    reference = "SR 220 Art. 29-30"


class monate_seit_entdeckung_mangel(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Monate seit Entdeckung des Irrtums/der Taeuschung oder Beseitigung der Furcht"
    reference = "SR 220 Art. 31 Abs. 2"


class vertrag_genehmigt_durch_zeitablauf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Vertrag durch Fristablauf als genehmigt gilt (Art. 31 OR)"
    reference = "SR 220 Art. 31"

    def formula(person, period, parameters):
        irrtum = person('vertrag_wegen_irrtum_anfechtbar', period)
        taeuschung = person('vertrag_wegen_taeuschung_anfechtbar', period)
        furcht = person('vertrag_wegen_furcht_anfechtbar', period)
        monate_seit_entdeckung = person('monate_seit_entdeckung_mangel', period)

        hat_mangel = (irrtum + taeuschung + furcht) > 0
        frist = parameters(period).or_vertragsrecht.anfechtung.genehmigungsfrist_monate

        # Abs. 1: Wer nicht binnen Jahresfrist eroeffnet -> Vertrag genehmigt
        return hat_mangel * (monate_seit_entdeckung > frist)
