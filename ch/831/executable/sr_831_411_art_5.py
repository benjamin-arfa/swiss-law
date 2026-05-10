"""SR 831.411 Art. 5

Generated from: ch/831/de/831.411.md

Art. 5: Mindestbetrag und Begrenzung - Minimum amount and limitations
for early withdrawal.

Abs. 1: Minimum early withdrawal amount is CHF 20,000.

Abs. 2: Minimum does not apply to acquisition of cooperative shares
or similar participations, nor to claims against vested benefits
institutions.

Abs. 3: Early withdrawal may be claimed every five years.

Abs. 4: If the insured person is over 50, withdrawal is limited to
the greater of:
a. The vested benefits at age 50 (+ repayments after 50, - withdrawals
   after 50)
b. Half the difference between current vested benefits and amount
   already used for home ownership
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wefv_alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der versicherten Person"
    reference = "SR 831.411 Art. 5 Abs. 4"


class wefv_freizuegigkeitsleistung_aktuell(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Aktuelle Freizuegigkeitsleistung"
    reference = "SR 831.411 Art. 5 Abs. 4"


class wefv_freizuegigkeitsleistung_alter_50(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Freizuegigkeitsleistung im Alter 50"
    reference = "SR 831.411 Art. 5 Abs. 4 Bst. a"


class wefv_rueckzahlungen_nach_50(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Rueckzahlungen nach dem Alter 50"
    reference = "SR 831.411 Art. 5 Abs. 4 Bst. a"


class wefv_vorbezuege_nach_50(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Vorbezuege oder Pfandverwertungen nach dem Alter 50 fuer Wohneigentum"
    reference = "SR 831.411 Art. 5 Abs. 4 Bst. a"


class wefv_bereits_fuer_wohneigentum_eingesetzt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Bereits fuer Wohneigentum eingesetzte Freizuegigkeitsleistung"
    reference = "SR 831.411 Art. 5 Abs. 4 Bst. b"


class wefv_ist_genossenschaft_oder_freizuegigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Erwerb von Genossenschaftsanteilen oder Ansprueche ggue. Freizuegigkeitseinrichtungen"
    reference = "SR 831.411 Art. 5 Abs. 2"


class wefv_vorbezug_maximal(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximaler Vorbezugsbetrag (Art. 5 WEFV)"
    reference = "SR 831.411 Art. 5"

    def formula(person, period, parameters):
        alter = person('wefv_alter', period.this_year)
        fl_aktuell = person('wefv_freizuegigkeitsleistung_aktuell', period)
        fl_50 = person('wefv_freizuegigkeitsleistung_alter_50', period)
        rueckzahlungen = person('wefv_rueckzahlungen_nach_50', period)
        vorbezuege = person('wefv_vorbezuege_nach_50', period)
        eingesetzt = person('wefv_bereits_fuer_wohneigentum_eingesetzt', period)

        # Under 50: full vested benefits available
        # Over 50: max of (a) or (b)
        variante_a = fl_50 + rueckzahlungen - vorbezuege
        variante_b = (fl_aktuell - eingesetzt) * 0.5
        betrag_ueber_50 = max_(variante_a, variante_b)

        return where(alter > 50, betrag_ueber_50, fl_aktuell)


class wefv_vorbezug_mindestbetrag_gilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Mindestbetrag von CHF 20'000 gilt fuer den Vorbezug"
    reference = "SR 831.411 Art. 5 Abs. 1-2"

    def formula(person, period, parameters):
        genossenschaft = person('wefv_ist_genossenschaft_oder_freizuegigkeit', period)
        # Minimum does NOT apply for cooperatives/vested benefits
        return not_(genossenschaft)


class wefv_vorbezug_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vorbezug ist zulaessig (Mindestbetrag und Begrenzung erfuellt, Art. 5 WEFV)"
    reference = "SR 831.411 Art. 5"

    def formula(person, period, parameters):
        maximal = person('wefv_vorbezug_maximal', period)
        mindestbetrag_gilt = person('wefv_vorbezug_mindestbetrag_gilt', period)
        mindestbetrag = 20000
        # Withdrawal is permissible if max available >= minimum (or minimum doesn't apply)
        return where(mindestbetrag_gilt, maximal >= mindestbetrag, maximal > 0)
