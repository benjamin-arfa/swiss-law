"""SR 837.056.2 Art. 1

Generated from: ch/837/de/837.056.2.md

Ansätze für Verpflegung am Kursort (Reimbursement rates for meals at course
location for unemployment insurance participants).

- Breakfast away from home: CHF 5
- Main meal away from home: CHF 15
- Main meal in subsidized canteen: CHF 10
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alv_kurs_fruehstueck_verguetung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "ALV-Vergütung für auswärtiges Frühstück am Kursort (CHF)"
    reference = "SR 837.056.2 Art. 1 Abs. 1 lit. a"

    def formula_2003_07(person, period, parameters):
        hat_auswaertiges_fruehstueck = person(
            'alv_kurs_auswaertiges_fruehstueck', period
        )
        anzahl_tage = person('alv_kurs_tage_im_monat', period)
        satz = parameters(period).sr837_056_2.verpflegung.fruehstueck
        return hat_auswaertiges_fruehstueck * anzahl_tage * satz


class alv_kurs_hauptmahlzeit_verguetung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "ALV-Vergütung für auswärtige Hauptmahlzeit am Kursort (CHF)"
    reference = "SR 837.056.2 Art. 1 Abs. 1 lit. b, Abs. 2"

    def formula_2003_07(person, period, parameters):
        hat_kantine = person('alv_kurs_kantine_verfuegbar', period)
        anzahl_tage = person('alv_kurs_tage_im_monat', period)
        satz_normal = parameters(period).sr837_056_2.verpflegung.hauptmahlzeit
        satz_kantine = parameters(period).sr837_056_2.verpflegung.hauptmahlzeit_kantine
        import numpy as np
        satz = np.where(hat_kantine, satz_kantine, satz_normal)
        return anzahl_tage * satz


class alv_kurs_auswaertiges_fruehstueck(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hat auswärtiges Frühstück am Kursort"
    reference = "SR 837.056.2 Art. 1 Abs. 1 lit. a"


class alv_kurs_kantine_verfuegbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kann sich zu kostendeckenden Preisen in Betriebskantine verpflegen"
    reference = "SR 837.056.2 Art. 1 Abs. 2"


class alv_kurs_tage_im_monat(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Kurstage im Monat"
    reference = "SR 837.056.2 Art. 1"
