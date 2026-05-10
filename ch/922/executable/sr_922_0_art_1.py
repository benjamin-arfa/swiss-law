"""SR 922.0 Art. 1

Generated from: ch/922/de/922.0.md

Art. 1: Zweck - Purpose of the Hunting Act (JSG):
a. Preserve species diversity and habitats of native/migratory mammals and birds
b. Protect endangered species
c. Limit wildlife damage to forest and agriculture to a tolerable level
d. Ensure appropriate use of wildlife populations through hunting
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jsg_zweck_artenvielfalt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme dient der Erhaltung der Artenvielfalt und Lebensräume wildlebender Säugetiere und Vögel"
    reference = "SR 922.0 Art. 1 Abs. 1 Bst. a"


class jsg_zweck_artenschutz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme dient dem Schutz bedrohter Tierarten"
    reference = "SR 922.0 Art. 1 Abs. 1 Bst. b"


class jsg_zweck_schadensbegrenzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme dient der Begrenzung von Wildschäden auf ein tragbares Mass"
    reference = "SR 922.0 Art. 1 Abs. 1 Bst. c"


class jsg_zweck_nutzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Massnahme gewährleistet angemessene Nutzung der Wildbestände durch Jagd"
    reference = "SR 922.0 Art. 1 Abs. 1 Bst. d"


class jsg_gesetzeszweck_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestens ein Gesetzeszweck des JSG ist erfüllt"
    reference = "SR 922.0 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        artenvielfalt = person('jsg_zweck_artenvielfalt', period)
        artenschutz = person('jsg_zweck_artenschutz', period)
        schaden = person('jsg_zweck_schadensbegrenzung', period)
        nutzung = person('jsg_zweck_nutzung', period)
        return (artenvielfalt + artenschutz + schaden + nutzung) > 0
