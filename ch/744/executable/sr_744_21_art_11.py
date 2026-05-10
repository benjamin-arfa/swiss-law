"""SR 744.21 Art. 11

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_trolleybus_anlage(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bauten und Anlagen dienen ganz oder überwiegend dem Bau und Betrieb einer Trolleybuslinie"
    reference = "SR 744.21 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        dient_ganz = person('anlage_dient_ganz_trolleybuslinie', period)
        dient_ueberwiegend = person('anlage_dient_ueberwiegend_trolleybuslinie', period)
        return dient_ganz + dient_ueberwiegend


class anlage_dient_ganz_trolleybuslinie(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anlage dient ganz dem Bau und Betrieb einer Trolleybuslinie"
    reference = "SR 744.21 Art. 11 Abs. 1"


class anlage_dient_ueberwiegend_trolleybuslinie(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anlage dient überwiegend dem Bau und Betrieb einer Trolleybuslinie"
    reference = "SR 744.21 Art. 11 Abs. 1"


class plangenehmigung_aufsichtsbehoerde_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybusanlage darf nur mit Plangenehmigung der Aufsichtsbehörde erstellt oder geändert werden"
    reference = "SR 744.21 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        ist_anlage = person('ist_trolleybus_anlage', period)
        wird_erstellt_oder_geaendert = person('trolleybusanlage_wird_erstellt_oder_geaendert', period)
        return ist_anlage * wird_erstellt_oder_geaendert


class trolleybusanlage_wird_erstellt_oder_geaendert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trolleybusanlage wird erstellt oder geändert"
    reference = "SR 744.21 Art. 11 Abs. 1"


class plangenehmigungsverfahren_nach_eisenbahngesetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Plangenehmigungsverfahren richtet sich nach dem Eisenbahngesetz vom 20. Dezember 1957 (SR 742.101)"
    reference = "SR 744.21 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        # Whenever plan approval is required for a trolleybus installation,
        # the procedure follows the Railway Act (SR 742.101) by operation of law.
        return person('plangenehmigung_aufsichtsbehoerde_erforderlich', period)
