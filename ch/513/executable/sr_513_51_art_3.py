"""SR 513.51 Art. 3

Generated from: ch/513/de/513.51.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)
Organisation = build_entity(key='organisation', plural='organisations', label='An organisation')


class jaehrlicher_bundesbeitrag_srk(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Jaehrlicher Bundesbeitrag an das SRK (Art. 3 SR 513.51)"
    reference = "SR 513.51 Art. 3"

    # Der Bund richtet dem SRK jaehrlich einen Beitrag aus.
    # Die Hoehe wird im Voranschlag festgesetzt (input variable).


class bund_gewaehrt_beitraege_an_srk(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "Bund traegt der Sonderstellung des SRK durch Beitraege Rechnung (Art. 3 Abs. 1 SR 513.51)"
    reference = "SR 513.51 Art. 3"

    def formula(organisation, period, parameters):
        return True


class srk_befreiung_taxen_gebühren_steuern(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "SRK kann von Taxen, Gebuehren und Steuern ganz oder teilweise befreit werden (Art. 3 Abs. 4 SR 513.51)"
    reference = "SR 513.51 Art. 3"

    def formula(organisation, period, parameters):
        # Erleichterungen koennen gewaehrt werden, soweit die gesetzlichen
        # Bestimmungen dies zulassen.
        return True
