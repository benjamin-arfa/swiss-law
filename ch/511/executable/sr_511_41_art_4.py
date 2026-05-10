"""SR 511.41 Art. 4 – Fälligkeit und Zahlungsfrist

Generated from: ch/511/de/511.41.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class hat_altersgrenze_erreicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat die Altersgrenze für die Militärdienstpflicht erreicht"
    reference = "SR 511.41 Art. 4 Abs. 1 lit. a"
    default_value = False


class aus_armee_ausgeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aus der Armee ausgeschlossen"
    reference = "SR 511.41 Art. 4 Abs. 1 lit. b"
    default_value = False


class militaerdienstuntauglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Militärdienstuntauglich erklärt"
    reference = "SR 511.41 Art. 4 Abs. 1 lit. c"
    default_value = False


class zum_zivildienst_zugelassen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zum Zivildienst zugelassen"
    reference = "SR 511.41 Art. 4 Abs. 1 lit. d"
    default_value = False


class rueckforderung_faellig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rückforderung der Ausbildungskosten ist fällig"
    reference = "SR 511.41 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('hat_altersgrenze_erreicht', period)
            + person('aus_armee_ausgeschlossen', period)
            + person('militaerdienstuntauglich', period)
            + person('zum_zivildienst_zugelassen', period)
        )


class zahlungsfrist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Zahlungsfrist in Tagen ab Rechtskraft der Verfügung"
    reference = "SR 511.41 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        # Art. 4 Abs. 2: Die Zahlungsfrist beträgt 90 Tage
        faellig = person('rueckforderung_faellig', period)
        return where(faellig, 90, 0)
