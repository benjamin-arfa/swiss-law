"""SR 744.21 Art. 11a

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_744_21_art_11a_subject_to_railway_regulations(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Unternehmen untersteht den für Eisenbahnen gültigen Vorschriften (SR 744.21 Art. 11a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2000/116/de#art_11_a"

    def formula(person, period, parameters):
        info_supervision = person('sr_744_21_art_11a_info_supervision', period)
        accident_reporting = person('sr_744_21_art_11a_accident_reporting', period)
        data_processing_bav = person('sr_744_21_art_11a_data_processing_bav', period)
        working_rest_time = person('sr_744_21_art_11a_working_rest_time', period)
        return info_supervision * accident_reporting * data_processing_bav * working_rest_time


class sr_744_21_art_11a_info_supervision(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterstellung unter Eisenbahnvorschriften: Information über die Aufsichtstätigkeit (SR 744.21 Art. 11a Abs. 1 Bst. a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2000/116/de#art_11_a"

    def formula(person, period, parameters):
        return person('sr_744_21_art_11a_subject_to_railway_regulations_applicable', period)


class sr_744_21_art_11a_accident_reporting(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterstellung unter Eisenbahnvorschriften: Meldung und Untersuchung von Unfällen und schweren Vorfällen (SR 744.21 Art. 11a Abs. 1 Bst. b)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2000/116/de#art_11_a"

    def formula(person, period, parameters):
        return person('sr_744_21_art_11a_subject_to_railway_regulations_applicable', period)


class sr_744_21_art_11a_data_processing_bav(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterstellung unter Eisenbahnvorschriften: Datenbearbeitung durch das BAV (SR 744.21 Art. 11a Abs. 1 Bst. c)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2000/116/de#art_11_a"

    def formula(person, period, parameters):
        return person('sr_744_21_art_11a_subject_to_railway_regulations_applicable', period)


class sr_744_21_art_11a_working_rest_time(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterstellung unter Eisenbahnvorschriften: Arbeits- und Ruhezeit des Personals (SR 744.21 Art. 11a Abs. 1 Bst. d)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2000/116/de#art_11_a"

    def formula(person, period, parameters):
        return person('sr_744_21_art_11a_subject_to_railway_regulations_applicable', period)


class sr_744_21_art_11a_subject_to_railway_regulations_applicable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen untersteht den Eisenbahnvorschriften gemäss Art. 11a (vorbehältlich Art. 12–15) (SR 744.21 Art. 11a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2000/116/de#art_11_a"

    def formula(person, period, parameters):
        # Applicability is determined externally; Art. 12–15 reserved
        return person('sr_744_21_is_regulated_enterprise', period)


class sr_744_21_is_regulated_enterprise(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist ein reguliertes Unternehmen gemäss SR 744.21"
    reference = "https://www.fedlex.admin.ch/eli/cc/2000/116/de"
