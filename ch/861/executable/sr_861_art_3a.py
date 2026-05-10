"""SR 861 Art. 3a

Generated from: ch/de/861.md

Financial aid for increasing cantonal and communal subsidies for
family-supplementary childcare. Conditions: subsidy increase with
goal of reducing third-party care costs; long-term financing;
one-time grant per canton.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kanton_subventionen_erhoehung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kanton die Summe der Subventionen fuer familienergaenzende Kinderbetreuung erhoeht"
    reference = "SR 861 Art. 3a Abs. 1"


class drittbetreuungskosten_eltern_reduziert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Drittbetreuungskosten der Eltern durch die Subventionserhoehung reduziert werden"
    reference = "SR 861 Art. 3a Abs. 1"


class arbeitgeber_beitraege_angerechnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob gesetzlich vorgeschriebene Arbeitgeberbeitraege an die Subventionserhoehung angerechnet werden"
    reference = "SR 861 Art. 3a Abs. 1"


class subventionserhoehung_finanzierung_langfristig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Finanzierung der Subventionserhoehung langfristig (mind. 6 Jahre) gesichert erscheint"
    reference = "SR 861 Art. 3a Abs. 2"


class finanzhilfe_subventionserhoehung_einmalig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob dem Kanton die Finanzhilfe waehrend der Laufzeit des Gesetzes nur einmal gewaehrt wird"
    reference = "SR 861 Art. 3a Abs. 3"

    def formula(person, period, parameters):
        return True
