"""SR 152.12 Art. 11 - Berechnung der Schutzfrist (Calculation of Protection Period)

Generated from: ch/152/de/152.12.md

Protection period starts:
- For case files: from the decision date
- For other files: from the date of the most recent document
Attached documents with no relevant information are not counted.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class entscheiddatum_bstger_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr des Entscheiddatums (fuer Verfahrensakten)"
    reference = "SR 152.12 Art. 11 Abs. 2"


class datum_juengstes_dokument_bstger_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr des juengsten Dokuments (fuer uebrige Akten)"
    reference = "SR 152.12 Art. 11 Abs. 2"


class schutzfrist_beginn_jahr_bstger(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Beginn der Schutzfrist (Jahr) beim Bundesstrafgericht"
    reference = "SR 152.12 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        ist_verfahrensakte = person('ist_verfahrensakte_bstger', period)
        entscheiddatum = person('entscheiddatum_bstger_jahr', period)
        juengstes = person('datum_juengstes_dokument_bstger_jahr', period)
        return where(ist_verfahrensakte, entscheiddatum, juengstes)


class schutzfrist_abgelaufen_bstger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schutzfrist beim Bundesstrafgericht abgelaufen ist"
    reference = "SR 152.12 Art. 10-11"

    def formula(person, period, parameters):
        beginn = person('schutzfrist_beginn_jahr_bstger', period)
        dauer = person('schutzfrist_bstger_jahre', period)
        aktuelles_jahr = period.start.year
        return aktuelles_jahr >= (beginn + dauer)
