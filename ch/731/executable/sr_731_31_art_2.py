"""SR 731.31 Art. 2

Generated from: ch/731/de/731.31.md

Definition of systemically critical companies (systemkritische Unternehmen).
Criteria: Swiss seat + >=1200 MW installed capacity + participation in
organized electricity markets.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_sitz_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen hat Sitz in der Schweiz"
    reference = "SR 731.31 Art. 2 Abs. 1 lit. a"


class firevo_kraftwerksleistung_mw(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "In der Schweiz installierte Kraftwerksleistung (Megawatt)"
    reference = "SR 731.31 Art. 2 Abs. 1 lit. b Ziff. 1"


class firevo_teilnahme_organisierte_maerkte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Teilnahme an organisierten Maerkten fuer Elektrizitaet"
    reference = "SR 731.31 Art. 2 Abs. 1 lit. b Ziff. 2"


class firevo_systemkritisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen ist systemkritisch im Sinne der FiREVO"
    reference = "SR 731.31 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        """Art. 2 Abs. 1: A company is systemically critical if it:
        a. has its seat in Switzerland; and
        b. directly or via affiliates:
           1. has >= 1200 MW installed capacity in Switzerland, and
           2. participates in organized electricity markets.
        """
        sitz = person('firevo_sitz_schweiz', period)
        leistung = person('firevo_kraftwerksleistung_mw', period)
        maerkte = person('firevo_teilnahme_organisierte_maerkte', period)

        mindestleistung = 1200.0  # MW threshold

        return sitz * (leistung >= mindestleistung) * maerkte


class firevo_systemkritisch_uvek(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vom UVEK als systemkritisch verfuegt (Art. 2 Abs. 2)"
    reference = "SR 731.31 Art. 2 Abs. 2"


class firevo_ist_systemkritisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen gilt als systemkritisch (automatisch oder per Verfuegung)"
    reference = "SR 731.31 Art. 2"

    def formula(person, period, parameters):
        auto = person('firevo_systemkritisch', period)
        uvek = person('firevo_systemkritisch_uvek', period)
        return auto + uvek
