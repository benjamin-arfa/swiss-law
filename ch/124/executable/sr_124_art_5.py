"""SR 124 Art. 5 - Ausbildung des Personals (Personnel Training)

Generated from: ch/de/124.md
Personnel must have adequate training covering: fundamental rights,
use of force, handling resistant persons, first aid, health risk assessment,
anti-corruption. Additional international law training for foreign missions.
Exception possible abroad if no qualified company available (max 6 months).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class sicherheitspersonal_grundrechte_ausbildung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitspersonal hat Ausbildung in Grundrechten und Persoenlichkeitsschutz"
    reference = "SR 124 Art. 5 Abs. 1 lit. a"
    default_value = False


class sicherheitspersonal_gewalt_ausbildung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitspersonal hat Ausbildung im Einsatz von koerperlicher Gewalt und Waffen"
    reference = "SR 124 Art. 5 Abs. 1 lit. b"
    default_value = False


class sicherheitspersonal_erste_hilfe_ausbildung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitspersonal hat Ausbildung in Erster Hilfe"
    reference = "SR 124 Art. 5 Abs. 1 lit. d"
    default_value = False


class sicherheitspersonal_ausnahme_ausland_max_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Vertragsdauer bei Ausnahme von Ausbildungsanforderungen im Ausland (Monate)"
    reference = "SR 124 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        return 6
