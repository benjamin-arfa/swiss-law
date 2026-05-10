"""SR 128.31 Art. 10

Generated from: ch/128/de/128.31.md

Personensicherheitspruefungen nach dem ISG: Assigns security-sensitive
activities to basic or extended personnel security check levels.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bearbeitet_vertraulich_klassifizierte_informationen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als vertraulich klassifizierte Informationen bearbeitet"
    reference = "SR 128.31 Art. 10 Abs. 1 Bst. a"


class betreibt_informatikmittel_hoher_schutz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Informatikmittel der Sicherheitsstufe hoher Schutz verwaltet/betreibt/wartet/prueft"
    reference = "SR 128.31 Art. 10 Abs. 1 Bst. b"


class zugang_sicherheitszone_1(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Zugang zu einer Sicherheitszone 1 oder Schutzzone 2 hat"
    reference = "SR 128.31 Art. 10 Abs. 1 Bst. c"


class voelkerrechtlicher_vertrag_grundsicherheitspruefung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein voelkerrechtlicher Vertrag eine Grundsicherheitspruefung verlangt"
    reference = "SR 128.31 Art. 10 Abs. 1 Bst. d"


class grundsicherheitspruefung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Grundsicherheitspruefung nach dem ISG erforderlich ist"
    reference = "SR 128.31 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        a = person('bearbeitet_vertraulich_klassifizierte_informationen', period)
        b = person('betreibt_informatikmittel_hoher_schutz', period)
        c = person('zugang_sicherheitszone_1', period)
        d = person('voelkerrechtlicher_vertrag_grundsicherheitspruefung', period)
        return a + b + c + d > 0


class bearbeitet_geheim_klassifizierte_informationen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als geheim klassifizierte Informationen bearbeitet"
    reference = "SR 128.31 Art. 10 Abs. 2 Bst. a"


class betreibt_informatikmittel_sehr_hoher_schutz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Informatikmittel der Sicherheitsstufe sehr hoher Schutz verwaltet/betreibt"
    reference = "SR 128.31 Art. 10 Abs. 2 Bst. b"


class zugang_sicherheitszone_2(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Zugang zu einer Sicherheitszone 2 oder Schutzzone 3 hat"
    reference = "SR 128.31 Art. 10 Abs. 2 Bst. c"


class taetig_bei_ndb_mnd_dpsa_cea_abnd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person bei NDB, MND, DPSA, CEA oder AB-ND taetig ist"
    reference = "SR 128.31 Art. 10 Abs. 2 Bst. d"


class taetig_bei_kantonaler_vollzugsbehoerde_ndg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person bei einer kantonalen Vollzugsbehoerde nach Art. 9 NDG taetig ist"
    reference = "SR 128.31 Art. 10 Abs. 2 Bst. e"


class voelkerrechtlicher_vertrag_erweiterte_pruefung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein voelkerrechtlicher Vertrag eine erweiterte Pruefung verlangt"
    reference = "SR 128.31 Art. 10 Abs. 2 Bst. f"


class erweiterte_personensicherheitspruefung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine erweiterte Personensicherheitspruefung nach dem ISG erforderlich ist"
    reference = "SR 128.31 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        a = person('bearbeitet_geheim_klassifizierte_informationen', period)
        b = person('betreibt_informatikmittel_sehr_hoher_schutz', period)
        c = person('zugang_sicherheitszone_2', period)
        d = person('taetig_bei_ndb_mnd_dpsa_cea_abnd', period)
        e = person('taetig_bei_kantonaler_vollzugsbehoerde_ndg', period)
        f = person('voelkerrechtlicher_vertrag_erweiterte_pruefung', period)
        return a + b + c + d + e + f > 0
