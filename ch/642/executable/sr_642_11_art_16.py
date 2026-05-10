"""SR 642.11 Art. 16

Generated from: ch/642/de/642.11.md

Art. 16 Steuerbare Einkuenfte - Grundsatz (Taxable income - Principle):
1. Income tax is levied on all recurring and one-time income.
2. Income includes benefits in kind (Naturalbezuege) of every type,
   in particular free board and lodging and the value of self-consumed
   products and goods from one's own business; valued at market value.
3. Capital gains from the sale of private assets are tax-free.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einkommen_wiederkehrend(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wiederkehrende Einkuenfte (CHF)"
    reference = "SR 642.11 Art. 16 Abs. 1"


class einkommen_einmalig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einmalige Einkuenfte (CHF)"
    reference = "SR 642.11 Art. 16 Abs. 1"


class naturalbezuege_marktwert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Naturalbezuege (freie Verpflegung, Unterkunft, Eigenprodukte) zum Marktwert (CHF)"
    reference = "SR 642.11 Art. 16 Abs. 2"


class kapitalgewinne_privatvermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kapitalgewinne aus Veraeusserung von Privatvermoegen (steuerfrei, CHF)"
    reference = "SR 642.11 Art. 16 Abs. 3"


class steuerbares_gesamteinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte steuerbare Einkuenfte vor Abzuegen (CHF)"
    reference = "SR 642.11 Art. 16"

    def formula(person, period, parameters):
        wiederkehrend = person('einkommen_wiederkehrend', period)
        einmalig = person('einkommen_einmalig', period)
        naturalbezuege = person('naturalbezuege_marktwert', period)
        # Art. 16 Abs. 3: Kapitalgewinne Privatvermoegen sind steuerfrei
        # (nicht eingerechnet)
        return wiederkehrend + einmalig + naturalbezuege
