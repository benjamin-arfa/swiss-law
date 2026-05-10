"""SR 142.209 Art. 4

Generated from: ch/142/de/142.209.md

Gebuehrenbemessung: Bei fehlendem festem Gebuehrenansatz nach Zeitaufwand.
Stundenansatz 100-250 Franken je nach erforderlicher Sachkenntnis.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stundenansatz_gebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Stundenansatz fuer Gebuehrenbemessung (CHF, 100-250)"
    reference = "SR 142.209 Art. 4 Abs. 2"


class zeitaufwand_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zeitaufwand fuer die Verfuegung/Dienstleistung (Stunden)"
    reference = "SR 142.209 Art. 4 Abs. 1"


class gebuehr_nach_zeitaufwand(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebuehr nach Zeitaufwand (CHF)"
    reference = "SR 142.209 Art. 4"

    def formula(person, period, parameters):
        satz = person('stundenansatz_gebuehr', period)
        stunden = person('zeitaufwand_stunden', period)
        # Stundenansatz muss zwischen 100 und 250 liegen
        satz_begrenzt = max_(min_(satz, 250), 100)
        return satz_begrenzt * stunden
