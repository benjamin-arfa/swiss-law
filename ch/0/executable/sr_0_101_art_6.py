"""SR 0.101 Art. 6

Generated from: ch/0/de/0.101.md

Right to a fair trial: Right to a fair and public hearing within a
reasonable time by an independent and impartial tribunal. Presumption
of innocence. Minimum rights of the accused.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class emrk_recht_auf_faires_verfahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf ein faires Verfahren vor einem unabhaengigen Gericht gilt"
    reference = "SR 0.101 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_unschuldsvermutung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Unschuldsvermutung gilt (bis zum gesetzlichen Beweis der Schuld)"
    reference = "SR 0.101 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_recht_auf_unterrichtung_anklage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf Unterrichtung ueber die Beschuldigung in verstaendlicher Sprache gilt"
    reference = "SR 0.101 Art. 6 Abs. 3 Bst. a"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_recht_auf_verteidigung_vorbereitung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf ausreichende Zeit und Gelegenheit zur Vorbereitung der Verteidigung gilt"
    reference = "SR 0.101 Art. 6 Abs. 3 Bst. b"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_recht_auf_verteidiger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf einen Verteidiger oder unentgeltlichen Beistand gilt"
    reference = "SR 0.101 Art. 6 Abs. 3 Bst. c"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_recht_auf_zeugenbefragung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf Befragung von Belastungszeugen und Ladung von Entlastungszeugen gilt"
    reference = "SR 0.101 Art. 6 Abs. 3 Bst. d"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)


class emrk_recht_auf_dolmetscher(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Recht auf unentgeltliche Unterstuetzung durch einen Dolmetscher gilt"
    reference = "SR 0.101 Art. 6 Abs. 3 Bst. e"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)
