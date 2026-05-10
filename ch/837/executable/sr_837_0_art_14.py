"""SR 837.0 Art. 14

Generated from: ch/837/de/837.0.md

Art. 14: Befreiung von der Erfuellung der Beitragszeit
(Exemption from contribution period requirement)

- Abs. 1: Exempt are persons who, within the framework period, were not
  employed for more than 12 months total and could not fulfil contribution
  time due to:
  a. education/retraining (if Swiss resident for 10+ years)
  b. illness, accident, or maternity (if Swiss resident during that time)
  c. stay in a Swiss detention or educational institution

- Abs. 2: Also exempt are persons forced to take up or expand employment
  due to separation/divorce, disability/death of spouse, loss of IV pension,
  provided the event was within the last year and they resided in Switzerland.

- Abs. 3: Swiss nationals returning from abroad (non-EU/EFTA, >1 year)
  are exempt for one year if they can prove foreign employment and had
  6+ months of Swiss contribution-liable employment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alv_befreit_ausbildung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Von Beitragszeit befreit wegen Ausbildung/Umschulung (Art. 14 Abs. 1 Bst. a)"
    reference = "SR 837.0 Art. 14 Abs. 1 Bst. a"


class alv_befreit_krankheit_unfall_mutterschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Von Beitragszeit befreit wegen Krankheit/Unfall/Mutterschaft (Art. 14 Abs. 1 Bst. b)"
    reference = "SR 837.0 Art. 14 Abs. 1 Bst. b"


class alv_befreit_haft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Von Beitragszeit befreit wegen Haftaufenthalt (Art. 14 Abs. 1 Bst. c)"
    reference = "SR 837.0 Art. 14 Abs. 1 Bst. c"


class alv_befreit_trennung_scheidung_tod(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Von Beitragszeit befreit wegen Trennung/Scheidung/Tod des Ehegatten (Art. 14 Abs. 2)"
    reference = "SR 837.0 Art. 14 Abs. 2"


class alv_befreit_ausland_rueckkehr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Von Beitragszeit befreit wegen Rueckkehr aus dem Ausland (Art. 14 Abs. 3)"
    reference = "SR 837.0 Art. 14 Abs. 3"


class alv_von_beitragszeit_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Von der Erfuellung der Beitragszeit befreit nach Art. 14 AVIG"
    reference = "SR 837.0 Art. 14"

    def formula(person, period, parameters):
        ausbildung = person('alv_befreit_ausbildung', period)
        krankheit = person('alv_befreit_krankheit_unfall_mutterschaft', period)
        haft = person('alv_befreit_haft', period)
        trennung = person('alv_befreit_trennung_scheidung_tod', period)
        ausland = person('alv_befreit_ausland_rueckkehr', period)
        return ausbildung + krankheit + haft + trennung + ausland
