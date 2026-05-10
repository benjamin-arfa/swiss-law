"""SR 783.018 Art. 4

Generated from: ch/783/de/783.018.md

Gebuehrenpflichtige Leistungen der PostCom. Feste Gebuehren:
- Streitigkeiten Hausbriefkaesten: CHF 200
- Streitigkeiten Hauszustellung: CHF 200
- Alle uebrigen: nach Zeitaufwand.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

GEBUEHR_STREITIGKEIT_HAUSBRIEFKASTEN = 200.0
GEBUEHR_STREITIGKEIT_HAUSZUSTELLUNG = 200.0


class postcom_leistungstyp(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Typ der PostCom-Leistung (1=Registrierung, 2=Postfachzugang, 3=Datenaustausch, 4=Grundversorgung, 5=Aufsicht, 6=Sanktionen, 7=Hausbriefkasten, 8=Hauszustellung, 9=Rechnungsstreit, 10=Andere)"
    reference = "SR 783.018 Art. 4"


class postcom_arbeitsstunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl aufgewendeter Arbeitsstunden fuer die PostCom-Leistung"
    reference = "SR 783.018 Art. 4"


class postcom_leistungsgebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gebuehr fuer die PostCom-Leistung in CHF"
    reference = "SR 783.018 Art. 4"

    def formula(person, period, parameters):
        typ = person('postcom_leistungstyp', period)
        stunden = person('postcom_arbeitsstunden', period)
        ansatz = person('postcom_gebuehrenansatz_pro_stunde', period)

        # Feste Gebuehren fuer Streitigkeiten
        fest_hausbriefkasten = (typ == 7) * GEBUEHR_STREITIGKEIT_HAUSBRIEFKASTEN
        fest_hauszustellung = (typ == 8) * GEBUEHR_STREITIGKEIT_HAUSZUSTELLUNG

        # Zeitaufwand fuer alle anderen Typen
        nach_zeitaufwand = ((typ != 7) * (typ != 8)) * stunden * ansatz

        return fest_hausbriefkasten + fest_hauszustellung + nach_zeitaufwand
