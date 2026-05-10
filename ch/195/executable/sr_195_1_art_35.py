"""SR 195.1 Art. 35

Generated from: ch/195/de/195.1.md

Rueckerstattungspflicht: Sozialhilfeempfaenger muessen Leistungen
zurueckerstatten wenn sie nicht mehr beduertig sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_nicht_mehr_beduertig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person keiner Sozialhilfe mehr bedarf und angemessener Lebensunterhalt gesichert ist"
    reference = "SR 195.1 Art. 35 Abs. 1"


class leistungen_vor_volljaehrigkeit_bezogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Leistungen vor der Volljaehrigkeit oder fuer die Ausbildung bezogen wurden"
    reference = "SR 195.1 Art. 35 Abs. 2"


class hat_leistungen_durch_unwahre_angaben_erwirkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Leistungen wissentlich durch unwahre oder unvollstaendige Angaben erwirkt hat"
    reference = "SR 195.1 Art. 35 Abs. 3"


class ist_erbe_mit_bereicherung_aus_nachlass(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Erbe aus dem Nachlass bereichert wird"
    reference = "SR 195.1 Art. 35 Abs. 4"


class rueckerstattungspflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person zur Rueckerstattung der Sozialhilfeleistungen verpflichtet ist"
    reference = "SR 195.1 Art. 35"

    def formula(person, period, parameters):
        nicht_beduertig = person('ist_nicht_mehr_beduertig', period)
        vor_volljaehrigkeit = person('leistungen_vor_volljaehrigkeit_bezogen', period)
        unwahre_angaben = person('hat_leistungen_durch_unwahre_angaben_erwirkt', period)
        erbe = person('ist_erbe_mit_bereicherung_aus_nachlass', period)
        # Abs. 1: Rueckerstattung wenn nicht mehr beduertig
        # Abs. 2: Ausnahme fuer Leistungen vor Volljaehrigkeit
        # Abs. 3: Immer rueckerstattungspflichtig bei unwahren Angaben
        # Abs. 4: Erben pflichtig soweit bereichert
        grundpflicht = nicht_beduertig * (1 - vor_volljaehrigkeit)
        return grundpflicht + unwahre_angaben + erbe > 0
