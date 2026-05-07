"""SR 453.0 Art. 3

Generated from: ch/453/de/453.0.md
Bewilligungen und Bescheinigungen des Ausfuhrstaates - Voraussetzungen fuer Einfuhr/Durchfuhr.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class exemplar_cites_anhang(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "CITES-Anhang der Art (I, II, III, keine)"
    reference = "SR 453.0 Art. 3 Abs. 1"
    default_value = "keine"


class hat_ausfuhrbewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausfuhrbewilligung des Ausfuhrstaates liegt vor"
    reference = "SR 453.0 Art. 3 Abs. 1 Bst. a"


class hat_wiederausfuhrbescheinigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wiederausfuhrbescheinigung des Wiederausfuhrstaates liegt vor"
    reference = "SR 453.0 Art. 3 Abs. 1 Bst. b"


class hat_vorerwerbsbescheinigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorerwerbsbescheinigung nach Art. VII Abs. 2 CITES liegt vor"
    reference = "SR 453.0 Art. 3 Abs. 1 Bst. c"


class hat_bescheinigung_art_vii_5(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bescheinigung nach Art. VII Abs. 5 CITES liegt vor"
    reference = "SR 453.0 Art. 3 Abs. 1 Bst. d"


class dokument_in_amtssprache_oder_en_es(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Dokument in Amtssprache, Englisch oder Spanisch abgefasst"
    reference = "SR 453.0 Art. 3 Abs. 2"


class einfuhr_cites_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einfuhr/Durchfuhr von CITES-Exemplaren ist dokumentarisch zulaessig"
    reference = "SR 453.0 Art. 3"

    def formula(person, period, parameters):
        anhang = person('exemplar_cites_anhang', period)
        ist_cites = (anhang == 'I') + (anhang == 'II') + (anhang == 'III')

        ausfuhr = person('hat_ausfuhrbewilligung', period)
        wiederausfuhr = person('hat_wiederausfuhrbescheinigung', period)
        vorerwerb = person('hat_vorerwerbsbescheinigung', period)
        art_vii_5 = person('hat_bescheinigung_art_vii_5', period)
        sprache = person('dokument_in_amtssprache_oder_en_es', period)

        hat_dokument = ausfuhr + wiederausfuhr + vorerwerb + art_vii_5
        return where(ist_cites, hat_dokument * sprache, True)
