"""SR 142.206 Art. 10

Generated from: ch/142/de/142.206.md

Zugangsberechtigte Stellen fuer EES-Daten ueber die zentrale
Zugangsstelle zur Gefahrenabwehr und Strafverfolgung: fedpol,
Nachrichtendienst des Bundes, Bundesanwaltschaft, kantonale
Polizei- und Strafverfolgungsbehoerden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_bundeskriminalpolizei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Stelle der Direktionsbereich Bundeskriminalpolizei bei fedpol ist"
    reference = "SR 142.206 Art. 10 Abs. 1 Bst. a Ziff. 1"


class ist_nachrichtendienst_bund(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Stelle zum Nachrichtendienst des Bundes gehoert"
    reference = "SR 142.206 Art. 10 Abs. 1 Bst. b"


class ist_bundesanwaltschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Stelle zur Bundesanwaltschaft gehoert"
    reference = "SR 142.206 Art. 10 Abs. 1 Bst. c"


class ist_kantonale_polizei_strafverfolgung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Stelle eine kantonale Polizei- oder Strafverfolgungsbehoerde ist"
    reference = "SR 142.206 Art. 10 Abs. 2"


class ees_zugangsberechtigt_gefahrenabwehr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Stelle zur Gefahrenabwehr und Strafverfolgung auf EES-Daten zugreifen darf"
    reference = "SR 142.206 Art. 10"

    def formula_2022_05(person, period, parameters):
        return (
            person('ist_bundeskriminalpolizei', period)
            + person('ist_nachrichtendienst_bund', period)
            + person('ist_bundesanwaltschaft', period)
            + person('ist_kantonale_polizei_strafverfolgung', period)
        ) > 0
