"""SR 913.211 Art. 7b

Generated from: ch/913/de/913.211.md

Zahlungen für gemeinschaftliche Initiativen:
- Kanton kann Teilzahlung und Schlusszahlung anfordern
- Minimaler Auszahlungsbetrag: 10'000 CHF pro Teilzahlung
- Maximale Teilzahlung: 80% des genehmigten Gesamtbeitrages
- Schlusszahlungsgesuch spätestens 3 Jahre nach Beitragsgewährung
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class genehmigter_gesamtbeitrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Genehmigter Gesamtbeitrag in CHF"
    reference = "SR 913.211 Art. 7b Abs. 1"


class beantragter_teilzahlungsbetrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Beantragter Teilzahlungsbetrag in CHF"
    reference = "SR 913.211 Art. 7b Abs. 1"


class jahre_seit_beitragsgewaehrung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit der Beitragsgewährung"
    reference = "SR 913.211 Art. 7b Abs. 3"


class teilzahlung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die beantragte Teilzahlung zulässig ist"
    reference = "SR 913.211 Art. 7b Abs. 1"

    def formula(person, period, parameters):
        beantragt = person('beantragter_teilzahlungsbetrag', period)
        gesamt = person('genehmigter_gesamtbeitrag', period)
        min_betrag = parameters(period).sr_913_211.min_teilzahlung_chf
        max_anteil = parameters(period).sr_913_211.max_teilzahlung_anteil

        return (beantragt >= min_betrag) * (beantragt <= gesamt * max_anteil)


class schlusszahlung_fristgerecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Schlusszahlungsgesuch fristgerecht eingereicht wird"
    reference = "SR 913.211 Art. 7b Abs. 3"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_beitragsgewaehrung', period)
        max_frist = parameters(period).sr_913_211.max_frist_schlusszahlung_jahre
        return jahre <= max_frist
