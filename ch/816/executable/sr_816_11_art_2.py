"""SR 816.11 Art. 2

Generated from: ch/816/de/816.11.md

Zugriffsrechte: Patientin/Patient kann Gesundheitsfachpersonen Zugriffsrechte
erteilen. In Notfallsituationen haben auch nicht berechtigte Fachpersonen Zugriff.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_gesundheitsfachperson(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person eine Gesundheitsfachperson ist"
    reference = "SR 816.11 Art. 2 Abs. 1"


class hat_zugriffsrecht_erteilt_bekommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Gesundheitsfachperson ein Zugriffsrecht erteilt wurde"
    reference = "SR 816.11 Art. 2 Abs. 1"


class ist_medizinische_notfallsituation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine medizinische Notfallsituation vorliegt"
    reference = "SR 816.11 Art. 2 Abs. 2"


# Encoding: 0=kein Zugriff, 1=nur normal, 2=normal+eingeschraenkt
class zugriffsrecht_stufe(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Stufe des erteilten Zugriffsrechts (0=kein, 1=normal, 2=normal+eingeschraenkt)"
    reference = "SR 816.11 Art. 2 Abs. 1"


class hat_zugriff_auf_epd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Gesundheitsfachperson auf das EPD zugreifen darf"
    reference = "SR 816.11 Art. 2"

    def formula(person, period, parameters):
        ist_fachperson = person('ist_gesundheitsfachperson', period)
        hat_recht = person('hat_zugriffsrecht_erteilt_bekommen', period)
        notfall = person('ist_medizinische_notfallsituation', period)
        # Zugriff: berechtigte Fachperson ODER Fachperson im Notfall
        return ist_fachperson * (hat_recht + notfall > 0)
