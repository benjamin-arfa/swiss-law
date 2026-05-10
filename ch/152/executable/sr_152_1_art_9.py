"""SR 152.1 Art. 9

Generated from: ch/152/de/152.1.md

Grundsatz der freien Einsichtnahme und Schutzfrist von 30 Jahren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class datum_juengstes_dokument(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr des juengsten Dokuments eines Geschaefts oder Dossiers"
    reference = "SR 152.1 Art. 10"


class aktuelles_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aktuelles Kalenderjahr"
    reference = "SR 152.1 Art. 9"


class schutzfrist_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die ordentliche 30-jaehrige Schutzfrist abgelaufen ist"
    reference = "SR 152.1 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        datum = person('datum_juengstes_dokument', period)
        aktuell = person('aktuelles_jahr', period)
        return (aktuell - datum) >= 30


class war_vor_ablieferung_oeffentlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Unterlagen bereits vor Ablieferung oeffentlich zugaenglich waren"
    reference = "SR 152.1 Art. 9 Abs. 2"


class archivgut_oeffentlich_zugaenglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Archivgut oeffentlich zugaenglich ist"
    reference = "SR 152.1 Art. 9"

    def formula(person, period, parameters):
        frist_ab = person('schutzfrist_abgelaufen', period)
        vorher_oeffentlich = person('war_vor_ablieferung_oeffentlich', period)
        return frist_ab + vorher_oeffentlich > 0
