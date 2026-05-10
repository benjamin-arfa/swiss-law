"""SR 642.11 Art. 24

Generated from: ch/642/de/642.11.md

Art. 24 Steuerfreie Einkuenfte (Tax-free income):
Tax-free are:
a. Wealth accrual from inheritance, bequest, gift, or marital property division;
b. Wealth accrual from redeemable private capital insurance (except
   vested benefits policies; Art. 20 Abs. 1 Bst. a reserved);
c. Capital payments upon job change from employer or occupational pension
   if reinvested within one year into pension scheme or vested benefits policy;
d. Support payments from public or private funds;
e. Benefits fulfilling family law obligations (except alimony per Art. 23 f);
f. Military/civil protection pay and pocket money for civil service;
fbis. Militia firefighter pay up to CHF 5,400/year for core duties;
g. Satisfaction payments (Genugtuung);
h. Income from supplementary benefits (EL) to AHV/IV;
i. Casino winnings from licensed games (not self-employment);
ibis. Individual winnings up to CHF 1,071,000 from major games and
     online casino games;
iter. Winnings from small games (Kleinspiele);
j. Individual winnings up to CHF 1,100 from promotional lotteries/skill games;
k. Income from bridging benefits for older unemployed (UEL).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vermoegenszufall_erbschaft_schenkung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermoegenszufall aus Erbschaft, Vermaechtnis, Schenkung oder gueterrechtlicher Auseinandersetzung (CHF)"
    reference = "SR 642.11 Art. 24 Bst. a"


class vermoegenszufall_kapitalversicherung_privat(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermoegenszufall aus rueckkaufsfaehiger privater Kapitalversicherung (CHF, steuerfrei)"
    reference = "SR 642.11 Art. 24 Bst. b"


class kapitalzahlung_stellenwechsel_reinvestiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kapitalzahlung bei Stellenwechsel innerhalb Jahresfrist in Vorsorge reinvestiert"
    reference = "SR 642.11 Art. 24 Bst. c"


class kapitalzahlung_stellenwechsel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kapitalzahlung bei Stellenwechsel vom Arbeitgeber oder Vorsorgeeinrichtung (CHF)"
    reference = "SR 642.11 Art. 24 Bst. c"


class unterstuetzungen_oeffentlich_privat(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Unterstuetzungen aus oeffentlichen oder privaten Mitteln (CHF, steuerfrei)"
    reference = "SR 642.11 Art. 24 Bst. d"


class sold_militaer_zivildienst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Sold fuer Militaer-/Schutzdienst und Taschengeld fuer Zivildienst (CHF, steuerfrei)"
    reference = "SR 642.11 Art. 24 Bst. f"


class sold_milizfeuerwehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Sold der Milizfeuerwehrleute fuer Kernaufgaben (CHF)"
    reference = "SR 642.11 Art. 24 Bst. fbis"


class sold_milizfeuerwehr_steuerfrei(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerfreier Anteil des Milizfeuerwehrsolds (CHF, max 5400)"
    reference = "SR 642.11 Art. 24 Bst. fbis"

    def formula(person, period, parameters):
        sold = person('sold_milizfeuerwehr', period)
        # Steuerfrei bis CHF 5'400 pro Jahr
        return min_(sold, 5400)


class genugtuungssummen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Genugtuungssummen (CHF, steuerfrei)"
    reference = "SR 642.11 Art. 24 Bst. g"


class einkuenfte_ergaenzungsleistungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus Ergaenzungsleistungen zur AHV/IV (CHF, steuerfrei)"
    reference = "SR 642.11 Art. 24 Bst. h"


class gewinn_spielbanken(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewinne aus Spielbankenspielen (CHF, steuerfrei wenn nicht selbstaendige Erwerbstaetigkeit)"
    reference = "SR 642.11 Art. 24 Bst. i"


class gewinn_grossspiele(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einzelgewinne aus Grossspielen oder Online-Spielbankenspielen (CHF)"
    reference = "SR 642.11 Art. 24 Bst. ibis"


class gewinn_grossspiele_steuerfrei(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerfreier Anteil der Grossspielgewinne (CHF, max 1'071'000)"
    reference = "SR 642.11 Art. 24 Bst. ibis"

    def formula(person, period, parameters):
        gewinn = person('gewinn_grossspiele', period)
        # Einzelgewinne bis CHF 1'071'000 steuerfrei
        return min_(gewinn, 1071000)


class gewinn_lotterien_verkaufsfoerderung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einzelgewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsfoerderung (CHF)"
    reference = "SR 642.11 Art. 24 Bst. j"


class gewinn_lotterien_steuerfrei(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerfreier Anteil der Lotteriegewinne zur Verkaufsfoerderung (CHF, max 1100)"
    reference = "SR 642.11 Art. 24 Bst. j"

    def formula(person, period, parameters):
        gewinn = person('gewinn_lotterien_verkaufsfoerderung', period)
        # Steuerfrei sofern Grenze von CHF 1'100 nicht ueberschritten
        return where(gewinn <= 1100, gewinn, 0)


class einkuenfte_ueberbrueckungsleistungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus Ueberbrueckungsleistungen fuer aeltere Arbeitslose (CHF, steuerfrei)"
    reference = "SR 642.11 Art. 24 Bst. k"


class steuerfreie_einkuenfte_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte steuerfreie Einkuenfte nach Art. 24 (CHF)"
    reference = "SR 642.11 Art. 24"

    def formula(person, period, parameters):
        erbschaft = person('vermoegenszufall_erbschaft_schenkung', period)
        kapitalversicherung = person('vermoegenszufall_kapitalversicherung_privat', period)
        unterstuetzung = person('unterstuetzungen_oeffentlich_privat', period)
        sold_mil = person('sold_militaer_zivildienst', period)
        sold_fw = person('sold_milizfeuerwehr_steuerfrei', period)
        genugtuung = person('genugtuungssummen', period)
        el = person('einkuenfte_ergaenzungsleistungen', period)
        spielbank = person('gewinn_spielbanken', period)
        grossspiel = person('gewinn_grossspiele_steuerfrei', period)
        lotterie = person('gewinn_lotterien_steuerfrei', period)
        uel = person('einkuenfte_ueberbrueckungsleistungen', period)

        return (erbschaft + kapitalversicherung + unterstuetzung +
                sold_mil + sold_fw + genugtuung + el +
                spielbank + grossspiel + lotterie + uel)
