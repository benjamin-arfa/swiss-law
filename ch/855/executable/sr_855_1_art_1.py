"""SR 855.1 Art. 1-5

Generated from: ch/855/de/855.1.md

Bundesbeschluss betreffend die Genehmigung des Übereinkommens über die
Rechtsstellung der Staatenlosen.

Art. 1: Approval of the Convention on the Status of Stateless Persons.
Art. 2: Authorization for the Federal Council to ratify.
Art. 3: Welfare provisions for stateless persons — same rules as for refugees
         per chapters 5 and 6 of the Asylum Act (SR 142.31).
Art. 4: Authorization to withdraw reservation to Art. 17 of Refugee Convention.
Art. 5: Publication provision.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class staatenlos_fuersorge_wie_fluechtling(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Untersteht die staatenlose Person den Fürsorgebestimmungen für Flüchtlinge?"
    reference = "SR 855.1 Art. 3, SR 142.31 Kap. 5-6"

    def formula_1999_10(person, period, parameters):
        ist_staatenlos = person('ist_staatenlos', period)
        untersteht_uebereinkommen = person(
            'untersteht_staatenlosenabkommen', period
        )
        return ist_staatenlos * untersteht_uebereinkommen


class ist_staatenlos(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ist die Person staatenlos?"
    reference = "SR 855.1, Übereinkommen vom 28. September 1954 (SR 0.142.40)"


class untersteht_staatenlosenabkommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Untersteht die Person dem Übereinkommen über die Rechtsstellung der Staatenlosen?"
    reference = "SR 855.1 Art. 3, SR 0.142.40"
