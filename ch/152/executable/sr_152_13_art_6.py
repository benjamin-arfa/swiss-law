"""SR 152.13 Art. 6 - Schutzfrist (Protection Period)

Generated from: ch/152/de/152.13.md

Protection periods for archived material at the Federal Administrative Court:
- General: 30 years (Art. 9 BGA)
- Case files: 50 years (Art. 11 BGA)
- Other documents with sensitive personal data/profiles, indexed by name: 50 years
- Documents already publicly accessible before archiving: remain public
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_prozessakte_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Prozessakte des Bundesverwaltungsgerichts handelt"
    reference = "SR 152.13 Art. 6 Abs. 2"


class nach_personennamen_erschlossen_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Unterlagen nach Personennamen erschlossen sind"
    reference = "SR 152.13 Art. 6 Abs. 3"


class enthaelt_schuetzenswerte_personendaten_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Unterlagen schuetzenswerte Personendaten oder Persoenlichkeitsprofile enthalten"
    reference = "SR 152.13 Art. 6 Abs. 3"


class vor_archivierung_oeffentlich_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Unterlagen vor der Archivierung oeffentlich zugaenglich waren"
    reference = "SR 152.13 Art. 6 Abs. 4"


class schutzfrist_bvger_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Laenge der Schutzfrist in Jahren fuer Archivgut des Bundesverwaltungsgerichts"
    reference = "SR 152.13 Art. 6"

    def formula(person, period, parameters):
        ist_prozessakte = person('ist_prozessakte_bvger', period)
        nach_namen = person('nach_personennamen_erschlossen_bvger', period)
        sensible_daten = person('enthaelt_schuetzenswerte_personendaten_bvger', period)
        vorher_oeffentlich = person('vor_archivierung_oeffentlich_bvger', period)

        # Bereits oeffentlich zugaenglich: bleibt oeffentlich (Schutzfrist 0)
        # Prozessakten: 50 Jahre
        # Nach Personennamen erschlossen + sensible Daten: 50 Jahre
        braucht_50 = (ist_prozessakte + (nach_namen * sensible_daten)) > 0

        return where(vorher_oeffentlich, 0, where(braucht_50, 50, 30))
