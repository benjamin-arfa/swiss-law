"""SR 784.104 Art. 4

Generated from: ch/784/de/784.104.md

Zuteilung von Adressierungselementen:
- BAKOM teilt auf Gesuch Adressierungselemente zu
- Gesuch muss Name, Adresse und gewünschtes Element enthalten
- Zuteilung kann verweigert werden bei Verdacht auf Rechtsverletzung,
  technischen Gründen, fehlender Schweiz-Nutzung, Nichtbezahlung, Konkurs
- Ausländische Gesuchsteller brauchen Korrespondenzadresse in der Schweiz
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesuch_name_und_adresse_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Name und Adresse im Gesuch angegeben sind"
    reference = "SR 784.104 Art. 4 Abs. 1bis Bst. a"


class gewuenschtes_element_angegeben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das gewünschte Adressierungselement im Gesuch angegeben ist"
    reference = "SR 784.104 Art. 4 Abs. 1bis Bst. b"


class verdacht_auf_rechtsverletzung_aefv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Verdacht besteht, dass mit dem Element Bundesrecht verletzt wird"
    reference = "SR 784.104 Art. 4 Abs. 3 Bst. a"


class verdacht_auf_blockierung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Verdacht besteht, dass Zuteilung an andere verhindert werden soll"
    reference = "SR 784.104 Art. 4 Abs. 3 Bst. abis"


class hauptsaechlich_schweiz_nutzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Element hauptsächlich in der Schweiz verwendet wird"
    reference = "SR 784.104 Art. 4 Abs. 3 Bst. c"


class verwaltungsgebuehren_bezahlt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verwaltungsgebühren bezahlt wurden"
    reference = "SR 784.104 Art. 4 Abs. 3 Bst. d"


class in_konkurs_oder_liquidation_aefv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich der Gesuchsteller in Konkurs, Liquidation oder Nachlassverfahren befindet"
    reference = "SR 784.104 Art. 4 Abs. 3 Bst. e"


class sitz_im_ausland_aefv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Gesuchsteller Sitz im Ausland hat"
    reference = "SR 784.104 Art. 4 Abs. 4"


class korrespondenzadresse_schweiz_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Korrespondenzadresse in der Schweiz bezeichnet wurde"
    reference = "SR 784.104 Art. 4 Abs. 4"


class gesuch_formell_vollstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Zuteilungsgesuch formell vollständig ist"
    reference = "SR 784.104 Art. 4 Abs. 1bis"

    def formula(person, period, parameters):
        name_adresse = person('gesuch_name_und_adresse_vorhanden', period)
        element = person('gewuenschtes_element_angegeben', period)
        ausland = person('sitz_im_ausland_aefv', period)
        korr = person('korrespondenzadresse_schweiz_vorhanden', period)

        return name_adresse * element * ((ausland == False) + (ausland * korr))


class zuteilung_kann_verweigert_werden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zuteilung des Adressierungselements verweigert werden kann"
    reference = "SR 784.104 Art. 4 Abs. 3"

    def formula(person, period, parameters):
        return (
            person('verdacht_auf_rechtsverletzung_aefv', period) +
            person('verdacht_auf_blockierung', period) +
            (person('hauptsaechlich_schweiz_nutzung', period) == False) +
            (person('verwaltungsgebuehren_bezahlt', period) == False) +
            person('in_konkurs_oder_liquidation_aefv', period)
        )
