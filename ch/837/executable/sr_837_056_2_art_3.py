"""SR 837.056.2 Art. 3

Generated from: ch/837/de/837.056.2.md

Ansätze für Reisekosten (Travel cost reimbursement rates for private vehicles
in unemployment insurance course attendance).

- Car (Motorwagen): CHF 0.50/km
- Motorcycle (Motorrad): CHF 0.25/km
- Moped (Motorfahrrad): CHF 0.10/km
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class alv_kurs_reisekosten_verguetung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "ALV-Reisekostenvergütung bei Benützung von Privatfahrzeugen (CHF)"
    reference = "SR 837.056.2 Art. 3"

    def formula_2003_07(person, period, parameters):
        import numpy as np

        fahrzeugtyp = person('alv_kurs_fahrzeugtyp', period)
        km_im_monat = person('alv_kurs_km_im_monat', period)

        p = parameters(period).sr837_056_2.reisekosten
        satz_auto = p.motorwagen
        satz_motorrad = p.motorrad
        satz_mofa = p.motorfahrrad

        satz = np.select(
            [
                fahrzeugtyp == 'motorwagen',
                fahrzeugtyp == 'motorrad',
                fahrzeugtyp == 'motorfahrrad',
            ],
            [satz_auto, satz_motorrad, satz_mofa],
            default=0.0
        )
        return km_im_monat * satz


class alv_kurs_fahrzeugtyp(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Typ des Privatfahrzeugs (motorwagen/motorrad/motorfahrrad)"
    reference = "SR 837.056.2 Art. 3"


class alv_kurs_km_im_monat(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gefahrene Kilometer im Monat für Kursbesuch"
    reference = "SR 837.056.2 Art. 3"
