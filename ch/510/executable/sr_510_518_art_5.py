"""SR 510.518 Art. 5 - Veroeffentlichungsverbot

Generated from: ch/510/de/510.518.md

Es ist verboten, ohne Bewilligung zu veroeffentlichen oder in den Verkehr
zu bringen: Photographien, Filme, Zeichnungen, Beschreibungen und Berichte
ueber militaerische Anlagen oder ueber militaerische Uebungen in solchen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_bewilligung_veroeffentlichung_mil_anlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Bewilligung zur Veroeffentlichung von Darstellungen/Berichten ueber militaerische Anlagen vorliegt"
    reference = "SR 510.518 Art. 5"


class veroeffentlichung_mil_anlage_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Veroeffentlichung von Darstellungen und Berichten ueber militaerische Anlagen verboten ist"
    reference = "SR 510.518 Art. 5"

    def formula(person, period, parameters):
        return not_(person('hat_bewilligung_veroeffentlichung_mil_anlage', period))
