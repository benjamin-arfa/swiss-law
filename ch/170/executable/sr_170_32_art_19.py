"""SR 170.32 Art. 19

Generated from: ch/170/de/170.32.md

Haftung besonderer Organisationen (ausserhalb ordentliche Bundesverwaltung)
und ihres Personals.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_organ_besondere_organisation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Organ oder Angestellter einer mit öffentlichen Aufgaben betrauten Organisation ausserhalb der Bundesverwaltung (Art. 19 Abs. 1 VG)"
    reference = "SR 170.32, Art. 19 Abs. 1"


class schaden_dritten_durch_organisation(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Einem Dritten durch die Organisation widerrechtlich zugefügter Schaden in CHF (Art. 19 Abs. 1 Bst. a VG)"
    reference = "SR 170.32, Art. 19 Abs. 1 Bst. a"


class organisation_kann_entschaedigung_leisten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Organisation vermag die geschuldete Entschädigung zu leisten (Art. 19 Abs. 1 Bst. a VG)"
    reference = "SR 170.32, Art. 19 Abs. 1 Bst. a"


class organisation_haftet_gegenueber_dritten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Organisation haftet dem Geschädigten nach Art. 3-6 VG (Art. 19 Abs. 1 Bst. a VG)"
    reference = "SR 170.32, Art. 19 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        ist_org = person('ist_organ_besondere_organisation', period)
        schaden = person('schaden_dritten_durch_organisation', period)
        return ist_org * (schaden > 0)


class bund_haftet_subsidiaer_fuer_organisation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund haftet subsidiär für den ungedeckten Betrag (Art. 19 Abs. 1 Bst. a VG)"
    reference = "SR 170.32, Art. 19 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        org_haftet = person('organisation_haftet_gegenueber_dritten', period)
        kann_leisten = person('organisation_kann_entschaedigung_leisten', period)
        return org_haftet * (1 - kann_leisten)
