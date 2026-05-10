"""SR 819.14 Art. 4a

Generated from: ch/819/de/819.14.md

Art. 4a Pflichten der Wirtschaftsakteure:
Obligations of economic operators derive from the EU Machinery Directive
and EU Market Surveillance Regulation:
a. Manufacturer: EU Machinery Directive Art. 5, EU MSR Art. 4(3)-(4)
b. Authorised representative: EU Machinery Directive Art. 5, EU MSR Art. 4(3)-(4), Art. 5
c. Importer, distributor, fulfilment service provider: EU MSR Art. 4(3)-(4)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class maschv_wirtschaftsakteur_rolle(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Rolle des Wirtschaftsakteurs (hersteller, bevollmaechtigter, importeur, haendler, fulfilment)"
    reference = "SR 819.14 Art. 4a"


class maschv_pflichten_eu_maschinenrichtlinie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Pflichten aus der EU-Maschinenrichtlinie gelten"
    reference = "SR 819.14 Art. 4a Bst. a-b"

    def formula(person, period, parameters):
        import numpy as np
        rolle = person('maschv_wirtschaftsakteur_rolle', period)
        return np.isin(rolle, ['hersteller', 'bevollmaechtigter'])


class maschv_pflichten_eu_marktueberwachung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Pflichten aus der EU-Marktueberwachungsverordnung gelten"
    reference = "SR 819.14 Art. 4a"

    def formula(person, period, parameters):
        # All economic operators have obligations under the EU MSR
        rolle = person('maschv_wirtschaftsakteur_rolle', period)
        return rolle != ''
