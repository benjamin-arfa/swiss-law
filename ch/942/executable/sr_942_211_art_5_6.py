"""SR 942.211 Art. 5 & 6

Generated from: ch/942/de/942.211.md

Art. 5: Bekanntgabe des Grundpreises - Base price disclosure:
- For measurable goods: base price must always be disclosed
- Pre-packaged goods: both detail and base price
- Exemptions: per-piece sales; standard volumes (1/2/5 L/kg/m etc.);
  items under CHF 2; items over CHF 150/kg (food) or 750/kg (other);
  gastro; pharmaceuticals (categories A, B, C)

Art. 6: Messbare Waren und Grundpreis - Measurable goods and base price:
- Measurable goods: price usually determined by volume, weight, length, or area
- Base price: price per liter, kilogram, meter, square meter, cubic meter (or decimal multiples)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pbv_ist_messbare_ware(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ware ist messbar (Preis nach Volumen, Gewicht, Masse, Länge oder Fläche)"
    reference = "SR 942.211 Art. 6 Abs. 1"


class pbv_detailpreis_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Detailpreis der Ware (CHF)"
    reference = "SR 942.211 Art. 3 Abs. 1"


class pbv_verkauf_per_stueck(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verkauf per Stück oder nach Stückzahl"
    reference = "SR 942.211 Art. 5 Abs. 3 Bst. a"


class pbv_standardmenge(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ware in Standardmenge (1, 2 oder 5 L/kg/m etc.)"
    reference = "SR 942.211 Art. 5 Abs. 3 Bst. b"


class pbv_ist_gastgewerblich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verkauf in gastgewerblichem Betrieb"
    reference = "SR 942.211 Art. 5 Abs. 3 Bst. i"


class pbv_ist_lebensmittel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ware ist ein Lebensmittel"
    reference = "SR 942.211 Art. 5 Abs. 3 Bst. h"


class pbv_grundpreis_pro_kg_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Grundpreis pro kg oder Liter (CHF)"
    reference = "SR 942.211 Art. 6 Abs. 2"


class pbv_grundpreis_bekanntgabepflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bekanntgabepflicht für Grundpreis besteht"
    reference = "SR 942.211 Art. 5"

    def formula(person, period, parameters):
        messbar = person('pbv_ist_messbare_ware', period)
        stueck = person('pbv_verkauf_per_stueck', period)
        standard = person('pbv_standardmenge', period)
        gastro = person('pbv_ist_gastgewerblich', period)
        detailpreis = person('pbv_detailpreis_chf', period)
        grundpreis_kg = person('pbv_grundpreis_pro_kg_chf', period)
        lebensmittel = person('pbv_ist_lebensmittel', period)

        # Exemptions
        unter_2_chf = detailpreis < 2.0
        ueber_schwelle = np.where(
            lebensmittel,
            grundpreis_kg > 150.0,  # Food: > 150 CHF/kg
            grundpreis_kg > 750.0   # Other: > 750 CHF/kg
        )

        befreit = stueck + standard + gastro + unter_2_chf + ueber_schwelle > 0
        return messbar * (1 - befreit)
