"""SR 0.101.1 Art. 9

Generated from: ch/0/de/0.101.1.md
"""

from openfisca_core.model_api import Variable

class territorial_scope(Variable):
    value_type = bool
    default_value = False
    label = "Territorial scope of the agreement"
    definition_period = "year"

    parameters = [
        {
            "name": "territories",
            "values": {
                "de": ["Zürich", "Bern"],
                "fr": ["Zurich", "Berne"]
            }
        }
    ]

    def formula(territory, period, parameters):
        territories = territory("territories", period)
        declared_territories = territory("declared_territories", period)
        return territories == declared_territories
