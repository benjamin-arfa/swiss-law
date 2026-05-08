"""SR 783.016.2 Art. 1

Generated from: ch/783/de/783.016.2.md

Geltungsbereich: Die VMAP gilt fuer Anbieterinnen von Postdiensten mit
Meldepflicht (ordentliche oder vereinfachte) und deren Arbeitsverhaeltnisse
sowie fuer Subunternehmerinnen mit >50% Umsatz aus Postdiensten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_anbieterin_postdienste_meldepflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Anbieterin von Postdiensten der ordentlichen oder vereinfachten Meldepflicht unterliegt"
    reference = "SR 783.016.2 Art. 1 Abs. 1"


class ist_subunternehmerin_postdienste(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Subunternehmerin handelt, die mehr als 50% des Umsatzes mit Postdiensten erzielt"
    reference = "SR 783.016.2 Art. 1 Abs. 2 Bst. b"


class anteil_umsatz_postdienste(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil des jaehrlichen Umsatzerloeses aus Postdiensten (0.0 bis 1.0)"
    reference = "SR 783.016.2 Art. 1 Abs. 2 Bst. b"


class vmap_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die VMAP auf das Arbeitsverhaeltnis anwendbar ist"
    reference = "SR 783.016.2 Art. 1"

    def formula(person, period, parameters):
        meldepflichtig = person('ist_anbieterin_postdienste_meldepflichtig', period)
        subunternehmerin = person('anteil_umsatz_postdienste', period) > 0.5
        return meldepflichtig + subunternehmerin
