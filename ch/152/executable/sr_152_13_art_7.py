"""SR 152.13 Art. 7 - Berechnung der Schutzfrist (Calculation of Protection Period)

Generated from: ch/152/de/152.13.md

Protection period starts:
- For case files: from the decision date
- For other files: from the date of the most recent document
Subsequently added documents without relevant information are not counted.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class entscheiddatum_bvger_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr des Entscheiddatums (fuer Prozessakten des BVGer)"
    reference = "SR 152.13 Art. 7 Abs. 2"


class datum_juengstes_dokument_bvger_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr des juengsten Dokuments (fuer uebrige Akten des BVGer)"
    reference = "SR 152.13 Art. 7 Abs. 2"


class schutzfrist_beginn_jahr_bvger(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Beginn der Schutzfrist (Jahr) beim Bundesverwaltungsgericht"
    reference = "SR 152.13 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        ist_prozessakte = person('ist_prozessakte_bvger', period)
        entscheiddatum = person('entscheiddatum_bvger_jahr', period)
        juengstes = person('datum_juengstes_dokument_bvger_jahr', period)
        return where(ist_prozessakte, entscheiddatum, juengstes)


class schutzfrist_abgelaufen_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Schutzfrist beim Bundesverwaltungsgericht abgelaufen ist"
    reference = "SR 152.13 Art. 6-7"

    def formula(person, period, parameters):
        beginn = person('schutzfrist_beginn_jahr_bvger', period)
        dauer = person('schutzfrist_bvger_jahre', period)
        aktuelles_jahr = period.start.year
        return aktuelles_jahr >= (beginn + dauer)
