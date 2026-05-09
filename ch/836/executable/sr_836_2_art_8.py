"""SR 836.2 Art. 8

Generated from: ch/836/de/836.2.md

Art. 8: Familienzulagen und Unterhaltsbeitraege.
Anspruchsberechtigte Personen, die auf Grund eines Gerichtsurteils
oder einer Vereinbarung zur Zahlung von Unterhaltsbeitraegen fuer
Kinder verpflichtet sind, muessen die Familienzulagen zusaetzlich
zu den Unterhaltsbeitraegen entrichten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class unterhaltsbeitrag_verpflichtet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist zur Zahlung von Unterhaltsbeitraegen verpflichtet (Gerichtsurteil/Vereinbarung)"
    reference = "SR 836.2 Art. 8"


class betrag_unterhaltsbeitrag(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Monatlicher Unterhaltsbeitrag gemaess Gerichtsurteil oder Vereinbarung"
    reference = "SR 836.2 Art. 8"


class gesamtzahlung_mit_familienzulage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Gesamtzahlung: Unterhaltsbeitrag plus Familienzulage (Art. 8 FamZG)"
    reference = "SR 836.2 Art. 8"

    def formula(person, period, parameters):
        unterhalt = person('betrag_unterhaltsbeitrag', period)
        kinderzulage = person('betrag_kinderzulage', period)
        ausbildungszulage = person('betrag_ausbildungszulage', period)
        familienzulage = kinderzulage + ausbildungszulage
        verpflichtet = person('unterhaltsbeitrag_verpflichtet', period)
        # Familienzulagen zusaetzlich zu den Unterhaltsbeitraegen
        return where(verpflichtet, unterhalt + familienzulage, familienzulage)
