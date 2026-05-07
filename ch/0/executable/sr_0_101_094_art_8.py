"""SR 0.101.094 Art. 8

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import Variable

class Ausschuss_Power_Unanimous_Inadmissible(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "The committee can declare the complaint inadmissible without further review"
    default = False

    def formula person(areas, period, datasets, other_variables):
        # assume that the other_variable 'is_complaint_inadmissible' is true if the committee has declared the complaint inadmissible
        return areas['is_complaint_inadmissible']  # implement logic for this variable
