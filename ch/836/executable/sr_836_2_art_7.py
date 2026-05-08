"""SR 836.2 Art. 7

Generated from: ch/836/de/836.2.md

Art. 7: Anspruchskonkurrenz - Priority order when multiple persons have a
claim for the same child:
a. employed person
b. person with parental authority
c. person the child mainly lives with
d. person under the family allowance scheme of the child's canton of residence
e. person with higher AHV-liable income from employment
f. person with higher AHV-liable income from self-employment

Abs. 2: Differential payment if first- and second-priority persons are under
different cantonal schemes.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity
from numpy import select as np_select

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_erwerbstaetig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist erwerbstätig"
    reference = "SR 836.2 Art. 7 Abs. 1 lit. a"


class hat_elterliche_sorge(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person hat die elterliche Sorge (oder hatte sie bis zur Mündigkeit)"
    reference = "SR 836.2 Art. 7 Abs. 1 lit. b"


class kind_lebt_ueberwiegend_bei_person(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kind lebt überwiegend bei dieser Person"
    reference = "SR 836.2 Art. 7 Abs. 1 lit. c"


class familienzulagenordnung_wohnsitzkanton_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Familienzulagenordnung im Wohnsitzkanton des Kindes ist auf diese Person anwendbar"
    reference = "SR 836.2 Art. 7 Abs. 1 lit. d"


class ahv_einkommen_unselbstaendig(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "AHV-pflichtiges Einkommen aus unselbstständiger Erwerbstätigkeit"
    reference = "SR 836.2 Art. 7 Abs. 1 lit. e"


class ahv_einkommen_selbstaendig(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "AHV-pflichtiges Einkommen aus selbstständiger Erwerbstätigkeit"
    reference = "SR 836.2 Art. 7 Abs. 1 lit. f"


class anspruchsprioriaet_familienzulage(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = (
        "Prioritätsstufe des Anspruchs auf Familienzulagen (1 = höchste Priorität, "
        "6 = niedrigste, 0 = kein Anspruch) nach Art. 7 Abs. 1 FamZG"
    )
    reference = "SR 836.2 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        erwerbstaetig = person('ist_erwerbstaetig', period)
        sorge = person('hat_elterliche_sorge', period)
        lebt_bei = person('kind_lebt_ueberwiegend_bei_person', period)
        kanton = person('familienzulagenordnung_wohnsitzkanton_anwendbar', period)
        # Priorität: 1 (höchste) bis 6 (niedrigste)
        # Erwerbstätige haben Priorität 1
        return where(erwerbstaetig, 1,
               where(sorge, 2,
               where(lebt_bei, 3,
               where(kanton, 4,
               5))))


class mindestansatz_kanton_zweitanspruch(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Gesetzlicher Mindestansatz im Kanton der zweitanspruchsberechtigten Person"
    reference = "SR 836.2 Art. 7 Abs. 2"


class mindestansatz_kanton_erstanspruch(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Gesetzlicher Mindestansatz im Kanton der erstanspruchsberechtigten Person"
    reference = "SR 836.2 Art. 7 Abs. 2"


class differenzzahlung_familienzulage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = (
        "Differenzzahlung der zweitanspruchsberechtigten Person, wenn deren "
        "kantonaler Mindestansatz höher ist (Art. 7 Abs. 2 FamZG)"
    )
    reference = "SR 836.2 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        zweit = person('mindestansatz_kanton_zweitanspruch', period)
        erst = person('mindestansatz_kanton_erstanspruch', period)
        differenz = zweit - erst
        return where(differenz > 0, differenz, 0)
