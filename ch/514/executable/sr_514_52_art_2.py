"""SR 514.52 Art. 2

Generated from: ch/514/de/514.52.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Organisation = build_entity(key='organisation', plural='organisations', label='An organisation')


class kampfflugzeug_vertragswert(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Vertragswert der Beschaffung in CHF"


class kampfflugzeug_max_finanzvolumen(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Maximales Finanzvolumen fuer Kampfflugzeuge in CHF (Art. 2 Abs. 1 lit. a SR 514.52)"
    reference = "SR 514.52 Art. 2"

    def formula(organisation, period, parameters):
        # Hoechstens 6 Milliarden Franken (Stand LIK Jan. 2018)
        return 6_000_000_000.0


class kampfflugzeug_offset_anteil_gesamt(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Erforderlicher Gesamtanteil Offsets am Vertragswert (Art. 2 Abs. 1 lit. b SR 514.52)"
    reference = "SR 514.52 Art. 2"

    def formula(organisation, period, parameters):
        # 60 Prozent des Vertragswertes
        return 0.60


class kampfflugzeug_offset_direkt_anteil(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Anteil direkte Offsets am Vertragswert (Art. 2 Abs. 1 lit. b SR 514.52)"
    reference = "SR 514.52 Art. 2"

    def formula(organisation, period, parameters):
        return 0.20


class kampfflugzeug_offset_indirekt_anteil(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Anteil indirekte Offsets am Vertragswert (Art. 2 Abs. 1 lit. b SR 514.52)"
    reference = "SR 514.52 Art. 2"

    def formula(organisation, period, parameters):
        return 0.40


class kampfflugzeug_offset_direkt_betrag(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Erforderlicher Betrag direkte Offsets in CHF"
    reference = "SR 514.52 Art. 2"

    def formula(organisation, period, parameters):
        vertragswert = organisation('kampfflugzeug_vertragswert', period)
        return vertragswert * 0.20


class kampfflugzeug_offset_indirekt_betrag(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Erforderlicher Betrag indirekte Offsets in CHF"
    reference = "SR 514.52 Art. 2"

    def formula(organisation, period, parameters):
        vertragswert = organisation('kampfflugzeug_vertragswert', period)
        return vertragswert * 0.40


class kampfflugzeug_offset_deutschschweiz_anteil(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Verteilschluessel Offsets Deutschschweiz (Art. 2 Abs. 1 lit. c SR 514.52)"
    reference = "SR 514.52 Art. 2"

    def formula(organisation, period, parameters):
        return 0.65


class kampfflugzeug_offset_westschweiz_anteil(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Verteilschluessel Offsets Westschweiz (Art. 2 Abs. 1 lit. c SR 514.52)"
    reference = "SR 514.52 Art. 2"

    def formula(organisation, period, parameters):
        return 0.30


class kampfflugzeug_offset_italienischsprachige_schweiz_anteil(Variable):
    value_type = float
    entity = Organisation
    definition_period = YEAR
    label = "Verteilschluessel Offsets italienischsprachige Schweiz (Art. 2 Abs. 1 lit. c SR 514.52)"
    reference = "SR 514.52 Art. 2"

    def formula(organisation, period, parameters):
        return 0.05
