"""SR 221.213.15 Art. 1

Generated from: ch/221/de/221.213.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_rahmenmietvertrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist die Vereinbarung ein Rahmenmietvertrag im Sinne von SR 221.213.15 Art. 1"
    reference = "SR 221.213.15 Art. 1"

    def formula(person, period, parameters):
        vereinbarung_zwischen_vermieter_und_mieterverband = person('vereinbarung_zwischen_vermieter_und_mieterverband', period)
        musterbestimmungen_aufgestellt = person('musterbestimmungen_aufgestellt', period)
        betrifft_wohn_oder_geschaeftsraeume = person('betrifft_wohn_oder_geschaeftsraeume', period)
        return vereinbarung_zwischen_vermieter_und_mieterverband * musterbestimmungen_aufgestellt * betrifft_wohn_oder_geschaeftsraeume


class vereinbarung_zwischen_vermieter_und_mieterverband(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vereinbarung zwischen Vermieter- und Mieterverbänden"
    reference = "SR 221.213.15 Art. 1 Abs. 1"


class musterbestimmungen_aufgestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Musterbestimmungen über Abschluss, Inhalt und Beendigung der Mietverhältnisse aufgestellt"
    reference = "SR 221.213.15 Art. 1 Abs. 1"


class betrifft_wohn_oder_geschaeftsraeume(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Betrifft Wohn- und Geschäftsräume"
    reference = "SR 221.213.15 Art. 1 Abs. 1"


class geltungsbereich_ganze_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Geltungsbereich für die ganze Schweiz"
    reference = "SR 221.213.15 Art. 1 Abs. 3 lit. a"


class geltungsbereich_ein_oder_mehrere_kantone(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Geltungsbereich für das Gebiet eines oder mehrerer Kantone"
    reference = "SR 221.213.15 Art. 1 Abs. 3 lit. b"


class anzahl_wohnungen_im_geltungsbereich(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Wohnungen im Geltungsbereich der Region"
    reference = "SR 221.213.15 Art. 1 Abs. 3 lit. c"


class anzahl_geschaeftsraeume_im_geltungsbereich(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Geschäftsräume im Geltungsbereich der Region"
    reference = "SR 221.213.15 Art. 1 Abs. 3 lit. c"


class geltungsbereich_region_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Region umfasst mindestens 30'000 Wohnungen oder 10'000 Geschäftsräume"
    reference = "SR 221.213.15 Art. 1 Abs. 3 lit. c"

    def formula(person, period, parameters):
        wohnungen = person('anzahl_wohnungen_im_geltungsbereich', period)
        geschaeftsraeume = person('anzahl_geschaeftsraeume_im_geltungsbereich', period)
        return (wohnungen >= 30000) + (geschaeftsraeume >= 10000)
