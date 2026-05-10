"""SR 822.11 Art. 17

Generated from: ch/822/de/822.11.md

Art. 17: Ausnahmen vom Nachtarbeitsverbot - Night work exceptions require
authorization. Permanent/regular night work requires technical or economic
necessity. Temporary night work requires urgent need. Night work between
23-24h and 5-6h requires urgent need. Employer needs worker's consent.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arg_nachtarbeit_dauerhaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Nachtarbeit ist dauerhaft oder regelmaessig wiederkehrend"
    reference = "SR 822.11 Art. 17 Abs. 2"


class arg_nachtarbeit_vorubergehend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Nachtarbeit ist voruebergehend"
    reference = "SR 822.11 Art. 17 Abs. 3"


class arg_nachtarbeit_technisch_wirtschaftlich_unentbehrlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Nachtarbeit ist aus technischen oder wirtschaftlichen Gruenden unentbehrlich"
    reference = "SR 822.11 Art. 17 Abs. 2"


class arg_nachtarbeit_dringendes_beduerfnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Dringendes Beduerfnis fuer Nachtarbeit ist nachgewiesen"
    reference = "SR 822.11 Art. 17 Abs. 3"


class arg_arbeitnehmer_einverstaendnis_nachtarbeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitnehmer hat sein Einverstaendnis zur Nachtarbeit gegeben"
    reference = "SR 822.11 Art. 17 Abs. 6"


class arg_nachtarbeit_bewilligungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Nachtarbeit ist bewilligungsfaehig nach Art. 17 ArG"
    reference = "SR 822.11 Art. 17"

    def formula(person, period, parameters):
        dauerhaft = person('arg_nachtarbeit_dauerhaft', period)
        vorubergehend = person('arg_nachtarbeit_vorubergehend', period)
        unentbehrlich = person('arg_nachtarbeit_technisch_wirtschaftlich_unentbehrlich', period)
        dringend = person('arg_nachtarbeit_dringendes_beduerfnis', period)
        einverstaendnis = person('arg_arbeitnehmer_einverstaendnis_nachtarbeit', period)

        # Abs. 2: Dauerhafte Nachtarbeit -> technisch/wirtschaftlich unentbehrlich
        dauerhaft_ok = dauerhaft * unentbehrlich

        # Abs. 3: Voruebergehende Nachtarbeit -> dringendes Beduerfnis
        vorubergehend_ok = vorubergehend * dringend

        # Abs. 6: Arbeitnehmer muss einverstanden sein
        sachlich_ok = dauerhaft_ok + vorubergehend_ok

        return sachlich_ok * einverstaendnis
