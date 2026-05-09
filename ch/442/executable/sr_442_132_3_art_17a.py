"""SR 442.132.3 Art. 17a

Generated from: ch/442/de/442.132.3.md

Art. 17a: Überbrückungsrente: Grundsatz - Personen, die sich vor dem
ordentlichen Rentenalter pensionieren lassen, können eine Überbrückungsrente
beziehen. Die Finanzierung erfolgt grundsätzlich durch die Mitarbeitenden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class anspruch_ueberbrueckungsrente_pro_helvetia(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Anspruch auf Überbrückungsrente bei vorzeitiger Pensionierung "
        "vor Erreichen des ordentlichen Rentenalters (Art. 17a Abs. 1)"
    )
    reference = "SR 442.132.3 Art. 17a Abs. 1"

    def formula(person, period, parameters):
        ist_personal = person('ist_personal_pro_helvetia', period)
        vorzeitige_pension = person('vorzeitige_pensionierung_pro_helvetia', period)
        return ist_personal * vorzeitige_pension


class ist_personal_pro_helvetia(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Personal der Stiftung Pro Helvetia"
    reference = "SR 442.132.3 Art. 1"


class vorzeitige_pensionierung_pro_helvetia(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Person lässt sich vor Erreichen des ordentlichen Rentenalters "
        "pensionieren"
    )
    reference = "SR 442.132.3 Art. 17a Abs. 1"


class ueberbrueckungsrente_finanziert_durch_mitarbeitende(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Überbrückungsrente wird von den betroffenen Mitarbeitenden "
        "finanziert (Art. 17a Abs. 2)"
    )
    reference = "SR 442.132.3 Art. 17a Abs. 2"

    def formula(person, period, parameters):
        hat_anspruch = person('anspruch_ueberbrueckungsrente_pro_helvetia', period)
        amtszeitbeschraenkung = person('amtszeitbeschraenkung_kader', period)
        restrukturierung = person('restrukturierung_pro_helvetia', period)
        # Mitarbeitende finanzieren, ausser bei Amtszeitbeschränkung oder Restrukturierung
        return hat_anspruch * (amtszeitbeschraenkung == False) * (restrukturierung == False)


class amtszeitbeschraenkung_kader(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegt eine Amtszeitbeschränkung bei Kadermitarbeitenden vor"
    reference = "SR 442.132.3 Art. 17a Abs. 3"


class stiftung_beteiligt_50_prozent_amtszeitbeschraenkung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Stiftung beteiligt sich zu 50% an der Überbrückungsrente bei "
        "Amtszeitbeschränkung von Kadermitarbeitenden, die das 60. Altersjahr "
        "vollendet haben (Art. 17a Abs. 3)"
    )
    reference = "SR 442.132.3 Art. 17a Abs. 3"

    def formula(person, period, parameters):
        amtszeitbeschraenkung = person('amtszeitbeschraenkung_kader', period)
        alter_60_vollendet = person('alter_60_vollendet', period)
        return amtszeitbeschraenkung * alter_60_vollendet


class alter_60_vollendet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat beim Ende des Arbeitsverhältnisses das 60. Altersjahr vollendet"
    reference = "SR 442.132.3 Art. 17a Abs. 3"
