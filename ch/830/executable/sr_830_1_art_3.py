"""SR 830.1 Art. 3

Generated from: ch/830/de/830.1.md

Art. 3: Krankheit - Definition of illness (Krankheit) in social insurance law.
An impairment of physical, mental or psychological health that is not the
result of an accident and requires medical examination/treatment or causes
incapacity for work.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beeintraechtigung_koerperlich_geistig_psychisch(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beeinträchtigung der körperlichen, geistigen oder psychischen Gesundheit"
    reference = "SR 830.1 Art. 3 Abs. 1"


class beeintraechtigung_ist_unfallfolge(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beeinträchtigung ist Folge eines Unfalles"
    reference = "SR 830.1 Art. 3 Abs. 1"


class erfordert_medizinische_untersuchung_oder_behandlung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beeinträchtigung erfordert medizinische Untersuchung oder Behandlung"
    reference = "SR 830.1 Art. 3 Abs. 1"


class hat_arbeitsunfaehigkeit_zur_folge(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beeinträchtigung hat eine Arbeitsunfähigkeit zur Folge"
    reference = "SR 830.1 Art. 3 Abs. 1"


class ist_krankheit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = (
        "Vorliegen einer Krankheit im Sinne von Art. 3 ATSG: Beeinträchtigung "
        "der Gesundheit, die nicht Unfallfolge ist und medizinische Behandlung "
        "erfordert oder Arbeitsunfähigkeit zur Folge hat"
    )
    reference = "SR 830.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        beeintraechtigung = person('beeintraechtigung_koerperlich_geistig_psychisch', period)
        nicht_unfall = 1 - person('beeintraechtigung_ist_unfallfolge', period)
        medizinisch = person('erfordert_medizinische_untersuchung_oder_behandlung', period)
        arbeitsunfaehig = person('hat_arbeitsunfaehigkeit_zur_folge', period)
        return beeintraechtigung * nicht_unfall * (medizinisch + arbeitsunfaehig - medizinisch * arbeitsunfaehig)


class ist_geburtsgebrechen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Krankheit bestand bei vollendeter Geburt (Geburtsgebrechen, Art. 3 Abs. 2)"
    reference = "SR 830.1 Art. 3 Abs. 2"
