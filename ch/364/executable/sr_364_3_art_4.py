"""SR 364.3 Art. 4

Generated from: ch/364/de/364.3.md

Schutz von Luftfahrzeugen: Zulaessige Zwangsmittel an Bord.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einsatz_an_bord_luftfahrzeug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Schutzeinsatz an Bord eines Luftfahrzeugs"
    reference = "SR 364.3 Art. 4"


class zwangsmittel_typ(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Typ des Zwangsmittels (fesselung, schlagstock, feuerwaffe_expansion, destabilisierung, wasserwerfer, pfeffer, diensthund, reizstoff, seriefeuerwaffe, mehrzweckwerfer, vollmantel, hilfsmunition)"
    reference = "SR 364.3 Art. 4"


class zwangsmittel_luftfahrzeug_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zwangsmittel ist bei Schutzeinsaetzen an Bord von Luftfahrzeugen zulaessig"
    reference = "SR 364.3 Art. 4"

    def formula(person, period, parameters):
        an_bord = person('einsatz_an_bord_luftfahrzeug', period)
        typ = person('zwangsmittel_typ', period)
        zulaessig = (
            (typ == 'fesselung') +
            (typ == 'schlagstock') +
            (typ == 'feuerwaffe_expansion') +
            (typ == 'destabilisierung')
        )
        return an_bord * zulaessig
