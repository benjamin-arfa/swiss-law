"""SR 419.1 Art. 9

Generated from: ch/419/de/419.1.md

Wettbewerb - staatliche Weiterbildung darf Wettbewerb nicht beeintraechtigen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class weiterbildung_zu_kostendeckenden_preisen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Weiterbildung wird zu mindestens kostendeckenden Preisen angeboten"
    reference = "SR 419.1 Art. 9 Abs. 2 Bst. a"


class weiterbildung_nicht_im_wettbewerb_mit_privaten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Weiterbildung steht nicht im Wettbewerb mit privaten nicht-subventionierten Angeboten"
    reference = "SR 419.1 Art. 9 Abs. 2 Bst. b"


class ueberwiegendes_oeffentliches_interesse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ueberwiegendes oeffentliches Interesse an Wettbewerbsbeeintraechtigung"
    reference = "SR 419.1 Art. 9 Abs. 3"


class wettbewerbsbeeintraechtigung_verhaeltnismaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wettbewerbsbeeintraechtigung ist verhaeltnismaessig"
    reference = "SR 419.1 Art. 9 Abs. 3"


class gesetzliche_grundlage_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesetzliche Grundlage fuer Wettbewerbsbeeintraechtigung vorhanden"
    reference = "SR 419.1 Art. 9 Abs. 3"


# --- Computed variables ---

class wettbewerb_nicht_beeintraechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Staatliche Weiterbildung beeintraechtigt Wettbewerb nicht"
    reference = "SR 419.1 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        kostendeckend = person('weiterbildung_zu_kostendeckenden_preisen', period)
        kein_wettbewerb = person('weiterbildung_nicht_im_wettbewerb_mit_privaten', period)
        return kostendeckend + kein_wettbewerb


class wettbewerbsbeeintraechtigung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wettbewerbsbeeintraechtigung ist zulaessig"
    reference = "SR 419.1 Art. 9 Abs. 2-3"

    def formula(person, period, parameters):
        nicht_beeintraechtigt = person('wettbewerb_nicht_beeintraechtigt', period)
        interesse = person('ueberwiegendes_oeffentliches_interesse', period)
        verhaeltnismaessig = person('wettbewerbsbeeintraechtigung_verhaeltnismaessig', period)
        gesetzlich = person('gesetzliche_grundlage_vorhanden', period)
        # Zulaessig wenn: keine Beeintraechtigung ODER (oeffentliches Interesse + verhaeltnismaessig + gesetzlich)
        return nicht_beeintraechtigt + (interesse * verhaeltnismaessig * gesetzlich)
