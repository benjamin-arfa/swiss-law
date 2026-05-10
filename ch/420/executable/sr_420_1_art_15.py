"""SR 420.1 Art. 15

Generated from: ch/420/de/420.1.md

Beitraege an Forschungseinrichtungen von nationaler Bedeutung - max. 50 Prozent.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_forschungsinfrastruktur(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine nichtkommerzielle Forschungsinfrastruktur (Art. 15 Abs. 3 Bst. a)"
    reference = "SR 420.1 Art. 15 Abs. 3 Bst. a"


class ist_forschungsinstitution(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine nichtkommerzielle Forschungsinstitution (Art. 15 Abs. 3 Bst. b)"
    reference = "SR 420.1 Art. 15 Abs. 3 Bst. b"


class ist_technologiekompetenzzentrum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein Technologiekompetenzzentrum (Art. 15 Abs. 3 Bst. c)"
    reference = "SR 420.1 Art. 15 Abs. 3 Bst. c"


class gesamtaufwand_investitionen_betrieb(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtaufwand fuer Investitionen und Betrieb"
    reference = "SR 420.1 Art. 15 Abs. 5"


class kompetitive_forschungsmittel(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kompetitive Forschungsmittel und Auftraege"
    reference = "SR 420.1 Art. 15 Abs. 5 Bst. b"


class unterstuetzungsbeitraege_dritte(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Summe der Unterstuetzungsbeitraege von Kantonen, oeffentlichen Gemeinwesen, Hochschulen und Privaten"
    reference = "SR 420.1 Art. 15 Abs. 5"


class wirtschaft_forschungskooperationen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Beitraege der Wirtschaft aus Forschungs- und Entwicklungskooperationen"
    reference = "SR 420.1 Art. 15 Abs. 5 Bst. c"


class grundfinanzierung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Grundfinanzierung (Gesamtaufwand minus kompetitive Mittel)"
    reference = "SR 420.1 Art. 15 Abs. 5"

    def formula(person, period, parameters):
        return max_(
            person('gesamtaufwand_investitionen_betrieb', period) -
            person('kompetitive_forschungsmittel', period),
            0
        )


class bundesbeitrag_hoechstsatz_forschungseinrichtung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstsatz des Bundesbeitrags fuer Forschungseinrichtung von nationaler Bedeutung"
    reference = "SR 420.1 Art. 15 Abs. 5"

    def formula(person, period, parameters):
        infrastruktur = person('ist_forschungsinfrastruktur', period)
        institution = person('ist_forschungsinstitution', period)
        techzentrum = person('ist_technologiekompetenzzentrum', period)

        gesamtaufwand = person('gesamtaufwand_investitionen_betrieb', period)
        grundfin = person('grundfinanzierung', period)
        dritte = person('unterstuetzungsbeitraege_dritte', period)
        wirtschaft = person('wirtschaft_forschungskooperationen', period)

        # Forschungsinfrastrukturen: max 50% Gesamtaufwand
        max_infrastruktur = gesamtaufwand * 0.5

        # Forschungsinstitutionen: max 50% Grundfinanzierung, max Summe Dritte
        max_institution = min_(grundfin * 0.5, dritte)

        # Technologiekompetenzzentren: max 50% Grundfinanzierung, max Summe Wirtschaft + Dritte
        max_techzentrum = min_(grundfin * 0.5, wirtschaft + dritte)

        return (
            infrastruktur * max_infrastruktur +
            institution * max_institution +
            techzentrum * max_techzentrum
        )
