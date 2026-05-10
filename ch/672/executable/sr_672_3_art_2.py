"""SR 672.3 Art. 2 — Voraussetzungen

Bundesgesetz über die Anerkennung privater Vereinbarungen zur Vermeidung der Doppelbesteuerung.
Generated from: ch/de/672/672.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class reziprozitaet_gewaehrleistet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Reziprozität ist gewährleistet (SR 672.3 Art. 2 lit. a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_2"


class vereinbar_mit_abkommenspolitik(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Vereinbarung ist mit der Abkommenspolitik der Schweiz zur Vermeidung der Doppelbesteuerung vereinbar (SR 672.3 Art. 2 lit. b)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_2"


class kommissionen_haben_zugestimmt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die zuständigen Kommissionen des National- und Ständerates haben der Anerkennung zugestimmt (SR 672.3 Art. 2 lit. c)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_2"


class voraussetzungen_anerkennung_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Voraussetzungen für die Anerkennung einer privaten Vereinbarung sind erfüllt (SR 672.3 Art. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_2"

    def formula(person, period, parameters):
        # Art. 2: Anerkennung setzt voraus:
        # a) Reziprozität gewährleistet
        # b) Vereinbarkeit mit Abkommenspolitik
        # c) Zustimmung der zuständigen Kommissionen
        reziprozitaet = person('reziprozitaet_gewaehrleistet', period)
        vereinbar = person('vereinbar_mit_abkommenspolitik', period)
        zustimmung = person('kommissionen_haben_zugestimmt', period)
        return reziprozitaet * vereinbar * zustimmung
