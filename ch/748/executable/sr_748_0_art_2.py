"""SR 748.0 Art. 2

Generated from: ch/748/de/748.0.md

Art. 2: Zugelassene Luftfahrzeuge - Aircraft permitted in Swiss airspace:
a. Swiss state aircraft
b. Aircraft in Swiss register with required documents (Art. 52, 56)
c. Special category aircraft (Art. 51, 108)
d. Foreign aircraft permitted by international agreement
e. Aircraft permitted by special FOCA order
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lfg_ist_schweizer_staatsluftfahrzeug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Luftfahrzeug ist ein schweizerisches Staatsluftfahrzeug"
    reference = "SR 748.0 Art. 2 Abs. 1 Bst. a"


class lfg_ist_im_register_eingetragen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Luftfahrzeug ist im schweizerischen Luftfahrzeugregister eingetragen (Art. 52)"
    reference = "SR 748.0 Art. 2 Abs. 1 Bst. b"


class lfg_hat_ausweise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Luftfahrzeug verfügt über die verlangten Ausweise (Art. 56)"
    reference = "SR 748.0 Art. 2 Abs. 1 Bst. b"


class lfg_ist_sonderkategorie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Luftfahrzeug gehört zu einer besonderen Kategorie mit Sonderregeln"
    reference = "SR 748.0 Art. 2 Abs. 1 Bst. c"


class lfg_auslaendisch_mit_abkommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ausländisches Luftfahrzeug mit zwischenstaatlicher Vereinbarung"
    reference = "SR 748.0 Art. 2 Abs. 1 Bst. d"


class lfg_bazl_sonderverfuegung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Luftfahrzeug hat besondere Verfügung des BAZL"
    reference = "SR 748.0 Art. 2 Abs. 1 Bst. e"


class lfg_zum_verkehr_zugelassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Luftfahrzeug ist zum Verkehr im schweizerischen Luftraum zugelassen"
    reference = "SR 748.0 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        staatslfz = person('lfg_ist_schweizer_staatsluftfahrzeug', period)
        register = person('lfg_ist_im_register_eingetragen', period)
        ausweise = person('lfg_hat_ausweise', period)
        sonder = person('lfg_ist_sonderkategorie', period)
        ausland = person('lfg_auslaendisch_mit_abkommen', period)
        bazl = person('lfg_bazl_sonderverfuegung', period)

        # b. requires both register and documents
        registriert_ok = register * ausweise

        return (staatslfz + registriert_ok + sonder + ausland + bazl) > 0
