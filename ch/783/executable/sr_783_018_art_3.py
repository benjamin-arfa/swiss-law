"""SR 783.018 Art. 3

Generated from: ch/783/de/783.018.md

Gebuehrenansaetze pro Arbeitsstunde:
- Administrative Mitarbeitende: CHF 105
- Spezialisten: CHF 180
- Leiter/in Fachsekretariat: CHF 200
- Kommissionsmitglieder: CHF 250
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


GEBUEHR_ADMIN = 105.0
GEBUEHR_SPEZIALIST = 180.0
GEBUEHR_LEITUNG = 200.0
GEBUEHR_KOMMISSION = 250.0


class postcom_personalkategorie(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Personalkategorie PostCom (1=Admin, 2=Spezialist, 3=Leitung, 4=Kommission)"
    reference = "SR 783.018 Art. 3"


class postcom_gebuehrenansatz_pro_stunde(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gebuehrenansatz pro Arbeitsstunde in CHF je nach Personalkategorie"
    reference = "SR 783.018 Art. 3"

    def formula(person, period, parameters):
        kategorie = person('postcom_personalkategorie', period)
        return (
            (kategorie == 1) * GEBUEHR_ADMIN
            + (kategorie == 2) * GEBUEHR_SPEZIALIST
            + (kategorie == 3) * GEBUEHR_LEITUNG
            + (kategorie == 4) * GEBUEHR_KOMMISSION
        )
