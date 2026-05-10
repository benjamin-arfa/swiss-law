"""SR 935.61 Art. 12

Generated from: ch/935/de/935.61.md

Art. 12: Berufsregeln
- Sorgfältige und gewissenhafte Berufsausübung (a)
- Unabhängige Berufsausübung in eigenem Namen und auf eigene Verantwortung (b)
- Meidung von Interessenkonflikten (c)
- Objektive Werbung (d)
- Kein Pactum de quota litis vor Abschluss (e)
- Berufshaftpflichtversicherung mind. 1 Mio CHF/Jahr (f)
- Amtliche Pflichtverteidigungen und unentgeltliche Rechtspflege (g)
- Trennung anvertrauter Vermögenswerte (h)
- Aufklärung über Rechnungsstellung (i)
- Meldepflicht bei Datenänderungen (j)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class anwalt_sorgfaeltige_berufsausuebung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Sorgfältige und gewissenhafte Berufsausübung"
    reference = "SR 935.61 Art. 12 Bst. a"


class anwalt_unabhaengige_ausuebung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Unabhängige Berufsausübung in eigenem Namen und auf eigene Verantwortung"
    reference = "SR 935.61 Art. 12 Bst. b"


class anwalt_kein_interessenkonflikt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Meidet Konflikte zwischen Interessen der Klientschaft und eigenen Beziehungen"
    reference = "SR 935.61 Art. 12 Bst. c"


class anwalt_haftpflichtversicherung_summe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherungssumme der Berufshaftpflichtversicherung in CHF pro Jahr"
    reference = "SR 935.61 Art. 12 Bst. f"


class anwalt_haftpflicht_genuegend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Berufshaftpflichtversicherung oder gleichwertige Sicherheit "
        "nach Massgabe der Risiken abgeschlossen (mind. 1 Mio CHF/Jahr)"
    )
    reference = "SR 935.61 Art. 12 Bst. f"

    def formula(person, period, parameters):
        summe = person('anwalt_haftpflichtversicherung_summe', period)
        min_summe = parameters(period).sr_935_61.min_haftpflicht_versicherungssumme
        return summe >= min_summe


class anwalt_vermoegenswerte_getrennt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anvertraute Vermögenswerte getrennt vom eigenen Vermögen aufbewahrt"
    reference = "SR 935.61 Art. 12 Bst. h"


class anwalt_berufsregeln_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Alle Berufsregeln nach Art. 12 BGFA eingehalten"
    reference = "SR 935.61 Art. 12"

    def formula(person, period, parameters):
        sorgfalt = person('anwalt_sorgfaeltige_berufsausuebung', period)
        unabhaengig = person('anwalt_unabhaengige_ausuebung', period)
        kein_konflikt = person('anwalt_kein_interessenkonflikt', period)
        haftpflicht = person('anwalt_haftpflicht_genuegend', period)
        vermoegen = person('anwalt_vermoegenswerte_getrennt', period)
        return sorgfalt * unabhaengig * kein_konflikt * haftpflicht * vermoegen
