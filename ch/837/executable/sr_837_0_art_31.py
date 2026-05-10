"""SR 837.0 Art. 31

Generated from: ch/837/de/837.0.md

Art. 31: Anspruchsvoraussetzungen (Kurzarbeitsentschaedigung)
(Eligibility for short-time work compensation)

- Abs. 1: Employees whose normal working hours are reduced or work is
  entirely suspended are entitled to short-time work compensation if:
  a. they are contribution-liable or below AHV minimum contribution age
  b. the work loss is countable (Art. 32)
  c. the employment relationship has not been terminated
  d. the work loss is expected to be temporary and likely to preserve jobs
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alv_kurzarbeit_beitragspflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Fuer die Versicherung beitragspflichtig oder Mindestalter nicht erreicht"
    reference = "SR 837.0 Art. 31 Abs. 1 Bst. a"


class alv_kurzarbeit_arbeitsausfall_anrechenbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitsausfall bei Kurzarbeit anrechenbar (Art. 32)"
    reference = "SR 837.0 Art. 31 Abs. 1 Bst. b"


class alv_kurzarbeit_nicht_gekuendigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitsverhaeltnis ist nicht gekuendigt"
    reference = "SR 837.0 Art. 31 Abs. 1 Bst. c"


class alv_kurzarbeit_voruebergehend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitsausfall voraussichtlich voruebergehend, Arbeitsplaetze erhaltbar"
    reference = "SR 837.0 Art. 31 Abs. 1 Bst. d"


class alv_anspruch_kurzarbeitsentschaedigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Kurzarbeitsentschaedigung nach Art. 31 AVIG"
    reference = "SR 837.0 Art. 31"

    def formula(person, period, parameters):
        beitragspflichtig = person('alv_kurzarbeit_beitragspflichtig', period)
        anrechenbar = person('alv_kurzarbeit_arbeitsausfall_anrechenbar', period)
        nicht_gekuendigt = person('alv_kurzarbeit_nicht_gekuendigt', period)
        voruebergehend = person('alv_kurzarbeit_voruebergehend', period)

        return beitragspflichtig * anrechenbar * nicht_gekuendigt * voruebergehend
