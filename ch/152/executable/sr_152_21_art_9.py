"""SR 152.21 Art. 9

Generated from: ch/152/de/152.21.md

Calculation of protection period: applies per dossier/case.
For litigation dossiers: judgement date is relevant.
For others: date of the most recent document.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_prozessdossier(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein Prozessdossier handelt"
    reference = "SR 152.21 Art. 9 Abs. 2"


class urteilsdatum_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr des Urteilsdatums (fuer Prozessdossiers)"
    reference = "SR 152.21 Art. 9 Abs. 2"


class juengstes_dokument_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahresdatum des juengsten Dokuments (fuer andere Unterlagen)"
    reference = "SR 152.21 Art. 9 Abs. 2"


class massgebendes_datum_schutzfrist_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Massgebendes Jahr fuer die Berechnung der Schutzfrist"
    reference = "SR 152.21 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        return where(
            person('ist_prozessdossier', period),
            person('urteilsdatum_jahr', period),
            person('juengstes_dokument_jahr', period)
        )


class schutzfrist_ablauf_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr in dem die Schutzfrist ablaeuft"
    reference = "SR 152.21 Art. 9"

    def formula(person, period, parameters):
        start = person('massgebendes_datum_schutzfrist_jahr', period)
        dauer = person('schutzfrist_jahre', period)
        return start + dauer
