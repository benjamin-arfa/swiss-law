"""SR 981.1 Art. 10 - Akontozahlungen

Generated from: ch/981/de/981.1.md

Fuer rechtskraeftig bewertete Ansprueche kann die Kommission
Akontozahlungen festsetzen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class anspruch_rechtskraeftig_bewertet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Anspruch ist rechtskraeftig bewertet"
    reference = "SR 981.1 Art. 10"


class akontozahlung_entschaedigung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Akontozahlung fuer die Entschaedigung (CHF)"
    reference = "SR 981.1 Art. 10"
