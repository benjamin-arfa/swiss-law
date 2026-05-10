"""SR 128.51 Art. 14

Generated from: ch/128/de/128.51.md

Zu meldende Cyberangriffe: Defines when functionality is endangered,
what counts as manipulation/data breach, when an attack is long-undetected,
and when extortion is involved.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mitarbeitende_von_systemunterbruechen_betroffen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Mitarbeitende oder Dritte von Systemunterbruechen betroffen sind"
    reference = "SR 128.51 Art. 14 Abs. 1 Bst. a"


class nur_notfallplaene_aufrechterhalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation ihre Taetigkeiten nur noch mit Notfallplaenen aufrechterhalten kann"
    reference = "SR 128.51 Art. 14 Abs. 1 Bst. b"


class funktionsfaehigkeit_gefaehrdet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Funktionsfaehigkeit einer kritischen Infrastruktur gefaehrdet ist"
    reference = "SR 128.51 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        unterbrueche = person('mitarbeitende_von_systemunterbruechen_betroffen', period)
        notfall = person('nur_notfallplaene_aufrechterhalten', period)
        return unterbrueche + notfall > 0


class informationen_unbefugt_eingesehen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob geschaeftsrelevante Informationen unbefugt eingesehen, veraendert oder offengelegt wurden"
    reference = "SR 128.51 Art. 14 Abs. 2 Bst. a"


class datenschutzverletzung_gemeldet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Meldung nach Art. 24 DSG ueber Verletzung der Datensicherheit erfolgt ist"
    reference = "SR 128.51 Art. 14 Abs. 2 Bst. b"


class manipulation_oder_abfluss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Manipulation oder ein Abfluss von Informationen vorliegt"
    reference = "SR 128.51 Art. 14 Abs. 2"

    def formula(person, period, parameters):
        unbefugt = person('informationen_unbefugt_eingesehen', period)
        dsg = person('datenschutzverletzung_gemeldet', period)
        return unbefugt + dsg > 0


class tage_seit_cybervorfall(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Tage seit dem Cybervorfall"
    reference = "SR 128.51 Art. 14 Abs. 3"


class cyberangriff_laengere_zeit_unentdeckt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Cyberangriff ueber einen laengeren Zeitraum unentdeckt blieb (mehr als 90 Tage)"
    reference = "SR 128.51 Art. 14 Abs. 3"

    def formula(person, period, parameters):
        return person('tage_seit_cybervorfall', period) > 90


class cyberangriff_mit_erpressung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Cyberangriff mit Erpressung, Drohung oder Noetigung verbunden ist"
    reference = "SR 128.51 Art. 14 Abs. 4"
