"""SR 314.1 Art. 4

Generated from: ch/314/de/314.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_zum_tatzeitpunkt(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der beschuldigten Person zum Zeitpunkt der Tat (in Jahren)"
    reference = "SR 314.1 Art. 4"


class betm_uebertretung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Widerhandlung betrifft das Betaeubungsmittelgesetz (BetmG)"
    reference = "SR 314.1 Art. 4 Abs. 2"


class gefaehrdung_oder_schaden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die beschuldigte Person hat jemanden gefaehrdet, verletzt oder Schaden verursacht"
    reference = "SR 314.1 Art. 4 Abs. 3 Bst. a"


class zusaetzliche_widerhandlung_nicht_in_liste(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der beschuldigten Person wird zusaetzlich eine nicht in der Bussenliste aufgefuehrte Widerhandlung vorgeworfen"
    reference = "SR 314.1 Art. 4 Abs. 3 Bst. b"


class beschuldigte_lehnt_verfahren_ab(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die beschuldigte Person lehnt das Ordnungsbussenverfahren ab"
    reference = "SR 314.1 Art. 4 Abs. 3 Bst. c"


class weitere_verfahrenshandlungen_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es sind Verfahrenshandlungen nach StPO erforderlich, die im OBG nicht vorgesehen sind"
    reference = "SR 314.1 Art. 4 Abs. 3 Bst. d"


class ordnungsbussenverfahren_ausgeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Ordnungsbussenverfahren ist ausgeschlossen (Ausnahmen nach Art. 4)"
    reference = "SR 314.1 Art. 4"

    def formula(person, period, parameters):
        alter = person('alter_zum_tatzeitpunkt', period)
        betm = person('betm_uebertretung', period)

        # Abs. 1: unter 15 Jahren generell ausgeschlossen
        unter_15 = alter < 15

        # Abs. 2: BetmG-Widerhandlungen unter 18 Jahren ausgeschlossen
        betm_unter_18 = betm * (alter < 18)

        # Abs. 3: Weitere Ausschluesse
        gefaehrdung = person('gefaehrdung_oder_schaden', period)
        zusaetzlich = person('zusaetzliche_widerhandlung_nicht_in_liste', period)
        ablehnung = person('beschuldigte_lehnt_verfahren_ab', period)
        weitere = person('weitere_verfahrenshandlungen_erforderlich', period)

        return unter_15 + betm_unter_18 + gefaehrdung + zusaetzlich + ablehnung + weitere > 0
