"""SR 711.4 Art. 3

Generated from: ch/711/de/711.4.md

Compensation rates for members of the federal valuation commissions.
- Presidency: CHF 160/hour
- Other members: CHF 130-240/hour (set by president based on expertise)
- Secretary: CHF 130/hour
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class schaetzungskommission_rolle(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Rolle in der Schaetzungskommission: 1=Praesidium, 2=Mitglied, 3=Sekretaer"
    reference = "SR 711.4 Art. 2"


class schaetzungskommission_nebenamtlich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Nebenamtliche Beschaeftigung in der Schaetzungskommission"
    reference = "SR 711.4 Art. 3 Abs. 1"
    default_value = True


class schaetzungskommission_stundensatz(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Stundenansatz fuer Kommissionstaetigkeit (CHF)"
    reference = "SR 711.4 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        rolle = person('schaetzungskommission_rolle', period)
        nebenamtlich = person('schaetzungskommission_nebenamtlich', period)

        # Art. 3 Abs. 2: hourly rates for part-time (nebenamtlich) members
        # a. Presidency: CHF 160
        # b. Other members: CHF 130-240 (use midpoint 185 as default)
        # c. Secretary: CHF 130
        praesidium_satz = 160.0
        mitglied_satz = 185.0  # midpoint of 130-240 range
        sekretaer_satz = 130.0

        satz = where(rolle == 1, praesidium_satz,
               where(rolle == 3, sekretaer_satz,
                     mitglied_satz))

        # Art. 3 Abs. 4: full-time members follow different rules
        return where(nebenamtlich, satz, 0.0)


class schaetzungskommission_arbeitsstunden(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Geleistete Arbeitsstunden fuer Kommissionstaetigkeit"
    reference = "SR 711.4 Art. 3 Abs. 1"


class schaetzungskommission_entschaedigung(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Entschaedigung fuer Kommissionstaetigkeit (CHF)"
    reference = "SR 711.4 Art. 3"

    def formula(person, period, parameters):
        stunden = person('schaetzungskommission_arbeitsstunden', period)
        stundensatz = person('schaetzungskommission_stundensatz', period)
        return stunden * stundensatz
