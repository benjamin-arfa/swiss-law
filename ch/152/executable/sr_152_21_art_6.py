"""SR 152.21 Art. 6

Generated from: ch/152/de/152.21.md

Protection periods for Federal Court archives:
- Default: 30 years (Art. 9 Archivierungsgesetz)
- Litigation files: 50 years (except purely public-law parties)
- Documents with sensitive personal data: 50 years
- Plenary/governing body minutes: 50 years
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_prozessakte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Prozessakte des Bundesgerichts handelt"
    reference = "SR 152.21 Art. 6 Abs. 2"


class nur_oeffentlich_rechtliche_beteiligte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob am Verfahren ausschliesslich oeffentlich-rechtliche Gemeinwesen beteiligt sind"
    reference = "SR 152.21 Art. 6 Abs. 2"


class enthaelt_besonders_schuetzenswerte_personendaten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Dokument besonders schuetzenswerte Personendaten enthaelt"
    reference = "SR 152.21 Art. 6 Abs. 3"


class ist_verhandlungsprotokoll_gesamtgericht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein Verhandlungsprotokoll des Gesamtgerichts oder der Leitungsorgane handelt"
    reference = "SR 152.21 Art. 6 Abs. 4"


class schutzfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anwendbare Schutzfrist in Jahren"
    reference = "SR 152.21 Art. 6"

    def formula(person, period, parameters):
        ist_prozess = person('ist_prozessakte', period)
        nur_oer = person('nur_oeffentlich_rechtliche_beteiligte', period)
        sensibel = person('enthaelt_besonders_schuetzenswerte_personendaten', period)
        protokoll = person('ist_verhandlungsprotokoll_gesamtgericht', period)

        # Prozessakten: 50 Jahre, ausser nur oer-Beteiligte
        verlaengert_prozess = ist_prozess * not_(nur_oer)
        # Andere Unterlagen mit sensiblen Daten: 50 Jahre
        verlaengert_daten = sensibel
        # Verhandlungsprotokolle: 50 Jahre
        verlaengert_protokoll = protokoll

        hat_verlaengerte_frist = (verlaengert_prozess + verlaengert_daten + verlaengert_protokoll) > 0

        return where(hat_verlaengerte_frist, 50, 30)
