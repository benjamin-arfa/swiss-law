"""SR 0.120 Art. 97

Generated from: ch/0/de/0.120.md
"""

from openfisca_core.model_api import *

class secretary_officials(Variable):
    value_type = lambda: list  # to represent the list of officials
    entity = None
    definition_period = YTD
    label = "list of Secretary-Office officials"

    def formula(social_security, period, parameters):
        return social_security.entities["secretary_office"].officials


class secretary_office(Entity):
    label = "Secretary Office of the OECD"
    entity_class = "Place"

    def __init__(self, region, country, year_start=2000):
        super secretary_office, self).__init__()
        self.region = region
        self.country = country
        self.year_start = year_start
        self.officials = []

    def add_official(self, name, surname, birthdate, position: str, year):
        new_official = {
            "name": name,
            "surname": surname,
            "birthdate": birthdate,
            "position": position,
            "year": year
        }
        self.officials.append(new_official)

    def remove_official(self, position, year):
        self.officials = [official for official in self.officials if (official ["position"] != position) or (official["year"] != year)]
