"""SR 744.21 Art. 13

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vehicle_has_operating_authorization(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug oder Anhänger hat vorherige Betriebsbewilligung der Aufsichtsbehörde"
    reference = "SR 744.21 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        return person('supervisory_authority_granted_authorization', period)


class vehicle_carries_company_identifier(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug trägt das Kennzeichen des Unternehmens"
    reference = "SR 744.21 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        return person('company_identifier_displayed_on_vehicle', period)


class vehicle_carries_number(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug trägt eine Nummer"
    reference = "SR 744.21 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        return person('vehicle_number_assigned_and_displayed', period)


class vehicle_authorization_replaces_registration(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bewilligung ersetzt den Fahrzeugausweis; Nummer ersetzt das Kontrollschild"
    reference = "SR 744.21 Art. 13 Abs. 2"

    def formula(person, period, parameters):
        has_authorization = person('vehicle_has_operating_authorization', period)
        return has_authorization


class vehicle_authorized_for_traffic(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeug/Anhänger erfüllt alle Voraussetzungen zur Zulassung zum Verkehr und Betriebseröffnung gemäss Art. 13"
    reference = "SR 744.21 Art. 13"

    def formula(person, period, parameters):
        has_authorization = person('vehicle_has_operating_authorization', period)
        has_company_identifier = person('vehicle_carries_company_identifier', period)
        has_number = person('vehicle_carries_number', period)
        return has_authorization * has_company_identifier * has_number


class supervisory_authority_granted_authorization(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aufsichtsbehörde hat die Bewilligung erteilt"
    reference = "SR 744.21 Art. 13 Abs. 1"


class company_identifier_displayed_on_vehicle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kennzeichen des Unternehmens am Fahrzeug angebracht"
    reference = "SR 744.21 Art. 13 Abs. 1"


class vehicle_number_assigned_and_displayed(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugnummer zugeteilt und angebracht"
    reference = "SR 744.21 Art. 13 Abs. 1"


class authorization_communicated_to_company(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bewilligung dem Unternehmen mitgeteilt"
    reference = "SR 744.21 Art. 13 Abs. 2"


class authorization_communicated_to_cantonal_authority(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bewilligung der zuständigen kantonalen Behörde mitgeteilt"
    reference = "SR 744.21 Art. 13 Abs. 2"


class authorization_fully_communicated(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bewilligung sowohl dem Unternehmen als auch der kantonalen Behörde mitgeteilt"
    reference = "SR 744.21 Art. 13 Abs. 2"

    def formula(person, period, parameters):
        communicated_to_company = person('authorization_communicated_to_company', period)
        communicated_to_canton = person('authorization_communicated_to_cantonal_authority', period)
        return communicated_to_company * communicated_to_canton
