"""SR 831.26 Art. 7

Generated from: ch/831/de/831.26.md

Cost participation by cantons:
- Cantons must co-finance stays so no disabled person needs social welfare
- If no suitable recognized institution available, person has right to
  canton's contribution at another institution meeting Art. 5 requirements
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kosten_aufenthalt_institution(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtkosten des Aufenthalts in einer anerkannten Institution (CHF)"
    reference = "SR 831.26 Art. 7 Abs. 1"


class eigenmittel_invalide_person(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eigenmittel der invaliden Person fuer den Institutionsaufenthalt (CHF)"
    reference = "SR 831.26 Art. 7 Abs. 1"


class institution_anerkannt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Institution durch den Kanton anerkannt ist"
    reference = "SR 831.26 Art. 7 Abs. 1"


class platz_in_anerkannter_institution_verfuegbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Platz in einer anerkannten Institution verfuegbar ist"
    reference = "SR 831.26 Art. 7 Abs. 2"


class kantonale_kostenbeteiligung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kantonale Kostenbeteiligung am Aufenthalt (CHF)"
    reference = "SR 831.26 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        kosten = person('kosten_aufenthalt_institution', period)
        eigenmittel = person('eigenmittel_invalide_person', period)
        anerkannt = person('institution_anerkannt', period)

        # Canton covers the gap so no social welfare is needed
        beteiligung = max_(kosten - eigenmittel, 0)
        return beteiligung * anerkannt


class anspruch_kostenbeteiligung_andere_institution(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf Kostenbeteiligung an einer anderen (nicht anerkannten) Institution"
    reference = "SR 831.26 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        ist_invalide = person('ist_invalide_person', period)
        kein_platz = not_(person('platz_in_anerkannter_institution_verfuegbar', period))
        voraussetzungen = person('institution_anerkennungsvoraussetzungen_erfuellt', period)
        return ist_invalide * kein_platz * voraussetzungen
