"""SR 442.132.3 Art. 17b

Generated from: ch/442/de/442.132.3.md

Art. 17b: Überbrückungsrente bei einer Restrukturierung - Die Stiftung
trägt die Kosten der Überbrückungsrente bei Restrukturierung unter
bestimmten kumulativen Voraussetzungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class restrukturierung_pro_helvetia(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es liegt eine Restrukturierung bei Pro Helvetia vor"
    reference = "SR 442.132.3 Art. 17b Abs. 1"


class arbeitsverhaeltnis_mindestens_5_jahre(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Arbeitsverhältnis hat mindestens fünf Jahre gedauert"
    reference = "SR 442.132.3 Art. 17b Abs. 1 lit. b"


class keine_zumutbare_stelle_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Die betroffene Person kann auf keiner zumutbaren Stelle "
        "entsprechend ihrem bisherigen Beschäftigungsgrad "
        "weiterbeschäftigt werden"
    )
    reference = "SR 442.132.3 Art. 17b Abs. 1 lit. c"


class keine_zumutbare_stelle_abgelehnt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die betroffene Person hat keine zumutbare Stelle abgelehnt"
    reference = "SR 442.132.3 Art. 17b Abs. 1 lit. d"


class stiftung_traegt_ueberbrueckungsrente_restrukturierung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Stiftung trägt die Kosten der Überbrückungsrente bei "
        "Restrukturierung, wenn alle kumulativen Voraussetzungen "
        "erfüllt sind (Art. 17b Abs. 1)"
    )
    reference = "SR 442.132.3 Art. 17b Abs. 1"

    def formula(person, period, parameters):
        restrukturierung = person('restrukturierung_pro_helvetia', period)
        alter_60 = person('alter_60_vollendet', period)
        mindestens_5_jahre = person('arbeitsverhaeltnis_mindestens_5_jahre', period)
        keine_stelle = person('keine_zumutbare_stelle_vorhanden', period)
        nicht_abgelehnt = person('keine_zumutbare_stelle_abgelehnt', period)
        return (
            restrukturierung
            * alter_60
            * mindestens_5_jahre
            * keine_stelle
            * nicht_abgelehnt
        )


class alter_bei_pensionierung(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der betroffenen Person zum Zeitpunkt der vorzeitigen Pensionierung"
    reference = "SR 442.132.3 Art. 17b Abs. 2-3"


class erhaelt_erhoehte_altersrente_63(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Person im Alter 60-62 bei Restrukturierung erhält die Altersrente, "
        "die ihr bei Pensionierung mit 63 zustünde, plus "
        "Überbrückungsrente (Art. 17b Abs. 2)"
    )
    reference = "SR 442.132.3 Art. 17b Abs. 2"

    def formula(person, period, parameters):
        anspruch = person('stiftung_traegt_ueberbrueckungsrente_restrukturierung', period)
        alter = person('alter_bei_pensionierung', period)
        alter_60_bis_62 = (alter >= 60) * (alter <= 62)
        return anspruch * alter_60_bis_62


class erhaelt_reglementarische_altersrente(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Person ab 63 Jahren bei Restrukturierung erhält reglementarische "
        "Altersrente plus Überbrückungsrente (Art. 17b Abs. 3)"
    )
    reference = "SR 442.132.3 Art. 17b Abs. 3"

    def formula(person, period, parameters):
        anspruch = person('stiftung_traegt_ueberbrueckungsrente_restrukturierung', period)
        alter = person('alter_bei_pensionierung', period)
        alter_ab_63 = alter >= 63
        return anspruch * alter_ab_63
