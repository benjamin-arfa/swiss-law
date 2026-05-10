"""SR 427.72 Art. 10

Generated from: ch/427/de/427.72.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anschaffungspreis_hilfsmittel(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anschaffungspreis des Forschungshilfsmittels in CHF"
    reference = "SR 427.72 Art. 10 Abs. 1"


class hilfsmittel_im_forschungsgesuch_vorgesehen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hilfsmittel war im Forschungsgesuch vorgesehen und bewilligt"
    reference = "SR 427.72 Art. 10 Abs. 1"


class hilfsmittel_genehmigungspflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anschaffung des Hilfsmittels erfordert vorgaengige Zustimmung des ASTRA"
    reference = "SR 427.72 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        preis = person('anschaffungspreis_hilfsmittel', period)
        im_gesuch = person('hilfsmittel_im_forschungsgesuch_vorgesehen', period)
        # Genehmigungspflichtig wenn Preis > 1000 CHF und nicht im Gesuch vorgesehen
        return (preis > 1000.0) * not_(im_gesuch)
