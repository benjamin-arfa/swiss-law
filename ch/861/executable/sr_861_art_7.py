"""SR 861 Art. 7

Generated from: ch/de/861.md

Decision and service contracts: BSV decides by decree on applications
from day-care, after-school care, and family day-care; innovation
projects via service contracts; subsidy increase and alignment projects
by decree.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bsv_entscheid_verfuegung_kita(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BSV durch Verfuegung ueber Gesuche der Kindertagesstaetten und schulergaenzenden Einrichtungen entscheidet"
    reference = "SR 861 Art. 7 Abs. 1"


class bsv_anhoerung_kanton(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BSV die zustaendige Behoerde des Kantons anhoert"
    reference = "SR 861 Art. 7 Abs. 1"


class bsv_innovationsprojekt_leistungsvertrag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BSV Innovationsprojekte aufgrund von Leistungsvertraegen gewaehrt"
    reference = "SR 861 Art. 7 Abs. 2"


class bsv_entscheid_verfuegung_subventionen_projekte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das BSV durch Verfuegung ueber Gesuche fuer Subventionserhoehung und Abstimmungsprojekte entscheidet"
    reference = "SR 861 Art. 7 Abs. 3"
