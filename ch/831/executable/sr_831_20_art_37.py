"""SR 831.20 Art. 37

Generated from: ch/831/de/831.20.md

Art. 37: Hoehe der Invalidenrenten - Amount of disability pensions:
- Abs. 1: The amount of the disability pension corresponds to the amount
  of the old-age pension (AHV).
- Abs. 1bis: If both spouses are entitled to pensions, the reduction rule
  of Art. 35 AHVG applies by analogy.
- Abs. 2: If an insured person with complete contribution record becomes
  disabled before age 25, the disability pension (and any supplementary
  pensions) amounts to at least 133 1/3 percent of the minimum full pension.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_vollstaendige_beitragsdauer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vollstaendige Beitragsdauer bei Eintritt der Invaliditaet"
    reference = "SR 831.20 Art. 37 Abs. 2"


class iv_alter_bei_invaliditaet(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter bei Eintritt der Invaliditaet (Jahre)"
    reference = "SR 831.20 Art. 37 Abs. 2"


class iv_mindestansatz_vollrente(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestansatz der zutreffenden Vollrente (CHF/Monat)"
    reference = "SR 831.20 Art. 37 Abs. 2"


class iv_altersrente_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Hoehe der entsprechenden AHV-Altersrente (CHF/Monat)"
    reference = "SR 831.20 Art. 37 Abs. 1"


class iv_beide_ehegatten_rentenberechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Beide Ehegatten sind IV-rentenberechtigt"
    reference = "SR 831.20 Art. 37 Abs. 1bis"


class iv_rente_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Hoehe der IV-Rente (Art. 37 IVG, CHF/Monat)"
    reference = "SR 831.20 Art. 37"

    def formula(person, period, parameters):
        altersrente = person('iv_altersrente_betrag', period)
        vollstaendig = person('iv_vollstaendige_beitragsdauer', period.this_year)
        alter = person('iv_alter_bei_invaliditaet', period.this_year)
        mindest = person('iv_mindestansatz_vollrente', period.this_year)

        # Abs. 1: IV pension = AHV pension amount
        rente = altersrente

        # Abs. 2: If complete contribution record and disabled before 25,
        # minimum is 133 1/3% of the minimum full pension rate
        jung_mindest = mindest * (4.0 / 3.0)  # 133 1/3 %
        jung_berechtigt = vollstaendig * (alter < 25)
        rente = where(
            jung_berechtigt,
            max_(rente, jung_mindest),
            rente
        )

        return rente
