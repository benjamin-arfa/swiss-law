"""SR 831.30 Art. 11a

Generated from: ch/831/de/831.30.md

Art. 11a: Verzicht auf Einkuenfte und Vermoegenswerte
(Relinquishment of income and assets)

Abs. 1: If a person voluntarily forgoes reasonable employment, a hypothetical
earned income is counted.

Abs. 3: Asset relinquishment exists if more than 10% of wealth is consumed
per year from the date of entitlement to AHV survivor's pension or IV pension,
without good reason. For wealth up to CHF 100,000 the limit is CHF 10,000/year.

Abs. 4: For old-age pensioners, Abs. 3 also applies to the 10 years before
the start of pension entitlement.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class el_verzichtet_auf_erwerbstaetigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person verzichtet freiwillig auf zumutbare Erwerbstaetigkeit"
    reference = "SR 831.30 Art. 11a Abs. 1"


class el_hypothetisches_erwerbseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hypothetisches Erwerbseinkommen bei Verzicht (Art. 11a Abs. 1)"
    reference = "SR 831.30 Art. 11a Abs. 1"


class el_vermoegen_bei_rentenanspruch(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermoegen bei Entstehung des Rentenanspruchs"
    reference = "SR 831.30 Art. 11a Abs. 3"


class el_jaehrlicher_vermoegensverbrauch(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher Vermoegensverbrauch seit Rentenanspruch"
    reference = "SR 831.30 Art. 11a Abs. 3"


class el_wichtiger_grund_vermoegensverbrauch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Wichtiger Grund fuer erhoehten Vermoegensverbrauch liegt vor"
    reference = "SR 831.30 Art. 11a Abs. 3"


class el_vermoegensverzicht_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermoegensverzicht liegt vor (Art. 11a Abs. 3 ELG)"
    reference = "SR 831.30 Art. 11a Abs. 3"

    def formula(person, period, parameters):
        import numpy as np
        vermoegen_start = person('el_vermoegen_bei_rentenanspruch', period)
        verbrauch = person('el_jaehrlicher_vermoegensverbrauch', period)
        wichtiger_grund = person('el_wichtiger_grund_vermoegensverbrauch', period)

        # Threshold: 10% of wealth, but for wealth <= 100,000 the limit is 10,000/year
        grenze_prozent = vermoegen_start * 0.10
        grenze_absolut = 10000.0
        grenze = np.where(vermoegen_start <= 100000.0, grenze_absolut, grenze_prozent)

        # Relinquishment if consumption exceeds limit AND no good reason
        ueberschreitung = verbrauch > grenze
        return ueberschreitung * not_(wichtiger_grund)
