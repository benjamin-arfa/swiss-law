"""SR 514.54 Art. 5

Generated from: ch/514/de/514.54.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_seriefeuerwaffe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Waffe ist eine Seriefeuerwaffe"


class ist_umgebaute_seriefeuerwaffe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Waffe ist eine zu halbautomatischer Feuerwaffe umgebaute Seriefeuerwaffe"


class ist_ordonnanzwaffe_aus_militaerbestaenden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ordonnanzfeuerwaffe direkt aus Militaerverwaltungsbestaenden uebernommen"


class halbautomatische_handfeuerwaffe_kuerzbar_unter_60cm(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Halbautomatische Handfeuerwaffe kann auf unter 60 cm gekuerzt werden"


class waffe_taeuscht_gebrauchsgegenstand_vor(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Feuerwaffe taeuscht einen Gebrauchsgegenstand vor"


class waffe_verboten_nach_art_5_abs_1(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Waffe ist verboten nach Art. 5 Abs. 1 SR 514.54"
    reference = "SR 514.54 Art. 5"

    def formula(person, period, parameters):
        serie = person('ist_seriefeuerwaffe', period)
        umgebaut = person('ist_umgebaute_seriefeuerwaffe', period)
        ordonnanz = person('ist_ordonnanzwaffe_aus_militaerbestaenden', period)
        kuerzbar = person('halbautomatische_handfeuerwaffe_kuerzbar_unter_60cm', period)
        taeuscht = person('waffe_taeuscht_gebrauchsgegenstand_vor', period)
        hohe_kap = person('ladevorrichtung_hohe_kapazitaet', period)

        # Verboten:
        # a) Seriefeuerwaffen
        # b) umgebaute Seriefeuerwaffen (ausser Ordonnanzwaffen aus Militaerbestaenden)
        # c) halbautomatische Zentralfeuerwaffen mit Ladevorrichtung hoher Kapazitaet
        # d) halbautomatische Handfeuerwaffen kuerzbar unter 60cm
        # e) Feuerwaffen die Gebrauchsgegenstand vortaeuschen
        verboten_a = serie
        verboten_b = umgebaut * (ordonnanz == False)
        verboten_c = hohe_kap
        verboten_d = kuerzbar
        verboten_e = taeuscht

        return verboten_a + verboten_b + verboten_c + verboten_d + verboten_e
