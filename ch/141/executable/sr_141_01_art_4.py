"""SR 141.01 Art. 4

Generated from: ch/141/de/141.01.md

Nichtbeachtung der oeffentlichen Sicherheit und Ordnung: Kriterien,
bei denen die Integration als nicht erfolgreich gilt (Strafregister,
Missachtung von Vorschriften, etc.).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class missachtung_vorschriften(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob gesetzliche Vorschriften und behoerdliche Verfuegungen erheblich oder wiederholt missachtet werden"
    reference = "SR 141.01 Art. 4 Abs. 1 Bst. a"


class nichterfuellung_verpflichtungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob wichtige oeffentlich-rechtliche oder privatrechtliche Verpflichtungen mutwillig nicht erfuellt werden"
    reference = "SR 141.01 Art. 4 Abs. 1 Bst. b"


class billigung_schwerer_straftaten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Verbrechen gegen oeffentlichen Frieden, Voelkermord, Kriegsverbrechen oeffentlich gebilligt oder beworben werden"
    reference = "SR 141.01 Art. 4 Abs. 1 Bst. c"


class vostra_unbedingte_strafe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine unbedingte Strafe oder teilbedingte Freiheitsstrafe fuer ein Vergehen oder Verbrechen in VOSTRA eingetragen ist"
    reference = "SR 141.01 Art. 4 Abs. 2 Bst. a"


class vostra_stationaere_massnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine stationaere Massnahme oder geschlossene Unterbringung in VOSTRA eingetragen ist"
    reference = "SR 141.01 Art. 4 Abs. 2 Bst. b"


class vostra_taetigkeitsverbot(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Taetigkeitsverbot, Kontakt-/Rayonverbot oder Landesverweisung in VOSTRA eingetragen ist"
    reference = "SR 141.01 Art. 4 Abs. 2 Bst. c"


class vostra_bedingte_strafe_hoch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine bedingte/teilbedingte Geldstrafe >90 Tagessaetze oder Freiheitsstrafe >3 Monate in VOSTRA eingetragen ist"
    reference = "SR 141.01 Art. 4 Abs. 2 Bst. d"


class vostra_bedingte_strafe_niedrig_nicht_bewaehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine bedingte/teilbedingte Geldstrafe <=90 Tagessaetze mit gescheiterter Probezeit in VOSTRA eingetragen ist"
    reference = "SR 141.01 Art. 4 Abs. 2 Bst. e"


class haengiges_strafverfahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein haengiges Strafverfahren gegen die Bewerberin oder den Bewerber vorliegt"
    reference = "SR 141.01 Art. 4 Abs. 5"


class nichtbeachtung_sicherheit_ordnung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die oeffentliche Sicherheit und Ordnung nicht beachtet wird (Integration nicht erfolgreich)"
    reference = "SR 141.01 Art. 4"

    def formula(person, period, parameters):
        abs1 = (
            person('missachtung_vorschriften', period)
            + person('nichterfuellung_verpflichtungen', period)
            + person('billigung_schwerer_straftaten', period)
        ) > 0
        abs2 = (
            person('vostra_unbedingte_strafe', period)
            + person('vostra_stationaere_massnahme', period)
            + person('vostra_taetigkeitsverbot', period)
            + person('vostra_bedingte_strafe_hoch', period)
            + person('vostra_bedingte_strafe_niedrig_nicht_bewaehrt', period)
        ) > 0
        return abs1 + abs2 > 0
