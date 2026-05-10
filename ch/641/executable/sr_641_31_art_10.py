"""SR 641.31 Art. 10

Generated from: ch/641/de/641.31.md

Tabaksteuer - Bemessung:
1. Steuer auf Tabakfabrikaten:
   a. Zigaretten, Zigarren, Zigarillos: je Stueck und in % des Kleinhandelspreises
   b. Feinschnitttabak, Wasserpfeifentabak: je Kilogramm und in % des
      Kleinhandelspreises
   c. Anderer Rauchtabak, Kau- und Schnupftabak: in % des Kleinhandelspreises
1bis. Steuer auf Ersatzprodukten:
   a. Nachfuellbare E-Zigaretten: je Milliliter
   b. Einweg-E-Zigaretten: je Milliliter
   c. Andere Ersatzprodukte: wie die Tabakfabrikate, die sie ersetzen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tstg_produkt_typ(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Tabakprodukt-Typ: 1=Zigaretten, 2=Zigarren/Zigarillos, 3=Feinschnitt, 4=Wasserpfeife, 5=anderer Rauchtabak, 6=Kau/Schnupftabak, 7=E-Zig nachfuellbar, 8=E-Zig Einweg, 9=anderes Ersatzprodukt"
    reference = "SR 641.31 Art. 10"


class tstg_anzahl_stueck(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Stueck (fuer Zigaretten, Zigarren, Zigarillos)"
    reference = "SR 641.31 Art. 10 Abs. 1 Bst. a"


class tstg_gewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gewicht in Kilogramm (fuer Feinschnitt und Wasserpfeifentabak)"
    reference = "SR 641.31 Art. 10 Abs. 1 Bst. b"


class tstg_volumen_ml(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Volumen in Milliliter (fuer E-Zigaretten-Fluessigkeiten)"
    reference = "SR 641.31 Art. 10 Abs. 1bis Bst. a-b"


class tstg_kleinhandelspreis(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Kleinhandelspreis des Tabakprodukts (CHF)"
    reference = "SR 641.31 Art. 10 Abs. 1"


class tstg_bemessungsart(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Bemessungsart: 1=Stueck+%, 2=kg+%, 3=nur %, 4=je ml"
    reference = "SR 641.31 Art. 10"

    def formula(person, period, parameters):
        typ = person('tstg_produkt_typ', period)
        # 1=Zigaretten/Zigarren/Zigarillos -> Stueck+%
        # 3=Feinschnitt, 4=Wasserpfeife -> kg+%
        # 5=anderer Rauchtabak, 6=Kau/Schnupf -> nur %
        # 7,8=E-Zig -> je ml
        # 9=anderes Ersatzprodukt -> wie ersetztes Produkt (vereinfacht: %)
        return (
            where(typ <= 2, 1,
            where((typ == 3) + (typ == 4), 2,
            where((typ == 5) + (typ == 6) + (typ == 9), 3,
            where((typ == 7) + (typ == 8), 4,
            0))))
        )
