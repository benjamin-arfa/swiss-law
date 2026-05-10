"""SR 291 Art. 9

Generated from: ch/291/de/291.md

Litispendenz: Ist eine Klage ueber denselben Gegenstand zwischen denselben
Parteien zuerst im Ausland haengig gemacht worden, so setzt das schweizerische
Gericht das Verfahren aus, wenn zu erwarten ist, dass das auslaendische
Gericht in angemessener Frist eine in der Schweiz anerkennbare Entscheidung
faellt. Das Gericht weist die Klage zurueck, sobald eine anerkennbare
auslaendische Entscheidung vorliegt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class klage_im_ausland_zuerst_haengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Klage ueber denselben Gegenstand zuerst im Ausland haengig gemacht wurde"
    reference = "SR 291 Art. 9 Abs. 1"


class auslaendische_entscheidung_anerkennbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die auslaendische Entscheidung in der Schweiz anerkennbar ist"
    reference = "SR 291 Art. 9 Abs. 1"


class auslaendische_entscheidung_in_angemessener_frist_erwartet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine anerkennbare auslaendische Entscheidung in angemessener Frist erwartet wird"
    reference = "SR 291 Art. 9 Abs. 1"


class verfahren_wird_ausgesetzt_wegen_litispendenz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das schweizerische Verfahren wegen auslaendischer Litispendenz ausgesetzt wird"
    reference = "SR 291 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        zuerst_haengig = person('klage_im_ausland_zuerst_haengig', period)
        anerkennbar_erwartet = person(
            'auslaendische_entscheidung_in_angemessener_frist_erwartet', period
        )
        return zuerst_haengig * anerkennbar_erwartet


class klage_wird_zurueckgewiesen_wegen_auslaendischer_entscheidung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Klage zurueckgewiesen wird wegen vorliegender anerkennbarer auslaendischer Entscheidung"
    reference = "SR 291 Art. 9 Abs. 3"

    def formula(person, period, parameters):
        zuerst_haengig = person('klage_im_ausland_zuerst_haengig', period)
        anerkennbar = person('auslaendische_entscheidung_anerkennbar', period)
        return zuerst_haengig * anerkennbar
