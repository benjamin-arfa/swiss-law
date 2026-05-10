"""SR 251.1 Art. 6

Generated from: ch/251/de/251.1.md

Beschlussfassung der Kommission: Beschlussfaehig wenn mindestens
die Haelfte der Mitglieder anwesend ist und mehr als die Haelfte
unabhaengige Sachverstaendige sind. Einfaches Mehr, Stichentscheid
durch Praesidenten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_kommissionsmitglieder(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtanzahl der Mitglieder der Wettbewerbskommission"
    reference = "SR 251.1 Art. 6 Abs. 1"


class anzahl_anwesende_mitglieder(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl anwesender Mitglieder bei der Sitzung"
    reference = "SR 251.1 Art. 6 Abs. 1 Bst. a"


class anzahl_anwesende_sachverstaendige(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl anwesender unabhaengiger Sachverstaendiger"
    reference = "SR 251.1 Art. 6 Abs. 1 Bst. b"


class kommission_ist_beschlussfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission beschlussfaehig ist"
    reference = "SR 251.1 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        gesamt = person('anzahl_kommissionsmitglieder', period)
        anwesend = person('anzahl_anwesende_mitglieder', period)
        sachverstaendige = person('anzahl_anwesende_sachverstaendige', period)

        # Mindestens Haelfte anwesend UND mehr als Haelfte der Anwesenden sind Sachverstaendige
        haelfte_anwesend = anwesend >= (gesamt / 2)
        mehrheit_sachverstaendig = sachverstaendige > (anwesend / 2)

        return haelfte_anwesend * mehrheit_sachverstaendig
