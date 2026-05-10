"""SR 152.12 Art. 10 - Schutzfrist (Protection Period)

Generated from: ch/152/de/152.12.md

Protection periods for archived material at the Federal Criminal Court:
- General: 30 years (Art. 9 BGA)
- Case files: 50 years (Art. 11 BGA), unless only public institutions participated
- Other documents with sensitive personal data: 50 years
- Minutes of plenary court, court management, chambers: 50 years
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_verfahrensakte_bstger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Verfahrensakte des Bundesstrafgerichts handelt"
    reference = "SR 152.12 Art. 10 Abs. 2"


class nur_oeffentlich_rechtliche_institutionen_beteiligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob am Verfahren ausschliesslich oeffentlich-rechtliche Institutionen teilgenommen haben"
    reference = "SR 152.12 Art. 10 Abs. 2"


class enthaelt_besonders_schuetzenswerte_personendaten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Unterlagen besonders schuetzenswerte Personendaten enthalten"
    reference = "SR 152.12 Art. 10 Abs. 3"


class ist_protokoll_gesamtgericht_oder_kammer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um Protokolle des Gesamtgerichts, der Gerichtsleitung oder der Kammern handelt"
    reference = "SR 152.12 Art. 10 Abs. 4"


class schutzfrist_bstger_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Laenge der Schutzfrist in Jahren fuer Archivgut des Bundesstrafgerichts"
    reference = "SR 152.12 Art. 10"

    def formula(person, period, parameters):
        ist_verfahrensakte = person('ist_verfahrensakte_bstger', period)
        nur_oeffentlich = person('nur_oeffentlich_rechtliche_institutionen_beteiligt', period)
        sensible_daten = person('enthaelt_besonders_schuetzenswerte_personendaten', period)
        ist_protokoll = person('ist_protokoll_gesamtgericht_oder_kammer', period)

        # Verfahrensakten: 50 Jahre, ausser nur oeffentlich-rechtliche Institutionen beteiligt
        verfahren_50 = ist_verfahrensakte * (1 - nur_oeffentlich)
        # Andere Unterlagen mit sensiblen Personendaten: 50 Jahre
        # Protokolle: 50 Jahre
        braucht_50 = (verfahren_50 + sensible_daten + ist_protokoll) > 0

        return where(braucht_50, 50, 30)
