"""SR 744.21 Art. 3

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unterliegt_bundesgesetzgebung_verpfaendung_eisenbahn(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen unterliegt Bundesgesetzgebung über Verpfändung und Zwangsliquidation von Eisenbahnunternehmen (SR 744.21 Art. 3 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1959/317_341_347/de#art_3"

    def formula(person, period, parameters):
        # Art. 3 Abs. 1: Companies subject to this law are subject to federal
        # legislation on pledging and forced liquidation of railway companies.
        unterliegt_gesetz = person('unterliegt_sr_744_21', period)
        return unterliegt_gesetz


class unterliegt_sr_744_21(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen unterliegt dem Gesetz SR 744.21 (Trolleybusgesetz)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1959/317_341_347/de"

    def formula(person, period, parameters):
        return person('ist_trolleybus_unternehmen', period)


class ist_trolleybus_unternehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Betreiber eines dem SR 744.21 unterstehenden Trolleybusunternehmens"
    reference = "https://www.fedlex.admin.ch/eli/cc/1959/317_341_347/de"


class pfandrecht_umfasst_elektrische_anlagen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pfandrecht umfasst dem elektrischen Betrieb dienende Grundstücke, Hochbauten und elektrische Anlagen (SR 744.21 Art. 3 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1959/317_341_347/de#art_3"

    def formula(person, period, parameters):
        # Art. 3 Abs. 2: The lien covers real estate, buildings, and electrical
        # installations used for electric operations.
        pfandrecht_besteht = person('unterliegt_bundesgesetzgebung_verpfaendung_eisenbahn', period)
        hat_elektrische_anlagen = person('hat_dem_elektrischen_betrieb_dienende_anlagen', period)
        return pfandrecht_besteht * hat_elektrische_anlagen


class hat_dem_elektrischen_betrieb_dienende_anlagen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen verfügt über dem elektrischen Betrieb dienende Grundstücke, Hochbauten oder elektrische Anlagen"
    reference = "https://www.fedlex.admin.ch/eli/cc/1959/317_341_347/de#art_3"
