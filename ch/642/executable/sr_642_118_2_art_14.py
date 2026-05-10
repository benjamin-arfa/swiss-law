"""SR 642.118.2 Art. 14

Generated from: ch/642/de/642.118.2.md

Art. 14: Nachtraegliche ordentliche Veranlagung bei Quasi-Ansaessigkeit -
Persons taxable under Art. 5(1) DBG who earn at least 90% of worldwide
gross income in Switzerland qualify as quasi-residents and may request
subsequent ordinary assessment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class quellensteuer_weltweite_bruttoeinkuenfte(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Weltweite Bruttoeinkuenfte inkl. Ehepartner (CHF/Jahr)"
    reference = "SR 642.118.2 Art. 14 Abs. 2"


class quellensteuer_in_ch_steuerbare_bruttoeinkuenfte(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "In der Schweiz steuerbare Bruttoeinkuenfte (CHF/Jahr)"
    reference = "SR 642.118.2 Art. 14 Abs. 2"


class quellensteuer_ist_grenzgaenger_it_art2b(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Grenzgaenger/in nach Art. 2 Bst. b Grenzgaengerabkommen CH-IT"
    reference = "SR 642.118.2 Art. 14 Abs. 3"


class quellensteuer_quasi_ansaessigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Quasi-Ansaessigkeit: mindestens 90% der weltweiten Bruttoeinkuenfte "
        "werden in der Schweiz versteuert"
    )
    reference = "SR 642.118.2 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        weltweit = person('quellensteuer_weltweite_bruttoeinkuenfte', period)
        in_ch = person('quellensteuer_in_ch_steuerbare_bruttoeinkuenfte', period)
        ist_it_grenzgaenger = person('quellensteuer_ist_grenzgaenger_it_art2b', period)

        # Abs. 1: mindestens 90 Prozent der weltweiten Bruttoeinkuenfte in CH
        anteil_ch = where(weltweit > 0, in_ch / weltweit, 0)
        quasi_ansaessig = anteil_ch >= 0.90

        # Abs. 3: Grenzgaenger nach Art. 2 Bst. b CH-IT sind ausgeschlossen
        return quasi_ansaessig * ~ist_it_grenzgaenger
