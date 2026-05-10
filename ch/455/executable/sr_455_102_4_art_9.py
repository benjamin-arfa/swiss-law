"""SR 455.102.4 Art. 9

Generated from: ch/455/de/455.102.4.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables
class tier_ist_belastungskategorie_3(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier ist Belastungskategorie 3 (Art. 9 lit. a SR 455.102.4)"
    reference = "SR 455.102.4 Art. 9 lit. a"


class zuchtziel_hat_belastung_kategorie_3_zur_folge(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuchtziel hat bei Nachkommen Belastung Kategorie 3 zur Folge (Art. 9 lit. b SR 455.102.4)"
    reference = "SR 455.102.4 Art. 9 lit. b"


class zuchtform_nicht_tiergerecht_haltbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuchtform kann nicht tiergerecht gehalten werden (Art. 9 lit. c Ziff. 1 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 9 lit. c Ziff. 1"


class zuchtform_keine_physiologische_koerperhaltung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuchtform kann keine physiologische Koerperhaltung einnehmen (Art. 9 lit. c Ziff. 2 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 9 lit. c Ziff. 2"


class zuchtform_keine_artgemaesse_fortbewegung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuchtform kann sich nicht artgemaess fortbewegen (Art. 9 lit. c Ziff. 3 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 9 lit. c Ziff. 3"


class zuchtform_ohne_menschliche_hilfe_nicht_lebensfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuchtform kann ohne menschliche Hilfe keine Nahrung aufnehmen oder keine Jungen aufziehen (Art. 9 lit. c Ziff. 4 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 9 lit. c Ziff. 4"


class verpaarung_kann_sinnesverlust_verursachen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gezielte Verpaarung kann Sinnesverlust bei Nachkommen verursachen (Art. 9 lit. d Ziff. 1 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 9 lit. d Ziff. 1"


class verpaarung_kann_schwergeburten_verursachen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aufgrund anatomischer Verhaeltnisse sind Schwergeburten zu erwarten (Art. 9 lit. d Ziff. 2 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 9 lit. d Ziff. 2"


class zuchteinsatz_verboten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuchteinsatz ist verboten nach Art. 9 SR 455.102.4"
    reference = "SR 455.102.4 Art. 9"

    def formula(person, period, parameters):
        kat_3 = person('tier_ist_belastungskategorie_3', period)
        ziel_kat_3 = person('zuchtziel_hat_belastung_kategorie_3_zur_folge', period)
        nicht_haltbar = person('zuchtform_nicht_tiergerecht_haltbar', period)
        keine_koerperhaltung = person('zuchtform_keine_physiologische_koerperhaltung', period)
        keine_fortbewegung = person('zuchtform_keine_artgemaesse_fortbewegung', period)
        nicht_lebensfaehig = person('zuchtform_ohne_menschliche_hilfe_nicht_lebensfaehig', period)
        sinnesverlust = person('verpaarung_kann_sinnesverlust_verursachen', period)
        schwergeburten = person('verpaarung_kann_schwergeburten_verursachen', period)

        # Zucht verboten wenn eine der Bedingungen a-d erfuellt
        koerper_problem = nicht_haltbar + keine_koerperhaltung + keine_fortbewegung + nicht_lebensfaehig
        verpaarungs_problem = sinnesverlust + schwergeburten
        return kat_3 + ziel_kat_3 + koerper_problem + verpaarungs_problem
