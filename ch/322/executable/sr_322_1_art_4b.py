"""SR 322.1 Art. 4b

Generated from: ch/322/de/322.1.md

Auditor: Erlaesst die Einstellungsverfuegung oder das Strafmandat;
gegebenenfalls erhebt er Anklage und vertritt die Anklage vor Gericht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_auditor_militaer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Auditor in der Militaerjustiz ist"
    reference = "SR 322.1 Art. 4b"


class kann_einstellungsverfuegung_erlassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine Einstellungsverfuegung erlassen kann"
    reference = "SR 322.1 Art. 4b"

    def formula_2018(person, period, parameters):
        return person('ist_auditor_militaer', period)


class kann_strafmandat_erlassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ein Strafmandat erlassen kann"
    reference = "SR 322.1 Art. 4b"

    def formula_2018(person, period, parameters):
        return person('ist_auditor_militaer', period)


class kann_anklage_erheben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Anklage erheben und vor Gericht vertreten kann"
    reference = "SR 322.1 Art. 4b"

    def formula_2018(person, period, parameters):
        return person('ist_auditor_militaer', period)
