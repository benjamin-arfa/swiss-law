"""SR 455.102.4 Art. 5

Generated from: ch/455/de/455.102.4.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables
class tier_hat_merkmal_mit_mittlerer_oder_starker_belastung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier weist Merkmal auf, das zu mittlerer oder starker Belastung fuehren kann (Art. 5 Abs. 1 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 5 Abs. 1"


class belastungsbeurteilung_vorgenommen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Belastungsbeurteilung wurde vorgenommen"
    reference = "SR 455.102.4 Art. 5 Abs. 1"


class beurteiler_hat_hochschulabschluss(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person mit Hochschulabschluss und Erfahrung in Veterinaermedizin, Ethologie oder Genetik (Art. 5 Abs. 4 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 5 Abs. 4"


class resultat_schriftlich_festgehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Resultat der Belastungsbeurteilung schriftlich festgehalten und unterschrieben (Art. 5 Abs. 5 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 5 Abs. 5"


class belastungsbeurteilung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Belastungsbeurteilung ist vor der Zucht erforderlich (Art. 5 Abs. 1 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return person('tier_hat_merkmal_mit_mittlerer_oder_starker_belastung', period)


class belastungsbeurteilung_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Belastungsbeurteilung ist gueltig durchgefuehrt (Art. 5 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 5"

    def formula(person, period, parameters):
        erforderlich = person('belastungsbeurteilung_erforderlich', period)
        vorgenommen = person('belastungsbeurteilung_vorgenommen', period)
        qualifiziert = person('beurteiler_hat_hochschulabschluss', period)
        dokumentiert = person('resultat_schriftlich_festgehalten', period)
        # Either not required, or all conditions met
        return not_(erforderlich) + (erforderlich * vorgenommen * qualifiziert * dokumentiert)
