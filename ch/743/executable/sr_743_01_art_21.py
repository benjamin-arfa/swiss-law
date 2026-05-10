"""SR 743.01 Art. 21

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Versicherungspflicht.
Seilbahnbetreiber muessen bei einem in der Schweiz zugelassenen
Versicherungsunternehmen gegen Haftpflichtfolgen versichert sein.
Ausgenommen: Ansprueche des Eigentuemers/Betreibers, bestimmte
Familienangehoerige bei Sachschaeden, befoerderte Sachen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class seilbahn_versicherungspflichtig(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob der Seilbahnbetreiber versicherungspflichtig ist"
    reference = "SR 743.01 Art. 21 Abs. 1"

    def formula(organisation, period, parameters):
        return organisation('seilbahn_sebg_anwendbar', period)


class seilbahn_versicherung_anspruch_eigentuemer_ausgenommen(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ansprueche des Eigentuemers/Betreibers sind von der Versicherungspflicht ausgenommen"
    reference = "SR 743.01 Art. 21 Abs. 2 Bst. a"

    def formula(organisation, period, parameters):
        return 1


class seilbahn_versicherung_sachschaeden_befoerderte_sachen_ausgenommen(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ansprueche aus Sachschaeden an befoerderten Sachen sind ausgenommen"
    reference = "SR 743.01 Art. 21 Abs. 2 Bst. c"

    def formula(organisation, period, parameters):
        return 1
