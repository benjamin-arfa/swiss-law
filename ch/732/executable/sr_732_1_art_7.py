"""SR 732.1 Art. 7

Generated from: ch/732/de/732.1.md

Bewilligungsvoraussetzungen: Die Bewilligung wird erteilt, wenn
Schutz, Nichtverbreitung, Embargo, Versicherung, Voelkerrecht
und Sachkunde gewaehrleistet sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schutz_mensch_umwelt_gewaehrleistet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Schutz von Mensch und Umwelt und die nukleare Sicherheit gewaehrleistet sind"
    reference = "SR 732.1 Art. 7 Bst. a"


class keine_nichtverbreitungs_gruende(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob keine Gruende der Nichtverbreitung von Kernwaffen entgegenstehen"
    reference = "SR 732.1 Art. 7 Bst. b"


class keine_embargo_zwangsmassnahmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob keine Zwangsmassnahmen nach Embargogesetz erlassen wurden"
    reference = "SR 732.1 Art. 7 Bst. c"


class versicherungsschutz_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der vorgeschriebene Versicherungsschutz nach Kernenergiehaftpflichtgesetz besteht"
    reference = "SR 732.1 Art. 7 Bst. d"


class keine_voelkerrechtlichen_hindernisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob keine voelkerrechtlichen Verpflichtungen entgegenstehen"
    reference = "SR 732.1 Art. 7 Bst. e"


class sachkunde_verantwortliche_personen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die verantwortlichen Personen die erforderliche Sachkunde haben"
    reference = "SR 732.1 Art. 7 Bst. f"


class bewilligung_kernmaterial_erteilbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Voraussetzungen fuer die Erteilung der Bewilligung erfuellt sind"
    reference = "SR 732.1 Art. 7"

    def formula(person, period, parameters):
        return (
            person('schutz_mensch_umwelt_gewaehrleistet', period)
            * person('keine_nichtverbreitungs_gruende', period)
            * person('keine_embargo_zwangsmassnahmen', period)
            * person('versicherungsschutz_vorhanden', period)
            * person('keine_voelkerrechtlichen_hindernisse', period)
            * person('sachkunde_verantwortliche_personen', period)
        )
