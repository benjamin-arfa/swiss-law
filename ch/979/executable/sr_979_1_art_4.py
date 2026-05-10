"""SR 979.1 Art. 4

Generated from: ch/979/de/979.1.md

Art. 4 Durchfuehrung der Mitgliedschaft und Vertretung der Schweiz:
1. The Federal Council cooperates with the SNB for implementing IMF membership.
   Details are set in an agreement between the Federal Council and the SNB.
2. The Federal Council designates Switzerland's representatives to the
   Bretton Woods institutions; for the IMF, this is done in agreement with the SNB.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bw_vertretung_bei_institution(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Name der Bretton-Woods-Institution, bei der die Schweiz vertreten wird"
    reference = "SR 979.1 Art. 4 Abs. 2"


class bw_einvernehmen_snb_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Einvernehmen mit der SNB fuer die Bezeichnung der Vertreter erforderlich ist"
    reference = "SR 979.1 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        institution = person('bw_vertretung_bei_institution', period)
        return institution == 'iwf'
