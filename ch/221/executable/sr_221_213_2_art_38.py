"""SR 221.213.2 Art. 38

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ertragswert_grundstueck(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ertragswert des einzelnen Grundstücks in CHF"
    reference = "SR 221.213.2 Art. 38 Abs. 1 lit. a"


class zinssatz_ertragswert(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Satz für die Verzinsung des Ertragswerts (vom Bundesrat festgesetzt)"
    reference = "SR 221.213.2 Art. 38 Abs. 1 lit. a"


class verpaechterlasten_grundstueck(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Abgeltung der Verpächterlasten in CHF"
    reference = "SR 221.213.2 Art. 38 Abs. 1 lit. b"


class zuschlag_allgemeine_vorteile(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zuschlag für allgemeine Vorteile einer Zupacht in CHF"
    reference = "SR 221.213.2 Art. 38 Abs. 1 lit. c"


class bessere_arrondierung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Grundstück ermöglicht eine bessere Arrondierung"
    reference = "SR 221.213.2 Art. 38 Abs. 2 lit. a"


class fuer_betrieb_guenstig_gelegen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Grundstück liegt für den Betrieb des Gewerbes günstig"
    reference = "SR 221.213.2 Art. 38 Abs. 2 lit. b"


class ist_landwirtschaftliches_gebaeude(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pachtgegenstand ist ein landwirtschaftliches Gebäude"
    reference = "SR 221.213.2 Art. 38 Abs. 3"


class zulaessiger_pachtzins_grundstueck(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zulässiger Pachtzins für einzelne Grundstücke in CHF"
    reference = "SR 221.213.2 Art. 38"

    def formula(person, period, parameters):
        ertragswert = person('ertragswert_grundstueck', period)
        zinssatz = person('zinssatz_ertragswert', period)
        verpaechterlasten = person('verpaechterlasten_grundstueck', period)
        zuschlag_vorteile = person('zuschlag_allgemeine_vorteile', period)
        arrondierung = person('bessere_arrondierung', period)
        guenstig = person('fuer_betrieb_guenstig_gelegen', period)
        ist_gebaeude = person('ist_landwirtschaftliches_gebaeude', period)

        grundbetrag = ertragswert * zinssatz + verpaechterlasten
        # Zuschlag für allgemeine Vorteile nicht für Gebäude (Abs. 3)
        vorteile = where(ist_gebaeude, 0, zuschlag_vorteile)
        # Betriebsbezogene Zuschläge von je max 15% (nicht für Gebäude)
        zuschlag_arrondierung = where(arrondierung * not_(ist_gebaeude), grundbetrag * 0.15, 0)
        zuschlag_lage = where(guenstig * not_(ist_gebaeude), grundbetrag * 0.15, 0)

        return grundbetrag + vorteile + zuschlag_arrondierung + zuschlag_lage
