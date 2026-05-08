"""SR 741.016 Art. 3

Generated from: ch/741/de/741.016.md

VKVoeV: Kompetenzen des UVEK
The UVEK (Federal Department for Environment, Transport, Energy and
Communications) may: (a) update technical details of international
regulations in VTS Annex 2, (b) declare new international construction
and equipment prescriptions binding, (c) approve amendments to the
AETR agreement.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class uvek_kompetenz_technische_details(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "UVEK darf technische Einzelheiten internationaler Regelungen nachfuehren (Art. 3 lit. a VKVoeV)"
    reference = "SR 741.016 Art. 3"

    def formula_2025_04_01(person, period, parameters):
        return True


class uvek_kompetenz_bauvorschriften(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "UVEK darf neue internationale Bau- und Ausruestungsvorschriften verbindlich erklaeren (Art. 3 lit. b VKVoeV)"
    reference = "SR 741.016 Art. 3"

    def formula_2025_04_01(person, period, parameters):
        return True


class uvek_kompetenz_aetr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "UVEK darf AETR-Aenderungen genehmigen (Art. 3 lit. c VKVoeV)"
    reference = "SR 741.016 Art. 3"

    def formula_2025_04_01(person, period, parameters):
        return True
