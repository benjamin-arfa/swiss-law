"""SR 734.0 Art. 3a

Generated from: ch/734/de/734.0.md

Gebuehren fuer Verfuegungen, Kontrollen und Dienstleistungen:
1. Der Bundesrat erlasst Bestimmungen ueber die Erhebung von angemessenen
   Gebuehren fuer Verfuegungen, Kontrollen und Dienstleistungen der
   Bundesverwaltung und des Starkstrominspektorats.
2. Das BFE erhebt von den Betreiberinnen angemessene Gebuehren fuer den
   Aufwand in den Kantonen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eleg_ist_anlagenbetreiber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Betreiberin einer Stark- oder Schwachstromanlage ist"
    reference = "SR 734.0 Art. 3a Abs. 2"


class eleg_gebuehrenpflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person gebuehrenpflichtig fuer Kontrollen/Dienstleistungen ist"
    reference = "SR 734.0 Art. 3a"

    def formula(person, period, parameters):
        betreiber = person('eleg_ist_anlagenbetreiber', period)
        return betreiber
