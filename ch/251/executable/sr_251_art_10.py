"""SR 251 Art. 10

Generated from: ch/de/251.md

Assessment of mergers: the Competition Commission may prohibit
a merger or approve it with conditions if it creates or reinforces
a market-dominant position that can eliminate effective competition,
unless improvements in another market outweigh the disadvantages.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zusammenschluss_begruendet_marktbeherrschung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Zusammenschluss eine marktbeherrschende Stellung begruendet oder verstaerkt"
    reference = "SR 251 Art. 10 Abs. 2 Bst. a"


class zusammenschluss_beseitigt_wettbewerb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob durch die Marktbeherrschung wirksamer Wettbewerb beseitigt werden kann"
    reference = "SR 251 Art. 10 Abs. 2 Bst. a"


class verbesserung_anderer_markt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Verbesserung der Wettbewerbsverhaeltnisse in einem anderen Markt die Nachteile ueberwiegt"
    reference = "SR 251 Art. 10 Abs. 2 Bst. b"


class zusammenschluss_untersagt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Zusammenschluss untersagt wird"
    reference = "SR 251 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        begruendet = person('zusammenschluss_begruendet_marktbeherrschung', period)
        beseitigt = person('zusammenschluss_beseitigt_wettbewerb', period)
        verbesserung = person('verbesserung_anderer_markt', period)
        return begruendet * beseitigt * (1 - verbesserung)
