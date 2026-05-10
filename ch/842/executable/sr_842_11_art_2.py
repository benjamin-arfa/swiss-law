"""SR 842.11 Art. 2

Generated from: ch/842/de/842.11.md

Art. 2: Anrechenbare Liegenschaftskosten
- Abs. a: 0.9% der Anlagekosten fuer Unterhaltskosten, Erneuerungsfonds,
  Risikozuschlag und oeffentliche Abgaben.
- Abs. b: 4% des nicht verbilligten Nettomietzinses fuer Verwaltungskosten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wfg_anlagekosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anlagekosten des Neubaus oder der umfassenden Erneuerung (CHF)"
    reference = "SR 842.11 Art. 2 Bst. a"


class wfg_nettomietzins_nicht_verbilligt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Nicht verbilligter Nettomietzins (CHF/Jahr)"
    reference = "SR 842.11 Art. 2 Bst. b"


class wfg_unterhaltskostenpauschale(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Pauschale fuer Unterhaltskosten, Erneuerungsfonds, Risikozuschlag "
        "und oeffentliche Abgaben (0.9% der Anlagekosten)"
    )
    reference = "SR 842.11 Art. 2 Bst. a"

    def formula(person, period, parameters):
        anlagekosten = person('wfg_anlagekosten', period)
        satz = parameters(period).wfg.unterhaltskostenpauschale_satz
        return anlagekosten * satz


class wfg_verwaltungskostenpauschale(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschale fuer Verwaltungskosten (4% des nicht verbilligten Nettomietzinses)"
    reference = "SR 842.11 Art. 2 Bst. b"

    def formula(person, period, parameters):
        mietzins = person('wfg_nettomietzins_nicht_verbilligt', period)
        satz = parameters(period).wfg.verwaltungskostenpauschale_satz
        return mietzins * satz


class wfg_anrechenbare_liegenschaftskosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total anrechenbare Liegenschaftskosten (CHF/Jahr)"
    reference = "SR 842.11 Art. 2"

    def formula(person, period, parameters):
        unterhalt = person('wfg_unterhaltskostenpauschale', period)
        verwaltung = person('wfg_verwaltungskostenpauschale', period)
        return unterhalt + verwaltung
