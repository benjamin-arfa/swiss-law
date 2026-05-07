"""SR 641.10 Art. 5

Generated from: ch/641/de/641.10.md

Art. 5 Beteiligungsrechte (Participation rights):
Defines the object of the emission levy: creation and increase of nominal value
of participation rights (shares, GmbH shares, cooperative shares, profit-sharing
certificates, participation certificates, cooperative bank participation shares).
Also covers equivalent events like shareholder contributions without capital
increase and majority transfer of liquidated companies.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class stg_beteiligungsrechte_begruendung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether participation rights are being created or their nominal value increased"
    reference = "SR 641.10 Art. 5 Abs. 1 Bst. a"


class stg_zuschuss_ohne_kapitalerhoehung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether a shareholder contribution is made without corresponding capital increase"
    reference = "SR 641.10 Art. 5 Abs. 2 Bst. a"


class stg_handwechsel_mehrheit_liquidiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether a majority transfer of shares in a liquidated company occurred"
    reference = "SR 641.10 Art. 5 Abs. 2 Bst. b"


class stg_emissionsabgabe_tatbestand(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether any emission levy triggering event occurred"
    reference = "SR 641.10 Art. 5"

    def formula(person, period, parameters):
        begruendung = person('stg_beteiligungsrechte_begruendung', period)
        zuschuss = person('stg_zuschuss_ohne_kapitalerhoehung', period)
        handwechsel = person('stg_handwechsel_mehrheit_liquidiert', period)
        return begruendung + zuschuss + handwechsel
