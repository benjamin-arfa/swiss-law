"""SR 501.31 Art. 9 - SANKO

Generated from: ch/501/de/501.31.md

Das SANKO unterstuetzt das BABS in allen sanitaetsdienstlichen Fragen
und Belangen und beraet es bei Aufgaben von strategischer Bedeutung.
Mitglieder von Amtes wegen sind Vertreter verschiedener Bundesaemter
und Konferenzen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_sanko_mitglied_von_amtes_wegen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person von Amtes wegen Mitglied des SANKO ist"
    reference = "SR 501.31 Art. 9 Abs. 2"


class ist_vertreter_gdk(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Zentralsekretaer der Schweizerischen Konferenz der kantonalen Gesundheitsdirektorinnen und -direktoren ist"
    reference = "SR 501.31 Art. 9 Abs. 2 lit. a"


class ist_vertreter_bag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Vertreter des Bundesamtes fuer Gesundheit ist"
    reference = "SR 501.31 Art. 9 Abs. 2 lit. c"


class ist_vertreter_babs_sanko(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Vertreter des Bundesamtes fuer Bevoelkerungsschutz im SANKO ist"
    reference = "SR 501.31 Art. 9 Abs. 2 lit. d"


class ist_vertreter_blv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Vertreter des Bundesamtes fuer Lebensmittelsicherheit und Veterinaerwesen ist"
    reference = "SR 501.31 Art. 9 Abs. 2 lit. e"


class ist_vertreter_fuehrungsstab_armee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Vertreter des Fuehrungsstabes der Armee ist"
    reference = "SR 501.31 Art. 9 Abs. 2 lit. f"


class sanko_koordination_besondere_lage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das SANKO auf Anordnung des Bundesrates auf Stufe Bund die Koordination bei besonderen/ausserordentlichen Lagen uebernimmt"
    reference = "SR 501.31 Art. 9 Abs. 3"
