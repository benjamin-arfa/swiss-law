"""SR 822.11 Art. 19

Generated from: ch/822/de/822.11.md

Art. 19: Sonntagsarbeit
- Abs. 1: Ausnahmen vom Sonntagsarbeitsverbot beduerften der Bewilligung
- Abs. 2: Dauernde Sonntagsarbeit: bewilligt wenn technisch/wirtschaftlich
  unentbehrlich
- Abs. 3: Voruebergehende Sonntagsarbeit: bei dringendem Beduerfnis;
  Lohnzuschlag von 50%
- Abs. 5: AN darf nicht ohne Einverstaendnis zu Sonntagsarbeit herangezogen
  werden
- Abs. 6: Kantone koennen max. 4 Sonntage/Jahr fuer Verkaufsgeschaefte
  bewilligungsfrei erklaeren
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arg_sonntagsarbeit_bewilligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Sonntagsarbeit ist bewilligt"
    reference = "SR 822.11 Art. 19 Abs. 1"


class arg_sonntagsarbeit_voruebergehend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Arbeitnehmer verrichtet voruebergehende Sonntagsarbeit"
    reference = "SR 822.11 Art. 19 Abs. 3"


class arg_sonntagsarbeit_einverstaendnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Arbeitnehmer hat Einverstaendnis zur Sonntagsarbeit gegeben"
    reference = "SR 822.11 Art. 19 Abs. 5"


class arg_sonntagsarbeit_lohnzuschlag_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Lohnzuschlag fuer Sonntagsarbeit in Prozent"
    reference = "SR 822.11 Art. 19 Abs. 3"

    def formula(person, period, parameters):
        voruebergehend = person('arg_sonntagsarbeit_voruebergehend', period)
        # 50% surcharge for temporary Sunday work
        return where(voruebergehend, 50.0, 0.0)


class arg_sonntagsarbeit_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Sonntagsarbeit ist zulaessig (bewilligt und mit Einverstaendnis)"
    reference = "SR 822.11 Art. 19"

    def formula(person, period, parameters):
        bewilligt = person('arg_sonntagsarbeit_bewilligt', period)
        einverstaendnis = person('arg_sonntagsarbeit_einverstaendnis', period)
        return bewilligt * einverstaendnis
