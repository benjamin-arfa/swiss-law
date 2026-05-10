"""SR 0.641.751.411 Art. 2 - Execution of environmental tax legislation

Art. 2: Swiss federal authorities enforce environmental tax legislation
on Liechtenstein territory on behalf of Liechtenstein.
- Par. 1: Swiss procedural law applies; substantive Liechtenstein law applies.
- Par. 2: Liechtenstein authorities act analogously to Swiss cantonal authorities
  for CO2 tax, emission reduction sanctions, and vehicle CO2 sanctions.
- Par. 3: Infractions prosecuted by competent Swiss/Liechtenstein authorities.

Generated from: ch/0/fr/0.641.751.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class autorites_federales_executent_li(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Swiss federal authorities enforce environmental tax law in LI (Art. 2 par. 1)"

    def formula(person, period, parameters):
        return person("entreprise_soumise_taxes_environnementales_li", period)


class droit_procedure_suisse_applicable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Swiss procedural law applies in Liechtenstein (Art. 2 par. 1)"

    def formula(person, period, parameters):
        return person("entreprise_soumise_taxes_environnementales_li", period)


class autorites_li_role_cantonal(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "LI authorities act analogously to Swiss cantonal authorities (Art. 2 par. 2)"

    def formula(person, period, parameters):
        return person("entreprise_soumise_taxes_environnementales_li", period)
