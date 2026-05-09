"""SR 641.51 Art. 2

Generated from: ch/641/de/641.51.md

Automobilsteuer - Begriffe:
1. Automobile fuer den Personen- oder Warentransport:
   a. Fahrzeuge fuer 10+ Personen, Stueckgewicht max. 1600 kg
   b. Personenautomobile, Breaks, Rennwagen
   c. Warentransportfahrzeuge, Stueckgewicht max. 1600 kg
2. Automobilchassis mit Fuehrerkabine gelten nicht als Automobile.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class astg_fahrzeug_typ(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Fahrzeugtyp: 1=Personenbefoerderung 10+, 2=Personenautomobil, 3=Warentransport, 4=Chassis, 0=anderes"
    reference = "SR 641.51 Art. 2"


class astg_stueckgewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Stueckgewicht des Fahrzeugs in Kilogramm"
    reference = "SR 641.51 Art. 2 Abs. 1"


class astg_ist_automobil(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Fahrzeug als Automobil im Sinne des AStG gilt"
    reference = "SR 641.51 Art. 2"

    def formula(person, period, parameters):
        typ = person('astg_fahrzeug_typ', period)
        gewicht = person('astg_stueckgewicht_kg', period)
        max_gewicht = parameters(period).sr_641_51.max_stueckgewicht_kg

        # Typ 1: Personenbefoerderung 10+, max 1600 kg
        ist_typ_a = (typ == 1) * (gewicht <= max_gewicht)
        # Typ 2: Personenautomobil (kein Gewichtslimit)
        ist_typ_b = (typ == 2)
        # Typ 3: Warentransport, max 1600 kg
        ist_typ_c = (typ == 3) * (gewicht <= max_gewicht)
        # Typ 4: Chassis = nicht Automobil

        return (ist_typ_a + ist_typ_b + ist_typ_c) > 0
