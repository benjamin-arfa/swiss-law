"""SR 196.1 Art. 3

Generated from: ch/196/de/196.1.md

Sperrung im Hinblick auf eine Rechtshilfezusammenarbeit: Der Bundesrat kann
Vermoegenswerte sperren, wenn bestimmte Voraussetzungen erfuellt sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_verfuegungsmacht_ueber_vermoegenswerte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die PEP oder nahestehende Person Verfuegungsmacht ueber Vermoegenswerte in der Schweiz hat"
    reference = "SR 196.1 Art. 3 Abs. 1 lit. a"


class ist_wirtschaftlich_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die PEP oder nahestehende Person an Vermoegenswerten wirtschaftlich berechtigt ist"
    reference = "SR 196.1 Art. 3 Abs. 1 lit. b"


class machtverlust_eingetreten_oder_absehbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Machtverlust der Regierung im Herkunftsstaat eingetreten ist oder sich als unaufhaltsam abzeichnet"
    reference = "SR 196.1 Art. 3 Abs. 2 lit. a"


class korruptionsgrad_notorisch_hoch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Korruptionsgrad im Herkunftsstaat notorisch hoch ist"
    reference = "SR 196.1 Art. 3 Abs. 2 lit. b"


class vermoegenswerte_wahrscheinlich_unrechtmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vermoegenswerte wahrscheinlich durch Korruption, ungetreue Geschaeftsbesorgung oder andere Verbrechen erworben wurden"
    reference = "SR 196.1 Art. 3 Abs. 2 lit. c"


class wahrung_schweizer_interessen_erfordert_sperrung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Wahrung der Schweizer Interessen die Sperrung erfordert"
    reference = "SR 196.1 Art. 3 Abs. 2 lit. d"


class sperrung_rechtshilfe_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sperrung im Hinblick auf Rechtshilfezusammenarbeit zulaessig ist"
    reference = "SR 196.1 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        pep_oder_nahestehend = person('ist_auslaendische_politisch_exponierte_person', period) + person('ist_nahestehende_person', period) > 0
        verfuegungsmacht_oder_berechtigt = person('hat_verfuegungsmacht_ueber_vermoegenswerte', period) + person('ist_wirtschaftlich_berechtigt', period) > 0
        machtverlust = person('machtverlust_eingetreten_oder_absehbar', period)
        korruption = person('korruptionsgrad_notorisch_hoch', period)
        unrechtmaessig = person('vermoegenswerte_wahrscheinlich_unrechtmaessig', period)
        interessen = person('wahrung_schweizer_interessen_erfordert_sperrung', period)
        return pep_oder_nahestehend * verfuegungsmacht_oder_berechtigt * machtverlust * korruption * unrechtmaessig * interessen
