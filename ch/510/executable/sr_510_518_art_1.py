"""SR 510.518 Art. 1 - Militaerische Anlagen

Generated from: ch/510/de/510.518.md

Als militaerische Anlagen gelten alle bestehenden oder im Bau befindlichen
Befestigungsanlagen sowie andere militaerische Anlagen, fuer welche im
Interesse der Landesverteidigung besondere Sicherheitsmassnahmen notwendig sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_militaerische_anlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine militaerische Anlage im Sinne des Bundesgesetzes handelt"
    reference = "SR 510.518 Art. 1 Abs. 1"


class ist_befestigungsanlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine bestehende oder im Bau befindliche Befestigungsanlage handelt"
    reference = "SR 510.518 Art. 1 Abs. 1"


class besondere_sicherheitsmassnahmen_notwendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob im Interesse der Landesverteidigung besondere Sicherheitsmassnahmen notwendig sind"
    reference = "SR 510.518 Art. 1 Abs. 1"


class durch_bundesrat_bezeichnete_anlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die militaerische Anlage durch den Bundesrat bezeichnet wurde"
    reference = "SR 510.518 Art. 1 Abs. 2"


class anlage_unterliegt_schutzgesetz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Anlage dem Bundesgesetz ueber den Schutz militaerischer Anlagen unterliegt"
    reference = "SR 510.518 Art. 1"

    def formula(person, period, parameters):
        ist_mil = person('ist_militaerische_anlage', period)
        bezeichnet = person('durch_bundesrat_bezeichnete_anlage', period)
        return ist_mil * bezeichnet
