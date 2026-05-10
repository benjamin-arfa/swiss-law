"""SR 241 Art. 3a

Generated from: ch/de/241.md

Discrimination in distance selling: price discrimination, blocking
or redirecting access to online portals based on nationality,
domicile, place of establishment, payment service provider, or
payment instrument origin.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class diskriminierung_preis_fernhandel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Kunde im Fernhandel beim Preis oder bei Zahlungsbedingungen diskriminiert wird"
    reference = "SR 241 Art. 3a Abs. 1 Bst. a"


class zugang_online_portal_blockiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Zugang zu einem Online-Portal blockiert oder beschraenkt wird"
    reference = "SR 241 Art. 3a Abs. 1 Bst. b"


class weiterleitung_andere_version(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kunde ohne Einverstaendnis zu einer anderen Version weitergeleitet wird"
    reference = "SR 241 Art. 3a Abs. 1 Bst. c"


class sachliche_rechtfertigung_fernhandel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine sachliche Rechtfertigung fuer die Diskriminierung vorliegt"
    reference = "SR 241 Art. 3a Abs. 1"


class diskriminierung_fernhandel_unlauter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine unlautere Diskriminierung im Fernhandel vorliegt"
    reference = "SR 241 Art. 3a"

    def formula(person, period, parameters):
        diskriminierung = (
            person('diskriminierung_preis_fernhandel', period)
            + person('zugang_online_portal_blockiert', period)
            + person('weiterleitung_andere_version', period)
        ) > 0
        keine_rechtfertigung = 1 - person('sachliche_rechtfertigung_fernhandel', period)
        return diskriminierung * keine_rechtfertigung
