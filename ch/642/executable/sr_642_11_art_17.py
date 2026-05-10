"""SR 642.11 Art. 17

Generated from: ch/642/de/642.11.md

Art. 17 Unselbstaendige Erwerbstaetigkeit - Grundsatz (Employment income):
1. Taxable are all income from private-law or public-law employment
   including secondary income such as compensation for special services,
   commissions, allowances, seniority/anniversary gifts, gratuities,
   tips, directors' fees, monetary benefits from employee participations,
   and other monetary advantages.
1bis. Costs of professional education borne by the employer do not
   constitute monetary advantages.
2. Capital payments from pension institutions connected with employment
   are taxed under Art. 38.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class einkommen_unselbstaendig_brutto(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bruttoeinkommen aus unselbstaendiger Erwerbstaetigkeit (CHF)"
    reference = "SR 642.11 Art. 17 Abs. 1"


class nebeneinkuenfte_arbeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Nebeneinkuenfte (Provisionen, Zulagen, Gratifikationen, Trinkgelder etc.) (CHF)"
    reference = "SR 642.11 Art. 17 Abs. 1"


class geldwerte_vorteile_mitarbeiterbeteiligungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Geldwerte Vorteile aus Mitarbeiterbeteiligungen (CHF)"
    reference = "SR 642.11 Art. 17 Abs. 1"


class arbeitgeber_weiterbildungskosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vom Arbeitgeber getragene Aus-/Weiterbildungskosten (steuerfrei, CHF)"
    reference = "SR 642.11 Art. 17 Abs. 1bis"


class kapitalabfindung_vorsorge(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kapitalabfindungen aus arbeitsbezogener Vorsorgeeinrichtung (Art. 38 DBG, CHF)"
    reference = "SR 642.11 Art. 17 Abs. 2"


class einkommen_unselbstaendig_steuerbar(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerbares Einkommen aus unselbstaendiger Erwerbstaetigkeit (CHF)"
    reference = "SR 642.11 Art. 17"

    def formula(person, period, parameters):
        brutto = person('einkommen_unselbstaendig_brutto', period)
        nebeneinkuenfte = person('nebeneinkuenfte_arbeit', period)
        beteiligungen = person('geldwerte_vorteile_mitarbeiterbeteiligungen', period)
        # Art. 17 Abs. 1bis: Weiterbildungskosten Arbeitgeber kein geldwerter Vorteil
        # Art. 17 Abs. 2: Kapitalabfindungen separat nach Art. 38 besteuert
        return brutto + nebeneinkuenfte + beteiligungen
