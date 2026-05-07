"""SR 453.0 Art. 7a

Generated from: ch/453/de/453.0.md
Pflichten beim oeffentlichen Anbieten von Exemplaren geschuetzter Arten.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class bietet_exemplar_oeffentlich_an(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person bietet Exemplar geschuetzter Art oeffentlich an"
    reference = "SR 453.0 Art. 7a"


class kontaktinformation_angegeben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kontaktinformation der anbietenden Person angegeben"
    reference = "SR 453.0 Art. 7a Bst. a"


class wissenschaftlicher_name_angegeben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wissenschaftlicher Name des Exemplars angegeben"
    reference = "SR 453.0 Art. 7a Bst. b"


class herkunft_angegeben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Herkunftsangabe (Natur/Zucht bzw. kuenstlich vermehrt) angegeben"
    reference = "SR 453.0 Art. 7a Bst. c"


class cites_anhang_angabe_angegeben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "CITES-Anhang-Angabe angegeben (bei Exemplaren nach Anhang I-III)"
    reference = "SR 453.0 Art. 7a Bst. d"


class informationspflicht_angebot_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Informationspflicht beim oeffentlichen Anbieten ist erfuellt"
    reference = "SR 453.0 Art. 7a"

    def formula(person, period, parameters):
        angebot = person('bietet_exemplar_oeffentlich_an', period)
        kontakt = person('kontaktinformation_angegeben', period)
        name = person('wissenschaftlicher_name_angegeben', period)
        herkunft = person('herkunft_angegeben', period)
        cites = person('cites_anhang_angabe_angegeben', period)
        return where(angebot, kontakt * name * herkunft * cites, True)
