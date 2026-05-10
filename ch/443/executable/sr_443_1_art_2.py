"""SR 443.1 Art. 2

Generated from: ch/443/de/443.1.md

Begriffe: Definition von Film und Schweizer Film. Ein Schweizer Film muss von
einem Autor/Autorin mit CH-Nationalitaet oder Wohnsitz realisiert, von Person/
Unternehmen mit Sitz in CH produziert werden (Mehrheit CH-Personen an Kapital/GL).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class regisseur_ch_nationalitaet_oder_wohnsitz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Regisseur CH-Nationalitaet oder Wohnsitz in CH hat"
    reference = "SR 443.1 Art. 2 Abs. 2 Bst. a"


class produzent_sitz_in_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Produzent Wohnsitz/Sitz in der Schweiz hat"
    reference = "SR 443.1 Art. 2 Abs. 2 Bst. b"


class mehrheit_kapital_gl_ch_personen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Mehrheit an Kapital und Geschaeftsleitung bei CH-Personen liegt"
    reference = "SR 443.1 Art. 2 Abs. 2 Bst. b"


class ist_schweizer_film(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Film als Schweizer Film gilt"
    reference = "SR 443.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        regisseur = person('regisseur_ch_nationalitaet_oder_wohnsitz', period)
        produzent = person('produzent_sitz_in_schweiz', period)
        mehrheit = person('mehrheit_kapital_gl_ch_personen', period)
        return regisseur * produzent * mehrheit
