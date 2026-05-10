"""SR 453.0 Art. 27a

Generated from: ch/453/de/453.0.md
Einfuhrverbote fuer Exemplare geschuetzter Arten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class exemplar_der_natur_entnommen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exemplar wurde der Natur entnommen"
    reference = "SR 453.0 Art. 27a Abs. 1 Bst. a"


class art_stark_gefaehrdet_oder_vom_aussterben_bedroht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Art ist stark gefaehrdet oder vom Aussterben bedroht (IUCN oder anderweitig belegt)"
    reference = "SR 453.0 Art. 27a Abs. 1 Bst. b Ziff. 1"


class art_durch_handel_gefaehrdet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Art ist durch internationalen Handel gefaehrdet"
    reference = "SR 453.0 Art. 27a Abs. 1 Bst. b Ziff. 2"


class herkunftsland_schuetzt_lebensraum_und_verbietet_entnahme(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesetzgebung des Herkunftslandes schuetzt Lebensraum und verbietet Entnahme"
    reference = "SR 453.0 Art. 27a Abs. 1 Bst. c"


class ist_lebendes_exemplar_fuer_zuchtprogramm(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Lebendes Exemplar fuer registriertes Zuchtprogramm"
    reference = "SR 453.0 Art. 27a Abs. 2"


class einfuhr_verboten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einfuhr des Exemplars ist verboten"
    reference = "SR 453.0 Art. 27a"

    def formula(person, period, parameters):
        natur = person('exemplar_der_natur_entnommen', period)
        gefaehrdet = person('art_stark_gefaehrdet_oder_vom_aussterben_bedroht', period)
        handel = person('art_durch_handel_gefaehrdet', period)
        herkunft = person('herkunftsland_schuetzt_lebensraum_und_verbietet_entnahme', period)
        zucht = person('ist_lebendes_exemplar_fuer_zuchtprogramm', period)

        # Verbot wenn alle Bedingungen Abs. 1 erfuellt
        verbot = natur * gefaehrdet * handel * herkunft

        # Ausnahme Abs. 2: lebende Exemplare fuer Zuchtprogramme
        return verbot * not_(zucht)
