"""SR 142.206 Art. 1

Generated from: ch/142/de/142.206.md

Gegenstand: Regelung des Datenkatalogs des EES, zugangsberechtigte
Stellen, Zugangsberechtigungen, Abfrage- und Zugangsverfahren,
Berichtigung/Ergaenzung/Loeschung, Datenschutz und Aufsicht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ees_datenkatalog_geregelt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Datenkatalog des EES und die Zugangsberechtigungen geregelt sind"
    reference = "SR 142.206 Art. 1 Bst. a"

    def formula_2022_05(person, period, parameters):
        return True


class ees_verfahren_abfrage_geregelt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verfahren fuer Abfrage und Zugang zu EES-Daten geregelt sind"
    reference = "SR 142.206 Art. 1 Bst. b"

    def formula_2022_05(person, period, parameters):
        return True


class ees_zentrale_zugangsstelle_geregelt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Zugang ueber die zentrale Zugangsstelle zur Gefahrenabwehr und Strafverfolgung geregelt ist"
    reference = "SR 142.206 Art. 1 Bst. c"

    def formula_2022_05(person, period, parameters):
        return True


class ees_datenschutz_geregelt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Rechte der betroffenen Personen, Datenschutz und Aufsicht geregelt sind"
    reference = "SR 142.206 Art. 1 Bst. e"

    def formula_2022_05(person, period, parameters):
        return True
