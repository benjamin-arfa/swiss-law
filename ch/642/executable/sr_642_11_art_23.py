"""SR 642.11 Art. 23

Generated from: ch/642/de/642.11.md

Art. 23 Uebrige Einkuenfte (Other taxable income):
Taxable are also:
a. All other income replacing employment income (Erwerbsersatz);
b. One-time or recurring payments upon death or for permanent physical
   or health impairments;
c. Compensation for giving up or not exercising an activity;
d. Compensation for not exercising a right;
e. [repealed]
f. Alimony/maintenance payments received by divorced, judicially or
   factually separated spouses, and maintenance for children under
   parental authority.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class einkommen_erwerbsersatz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte, die an die Stelle des Einkommens aus Erwerbstaetigkeit treten (CHF)"
    reference = "SR 642.11 Art. 23 Bst. a"


class einkommen_zahlungen_tod_koerperschaden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einmalige oder wiederkehrende Zahlungen bei Tod oder fuer bleibende koerperliche/gesundheitliche Nachteile (CHF)"
    reference = "SR 642.11 Art. 23 Bst. b"


class entschaedigung_aufgabe_taetigkeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Entschaedigungen fuer die Aufgabe oder Nichtausuebung einer Taetigkeit (CHF)"
    reference = "SR 642.11 Art. 23 Bst. c"


class entschaedigung_nichtausuebung_recht(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Entschaedigungen fuer die Nichtausuebung eines Rechtes (CHF)"
    reference = "SR 642.11 Art. 23 Bst. d"


class erhaltene_unterhaltsbeitraege(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Erhaltene Unterhaltsbeitraege bei Scheidung/Trennung inkl. fuer Kinder (CHF)"
    reference = "SR 642.11 Art. 23 Bst. f"


class einkommen_uebrige_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte uebrige steuerbare Einkuenfte nach Art. 23 (CHF)"
    reference = "SR 642.11 Art. 23"

    def formula(person, period, parameters):
        erwerbsersatz = person('einkommen_erwerbsersatz', period)
        tod_koerperschaden = person('einkommen_zahlungen_tod_koerperschaden', period)
        aufgabe = person('entschaedigung_aufgabe_taetigkeit', period)
        nichtausuebung = person('entschaedigung_nichtausuebung_recht', period)
        unterhalt = person('erhaltene_unterhaltsbeitraege', period)

        return erwerbsersatz + tod_koerperschaden + aufgabe + nichtausuebung + unterhalt
