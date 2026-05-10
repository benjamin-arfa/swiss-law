"""SR 141.0 Art. 24a - Personen der dritten Auslaendergeneration

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class grosselternteil_in_schweiz_geboren_oder_aufenthaltsrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mindestens ein Grosselternteil ist in der Schweiz geboren oder hat ein Aufenthaltsrecht erworben"
    reference = "SR 141.0 Art. 24a Abs. 1 lit. a"


class elternteil_niederlassungsbewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mindestens ein Elternteil hat eine Niederlassungsbewilligung erworben"
    reference = "SR 141.0 Art. 24a Abs. 1 lit. b"


class elternteil_10_jahre_aufenthalt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mindestens ein Elternteil hat sich mindestens 10 Jahre in der Schweiz aufgehalten"
    reference = "SR 141.0 Art. 24a Abs. 1 lit. b"


class elternteil_5_jahre_obligatorische_schule(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mindestens ein Elternteil hat mindestens 5 Jahre die obligatorische Schule in der Schweiz besucht"
    reference = "SR 141.0 Art. 24a Abs. 1 lit. b"


class kind_in_schweiz_geboren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind wurde in der Schweiz geboren"
    reference = "SR 141.0 Art. 24a Abs. 1 lit. c"


class kind_besitzt_niederlassungsbewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind besitzt eine Niederlassungsbewilligung"
    reference = "SR 141.0 Art. 24a Abs. 1 lit. d"


class kind_5_jahre_obligatorische_schule(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind hat mindestens 5 Jahre die obligatorische Schule in der Schweiz besucht"
    reference = "SR 141.0 Art. 24a Abs. 1 lit. d"


class alter_person_art24a(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person in Jahren (fuer Art. 24a)"
    reference = "SR 141.0 Art. 24a Abs. 2"


# Computed variables

class anspruch_erleichterte_einbuergerung_dritte_generation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf erleichterte Einbuergerung als Person der dritten Auslaendergeneration"
    reference = "SR 141.0 Art. 24a"

    def formula(self, period, parameters):
        # lit. a: Grosselternteil
        grosseltern = self('grosselternteil_in_schweiz_geboren_oder_aufenthaltsrecht', period)

        # lit. b: Elternteil
        eltern_niederlassung = self('elternteil_niederlassungsbewilligung', period)
        eltern_aufenthalt = self('elternteil_10_jahre_aufenthalt', period)
        eltern_schule = self('elternteil_5_jahre_obligatorische_schule', period)
        eltern_ok = eltern_niederlassung * eltern_aufenthalt * eltern_schule

        # lit. c: In der Schweiz geboren
        geboren = self('kind_in_schweiz_geboren', period)

        # lit. d: Niederlassung und Schule
        niederlassung = self('kind_besitzt_niederlassungsbewilligung', period)
        schule = self('kind_5_jahre_obligatorische_schule', period)
        kind_ok = niederlassung * schule

        # Abs. 2: Bis zum vollendeten 25. Altersjahr
        alter = self('alter_person_art24a', period)
        alter_ok = alter <= 25

        return grosseltern * eltern_ok * geboren * kind_ok * alter_ok
