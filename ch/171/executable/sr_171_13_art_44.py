"""SR 171.13 Art. 44

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class redezeit_berichterstatter_eintretensdebatte_minuten(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Redezeit der Berichterstatter der Kommissionen in der Eintretensdebatte (insgesamt, Minuten)"
    reference = "SR 171.13 Art. 44 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return 20


class redezeit_bundesrat_eintretensdebatte_minuten(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Redezeit der Vertreterin oder des Vertreters des Bundesrates in der Eintretensdebatte (Minuten)"
    reference = "SR 171.13 Art. 44 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        return 20


class redezeit_fraktionssprecher_eintretensdebatte_minuten(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Redezeit der Fraktionssprecher in der Eintretensdebatte (je, Minuten)"
    reference = "SR 171.13 Art. 44 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        return 10


class redezeit_uebrige_redner_eintretensdebatte_minuten(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Redezeit der übrigen Rednerinnen und Redner in der Eintretensdebatte (Minuten)"
    reference = "SR 171.13 Art. 44 Abs. 1 Bst. d"

    def formula(person, period, parameters):
        return 5


class redezeit_andere_debatten_minuten(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Redezeit in anderen Debatten für Fraktionssprecher, Antragsteller, Urheber und Einzelredner (Minuten)"
    reference = "SR 171.13 Art. 44 Abs. 2"

    def formula(person, period, parameters):
        return 5
