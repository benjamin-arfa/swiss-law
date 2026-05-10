"""SR 611.015.3 Art. 3

Generated from: ch/611/de/611.015.3.md

SKB-Verordnung - Art. 3: Kontoberechtigte Angestellte. Berechtigt zu einer
Kontobeziehung mit der Sparkasse Bundespersonal (SKB) sind Angestellte
der zentralen und dezentralen Bundesverwaltung, Parlamentsdienste,
Bundesgerichte etc.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_angestellte_zentrale_bundesverwaltung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angestellte/r der zentralen Bundesverwaltung nach Anhang 1 RVOV"
    reference = "SR 611.015.3 Art. 3 Abs. 1 lit. a"


class ist_angestellte_dezentrale_bundesverwaltung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angestellte/r der dezentralen Bundesverwaltung nach Anhang 1 RVOV"
    reference = "SR 611.015.3 Art. 3 Abs. 1 lit. b"


class ist_angestellte_parlamentsdienste(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angestellte/r der Parlamentsdienste nach ParlG"
    reference = "SR 611.015.3 Art. 3 Abs. 1 lit. c"


class ist_angestellte_bundesgericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angestellte/r eines Bundesgerichts (BVGer, BStGer, BPatGer, BGer)"
    reference = "SR 611.015.3 Art. 3 Abs. 1 lit. d-g"


class ist_angestellte_bundesanwaltschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angestellte/r der Bundesanwaltschaft nach Art. 22 StBOG"
    reference = "SR 611.015.3 Art. 3 Abs. 1 lit. h"


class beurlaubt_laenger_als_drei_jahre(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist für länger als drei Jahre beurlaubt"
    reference = "SR 611.015.3 Art. 3 Abs. 2 lit. a"


class befristet_angestellt_weniger_als_drei_jahre(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Person ist ab dem Zeitpunkt des Antrags auf Kontoeröffnung auf "
        "weniger als drei Jahre befristet angestellt"
    )
    reference = "SR 611.015.3 Art. 3 Abs. 2 lit. b"


class berechtigt_skb_konto_angestellte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigt zu einer Kontobeziehung mit der SKB als Angestellte/r (Art. 3)"
    reference = "SR 611.015.3 Art. 3"

    def formula(person, period, parameters):
        # Abs. 1: Grundsätzlich berechtigt
        zentral = person('ist_angestellte_zentrale_bundesverwaltung', period)
        dezentral = person('ist_angestellte_dezentrale_bundesverwaltung', period)
        parlament = person('ist_angestellte_parlamentsdienste', period)
        gericht = person('ist_angestellte_bundesgericht', period)
        ba = person('ist_angestellte_bundesanwaltschaft', period)
        grundsaetzlich_berechtigt = zentral + dezentral + parlament + gericht + ba

        # Abs. 2: Ausschlussgründe
        beurlaubt = person('beurlaubt_laenger_als_drei_jahre', period)
        befristet = person('befristet_angestellt_weniger_als_drei_jahre', period)
        ausgeschlossen = beurlaubt + befristet

        return grundsaetzlich_berechtigt * (1 - ausgeschlossen)


class hinterbliebene_person_bezieht_rente_publica(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Hinterbliebene Person bezieht Ehegatten- oder Lebenspartnerrente "
        "aus offenem Vorsorgewerk von PUBLICA"
    )
    reference = "SR 611.015.3 Art. 3 Abs. 3"


class berechtigt_skb_konto_hinterbliebene(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Hinterbliebene Person ist zu einer Kontobeziehung mit der SKB "
        "berechtigt (Art. 3 Abs. 3)"
    )
    reference = "SR 611.015.3 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        return person('hinterbliebene_person_bezieht_rente_publica', period)
