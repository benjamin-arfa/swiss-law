"""SR 371 Art. 7 - Gesuch (Application)

Generated from: ch/de/371.md
Applications can be filed by the convicted person, their relatives after death,
or by Swiss human rights / historical research organizations.
Organizations may not file against the will of the person or their relatives.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class ist_angehoerige_verurteilter_person(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Angehoerige/r einer verurteilten Person nach StGB Art. 110 Ziff. 1"
    reference = "SR 371 Art. 7 Abs. 2 lit. a"
    default_value = False


class ist_berechtigte_organisation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation mit Sitz in der Schweiz, schweizerisch beherrscht, fuer Menschenrechte oder Geschichtsaufarbeitung"
    reference = "SR 371 Art. 7 Abs. 2 lit. b"
    default_value = False


class gesuchsberechtigt_rehabilitierung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigt, ein Gesuch um Feststellung der Aufhebung zu stellen"
    reference = "SR 371 Art. 7"

    def formula(person, period, parameters):
        ist_helfer = person('gilt_als_fluechtlingshelfer', period)
        ist_angehoerig = person('ist_angehoerige_verurteilter_person', period)
        ist_org = person('ist_berechtigte_organisation', period)
        return ist_helfer + ist_angehoerig + ist_org
