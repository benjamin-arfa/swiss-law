"""SR 956.1 Art. 42

Generated from: ch/956/de/956.1.md

Amtshilfe mit ausländischen Finanzmarktaufsichtsbehörden:
- FINMA kann ausländische Behörden um Informationen ersuchen
- Übermittlung nicht öffentlich zugänglicher Informationen nur wenn:
  - ausschliesslich zum Vollzug des Finanzmarktrechts verwendet
  - ersuchende Behörden an Amts-/Berufsgeheimnis gebunden
- Amtshilfe wird zügig geleistet
- Verhältnismässigkeitsgrundsatz
- Keine Übermittlung über offensichtlich unbeteiligte Personen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_auslaendische_finanzmarktaufsicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine ausländische Finanzmarktaufsichtsbehörde handelt"
    reference = "SR 956.1 Art. 42 Abs. 1"


class information_fuer_finanzmarktrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Information ausschliesslich zum Vollzug des Finanzmarktrechts verwendet wird"
    reference = "SR 956.1 Art. 42 Abs. 2 Bst. a"


class behoerde_an_geheimnis_gebunden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die ersuchende Behörde an Amts- oder Berufsgeheimnis gebunden ist"
    reference = "SR 956.1 Art. 42 Abs. 2 Bst. b"


class person_offensichtlich_unbeteiligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die betroffene Person offensichtlich nicht in die Angelegenheit verwickelt ist"
    reference = "SR 956.1 Art. 42 Abs. 4"


class amtshilfe_uebermittlung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Übermittlung nicht öffentlicher Informationen an ausländische Behörde zulässig ist"
    reference = "SR 956.1 Art. 42 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('ist_auslaendische_finanzmarktaufsicht', period) *
            person('information_fuer_finanzmarktrecht', period) *
            person('behoerde_an_geheimnis_gebunden', period) *
            (person('person_offensichtlich_unbeteiligt', period) == False)
        )
