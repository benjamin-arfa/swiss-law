"""SR 354.1 § 15

Generated from: ch/354/de/354.1.md
Transport timing rules.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transport_ankunftszeit_stunde(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Ankunftszeit des Transports (Stunde, 0-23)"
    reference = "SR 354.1 § 15"


class ist_verbotener_transporttag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist der Transporttag ein Sonntag oder Feiertag (Neujahr, Karfreitag, Auffahrt, Weihnacht)"
    reference = "SR 354.1 § 15"


class transport_zeitlich_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Transport ist zeitlich zulaessig (nicht nach 20 Uhr, nicht an Sonn-/Feiertagen)"
    reference = "SR 354.1 § 15"

    def formula(person, period):
        ankunft = person('transport_ankunftszeit_stunde', period)
        verbotener_tag = person('ist_verbotener_transporttag', period)
        # Ankunft nicht spaeter als 20 Uhr
        ankunft_ok = ankunft <= 20
        # Keine Transporte an Sonntagen und bestimmten Feiertagen
        return ankunft_ok * not_(verbotener_tag)
