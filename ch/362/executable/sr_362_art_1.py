"""SR 362 Art. 1

Generated from: ch/de/362.md

Approval of the bilateral agreements between Switzerland and the EU
on Schengen and Dublin association; cantonal participation; border
guard corps minimum staffing.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schengen_abkommen_genehmigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Schengen-Assoziierungsabkommen genehmigt ist"
    reference = "SR 362 Art. 1 Abs. 1 Bst. a"


class dublin_abkommen_genehmigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Dublin-Assoziierungsabkommen genehmigt ist"
    reference = "SR 362 Art. 1 Abs. 1 Bst. b"


class island_norwegen_uebereinkommen_genehmigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Uebereinkommen mit Island und Norwegen genehmigt ist"
    reference = "SR 362 Art. 1 Abs. 1 Bst. c"


class briefwechsel_abkommen_genehmigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Abkommen in Form eines Briefwechsels genehmigt ist"
    reference = "SR 362 Art. 1 Abs. 1 Bst. d"


class kantone_beteiligung_vereinbarung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Bund und Kantone die Beteiligung der Kantone an der Umsetzung des Schengen- und Dublin-Besitzstands geregelt haben"
    reference = "SR 362 Art. 1 Abs. 2"


class grenzwachtkorps_mindestbestand(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestbestand des Grenzwachtkorps (Stand 31.12.2003)"
    reference = "SR 362 Art. 1 Abs. 3"


class grenzwachtkorps_sicherheitsaufgaben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Grenzwachtkorps Sicherheitsaufgaben in Zusammenarbeit mit kantonaler und Bundespolizei erfuellt"
    reference = "SR 362 Art. 1 Abs. 3"


class eu_grenzschutzagentur_personal_nicht_zulasten_national(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die personellen Ressourcen fuer die EU-Grenz- und Kuestenwache nicht zu Lasten des nationalen Grenzschutzes gehen"
    reference = "SR 362 Art. 1 Abs. 3bis"


class bundesrat_ratifikation_ermaechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat zur Ratifikation der Abkommen ermaechtigt ist"
    reference = "SR 362 Art. 1 Abs. 4"
