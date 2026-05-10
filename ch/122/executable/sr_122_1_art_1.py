"""SR 122.1 Art. 1

Generated from: ch/122/de/122.1.md

Verbot: Hamas and related organisations are prohibited. The Federal Council
may ban additional organisations whose leadership, goals, or means match
those of Hamas and that support terrorist or violent-extremist activities.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_hamas(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation die Hamas ist"
    reference = "SR 122.1 Art. 1 Abs. 1 Bst. a"


class ist_tarn_oder_nachfolgeorganisation_hamas(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation eine Tarn- oder Nachfolgeorganisation der Hamas ist oder in deren Auftrag handelt"
    reference = "SR 122.1 Art. 1 Abs. 1 Bst. b"


class fuehrung_uebereinstimmung_hamas(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Fuehrungspersonen, Zielsetzung oder Mittel mit der Hamas uebereinstimmen"
    reference = "SR 122.1 Art. 1 Abs. 2"


class unterstuetzt_terroristische_aktivitaeten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation terroristische oder gewalttaetig-extremistische Aktivitaeten unterstuetzt"
    reference = "SR 122.1 Art. 1 Abs. 2"


class bedroht_sicherheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation die innere oder aeussere Sicherheit konkret bedroht"
    reference = "SR 122.1 Art. 1 Abs. 2"


class bundesrat_verbot(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat die Organisation verboten hat (Art. 1 Abs. 2)"
    reference = "SR 122.1 Art. 1 Abs. 2"


class organisation_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation nach Art. 1 verboten ist"
    reference = "SR 122.1 Art. 1"

    def formula(person, period, parameters):
        hamas = person('ist_hamas', period)
        tarn = person('ist_tarn_oder_nachfolgeorganisation_hamas', period)
        br_verbot = person('bundesrat_verbot', period)
        return hamas + tarn + br_verbot > 0


class gilt_als_terroristische_organisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die verbotene Organisation als terroristische Organisation nach Art. 260ter Abs. 1 Bst. a Ziff. 2 StGB gilt"
    reference = "SR 122.1 Art. 1 Abs. 3"

    def formula(person, period, parameters):
        return person('organisation_verboten', period)
