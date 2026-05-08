"""SR 734.0 Art. 4

Generated from: ch/734/de/734.0.md

Art. 4: Geltungsbereich Schwachstromanlagen
- Abs. 1: Schwachstromanlagen die oeffentlichen Grund und Boden oder
  Eisenbahngebiet benutzen oder zufolge der Naehe von Starkstromanlagen
  zu Betriebsstoerungen oder Gefaehrdungen fuehren koennen.
- Abs. 2: Schwachstromanlagen duerfen die Erde als Leitung benutzen,
  ausser oeffentliche Telefonleitungen bei Stoerungsgefahr durch Starkstrom.
- Abs. 3: Der Bundesrat bezeichnet die plangenehmigungspflichtigen
  Schwachstromanlagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class eleg_schwachstrom_nutzt_oeffentlichen_grund(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwachstromanlage nutzt oeffentlichen Grund und Boden oder Eisenbahngebiet"
    reference = "SR 734.0 Art. 4 Abs. 1"


class eleg_schwachstrom_naehe_starkstrom(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwachstromanlage in der Naehe von Starkstromanlagen (Stoerungsgefahr)"
    reference = "SR 734.0 Art. 4 Abs. 1"


class eleg_schwachstrom_unter_gesetz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwachstromanlage faellt unter das EleG"
    reference = "SR 734.0 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        oeffentlich = person('eleg_schwachstrom_nutzt_oeffentlichen_grund', period)
        naehe = person('eleg_schwachstrom_naehe_starkstrom', period)
        return oeffentlich + naehe > 0


class eleg_schwachstrom_erdleitung_erlaubt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwachstromanlage darf die Erde als Leitung benutzen"
    reference = "SR 734.0 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        ist_schwach = person('eleg_anlage_ist_schwachstrom', period)
        # Oeffentliche Telefonleitungen bei Stoerungsgefahr sind ausgenommen
        # (vereinfacht: Erdleitung fuer Schwachstrom generell erlaubt)
        return ist_schwach
