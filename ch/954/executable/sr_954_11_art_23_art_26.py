"""SR 954.11 Art. 23, 26

Generated from: ch/954/de/954.11.md

Organisation und Risikomanagement bei Vermoegensverwaltern/Trustees:
- Art. 23: Unterschrift zu zweien; Vertretung durch Person mit
  Wohnsitz Schweiz; FINMA kann Organ fuer Oberleitung verlangen
  bei >=10 Vollzeitstellen oder Bruttoertrag >5 Mio. CHF.
- Art. 26: Risikomanagement und interne Kontrolle; Unabhaengigkeit
  nicht erforderlich bei <=5 Vollzeitstellen oder Bruttoertrag <2 Mio.
  CHF. Interne Revision ab >10 Mio. CHF Bruttoertrag.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class finiv_vv_vollzeitstellen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Vollzeitstellen des Vermoegensverwalters/Trustees"
    reference = "SR 954.11 Art. 23 Abs. 3"


class finiv_vv_bruttoertrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Jaehrlicher Bruttoertrag (CHF)"
    reference = "SR 954.11 Art. 23 Abs. 3"


class finiv_finma_kann_oberleitungsorgan_verlangen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "FINMA kann Oberleitungsorgan verlangen (>=10 VZS oder >5 Mio. Ertrag)"
    reference = "SR 954.11 Art. 23 Abs. 3"

    def formula_2020(person, period, parameters):
        stellen = person('finiv_vv_vollzeitstellen', period)
        ertrag = person('finiv_vv_bruttoertrag', period)

        p = parameters(period).sr954_11
        return (
            (stellen >= p.oberleitungsorgan_min_vollzeitstellen)
            + (ertrag > p.oberleitungsorgan_min_ertrag)
        )


class finiv_risikomanagement_unabhaengigkeit_nicht_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unabhaengigkeit Risikomanagement nicht erforderlich (<=5 VZS oder <2 Mio.)"
    reference = "SR 954.11 Art. 26 Abs. 2"

    def formula_2020(person, period, parameters):
        stellen = person('finiv_vv_vollzeitstellen', period)
        ertrag = person('finiv_vv_bruttoertrag', period)

        p = parameters(period).sr954_11
        return (
            (stellen <= p.risiko_unabhaengigkeit_max_stellen)
            * (ertrag < p.risiko_unabhaengigkeit_max_ertrag)
        )


class finiv_interne_revision_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Interne Revision kann verlangt werden (Ertrag >10 Mio.)"
    reference = "SR 954.11 Art. 26 Abs. 4"

    def formula_2020(person, period, parameters):
        ertrag = person('finiv_vv_bruttoertrag', period)

        p = parameters(period).sr954_11
        return ertrag > p.interne_revision_min_ertrag
