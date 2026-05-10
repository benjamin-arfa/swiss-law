"""SR 235.1 Art. 4

Generated from: ch/235/de/235.1.md

Grundsaetze: Rechtmaessigkeit, Treu und Glauben, Verhaeltnismaessigkeit,
Zweckbindung, Erkennbarkeit, Einwilligung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_bearbeitung_rechtmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Personendaten werden rechtmaessig bearbeitet"
    reference = "SR 235.1 Art. 4 Abs. 1"


class dsg_bearbeitung_nach_treu_und_glauben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bearbeitung erfolgt nach Treu und Glauben und ist verhaeltnismaessig"
    reference = "SR 235.1 Art. 4 Abs. 2"


class dsg_zweckbindung_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten werden nur zum angegebenen/ersichtlichen/gesetzlichen Zweck bearbeitet"
    reference = "SR 235.1 Art. 4 Abs. 3"


class dsg_beschaffung_erkennbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Beschaffung und Zweck der Bearbeitung sind fuer die betroffene Person erkennbar"
    reference = "SR 235.1 Art. 4 Abs. 4"


class dsg_einwilligung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einwilligung der betroffenen Person ist erforderlich"
    reference = "SR 235.1 Art. 4 Abs. 5"


class dsg_einwilligung_nach_information_freiwillig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einwilligung erfolgt nach angemessener Information freiwillig"
    reference = "SR 235.1 Art. 4 Abs. 5"


class dsg_besonders_schuetzenswerte_daten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Besonders schuetzenswerte Personendaten oder Persoenlichkeitsprofile werden bearbeitet"
    reference = "SR 235.1 Art. 4 Abs. 5"


class dsg_einwilligung_ausdruecklich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einwilligung erfolgt ausdruecklich"
    reference = "SR 235.1 Art. 4 Abs. 5"


class dsg_einwilligung_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einwilligung ist gueltig nach Art. 4 Abs. 5 DSG"
    reference = "SR 235.1 Art. 4 Abs. 5"

    def formula(person, period, parameters):
        erforderlich = person('dsg_einwilligung_erforderlich', period)
        freiwillig = person('dsg_einwilligung_nach_information_freiwillig', period)
        besonders = person('dsg_besonders_schuetzenswerte_daten', period)
        ausdruecklich = person('dsg_einwilligung_ausdruecklich', period)
        # Einwilligung gueltig wenn: freiwillig nach Information UND
        # bei besonders schuetzenswerten Daten zusaetzlich ausdruecklich
        return erforderlich * freiwillig * (not_(besonders) + ausdruecklich)


class dsg_grundsaetze_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Alle Grundsaetze nach Art. 4 DSG sind eingehalten"
    reference = "SR 235.1 Art. 4"

    def formula(person, period, parameters):
        rechtmaessig = person('dsg_bearbeitung_rechtmaessig', period)
        treu_glauben = person('dsg_bearbeitung_nach_treu_und_glauben', period)
        zweck = person('dsg_zweckbindung_eingehalten', period)
        erkennbar = person('dsg_beschaffung_erkennbar', period)
        einwilligung_erf = person('dsg_einwilligung_erforderlich', period)
        einwilligung_ok = person('dsg_einwilligung_gueltig', period)
        return rechtmaessig * treu_glauben * zweck * erkennbar * (not_(einwilligung_erf) + einwilligung_ok)
