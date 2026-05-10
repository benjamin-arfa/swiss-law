"""SR 0.101 Art. 5

Generated from: ch/0/de/0.101.md

Right to liberty and security: Everyone has the right to liberty and
security of person. Lawful deprivation of liberty only in specified
cases. Rights of arrested persons.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class emrk_recht_auf_freiheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf Freiheit und Sicherheit gilt"
    reference = "SR 0.101 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_freiheitsentzug_nach_verurteilung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein rechtmaessiger Freiheitsentzug nach Verurteilung durch ein Gericht vorliegt"
    reference = "SR 0.101 Art. 5 Abs. 1 Bst. a"


class emrk_freiheitsentzug_gerichtliche_anordnung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Freiheitsentzug wegen Nichtbefolgung einer gerichtlichen Anordnung vorliegt"
    reference = "SR 0.101 Art. 5 Abs. 1 Bst. b"


class emrk_freiheitsentzug_straftatverdacht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Festnahme wegen hinreichenden Straftatverdachts vorliegt"
    reference = "SR 0.101 Art. 5 Abs. 1 Bst. c"


class emrk_freiheitsentzug_minderjaehrige(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Freiheitsentzug bei Minderjaehrigen zum Zweck ueberwachter Erziehung vorliegt"
    reference = "SR 0.101 Art. 5 Abs. 1 Bst. d"


class emrk_freiheitsentzug_ansteckende_krankheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Freiheitsentzug zur Verhinderung ansteckender Krankheiten vorliegt"
    reference = "SR 0.101 Art. 5 Abs. 1 Bst. e"


class emrk_freiheitsentzug_auslieferung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Festnahme zur Verhinderung unerlaubter Einreise oder bei Auslieferung vorliegt"
    reference = "SR 0.101 Art. 5 Abs. 1 Bst. f"


class emrk_freiheitsentzug_rechtmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Freiheitsentzug nach EMRK Art. 5 rechtmaessig ist"
    reference = "SR 0.101 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        a = person('emrk_freiheitsentzug_nach_verurteilung', period)
        b = person('emrk_freiheitsentzug_gerichtliche_anordnung', period)
        c = person('emrk_freiheitsentzug_straftatverdacht', period)
        d = person('emrk_freiheitsentzug_minderjaehrige', period)
        e = person('emrk_freiheitsentzug_ansteckende_krankheit', period)
        f = person('emrk_freiheitsentzug_auslieferung', period)
        return a + b + c + d + e + f


class emrk_recht_auf_haftpruefung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf gerichtliche Pruefung des Freiheitsentzugs gilt"
    reference = "SR 0.101 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_anspruch_schadenersatz_freiheitsentzug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Anspruch auf Schadenersatz bei rechtswidrigem Freiheitsentzug besteht"
    reference = "SR 0.101 Art. 5 Abs. 5"

    def formula(person, period, parameters):
        rechtmaessig = person('emrk_freiheitsentzug_rechtmaessig', period)
        return not_(rechtmaessig)
