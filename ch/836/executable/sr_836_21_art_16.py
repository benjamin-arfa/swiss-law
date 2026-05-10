"""SR 836.21 Art. 16 - Non-employed persons (Nichterwerbstaetige)

Art. 16: The following are NOT considered non-employed for purposes of FamZG:
(a) Persons receiving an AHV old-age pension after reaching ordinary retirement age
(b) Persons in undivided marriage whose spouse receives an AHV old-age pension
(c) Persons whose AHV contributions are deemed paid under Art. 3 par. 3 AHVG
(d) Asylum seekers, provisionally admitted persons, etc. whose contributions
    have not yet been determined under Art. 14 par. 2bis AHVG

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bezieht_ahv_altersrente(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person receives AHV old-age pension (Art. 16 let. a FamZV)"
    default_value = False


class ehepartner_bezieht_ahv_altersrente(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Spouse receives AHV old-age pension (Art. 16 let. b FamZV)"
    default_value = False


class ahv_beitraege_als_bezahlt_geltend(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "AHV contributions deemed paid under Art. 3 par. 3 AHVG (Art. 16 let. c FamZV)"
    default_value = False


class asylsuchend_beitraege_nicht_festgesetzt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Asylum seeker whose AHV contributions not yet determined (Art. 16 let. d FamZV)"
    default_value = False


class gilt_als_nichterwerbstaetig_famzg(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is considered non-employed under FamZG (Art. 16 FamZV, exclusions applied)"

    def formula(person, period, parameters):
        ahv_rente = person("bezieht_ahv_altersrente", period)
        ehepartner_rente = person("ehepartner_bezieht_ahv_altersrente", period)
        beitraege_bezahlt = person("ahv_beitraege_als_bezahlt_geltend", period)
        asyl = person("asylsuchend_beitraege_nicht_festgesetzt", period)

        # These persons are NOT considered non-employed
        ausschluss = ahv_rente + ehepartner_rente + beitraege_bezahlt + asyl

        # Person must be non-employed AND not excluded
        nichterwerbstaetig = not_(person("selbststaendig_erwerbstaetig", period)) * \
                             (person("einkommen_unselbststaendig", period) == 0)
        return nichterwerbstaetig * not_(ausschluss)
