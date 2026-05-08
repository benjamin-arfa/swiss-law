"""SR 721.80 Art. 50a

Generated from: ch/721/de/721.80.md

Art. 50a - Wasserzins exemptions for plants with investment subsidies (Art. 26 EnG):
1a. New plants: no Wasserzins during construction + 10 years from commissioning
    on the full gross capacity.
1b. Substantial expansion/renewal: no Wasserzins for 10 years from commissioning
    on the additional gross capacity only.
2. These exemptions also apply to the special taxes under Art. 49(2).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wrg_investitionsbeitrag_neuanlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the plant is a new installation with investment subsidy under Art. 26 EnG"
    reference = "SR 721.80 Art. 50a Abs. 1 Bst. a"


class wrg_investitionsbeitrag_erweiterung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the plant is a substantially expanded/renewed installation with investment subsidy"
    reference = "SR 721.80 Art. 50a Abs. 1 Bst. b"


class wrg_jahre_seit_inbetriebnahme(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Years since commissioning of the (new/expanded) plant"
    reference = "SR 721.80 Art. 50a Abs. 1"


class wrg_zusaetzliche_bruttoleistung_kw(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Additional gross capacity from expansion/renewal (kW)"
    reference = "SR 721.80 Art. 50a Abs. 1 Bst. b"


class wrg_investitionsbeitrag_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the plant currently benefits from Wasserzins exemption due to investment subsidy"
    reference = "SR 721.80 Art. 50a"

    def formula(person, period, parameters):
        neuanlage = person('wrg_investitionsbeitrag_neuanlage', period)
        erweiterung = person('wrg_investitionsbeitrag_erweiterung', period)
        in_baufrist = person('wrg_in_baufrist', period)
        jahre = person('wrg_jahre_seit_inbetriebnahme', period)
        p = parameters(period).sr_721_80

        befreiung_jahre_neu = p.investitionsbeitrag_befreiung_neuanlage_jahre
        befreiung_jahre_erw = p.investitionsbeitrag_befreiung_erweiterung_jahre

        # New plant: exempt during construction + 10 years from commissioning
        neu_befreit = neuanlage * (in_baufrist + (jahre <= befreiung_jahre_neu))

        # Expansion: exempt for 10 years on additional capacity
        erw_befreit = erweiterung * (jahre <= befreiung_jahre_erw)

        return neu_befreit + erw_befreit > 0
