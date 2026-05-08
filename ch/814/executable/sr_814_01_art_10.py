"""SR 814.01 Art. 10

Generated from: ch/814/de/814.01.md

Katastrophenschutz: Pflicht zu Schutzmassnahmen fuer Anlagen, die bei
ausserordentlichen Ereignissen schwer schaedigen koennen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class betreibt_anlage_mit_katastrophenrisiko(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person eine Anlage betreibt/will, die bei ausserordentlichen Ereignissen schwer schaedigen kann"
    reference = "SR 814.01 Art. 10 Abs. 1"


class hat_katastrophenschutzmassnahmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die notwendigen Katastrophenschutzmassnahmen getroffen wurden"
    reference = "SR 814.01 Art. 10 Abs. 1"


class hat_sicherheitsabstaende_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die erforderlichen Sicherheitsabstaende eingehalten werden"
    reference = "SR 814.01 Art. 10 Abs. 1"


class hat_alarmorganisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Alarmorganisation gewaehrleistet ist"
    reference = "SR 814.01 Art. 10 Abs. 1"


class katastrophenschutz_pflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Katastrophenschutzpflichten hat"
    reference = "SR 814.01 Art. 10"

    def formula(person, period, parameters):
        return person('betreibt_anlage_mit_katastrophenrisiko', period)


class hat_ausserordentliches_ereignis_gemeldet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Inhaber ein ausserordentliches Ereignis unverzueglich der Meldestelle gemeldet hat"
    reference = "SR 814.01 Art. 10 Abs. 3"
