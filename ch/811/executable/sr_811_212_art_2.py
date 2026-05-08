"""SR 811.212 Art. 2

Generated from: ch/811/de/811.212.md

Bachelorstudiengang in Pflege - Kompetenzen:
- Verantwortung für Pflegeprozess aller Altersgruppen
- Klinische Untersuchungen und Anamnesen
- Pflegeziele festlegen und Interventionen durchführen
- Wissenschaftliche Abstützung und Qualitätsstandards
- Versorgungskontinuität gewährleisten
- Prävention und Gesundheitsförderung
- Notfallmassnahmen ergreifen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kompetenz_pflegeprozess_verantwortung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kompetenz: Verantwortung für Pflegeprozess übernehmen"
    reference = "SR 811.212 Art. 2 Bst. a"


class kompetenz_klinische_untersuchung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kompetenz: Klinische Untersuchungen und Pflegediagnosen"
    reference = "SR 811.212 Art. 2 Bst. b"


class kompetenz_interventionen_wissenschaftlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kompetenz: Interventionen auf wissenschaftliche Erkenntnisse abstützen"
    reference = "SR 811.212 Art. 2 Bst. d"


class kompetenz_versorgungskontinuitaet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kompetenz: Versorgungskontinuität gewährleisten"
    reference = "SR 811.212 Art. 2 Bst. e"


class kompetenz_notfallmassnahmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kompetenz: Lebenserhaltende Massnahmen in Notfallsituationen"
    reference = "SR 811.212 Art. 2 Bst. g"


class kompetenz_forschungsbeteiligung_pflege(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kompetenz: Forschungsbedarf erkennen und an Forschung beteiligen"
    reference = "SR 811.212 Art. 2 Bst. j"


class erfuellt_kompetenzen_pflege(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Kernkompetenzen des Bachelorstudiengangs Pflege erfüllt sind"
    reference = "SR 811.212 Art. 2"

    def formula(person, period, parameters):
        return (
            person('kompetenz_pflegeprozess_verantwortung', period) *
            person('kompetenz_klinische_untersuchung', period) *
            person('kompetenz_interventionen_wissenschaftlich', period) *
            person('kompetenz_versorgungskontinuitaet', period) *
            person('kompetenz_notfallmassnahmen', period) *
            person('kompetenz_forschungsbeteiligung_pflege', period)
        )
