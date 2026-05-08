"""SR 957.1 Art. 3-5

Generated from: ch/957/de/957.1.md

Bucheffekten und Verwahrungsstellen:
- Bucheffekten = vertretbare Forderungs-/Mitgliedschaftsrechte,
  die einem Effektenkonto gutgeschrieben sind
- Verwahrungsstellen: Banken, Wertpapierhäuser, Fondsleitungen,
  Zentralverwahrer, SNB, Post, DLT-Handelssysteme
- Qualifizierte Anleger: Verwahrungsstellen, beaufsichtigte Versicherungen,
  öffentlich-rechtliche Körperschaften, Vorsorgeeinrichtungen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_vertretbares_recht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein vertretbares Forderungs- oder Mitgliedschaftsrecht handelt"
    reference = "SR 957.1 Art. 3 Abs. 1"


class ist_effektenkonto_gutgeschrieben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht einem Effektenkonto gutgeschrieben ist"
    reference = "SR 957.1 Art. 3 Abs. 1 Bst. a"


class ist_bucheffekte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Bucheffekte im Sinne des BEG vorliegt"
    reference = "SR 957.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('ist_vertretbares_recht', period) *
            person('ist_effektenkonto_gutgeschrieben', period)
        )


class typ_verwahrungsstelle(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Typ der Verwahrungsstelle: bank, wertpapierhaus, fondsleitung, zentralverwahrer, snb, post, dlt"
    reference = "SR 957.1 Art. 4 Abs. 2"


class ist_verwahrungsstelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Institution eine Verwahrungsstelle im Sinne des BEG ist"
    reference = "SR 957.1 Art. 4"


class ist_qualifizierte_anlegerin(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine qualifizierte Anlegerin im Sinne des BEG ist"
    reference = "SR 957.1 Art. 5 Bst. d"
