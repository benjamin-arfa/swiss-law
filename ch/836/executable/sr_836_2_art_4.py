"""SR 836.2 Art. 4

Generated from: ch/836/de/836.2.md

Art. 4: Anspruchsberechtigung fuer Kinder.
Abs. 1: Zum Anspruch auf Familienzulagen berechtigen:
  a. Kinder, zu denen ein Kindesverhaeltnis im Sinne des ZGB besteht
  b. Stiefkinder
  c. Pflegekinder
  d. Geschwister und Enkelkinder, wenn die bezugsberechtigte Person
     fuer deren Unterhalt in ueberwiegendem Mass aufkommt
Abs. 3: Fuer im Ausland wohnhafte Kinder richtet sich der Anspruch
        nach zwischenstaatlichen Vereinbarungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class hat_kindesverhaeltnis(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Es besteht ein Kindesverhaeltnis im Sinne des ZGB (Art. 4 Abs. 1 lit. a)"
    reference = "SR 836.2 Art. 4 Abs. 1 lit. a"


class ist_stiefkind(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kind ist Stiefkind (Art. 4 Abs. 1 lit. b)"
    reference = "SR 836.2 Art. 4 Abs. 1 lit. b"


class ist_pflegekind(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kind ist Pflegekind (Art. 4 Abs. 1 lit. c)"
    reference = "SR 836.2 Art. 4 Abs. 1 lit. c"


class ist_geschwister_oder_enkelkind(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kind ist Geschwister oder Enkelkind der bezugsberechtigten Person (Art. 4 Abs. 1 lit. d)"
    reference = "SR 836.2 Art. 4 Abs. 1 lit. d"


class ueberwiegender_unterhalt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Bezugsberechtigte Person kommt fuer Unterhalt in ueberwiegendem Mass auf (Art. 4 Abs. 1 lit. d)"
    reference = "SR 836.2 Art. 4 Abs. 1 lit. d"


class kind_wohnt_im_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kind wohnt im Ausland (Art. 4 Abs. 3)"
    reference = "SR 836.2 Art. 4 Abs. 3"


class zwischenstaatliche_vereinbarung_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Zwischenstaatliche Vereinbarung besteht fuer Kind im Ausland"
    reference = "SR 836.2 Art. 4 Abs. 3"


class kind_berechtigt_familienzulage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kind berechtigt zum Anspruch auf Familienzulagen nach Art. 4 FamZG"
    reference = "SR 836.2 Art. 4"

    def formula(person, period, parameters):
        kindesverhaeltnis = person('hat_kindesverhaeltnis', period)
        stiefkind = person('ist_stiefkind', period)
        pflegekind = person('ist_pflegekind', period)
        geschwister_enkel = person('ist_geschwister_oder_enkelkind', period)
        unterhalt = person('ueberwiegender_unterhalt', period)
        im_ausland = person('kind_wohnt_im_ausland', period)
        vereinbarung = person('zwischenstaatliche_vereinbarung_vorhanden', period)

        # lit. a-c: Kindesverhaeltnis, Stiefkind oder Pflegekind
        grundberechtigung = kindesverhaeltnis + stiefkind + pflegekind

        # lit. d: Geschwister/Enkelkinder nur wenn ueberwiegender Unterhalt
        geschwister_berechtigt = geschwister_enkel * unterhalt

        berechtigt = (grundberechtigung + geschwister_berechtigt) > 0

        # Abs. 3: Im Ausland nur mit zwischenstaatlicher Vereinbarung
        return berechtigt * where(im_ausland, vereinbarung, 1)
