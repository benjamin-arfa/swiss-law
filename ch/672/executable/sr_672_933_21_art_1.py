"""SR 672.933.21 Art. 1 — Zuständigkeit für Informationsaustausch (CH-ES DBA)

Verordnung zum schweizerisch-spanischen Doppelbesteuerungsabkommen.
Art. 1: Die Eidgenössische Steuerverwaltung (ESTV) ist zuständig für die
Erteilung der in Art. 25bis Abs. 1 lit. a und b DBA vorgesehenen Auskünfte
an spanische Behörden. Bei Anständen entscheidet die ESTV.

Generated from: ch/672/de/672.933.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_switzerland.entities import Person


class auskunftsbegehren_es_eingegangen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Spanisches Auskunftsbegehren gemäss Art. 25bis Abs. 1 lit. a/b DBA ist eingegangen"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_1"


class estv_zustaendig_informationsaustausch_es(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "ESTV ist zuständig für den Informationsaustausch mit Spanien (SR 672.933.21 Art. 1 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_1"
    default_value = True


class beschwerde_moeglich_gegen_estv_entscheid(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "ESTV-Entscheid unterliegt Beschwerde nach Bundesrechtspflege (SR 672.933.21 Art. 1 Abs. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_1"
    default_value = True
