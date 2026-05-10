"""SR 0.131.351.4 Art. 2

Generated from: ch/0/de/0.131.351.4.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class engagement_country(Variable):
    value_type = String
    default_value = "Einsatzstaat"
    label = "Engagement Country (Art. 2 SR 0.131.351.4)"

    def formula_implementation(strucdata, period, parameters):
        return strucdata

class sending_country(Variable):
    value_type = String
    default_value = "Entsendestaat"
    label = "Sending Country (Art. 2 SR 0.131.351.4)"

    def formula_implementation(strucdata, period, parameters):
        return strucdata

class equipment_items(Variable):
    value_type = String
    default_value = "Ausrüstungsgegenstände"
    label = "Equipment Items (Art. 2 SR 0.131.351.4)"

    def formula_implementation(strucdata, period, parameters):
        return strucdata

class relief_goods(Variable):
    value_type = String
    default_value = "Hilfsgüter"
    label = "Relief Goods (Art. 2 SR 0.131.351.4)"

    def formula_implementation(strucdata, period, parameters):
        return strucdata

class relief_teams(Variable):
    value_type = String
    default_value = "Hilfsmannschaften"
    label = "Relief Teams (Art. 2 SR 0.131.351.4)"

    def formula_implementation(strucdata, period, parameters):
        return strucdata
