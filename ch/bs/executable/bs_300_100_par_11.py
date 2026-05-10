"""BS 300.100 § 11

Generated from: ch/bs/de/300.100.md

§ 11 Grundsatz (Zahnpflege): The canton ensures social dental care in
cooperation with private providers. It may operate dental clinics for
adults and for children/youth. It may agree on tariffs with dental
associations for economically disadvantaged BS residents.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bs_wirtschaftlich_schwaecher_gestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Wirtschaftlich schwaecher gestellt (BS 300.100 § 11 Abs. 3)"
    reference = "BS 300.100 § 11 Abs. 3"


class bs_soziale_zahnpflege_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Berechtigt fuer soziale Zahnpflege mit vereinbartem Tarif (BS 300.100 § 11)"
    reference = "BS 300.100 § 11 Abs. 3"

    def formula(person, period, parameters):
        wohnsitz = person('bs_wohnsitz_bs', period)
        schwaecher = person('bs_wirtschaftlich_schwaecher_gestellt', period)
        return wohnsitz * schwaecher
