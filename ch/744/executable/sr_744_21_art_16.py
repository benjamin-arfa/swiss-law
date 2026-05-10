"""SR 744.21 Art. 16

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class has_liability_insurance(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen hat eine Haftpflichtversicherung abgeschlossen (Art. 16 Abs. 1)"
    reference = "SR 744.21 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        return person('insurance_with_approved_insurer', period) * person('insurance_contract_approved', period)


class insurance_meets_minimum_amount(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Versicherungssumme entspricht mindestens dem gesetzlichen Minimum für schwere Motorwagen zum Personentransport (Art. 16 Abs. 1)"
    reference = "SR 744.21 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        insured_amount = person('liability_insurance_amount', period)
        minimum_amount = person('minimum_insurance_amount_heavy_vehicle_passenger', period)
        return insured_amount >= minimum_amount


class liability_insurance_amount(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Versicherungssumme der Haftpflichtversicherung des Unternehmens (CHF)"
    reference = "SR 744.21 Art. 16 Abs. 1"


class minimum_insurance_amount_heavy_vehicle_passenger(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mindestversicherungssumme gemäss Bundesgesetzgebung über Motorfahrzeugverkehr für schwere Motorwagen zum Personentransport (CHF)"
    reference = "SR 744.21 Art. 16 Abs. 1"


class insurance_with_approved_insurer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Versicherung bei einem vom Bundesrat zugelassenen oder von der Aufsichtsbehörde anerkannten Versicherungsunternehmen abgeschlossen (Art. 16 Abs. 2)"
    reference = "SR 744.21 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        federal_council_approved = person('insurer_approved_by_federal_council', period)
        supervisory_authority_approved = person('insurer_recognised_by_supervisory_authority', period)
        return federal_council_approved + supervisory_authority_approved


class insurer_approved_by_federal_council(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Versicherer ist vom Bundesrat in der Schweiz zum Geschäftsbetrieb zugelassen"
    reference = "SR 744.21 Art. 16 Abs. 2"


class insurer_recognised_by_supervisory_authority(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Versicherer ist von der Aufsichtsbehörde als Einrichtung anerkannt"
    reference = "SR 744.21 Art. 16 Abs. 2"


class insurance_contract_approved(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Versicherungsvertrag wurde von der Aufsichtsbehörde genehmigt (Art. 16 Abs. 2)"
    reference = "SR 744.21 Art. 16 Abs. 2"


class operation_permitted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Betrieb darf eröffnet oder aufrechterhalten werden – Versicherung muss bestehen (Art. 16 Abs. 3)"
    reference = "SR 744.21 Art. 16 Abs. 3"

    def formula(person, period, parameters):
        insurance_active = person('insurance_currently_active', period)
        insurance_valid = person('has_liability_insurance', period.this_year)
        meets_minimum = person('insurance_meets_minimum_amount', period.this_year)
        return insurance_active * insurance_valid * meets_minimum


class insurance_currently_active(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Versicherung ist im laufenden Monat aktiv (nicht ausgesetzt oder beendet) (Art. 16 Abs. 3)"
    reference = "SR 744.21 Art. 16 Abs. 3"


class insurer_reported_suspension_to_supervisory_authority(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Versicherer hat Aussetzen oder Aufhören der Versicherung der Aufsichtsbehörde gemeldet (Art. 16 Abs. 3)"
    reference = "SR 744.21 Art. 16 Abs. 3"
