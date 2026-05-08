"""SR 741.016 Art. 4

Generated from: ch/741/de/741.016.md

VKVoeV: Kompetenzen des ASTRA
The ASTRA (Federal Roads Office) may approve the following amendments,
provided they are of limited scope: (a) recognition of licences,
certificates, training and permits, (b) UN Regulation 1958 amendments,
(c) ADR annex amendments.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class astra_kompetenz_ausweise(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "ASTRA darf Aenderungen zur Anerkennung von Ausweisen genehmigen (Art. 4 lit. a VKVoeV)"
    reference = "SR 741.016 Art. 4"

    def formula_2025_04_01(person, period, parameters):
        return True


class astra_kompetenz_un_regelung_1958(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "ASTRA darf Aenderungen des UN-Uebereinkommens von 1958 genehmigen (Art. 4 lit. b VKVoeV)"
    reference = "SR 741.016 Art. 4"

    def formula_2025_04_01(person, period, parameters):
        return True


class astra_kompetenz_adr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "ASTRA darf Aenderungen der ADR-Anlagen genehmigen (Art. 4 lit. c VKVoeV)"
    reference = "SR 741.016 Art. 4"

    def formula_2025_04_01(person, period, parameters):
        return True
