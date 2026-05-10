"""SR 235.1 Art. 10

Generated from: ch/235/de/235.1.md

Einschraenkungen des Auskunftsrechts fuer Medienschaffende.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_datensammlung_fuer_medien(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Datensammlung wird ausschliesslich fuer redaktionellen Teil eines periodischen Mediums verwendet"
    reference = "SR 235.1 Art. 10 Abs. 1"


class dsg_daten_informationsquellen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Personendaten geben Aufschluss ueber Informationsquellen"
    reference = "SR 235.1 Art. 10 Abs. 1 lit. a"


class dsg_medienschaffende_arbeitsinstrument(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Datensammlung dient Medienschaffenden ausschliesslich als persoenliches Arbeitsinstrument"
    reference = "SR 235.1 Art. 10 Abs. 2"


class dsg_medien_auskunft_eingeschraenkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auskunftsrecht ist fuer Medienschaffende eingeschraenkt"
    reference = "SR 235.1 Art. 10"

    def formula(person, period, parameters):
        medien = person('dsg_datensammlung_fuer_medien', period)
        quellen = person('dsg_daten_informationsquellen', period)
        arbeitsinstrument = person('dsg_medienschaffende_arbeitsinstrument', period)
        return (medien * quellen) + arbeitsinstrument > 0
