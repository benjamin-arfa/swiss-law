"""SR 922.0 Art. 7 & 7a

Generated from: ch/922/de/922.0.md

Art. 7: Artenschutz - Species protection:
- All animals under Art. 2 not belonging to a huntable species are protected
- Cantons ensure sufficient protection from disturbance
- Cantons regulate protection of mother/young animals during hunting and adult birds during breeding

Art. 7a: Regulation of ibex and wolves:
- Cantons may regulate ibex (Aug 1 - Nov 30) and wolves (Sep 1 - Jan 31) with federal approval
- Must not endanger populations; must be necessary for habitat/diversity/damage prevention
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class jsg_ist_geschuetzte_art(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Tier gehört zu einer geschützten Art (nicht jagdbar, Art. 7 Abs. 1)"
    reference = "SR 922.0 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        im_geltungsbereich = person('jsg_tier_im_geltungsbereich', period)
        ist_jagdbar = person('jsg_ist_jagdbare_art', period)
        # Protected = in scope of JSG but not huntable
        return im_geltungsbereich * (1 - ist_jagdbar)


class jsg_ist_steinbock(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Tier ist ein Steinbock"
    reference = "SR 922.0 Art. 7a Abs. 1 Bst. a"


class jsg_ist_wolf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Tier ist ein Wolf"
    reference = "SR 922.0 Art. 7a Abs. 1 Bst. b"


class jsg_regulierung_steinbock_monat(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Aktueller Monat für Steinbock-Regulierung"
    reference = "SR 922.0 Art. 7a Abs. 1 Bst. a"


class jsg_regulierung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bestandsregulierung ist zeitlich zulässig (Art. 7a)"
    reference = "SR 922.0 Art. 7a Abs. 1"

    def formula(person, period, parameters):
        steinbock = person('jsg_ist_steinbock', period)
        wolf = person('jsg_ist_wolf', period)
        monat = period.start.month

        # Ibex: Aug 1 - Nov 30 (months 8-11)
        steinbock_ok = steinbock * ((monat >= 8) * (monat <= 11))
        # Wolf: Sep 1 - Jan 31 (months 9-12 or 1)
        wolf_ok = wolf * ((monat >= 9) + (monat <= 1))

        return (steinbock_ok + wolf_ok) > 0


class jsg_regulierung_zweck_lebensraum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Regulierung dient dem Schutz von Lebensräumen oder Erhaltung der Artenvielfalt"
    reference = "SR 922.0 Art. 7a Abs. 2 Bst. a"


class jsg_regulierung_zweck_schadensverhuetung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Regulierung dient der Schadens-/Gefährdungsverhütung (wenn Schutzmassnahmen nicht ausreichen)"
    reference = "SR 922.0 Art. 7a Abs. 2 Bst. b"


class jsg_regulierung_zweck_wildbestand(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Regulierung dient der Erhaltung regional angemessener Wildbestände"
    reference = "SR 922.0 Art. 7a Abs. 2 Bst. c"


class jsg_regulierung_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Alle Voraussetzungen für eine Bestandsregulierung nach Art. 7a sind erfüllt"
    reference = "SR 922.0 Art. 7a Abs. 2"

    def formula(person, period, parameters):
        lebensraum = person('jsg_regulierung_zweck_lebensraum', period)
        schaden = person('jsg_regulierung_zweck_schadensverhuetung', period)
        wildbestand = person('jsg_regulierung_zweck_wildbestand', period)
        # At least one purpose must be fulfilled
        return (lebensraum + schaden + wildbestand) > 0
