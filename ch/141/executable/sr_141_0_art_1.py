"""SR 141.0 Art. 1 - Erwerb durch Abstammung

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class eltern_verheiratet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Eltern sind miteinander verheiratet"
    reference = "SR 141.0 Art. 1 Abs. 1 lit. a"


class vater_oder_mutter_schweizer_buerger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vater oder Mutter ist Schweizer Buergerin oder Buerger"
    reference = "SR 141.0 Art. 1 Abs. 1"


class mutter_schweizer_buergerin(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Mutter ist Schweizer Buergerin"
    reference = "SR 141.0 Art. 1 Abs. 1 lit. b"


class vater_schweizer_buerger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Vater ist Schweizer Buerger"
    reference = "SR 141.0 Art. 1 Abs. 2"


class kindesverhaeltnis_zum_vater_begruendet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kindesverhaeltnis zum Vater ist begruendet"
    reference = "SR 141.0 Art. 1 Abs. 2"


class person_ist_minderjaehrig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist minderjaehrig"
    reference = "SR 141.0 Art. 1 Abs. 2"


# Computed variables

class schweizer_buerger_durch_abstammung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist Schweizer Buergerin oder Buerger durch Abstammung von Geburt an"
    reference = "SR 141.0 Art. 1 Abs. 1"

    def formula(self, period, parameters):
        # lit. a: Kind verheirateter Eltern, wobei Vater oder Mutter Schweizer
        verheiratet = self('eltern_verheiratet', period)
        elternteil_schweizer = self('vater_oder_mutter_schweizer_buerger', period)
        lit_a = verheiratet * elternteil_schweizer

        # lit. b: Kind einer Schweizerin, die mit dem Vater nicht verheiratet ist
        mutter_schweizerin = self('mutter_schweizer_buergerin', period)
        nicht_verheiratet = not_(verheiratet)
        lit_b = mutter_schweizerin * nicht_verheiratet

        return lit_a + lit_b > 0


class schweizer_buerger_durch_kindesverhaeltnis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erwerb des Schweizer Buergerrechts durch Begruendung des Kindesverhaeltnisses zum schweizerischen Vater"
    reference = "SR 141.0 Art. 1 Abs. 2"

    def formula(self, period, parameters):
        minderjaehrig = self('person_ist_minderjaehrig', period)
        vater_schweizer = self('vater_schweizer_buerger', period)
        nicht_verheiratet = not_(self('eltern_verheiratet', period))
        kindesverhaeltnis = self('kindesverhaeltnis_zum_vater_begruendet', period)
        return minderjaehrig * vater_schweizer * nicht_verheiratet * kindesverhaeltnis
