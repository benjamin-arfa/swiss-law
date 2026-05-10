"""SR 923.0 Art. 1 & 2

Generated from: ch/923/de/923.0.md

Art. 1: Zweck - Purpose of the Fishing Act (BGF):
a. Preserve/improve/restore natural species diversity and stocks of native fish, crayfish, and fish food organisms
b. Protect endangered species and breeds
c. Ensure sustainable use of fish and crayfish stocks
d. Promote fisheries research

Art. 2: Geltungsbereich - Scope:
1. Applies to public and private waters
2. Fish farms and certain artificial private waters: only Arts. 6, 16(c,d), 8-10 apply
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bgf_ist_oeffentliches_gewaesser(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewässer ist ein öffentliches Gewässer"
    reference = "SR 923.0 Art. 2 Abs. 1"


class bgf_ist_privates_gewaesser(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewässer ist ein privates Gewässer"
    reference = "SR 923.0 Art. 2 Abs. 1"


class bgf_ist_fischzuchtanlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anlage ist eine Fischzuchtanlage"
    reference = "SR 923.0 Art. 2 Abs. 2"


class bgf_ist_kuenstliches_privatgewaesser(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewässer ist ein künstlich angelegtes privates Gewässer ohne natürlichen Fischzugang"
    reference = "SR 923.0 Art. 2 Abs. 2"


class bgf_im_geltungsbereich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewässer fällt in den Geltungsbereich des BGF"
    reference = "SR 923.0 Art. 2"

    def formula(person, period, parameters):
        oeffentlich = person('bgf_ist_oeffentliches_gewaesser', period)
        privat = person('bgf_ist_privates_gewaesser', period)
        return (oeffentlich + privat) > 0


class bgf_volles_gesetz_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtes BGF ist anwendbar (nicht nur Teilbestimmungen)"
    reference = "SR 923.0 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        im_bereich = person('bgf_im_geltungsbereich', period)
        zuchtanlage = person('bgf_ist_fischzuchtanlage', period)
        kuenstlich = person('bgf_ist_kuenstliches_privatgewaesser', period)
        # Full act applies unless it's a fish farm or artificial private water
        return im_bereich * (1 - zuchtanlage) * (1 - kuenstlich)
