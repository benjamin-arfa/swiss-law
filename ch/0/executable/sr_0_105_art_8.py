"""SR 0.105 Art. 8

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# List of Art. 4 crimes, parameterizable
ARTICLE_4_CRIMES = {
    "crime_1",
    "crime_2",
}

class ahv_extradition_crimes(Variable):
    value_type = bool
    unit = 'currency'
    entity = Person
    definition_period = NONE  # Not applicable
    label = "AHV extradition crimes (Art. 8 SR 0.105)"

    def formula(person, period, parameters):
        # Using a fixed set in this example, but can be parameterized

        # Assuming person has the following variables
        # person("is_crime_1", period), person("is_crime_2", period), ...

        # This is a simplified example; the actual implementation
        # would require defining the parameters and using them to access the variable values
        # ahv_extradition_crimes = person("has_extradition_crimes", period)

        crimes_map = {
            # Map variable to Article 4 crime
            "crime_1": person("is_crime_1"),
            "crime_2": person("is_crime_2"),
        }

        return person(count=crimes_map)
