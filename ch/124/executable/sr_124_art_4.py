"""SR 124 Art. 4 - Anforderungen an das Unternehmen (Company Requirements)

Generated from: ch/de/124.md
The company must meet requirements: recruitment/training guarantees,
good reputation, solvency, internal controls, legal authorization,
and liability insurance with adequate coverage.
Exception for insurance if costs are disproportionate and risk is low.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class sicherheitsunternehmen_guter_ruf(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitsunternehmen hat nachgewiesenen guten Ruf und einwandfreies Geschaeftsgebaren"
    reference = "SR 124 Art. 4 Abs. 1 lit. b"
    default_value = False


class sicherheitsunternehmen_zahlungsfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitsunternehmen ist zahlungsfaehig"
    reference = "SR 124 Art. 4 Abs. 1 lit. c"
    default_value = False


class sicherheitsunternehmen_internes_kontrollsystem(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitsunternehmen verfuegt ueber angemessenes internes Kontrollsystem"
    reference = "SR 124 Art. 4 Abs. 1 lit. d"
    default_value = False


class sicherheitsunternehmen_haftpflichtversicherung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitsunternehmen hat Haftpflichtversicherung mit dem Risiko entsprechender Deckungssumme"
    reference = "SR 124 Art. 4 Abs. 1 lit. f"
    default_value = False


class sicherheitsunternehmen_erfuellt_anforderungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitsunternehmen erfuellt alle Anforderungen nach Art. 4"
    reference = "SR 124 Art. 4"

    def formula(person, period, parameters):
        ruf = person('sicherheitsunternehmen_guter_ruf', period)
        solvent = person('sicherheitsunternehmen_zahlungsfaehig', period)
        kontrolle = person('sicherheitsunternehmen_internes_kontrollsystem', period)
        versicherung = person('sicherheitsunternehmen_haftpflichtversicherung', period)
        return ruf * solvent * kontrolle * versicherung
