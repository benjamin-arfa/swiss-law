"""SR 915.8 Art. 5

Generated from: ch/915/de/915.8.md

FKINV - Art. 5: Beurteilung des Gesuchs und Entscheid ueber die Finanzhilfe.
BLW beurteilt Gesuche anhand definierter Kriterien.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fkinv_gesuchsunterlagen_vollstaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eingereichte Gesuchsunterlagen sind vollstaendig (Art. 5 Abs. 1 lit. a)"
    reference = "SR 915.8 Art. 5 Abs. 1 lit. a"


class fkinv_kosteneffizienz_gegeben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kosteneffizienz und Wirtschaftlichkeit sind gegeben (Art. 5 Abs. 1 lit. b)"
    reference = "SR 915.8 Art. 5 Abs. 1 lit. b"


class fkinv_konzeption_umsetzung_wirkungskontrolle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Konzeption, Umsetzung und Wirkungskontrolle der Leistungen sind ueberzeugend (Art. 5 Abs. 1 lit. c)"
    reference = "SR 915.8 Art. 5 Abs. 1 lit. c"


class fkinv_beitrag_bundesstrategien(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beitrag an die Umsetzung bestehender Strategien des Bundes (Art. 5 Abs. 1 lit. d)"
    reference = "SR 915.8 Art. 5 Abs. 1 lit. d"


class fkinv_ergebnisse_vorangegangener_perioden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "In vorangegangenen Beitragsperioden erreichte Ergebnisse sind zufriedenstellend (Art. 5 Abs. 1 lit. e)"
    reference = "SR 915.8 Art. 5 Abs. 1 lit. e"


class fkinv_gesuch_genehmigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BLW genehmigt das Gesuch um Finanzhilfe (Art. 5 Abs. 3)"
    reference = "SR 915.8 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        # Art. 5 Abs. 1: BLW beurteilt Gesuche aufgrund der Kriterien a-e.
        voraussetzungen = person('fkinv_finanzhilfe_voraussetzungen_erfuellt', period)
        unterlagen = person('fkinv_gesuchsunterlagen_vollstaendig', period)
        effizienz = person('fkinv_kosteneffizienz_gegeben', period)
        konzeption = person('fkinv_konzeption_umsetzung_wirkungskontrolle', period)
        strategien = person('fkinv_beitrag_bundesstrategien', period)
        eingereicht = person('fkinv_gesuch_beim_blw_eingereicht', period)
        return voraussetzungen * unterlagen * effizienz * konzeption * strategien * eingereicht
