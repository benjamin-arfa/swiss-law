"""SR 642.21 Art. 17 - Verjaehrung (Statute of Limitations)

Generated from: ch/642/de/642.21.md

Art. 17: The tax claim expires 5 years after the end of the calendar
year in which it arose (Art. 12).
- Limitation does not begin or is suspended while the claim is secured
  or no liable person has domicile in Switzerland.
- Limitation is interrupted by any acknowledgment of the claim or any
  official act brought to the attention of a liable person.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vstg_entstehungsjahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Kalenderjahr, in dem die Verrechnungssteuerforderung entstanden ist"
    reference = "SR 642.21 Art. 17 Abs. 1"


class vstg_forderung_sichergestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Steuerforderung sichergestellt ist (hemmt Verjaehrung)"
    reference = "SR 642.21 Art. 17 Abs. 2"


class vstg_zahlungspflichtiger_inland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Zahlungspflichtiger im Inland Wohnsitz hat"
    reference = "SR 642.21 Art. 17 Abs. 2"


class vstg_verjaehrung_unterbrochen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verjaehrung durch Anerkennung oder Amtshandlung unterbrochen wurde"
    reference = "SR 642.21 Art. 17 Abs. 3"


class vstg_forderung_verjaehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verrechnungssteuerforderung verjaehrt ist"
    reference = "SR 642.21 Art. 17"

    def formula(person, period, parameters):
        import numpy as np
        entstehungsjahr = person('vstg_entstehungsjahr', period)
        sichergestellt = person('vstg_forderung_sichergestellt', period)
        inland = person('vstg_zahlungspflichtiger_inland', period)
        unterbrochen = person('vstg_verjaehrung_unterbrochen', period)

        p = parameters(period).sr_642_21
        frist = p.verjaehrungsfrist_jahre

        aktuelles_jahr = period.start.year
        jahre_vergangen = aktuelles_jahr - entstehungsjahr

        # Limitation is suspended if secured or no domestic domicile
        gehemmt = sichergestellt + np.logical_not(inland)

        # Expired if: years > limitation period AND not suspended AND not interrupted
        return (
            (jahre_vergangen > frist)
            * np.logical_not(gehemmt)
            * np.logical_not(unterbrochen)
        )
