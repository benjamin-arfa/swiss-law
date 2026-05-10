"""SR 642.118.2 Art. 19

Generated from: ch/642/de/642.118.2.md

Art. 19: Kapitalleistungen aus Vorsorge an im Ausland wohnhafte Empfaenger -
Capital benefits from pension funds to non-residents are always subject to
withholding tax. Refund possible within 3 years if conditions are met.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class quellensteuer_kapitalleistung_vorsorge(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kapitalleistung aus Vorsorge an im Ausland wohnhafte Person (CHF)"
    reference = "SR 642.118.2 Art. 19 Abs. 1"


class quellensteuer_kapitalleistung_wohnsitz_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Empfaenger der Kapitalleistung hat Wohnsitz im Ausland"
    reference = "SR 642.118.2 Art. 19 Abs. 1"


class quellensteuer_kapitalleistung_quellensteuerpflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Kapitalleistung aus Vorsorge unterliegt ungeachtet staatsvertraglicher "
        "Regelungen der Quellensteuer"
    )
    reference = "SR 642.118.2 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        kapitalleistung = person('quellensteuer_kapitalleistung_vorsorge', period)
        ausland = person('quellensteuer_kapitalleistung_wohnsitz_ausland', period)

        # Abs. 1: Kapitalleistungen an Auslandwohnhafte unterliegen
        # IMMER der Quellensteuer
        return (kapitalleistung > 0) * ausland


class quellensteuer_kapitalleistung_rueckerstattung_antrag_innert_frist(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Antrag auf Rueckerstattung innerhalb von 3 Jahren seit Auszahlung gestellt"
    reference = "SR 642.118.2 Art. 19 Abs. 2 Bst. a"


class quellensteuer_kapitalleistung_wohnsitzstaat_bestaetigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Bestaetigung der Steuerbehoerde des Wohnsitzstaates liegt vor "
        "(Kenntnisnahme und Ansaessigkeit im DBA-Sinn)"
    )
    reference = "SR 642.118.2 Art. 19 Abs. 2 Bst. b"


class quellensteuer_kapitalleistung_rueckerstattungsanspruch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf zinslose Rueckerstattung der Quellensteuer auf Kapitalleistung"
    reference = "SR 642.118.2 Art. 19 Abs. 2"

    def formula(person, period, parameters):
        pflichtig = person('quellensteuer_kapitalleistung_quellensteuerpflichtig', period)
        innert_frist = person(
            'quellensteuer_kapitalleistung_rueckerstattung_antrag_innert_frist', period
        )
        bestaetigung = person(
            'quellensteuer_kapitalleistung_wohnsitzstaat_bestaetigung', period
        )

        # Abs. 2: Rueckerstattung wenn Antrag innert 3 Jahren UND
        # Bestaetigung des Wohnsitzstaates vorliegt
        return pflichtig * innert_frist * bestaetigung
