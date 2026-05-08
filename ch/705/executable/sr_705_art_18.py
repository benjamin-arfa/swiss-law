"""SR 705 Art. 18 - Beschwerdelegitimation (Right to Appeal)

Generated from: ch/de/705.md
Municipalities and cantons have standing to appeal against decisions
affecting bicycle paths. Municipalities that did not appeal may only
rejoin proceedings if the decision is changed in favor of another party.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class gemeinde_beschwerdeberechtigt_veloweg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gemeinde ist zur Beschwerde berechtigt, sofern ihr Gebiet von Veloweg-Verfuegung betroffen ist"
    reference = "SR 705 Art. 18 Abs. 1"
    default_value = False


class kanton_beschwerdeberechtigt_veloweg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kanton ist zur Beschwerde gegen Bundesverfuegungen im Bereich Velowege berechtigt"
    reference = "SR 705 Art. 18 Abs. 2"

    def formula(person, period, parameters):
        return True
