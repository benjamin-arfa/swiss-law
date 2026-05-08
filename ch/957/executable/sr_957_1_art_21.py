"""SR 957.1 Art. 21-22

Generated from: ch/957/de/957.1.md

Rechte der Verwahrungsstelle:
- Rückbehalts- und Verwertungsrecht für fällige Forderungen aus Verwahrung
- Erlischt bei Gutschrift auf anderes Effektenkonto
- Nutzungsrecht: Kontoinhaberin kann Verwahrungsstelle Verfügungsrecht einräumen
- Nicht-qualifizierte Anleger: schriftliche Ermächtigung erforderlich,
  nicht in AGB zulässig
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class forderung_aus_verwahrung_faellig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine fällige Forderung aus der Verwahrung oder Vorleistung besteht"
    reference = "SR 957.1 Art. 21 Abs. 1"


class rueckbehaltsrecht_verwahrungsstelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Verwahrungsstelle ein Rückbehalts- und Verwertungsrecht hat"
    reference = "SR 957.1 Art. 21 Abs. 1"

    def formula(person, period, parameters):
        return person('forderung_aus_verwahrung_faellig', period)


class nutzungsrecht_eingeraeumt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Verwahrungsstelle ein Nutzungsrecht an Bucheffekten eingeräumt wurde"
    reference = "SR 957.1 Art. 22 Abs. 1"


class ermaechtig_schriftlich_erteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Ermächtigung schriftlich (nicht in AGB) erteilt wurde"
    reference = "SR 957.1 Art. 22 Abs. 2"


class nutzungsrecht_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Nutzungsrecht gültig eingeräumt wurde"
    reference = "SR 957.1 Art. 22"

    def formula(person, period, parameters):
        eingeraeumt = person('nutzungsrecht_eingeraeumt', period)
        qualifiziert = person('ist_qualifizierte_anlegerin', period)
        schriftlich = person('ermaechtig_schriftlich_erteilt', period)

        return eingeraeumt * (qualifiziert + schriftlich)
