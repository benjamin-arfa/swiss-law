"""SR 192.121 Art. 7

Generated from: ch/192/de/192.121.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class quasizwischenstaatliche_org_archiv_unverletzlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unverletzlichkeit der Archive einer quasizwischenstaatlichen Organisation"
    reference = "SR 192.121 Art. 7"

class quasizwischenstaatliche_org_direkte_steuer_befreit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befreiung von direkten Steuern fuer quasizwischenstaatliche Organisation"
    reference = "SR 192.121 Art. 7"

class quasizwischenstaatliche_org_indirekte_steuer_befreit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befreiung von indirekten Steuern fuer quasizwischenstaatliche Organisation"
    reference = "SR 192.121 Art. 7"

class quasizwischenstaatliche_org_freie_finanzmittel(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Freie Verfuegung ueber Finanzmittel fuer quasizwischenstaatliche Organisation"
    reference = "SR 192.121 Art. 7"
