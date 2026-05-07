"""SR 744.21 Art. 18a

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class sr_744_21_art_18a_bundesrat_abgaben_vollzug(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SR 744.21 Art. 18a: Der Bundesrat setzt die für den Vollzug des Eisenbahngesetzes zu erhebenden Abgaben fest."
    reference = "https://www.fedlex.admin.ch/eli/cc/1958/335_341_347/de#art_18_a"

    def formula(person, period, parameters):
        return True
