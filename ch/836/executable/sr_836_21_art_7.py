"""SR 836.21 Art. 7 - Children abroad (Kinder im Ausland)

Art. 7: Family allowances for children domiciled abroad are only paid if
required by international agreements. For children leaving CH for education,
domicile in CH is presumed for up to 5 years (starting at earliest at age 15).
Employees compulsorily insured under AHV (Art. 1a par. 1 let. c or par. 3
let. a AHVG) are entitled even without a treaty obligation.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kind_wohnsitz_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child is domiciled abroad (Art. 7 par. 1 FamZV)"
    default_value = False


class zwischenstaatliche_vereinbarung_famz(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "International agreement requires payment of family allowances (Art. 7 par. 1 FamZV)"
    default_value = False


class kind_ausbildung_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child left CH for education purposes (Art. 7 par. 1bis FamZV)"
    default_value = False


class dauer_ausbildung_ausland_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Years of education abroad (Art. 7 par. 1bis FamZV)"
    default_value = 0


class kind_alter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Age of the child in years"
    default_value = 0


class wohnsitz_schweiz_vermutet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Swiss domicile presumed for child abroad for education (Art. 7 par. 1bis FamZV)"

    def formula(person, period, parameters):
        ausbildung = person("kind_ausbildung_ausland", period)
        dauer = person("dauer_ausbildung_ausland_jahre", period.this_year)
        alter = person("kind_alter", period.this_year)
        return ausbildung * (dauer <= 5) * (alter >= 15)


class obligatorisch_ahv_versichert_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Employee compulsorily insured under AHV abroad (Art. 1a par. 1 let. c / par. 3 let. a AHVG)"
    default_value = False


class anspruch_familienzulagen_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Entitlement to family allowances for children abroad (Art. 7 FamZV)"

    def formula(person, period, parameters):
        ausland = person("kind_wohnsitz_ausland", period)
        vereinbarung = person("zwischenstaatliche_vereinbarung_famz", period)
        vermutet = person("wohnsitz_schweiz_vermutet", period)
        oblig_ahv = person("obligatorisch_ahv_versichert_ausland", period)

        # Not abroad -> normal domestic entitlement (not handled here)
        # Abroad: allowed if treaty requires, OR domicile is presumed, OR compulsory AHV
        return ausland * (vereinbarung + vermutet + oblig_ahv)
