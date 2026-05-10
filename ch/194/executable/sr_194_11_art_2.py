"""SR 194.11 Art. 2 - Besondere Aufgaben der Landeskommunikation im Falle einer Imagebedrohung oder -krise

Generated from: ch/194/de/194.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class ansehen_schweiz_im_ausland_ernsthaft_bedroht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Ansehen der Schweiz im Ausland ist ernsthaft bedroht"
    reference = "SR 194.11 Art. 2"


class imagekrise_eingetreten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine Imagekrise ist bereits eingetreten"
    reference = "SR 194.11 Art. 2"


# Computed variables

class eda_muss_kommunikationskonzept_vorlegen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das EDA unterbreitet dem Bundesrat ein Kommunikationskonzept"
    reference = "SR 194.11 Art. 2"

    def formula(self, period, parameters):
        bedroht = self('ansehen_schweiz_im_ausland_ernsthaft_bedroht', period)
        krise = self('imagekrise_eingetreten', period)
        return bedroht + krise > 0
