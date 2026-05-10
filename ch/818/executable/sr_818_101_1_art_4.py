"""SR 818.101.1 Art. 4

Generated from: ch/818/de/818.101.1.md

Gegenstand der Meldepflicht: Beobachtungen in Ausuebung der beruflichen
Taetigkeit, Spitaeler und Laboratorien muessen die Meldetaetigkeit sicherstellen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_meldepflichtige_fachperson(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person eine meldepflichtige Fachperson ist (Aerztin/Arzt, Spital, Labor)"
    reference = "SR 818.101.1 Art. 4 Abs. 1"


class hat_meldepflichtige_beobachtung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine meldepflichtige Beobachtung in Ausuebung der beruflichen Taetigkeit gemacht wurde"
    reference = "SR 818.101.1 Art. 4 Abs. 1"


class ist_spital_oder_institution(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person ein Spital oder eine Institution des Gesundheitswesens vertritt"
    reference = "SR 818.101.1 Art. 4 Abs. 2"


class ist_laboratorium(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person ein Laboratorium vertritt"
    reference = "SR 818.101.1 Art. 4 Abs. 2"


class meldepflicht_uebertragbare_krankheiten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Meldepflicht fuer uebertragbare Krankheiten besteht"
    reference = "SR 818.101.1 Art. 4"

    def formula(person, period, parameters):
        ist_fachperson = person('ist_meldepflichtige_fachperson', period)
        hat_beobachtung = person('hat_meldepflichtige_beobachtung', period)
        return ist_fachperson * hat_beobachtung
