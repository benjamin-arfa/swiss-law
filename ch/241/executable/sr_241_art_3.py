"""SR 241 Art. 3

Generated from: ch/de/241.md

Specific unfair advertising and sales methods (non-exhaustive list).
Key prohibitions include: disparagement (a), false claims (b),
misleading titles (c), confusion (d), unfair comparisons (e),
below-cost sales (f), deceptive add-ons (g), aggressive sales (h),
concealment of product properties (i), consumer credit violations (k-n),
unsolicited mass advertising (o), deceptive directory entries (p-q),
pyramid schemes (r), e-commerce deficiencies (s), misleading
prize competitions (t), ignoring do-not-call lists (u-w),
unsubstantiated climate claims (x).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class herabsetzung_mitbewerber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Mitbewerber durch unrichtige oder unnoetig verletzende Aeusserungen herabgesetzt werden"
    reference = "SR 241 Art. 3 Abs. 1 Bst. a"


class unrichtige_angaben_ueber_sich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ueber sich selbst unrichtige oder irrefuehrende Angaben gemacht werden"
    reference = "SR 241 Art. 3 Abs. 1 Bst. b"


class verwechslungsgefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Verwechslungen mit Waren oder Geschaeftsbetrieb eines anderen herbeigefuehrt werden"
    reference = "SR 241 Art. 3 Abs. 1 Bst. d"


class unter_einstandspreis_angeboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Waren wiederholt unter Einstandspreisen angeboten werden"
    reference = "SR 241 Art. 3 Abs. 1 Bst. f"


class aggressive_verkaufsmethoden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Kunden durch aggressive Verkaufsmethoden in der Entscheidungsfreiheit beeintraechtigt werden"
    reference = "SR 241 Art. 3 Abs. 1 Bst. h"


class massenwerbung_ohne_einwilligung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Massenwerbung ohne Einwilligung fernmeldetechnisch gesendet wird"
    reference = "SR 241 Art. 3 Abs. 1 Bst. o"


class schneeball_system(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Schneeball-, Lawinen- oder Pyramidensystem betrieben wird"
    reference = "SR 241 Art. 3 Abs. 1 Bst. r"


class e_commerce_informationspflicht_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob im elektronischen Geschaeftsverkehr Informationspflichten verletzt werden"
    reference = "SR 241 Art. 3 Abs. 1 Bst. s"


class werbeanruf_ohne_rufnummer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Werbeanrufe ohne angezeigte Rufnummer getaetigt werden"
    reference = "SR 241 Art. 3 Abs. 1 Bst. v"


class klimabelastung_unbelegte_angaben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob unbelegte Angaben zur Klimabelastung gemacht werden"
    reference = "SR 241 Art. 3 Abs. 1 Bst. x"


class unlautere_werbemethode(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine unlautere Werbe- oder Verkaufsmethode nach Art. 3 vorliegt"
    reference = "SR 241 Art. 3"

    def formula(person, period, parameters):
        return (
            person('herabsetzung_mitbewerber', period)
            + person('unrichtige_angaben_ueber_sich', period)
            + person('verwechslungsgefahr', period)
            + person('unter_einstandspreis_angeboten', period)
            + person('aggressive_verkaufsmethoden', period)
            + person('massenwerbung_ohne_einwilligung', period)
            + person('schneeball_system', period)
            + person('e_commerce_informationspflicht_verletzt', period)
            + person('werbeanruf_ohne_rufnummer', period)
            + person('klimabelastung_unbelegte_angaben', period)
        ) > 0
