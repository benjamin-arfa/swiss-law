"""SR 141.01 Art. 6

Generated from: ch/141/de/141.01.md

Sprachnachweis: Muendliche Kompetenzen mindestens B1, schriftliche
mindestens A2 in einer Landessprache. Nachweis gilt als erbracht bei
Muttersprache, 5 Jahre Schulbesuch, Sekundarstufe-II/Tertiaer-Abschluss
oder anerkanntem Sprachtest.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sprachkompetenz_muendlich_b1(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob muendliche Sprachkompetenzen mindestens auf Referenzniveau B1 in einer Landessprache vorliegen"
    reference = "SR 141.01 Art. 6 Abs. 1"


class sprachkompetenz_schriftlich_a2(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob schriftliche Sprachkompetenzen mindestens auf Referenzniveau A2 in einer Landessprache vorliegen"
    reference = "SR 141.01 Art. 6 Abs. 1"


class landessprache_ist_muttersprache(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Landessprache als Muttersprache gesprochen und geschrieben wird"
    reference = "SR 141.01 Art. 6 Abs. 2 Bst. a"


class schulbesuch_landessprache_5_jahre(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob mindestens fuenf Jahre die obligatorische Schule in einer Landessprache besucht wurde"
    reference = "SR 141.01 Art. 6 Abs. 2 Bst. b"


class ausbildung_sekundarstufe_landessprache(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Ausbildung auf Sekundarstufe II oder Tertiaerstufe in einer Landessprache abgeschlossen wurde"
    reference = "SR 141.01 Art. 6 Abs. 2 Bst. c"


class anerkannter_sprachnachweis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein anerkannter Sprachnachweis die erforderlichen Kompetenzen bescheinigt"
    reference = "SR 141.01 Art. 6 Abs. 2 Bst. d"


class sprachnachweis_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Sprachnachweis fuer die Einbuergerung erfuellt ist"
    reference = "SR 141.01 Art. 6"

    def formula(person, period, parameters):
        direkt = (
            person('sprachkompetenz_muendlich_b1', period)
            * person('sprachkompetenz_schriftlich_a2', period)
        )
        alternativ = (
            person('landessprache_ist_muttersprache', period)
            + person('schulbesuch_landessprache_5_jahre', period)
            + person('ausbildung_sekundarstufe_landessprache', period)
            + person('anerkannter_sprachnachweis', period)
        ) > 0
        return direkt + alternativ > 0
