"""SR 642.11 Art. 27

Generated from: ch/642/de/642.11.md

Art. 27 Allgemeines - Selbstaendige Erwerbstaetigkeit (General deductions
for self-employment):
1. Business or professionally justified costs are deductible from
   self-employment income.
2. These include in particular:
   a. Depreciation and provisions (Art. 28, 29);
   b. Realized and booked losses on business assets;
   c. Contributions to pension institutions for own personnel
      (if misuse excluded);
   d. Interest on business debts and interest attributable to
      participations per Art. 18 Abs. 2;
   e. Costs of professional training/continuing education including
      retraining of own personnel;
   f. Profit-skimming sanctions insofar as they have no punitive purpose.
3. NOT deductible:
   a. Bribery payments under Swiss criminal law;
   b. Expenditures enabling crimes or as consideration for crimes;
   c. Fines and monetary penalties;
   d. Financial administrative sanctions with punitive purpose.
4. Foreign criminal/admin sanctions are deductible if:
   a. Against Swiss public order; or
   b. Taxpayer credibly shows they did everything reasonable to comply.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_selbstaendig_erwerbend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist selbstaendig erwerbstaetig"
    reference = "SR 642.11 Art. 18, Art. 27"


class geschaeftsmaessig_begruendete_kosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Geschaefts- oder beruflich begruendete Kosten der selbstaendigen Erwerbstaetigkeit (CHF)"
    reference = "SR 642.11 Art. 27 Abs. 1"


class abschreibungen_selbstaendig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abschreibungen auf Geschaeftsvermoegen (CHF)"
    reference = "SR 642.11 Art. 27 Abs. 2 Bst. a, Art. 28"


class rueckstellungen_selbstaendig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Rueckstellungen (CHF)"
    reference = "SR 642.11 Art. 27 Abs. 2 Bst. a, Art. 29"


class verluste_geschaeftsvermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eingetretene und verbuchte Verluste auf Geschaeftsvermoegen (CHF)"
    reference = "SR 642.11 Art. 27 Abs. 2 Bst. b"


class beitraege_vorsorge_personal(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zuwendungen an Vorsorgeeinrichtungen zugunsten des eigenen Personals (CHF)"
    reference = "SR 642.11 Art. 27 Abs. 2 Bst. c"


class zinsen_geschaeftsschulden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zinsen auf Geschaeftsschulden und Beteiligungen nach Art. 18 Abs. 2 (CHF)"
    reference = "SR 642.11 Art. 27 Abs. 2 Bst. d"


class kosten_weiterbildung_personal(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten der berufsorientierten Aus-/Weiterbildung inkl. Umschulung des eigenen Personals (CHF)"
    reference = "SR 642.11 Art. 27 Abs. 2 Bst. e"


class gewinnabschoepfende_sanktionen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewinnabschoepfende Sanktionen ohne Strafzweck (CHF)"
    reference = "SR 642.11 Art. 27 Abs. 2 Bst. f"


class nicht_abziehbare_sanktionen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Nicht abziehbare Bussen, Geldstrafen und Sanktionen mit Strafzweck (CHF)"
    reference = "SR 642.11 Art. 27 Abs. 3"


class abzuege_selbstaendige_erwerbstaetigkeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte abzugsfaehige Kosten aus selbstaendiger Erwerbstaetigkeit (CHF)"
    reference = "SR 642.11 Art. 27"

    def formula(person, period, parameters):
        ist_selbst = person('ist_selbstaendig_erwerbend', period)
        geschaeft = person('geschaeftsmaessig_begruendete_kosten', period)
        abschreibungen = person('abschreibungen_selbstaendig', period)
        rueckstellungen = person('rueckstellungen_selbstaendig', period)
        verluste = person('verluste_geschaeftsvermoegen', period)
        vorsorge = person('beitraege_vorsorge_personal', period)
        zinsen = person('zinsen_geschaeftsschulden', period)
        weiterbildung = person('kosten_weiterbildung_personal', period)
        sanktionen = person('gewinnabschoepfende_sanktionen', period)

        total = (geschaeft + abschreibungen + rueckstellungen + verluste +
                 vorsorge + zinsen + weiterbildung + sanktionen)

        # Nur abziehbar wenn selbstaendig erwerbend
        return where(ist_selbst, total, 0)
