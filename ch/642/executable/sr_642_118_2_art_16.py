"""SR 642.118.2 Art. 16

Generated from: ch/642/de/642.118.2.md

Art. 16: Kuenstler, Sportler, Referenten - Calculation of daily income for
foreign artists, athletes, and lecturers. Total income divided by number of
performance and rehearsal days.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class quellensteuer_kuenstler_bruttoeinkuenfte(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = (
        "Bruttoeinkuenfte von Kuenstlern/Sportlern/Referenten inkl. Zulagen, "
        "Naturalleistungen und vom Veranstalter uebernommene Spesen (CHF)"
    )
    reference = "SR 642.118.2 Art. 16 Abs. 1"


class quellensteuer_kuenstler_auftrittsprobetage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Auftritts- und Probetage"
    reference = "SR 642.118.2 Art. 16 Abs. 1"


class quellensteuer_kuenstler_gruppenmitglieder(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der Kuenstlergruppe (0 = Einzelperson)"
    reference = "SR 642.118.2 Art. 16 Abs. 2"
    default_value = 0


class quellensteuer_kuenstler_tageseinkuenfte(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Tageseinkuenfte von Kuenstlern/Sportlern/Referenten (CHF/Tag)"
    reference = "SR 642.118.2 Art. 16"

    def formula(person, period, parameters):
        brutto = person('quellensteuer_kuenstler_bruttoeinkuenfte', period)
        tage = person('quellensteuer_kuenstler_auftrittsprobetage', period)
        mitglieder = person('quellensteuer_kuenstler_gruppenmitglieder', period)

        # Abs. 1: Tageseinkuenfte = Bruttoeinkuenfte / Auftritts- und Probetage
        tageseinkommen = where(tage > 0, brutto / tage, 0)

        # Abs. 2: Bei Gruppen: durchschnittliches Tageseinkommen pro Kopf
        return where(mitglieder > 0, tageseinkommen / mitglieder, tageseinkommen)
