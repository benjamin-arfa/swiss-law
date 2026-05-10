"""SR 321.0 Art. 18

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schuldunfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Taeter war zur Tatzeit schuldunfaehig (nicht faehig Unrecht einzusehen oder danach zu handeln)"
    reference = "SR 321.0 Art. 18 Abs. 1"


class vermindert_schuldfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Taeter war zur Tatzeit vermindert schuldfaehig"
    reference = "SR 321.0 Art. 18 Abs. 2"


class selbstverschuldete_schuldunfaehigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schuldunfaehigkeit haette vermieden werden koennen (actio libera in causa)"
    reference = "SR 321.0 Art. 18 Abs. 4"


class strafbar_trotz_schuldunfaehigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist trotz Schuldunfaehigkeit strafbar (wegen Selbstverschulden)"
    reference = "SR 321.0 Art. 18"

    def formula(person, period, parameters):
        unfaehig = person('schuldunfaehig', period)
        vermindert = person('vermindert_schuldfaehig', period)
        selbstverschuldet = person('selbstverschuldete_schuldunfaehigkeit', period)
        # Abs. 1-3 nicht anwendbar wenn selbstverschuldet (Abs. 4)
        return (unfaehig + vermindert > 0) * selbstverschuldet
