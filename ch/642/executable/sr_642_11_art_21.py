"""SR 642.11 Art. 21

Generated from: ch/642/de/642.11.md

Art. 21 Unbewegliches Vermoegen (Real estate income):
1. Taxable are income from immovable property, in particular:
   a. All income from rental, lease, usufruct or other use;
   b. The imputed rental value (Eigenmietwert) of owner-occupied property;
   c. Income from building-right contracts (Baurecht);
   d. Income from exploitation of gravel, sand and other soil components.
2. The imputed rental value is determined considering local conditions
   and actual use of the owner-occupied property at the place of domicile.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einkommen_vermietung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus Vermietung, Verpachtung, Nutzniessung von Liegenschaften (CHF)"
    reference = "SR 642.11 Art. 21 Abs. 1 Bst. a"


class eigenmietwert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eigenmietwert der selbstbewohnten Liegenschaft (CHF)"
    reference = "SR 642.11 Art. 21 Abs. 1 Bst. b"


class ist_eigentuemer_selbstbewohnt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person bewohnt eigene Liegenschaft oder hat unentgeltliches Nutzungsrecht"
    reference = "SR 642.11 Art. 21 Abs. 1 Bst. b"


class einkommen_baurechtsvertraege(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus Baurechtsvertraegen (CHF)"
    reference = "SR 642.11 Art. 21 Abs. 1 Bst. c"


class einkommen_bodenausbeutung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus Ausbeutung von Kies, Sand und anderen Bodenbestandteilen (CHF)"
    reference = "SR 642.11 Art. 21 Abs. 1 Bst. d"


class einkommen_unbewegliches_vermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte steuerbare Einkuenfte aus unbeweglichem Vermoegen (CHF)"
    reference = "SR 642.11 Art. 21"

    def formula(person, period, parameters):
        vermietung = person('einkommen_vermietung', period)
        eigenmietwert_betrag = person('eigenmietwert', period)
        ist_eigentuemer = person('ist_eigentuemer_selbstbewohnt', period)
        baurecht = person('einkommen_baurechtsvertraege', period)
        boden = person('einkommen_bodenausbeutung', period)

        # Eigenmietwert nur wenn selbstbewohnt (Abs. 1 Bst. b)
        eigenmietwert_steuerbar = where(ist_eigentuemer, eigenmietwert_betrag, 0)

        return vermietung + eigenmietwert_steuerbar + baurecht + boden
