"""SR 836.2 Art. 19

Generated from: ch/836/de/836.2.md

Art. 19: Anspruch auf Familienzulagen fuer Nichterwerbstaetige.
Abs. 1: In der AHV obligatorisch versicherte Personen, die bei der
AHV als Nichterwerbstaetige erfasst sind, haben Anspruch auf
Familienzulagen nach Art. 3 und 5. Zustaendig ist der Wohnsitzkanton.
Abs. 1bis: Personen, die als Arbeitnehmer oder Selbstaendigerwerbende
obligatorisch versichert sind, deren Einkommen aber den Mindestlohn
nicht erreicht, gelten ebenfalls als Nichterwerbstaetige.
Abs. 2: Nichterwerbstaetige, die eine Rente oder ein Taggeld beziehen
(einschliesslich Leistungsempfaenger von ALV, IV, EO, MV),
haben keinen Anspruch.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_nichterwerbstaetig_ahv(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist bei der AHV als Nichterwerbstaetige erfasst"
    reference = "SR 836.2 Art. 19 Abs. 1"


class bezieht_rente_oder_taggeld(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person bezieht eine Rente oder ein Taggeld (ALV, IV, EO, MV etc.)"
    reference = "SR 836.2 Art. 19 Abs. 2"


class einkommen_unter_mindestlohn(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Einkommen aus Erwerbstaetigkeit erreicht den Mindestlohn nach Art. 13 Abs. 1bis nicht"
    reference = "SR 836.2 Art. 19 Abs. 1bis"

    def formula(person, period, parameters):
        lohn = person('monatslohn', period)
        mindestlohn = person('mindestlohn_familienzulage', period)
        erwerbstaetig = person('ist_erwerbstaetig', period)
        return erwerbstaetig * (lohn < mindestlohn)


class anspruch_familienzulage_nichterwerbstaetig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Anspruch auf Familienzulagen als Nichterwerbstaetige (Art. 19 FamZG)"
    reference = "SR 836.2 Art. 19"

    def formula(person, period, parameters):
        ahv_versichert = person('ist_ahv_obligatorisch_versichert', period)
        nichterwerbstaetig = person('ist_nichterwerbstaetig_ahv', period)
        unter_mindestlohn = person('einkommen_unter_mindestlohn', period)
        bezieht_rente = person('bezieht_rente_oder_taggeld', period)

        # Abs. 1: AHV-versichert und als Nichterwerbstaetig erfasst
        # Abs. 1bis: Oder Erwerbstaetige unter Mindestlohn
        berechtigt = ahv_versichert * ((nichterwerbstaetig + unter_mindestlohn) > 0)

        # Abs. 2: Ausschluss bei Rentenbezug oder Taggeld
        return berechtigt * (1 - bezieht_rente)
