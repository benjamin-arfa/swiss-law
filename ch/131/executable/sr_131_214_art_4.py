"""SR 131.214 Art. 4

Generated from: ch/131/de/131.214.md

Staatshaftung: Der Kanton, Gemeinden und öffentlichrechtliche Körperschaften
haften für widerrechtlich verursachten Schaden ihrer Organe. Widerrechtlich
in persönlicher Freiheit Eingeschränkte oder schuldlos Verhaftete haben
Anspruch auf Schadenersatz und Genugtuung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class organ_handelt_amtlich_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Organ in Ausübung amtlicher Tätigkeit handelt"
    reference = "SR 131.214 Art. 4 Abs. 1"


class schaden_widerrechtlich_verursacht_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Schaden widerrechtlich verursacht wurde"
    reference = "SR 131.214 Art. 4 Abs. 1"


class staatshaftung_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kanton Uri für den Schaden haftet"
    reference = "SR 131.214 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        amtlich = person('organ_handelt_amtlich_uri', period)
        widerrechtlich = person('schaden_widerrechtlich_verursacht_uri', period)
        return amtlich * widerrechtlich


class freiheit_widerrechtlich_eingeschraenkt_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person in ihrer persönlichen Freiheit widerrechtlich schwer eingeschränkt wurde"
    reference = "SR 131.214 Art. 4 Abs. 2"


class schuldlos_verhaftet_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person schuldlos verhaftet wurde"
    reference = "SR 131.214 Art. 4 Abs. 2"


class anspruch_schadenersatz_genugtuung_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Anspruch auf Schadenersatz und Genugtuung hat"
    reference = "SR 131.214 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        freiheit = person('freiheit_widerrechtlich_eingeschraenkt_uri', period)
        verhaftet = person('schuldlos_verhaftet_uri', period)
        return freiheit + verhaftet > 0
