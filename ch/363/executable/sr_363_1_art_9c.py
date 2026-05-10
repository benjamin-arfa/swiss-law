"""SR 363.1 Art. 9c

Generated from: ch/363/de/363.1.md

Koordinationsstelle: Bearbeitungsgebuehren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dna_bearbeitungstyp(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Typ der DNA-Bearbeitung (personenprofil, spurenprofil, suchlauf_6a4, y_dna, verwandtschaft, vermisst, unbekannte_leiche, verwandte_vermisst)"
    reference = "SR 363.1 Art. 9c Abs. 1"


class dna_bearbeitungsgebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebuehr der Koordinationsstelle fuer die DNA-Bearbeitung (CHF)"
    reference = "SR 363.1 Art. 9c Abs. 1"

    def formula(person, period, parameters):
        typ = person('dna_bearbeitungstyp', period)
        return select(
            [typ == 'personenprofil', typ == 'spurenprofil', typ == 'suchlauf_6a4',
             typ == 'y_dna', typ == 'verwandtschaft', typ == 'vermisst',
             typ == 'unbekannte_leiche', typ == 'verwandte_vermisst'],
            [20.0, 40.0, 60.0, 40.0, 200.0, 40.0, 60.0, 40.0],
            default=0.0
        )


class dna_ausserordentlicher_fall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ausserordentlicher Fall ausserhalb der regulaeren Dienstzeiten"
    reference = "SR 363.1 Art. 9c Abs. 2"


class dna_ausserordentlich_arbeitsstunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Angefangene Arbeitsstunden bei ausserordentlichem Fall"
    reference = "SR 363.1 Art. 9c Abs. 2"


class dna_ausserordentlich_gebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebuehr fuer ausserordentliche Faelle (Grundgebuehr + Stundenansatz) (CHF)"
    reference = "SR 363.1 Art. 9c Abs. 2"

    def formula(person, period, parameters):
        ist_ausserordentlich = person('dna_ausserordentlicher_fall', period)
        stunden = person('dna_ausserordentlich_arbeitsstunden', period)
        # Grundgebuehr 300 CHF + 128 CHF pro angefangene Arbeitsstunde
        return ist_ausserordentlich * (300.0 + stunden * 128.0)
