"""SR 455.110.2 Art. 4

Generated from: ch/455/de/455.110.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_rind_schaf_ziege_oder_schwein(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier ist Rind, Schaf, Ziege oder Schwein"
    reference = "SR 455.110.2 Art. 4"


class tier_verbleibt_in_transportbehaelter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier verbleibt bis zur Schlachtung in Transportbehaeltern"
    reference = "SR 455.110.2 Art. 4 Abs. 2"


class wartebereich_hat_aktive_belueftung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wartebereich hat aktives Belueftungssystem"
    reference = "SR 455.110.2 Art. 4 Abs. 2"


class ist_milchabhaengiges_jungtier(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier ist milchabhaengiges Jungtier"
    reference = "SR 455.110.2 Art. 4 Abs. 3"


class maximale_schlachtfrist_stunden(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Frist nach Ankunft bis zur Schlachtung in Stunden (Art. 4 SR 455.110.2)"
    reference = "SR 455.110.2 Art. 4"

    def formula(person, period, parameters):
        ist_milch_jungtier = person('ist_milchabhaengiges_jungtier', period)
        in_behaelter = person('tier_verbleibt_in_transportbehaelter', period)
        hat_belueftung = person('wartebereich_hat_aktive_belueftung', period)
        ist_grossvieh = person('ist_rind_schaf_ziege_oder_schwein', period)

        # Abs. 3: Milchabhaengige Jungtiere: am Tag der Ankunft (hier: ~12h als Annaeherung)
        # Abs. 2: In Transportbehaeltern: 2h, mit Belueftung max 4h
        # Abs. 1: Andere Tiere als Rinder/Schafe/Ziegen/Schweine: 4h
        # Grossvieh hat keine explizite Frist in Abs. 1 (unterliegt anderen Bestimmungen)
        frist_behaelter = where(hat_belueftung, 4.0, 2.0)

        return where(
            ist_milch_jungtier, 12.0,
            where(in_behaelter, frist_behaelter,
                   where(ist_grossvieh, 24.0, 4.0))
        )
