"""SR 143.13 Art. 2

Generated from: ch/143/de/143.13.md

Pass 2003 and Pass 2006: Applications must be submitted by 15 February 2010
at the latest. Issuing authorities enter applications by 23 February 2010.
Personal appearance for biometric data capture for Pass 2006 by 23 February 2010.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antrag_pass_2003_oder_2006_eingereicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Antrag fuer Pass 2003 oder Pass 2006 eingereicht wurde"
    reference = "SR 143.13 Art. 2 Abs. 1"


class antrag_frist_pass_2003_2006(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Letzte Frist fuer Einreichung eines Antrags fuer Pass 2003/2006"
    reference = "SR 143.13 Art. 2 Abs. 1"
    default_value = "2010-02-15"


class eingabe_isa_frist(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Letzte Frist fuer Eingabe und Produktionsfreigabe im ISA durch ausstellende Behoerden"
    reference = "SR 143.13 Art. 2 Abs. 2"
    default_value = "2010-02-23"


class biometrische_erfassung_frist_pass_2006(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Letzte Frist fuer persoenliche Vorsprache zur Erfassung biometrischer Daten fuer Pass 2006"
    reference = "SR 143.13 Art. 2 Abs. 3"
    default_value = "2010-02-23"
