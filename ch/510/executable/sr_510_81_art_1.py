"""SR 510.81 Art. 1 - Geltungsbereich

Generated from: ch/510/de/510.81.md

Diese Verordnung regelt die Befreiung von Zoellen und bestimmten Steuern
fuer Truppen von Teilnehmerstaaten der Partnerschaft fuer den Frieden
(PfP-Truppen), fuer Mitglieder dieser Truppe und das entsprechende
zivile Gefolge.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_pfp_truppe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um Truppen eines Teilnehmerstaats der Partnerschaft fuer den Frieden (PfP) handelt"
    reference = "SR 510.81 Art. 1"


class ist_mitglied_pfp_truppe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Mitglied einer PfP-Truppe ist"
    reference = "SR 510.81 Art. 1"


class ist_ziviles_gefolge_pfp(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person zum zivilen Gefolge einer PfP-Truppe gehoert"
    reference = "SR 510.81 Art. 1"
