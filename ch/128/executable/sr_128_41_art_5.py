"""SR 128.41 Art. 5

Generated from: ch/128/de/128.41.md

Pruefung des Antrags: The operational security office must not waive the
procedure when specific conditions regarding classified information or
cross-departmental IT resources are met.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class auftrag_umfasst_geheime_informationen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Auftrag als geheim klassifizierte Informationen oder Informatikmittel sehr hoher Schutz umfasst"
    reference = "SR 128.41 Art. 5 Abs. 2 Bst. a"


class auftrag_umfasst_vertraulich_mehrere_behoerden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Auftrag vertrauliche Informationen umfasst, die mehrere Behoerden oder Departemente betreffen"
    reference = "SR 128.41 Art. 5 Abs. 2 Bst. b"


class auftrag_umfasst_behoerdenuebergreifende_it(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Auftrag Informatikmittel hoher Schutz fuer behoerdenuebergreifende Aufgaben umfasst"
    reference = "SR 128.41 Art. 5 Abs. 2 Bst. c"


class betrieb_benoetigt_internationale_bescheinigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Betrieb eine internationale Betriebssicherheitsbescheinigung benoetigt"
    reference = "SR 128.41 Art. 5 Abs. 2 Bst. d"


class verzicht_auf_verfahren_unzulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob auf die Einleitung des Verfahrens nicht verzichtet werden darf"
    reference = "SR 128.41 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        a = person('auftrag_umfasst_geheime_informationen', period)
        b = person('auftrag_umfasst_vertraulich_mehrere_behoerden', period)
        c = person('auftrag_umfasst_behoerdenuebergreifende_it', period)
        d = person('betrieb_benoetigt_internationale_bescheinigung', period)
        return a + b + c + d > 0
