"""SR 251 Art. 5

Generated from: ch/de/251.md

Inadmissible competition agreements: agreements that significantly
impair competition without efficiency justification, or that
eliminate effective competition. Presumptions for horizontal
(price-fixing, quantity restrictions, market allocation) and
vertical (minimum/fixed prices, territorial allocation) restraints.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class abrede_beeintraechtigt_wettbewerb_erheblich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Abrede den Wettbewerb erheblich beeintraechtigt"
    reference = "SR 251 Art. 5 Abs. 1"


class abrede_effizienz_gerechtfertigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Abrede durch wirtschaftliche Effizienz gerechtfertigt ist"
    reference = "SR 251 Art. 5 Abs. 2"


class abrede_beseitigt_wirksamen_wettbewerb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Abrede zur Beseitigung wirksamen Wettbewerbs fuehrt"
    reference = "SR 251 Art. 5 Abs. 1"


class horizontale_preisabrede(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine horizontale Preisabrede vorliegt (Vermutung der Wettbewerbsbeseitigung)"
    reference = "SR 251 Art. 5 Abs. 3 Bst. a"


class horizontale_mengenabrede(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine horizontale Mengenabrede vorliegt"
    reference = "SR 251 Art. 5 Abs. 3 Bst. b"


class horizontale_marktaufteilung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine horizontale Marktaufteilung vorliegt"
    reference = "SR 251 Art. 5 Abs. 3 Bst. c"


class vertikale_preisbindung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine vertikale Mindest- oder Festpreisbindung vorliegt"
    reference = "SR 251 Art. 5 Abs. 4"


class vermutung_wettbewerbsbeseitigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vermutung der Beseitigung wirksamen Wettbewerbs greift"
    reference = "SR 251 Art. 5 Abs. 3-4"

    def formula(person, period, parameters):
        return (
            person('horizontale_preisabrede', period)
            + person('horizontale_mengenabrede', period)
            + person('horizontale_marktaufteilung', period)
            + person('vertikale_preisbindung', period)
        ) > 0


class abrede_unzulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Wettbewerbsabrede unzulaessig ist"
    reference = "SR 251 Art. 5"

    def formula(person, period, parameters):
        beseitigung = person('abrede_beseitigt_wirksamen_wettbewerb', period)
        erheblich = person('abrede_beeintraechtigt_wettbewerb_erheblich', period)
        effizienz = person('abrede_effizienz_gerechtfertigt', period)
        return beseitigung + (erheblich * (1 - effizienz)) > 0
