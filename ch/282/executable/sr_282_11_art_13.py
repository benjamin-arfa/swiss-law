"""SR 282.11 Art. 13 - Eingriffe in Obligationaersrechte

Generated from: ch/282/de/282.11.md

This article enumerates the types of interventions possible in bondholder
rights. The specific measures (a-f) are modeled as input variables.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class gemeinwesen_hat_anleihensobligationen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Gemeinwesen hat Anleihensobligationen mit einheitlichen Bedingungen herausgegeben"
    reference = "SR 282.11 Art. 13"


class gemeinwesen_ausserstande_verpflichtungen_zu_erfuellen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Gemeinwesen ist ausserstande, seine Verpflichtungen rechtzeitig zu erfuellen"
    reference = "SR 282.11 Art. 13"


class amortisationsfrist_erstreckung_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Beantragte Erstreckung der Amortisationsfrist in Jahren"
    reference = "SR 282.11 Art. 13 lit. a"


class stundung_kapital_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Beantragte Stundungsdauer fuer Kapitalbetraege in Jahren"
    reference = "SR 282.11 Art. 13 lit. b"


class stundung_zinsen_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Beantragte Stundungsdauer fuer Zinsen in Jahren"
    reference = "SR 282.11 Art. 13 lit. c"


class zinsfuss_herabsetzung_faktor(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Faktor der Herabsetzung des Zinsfusses (min 0.5 = Haelfte)"
    reference = "SR 282.11 Art. 13 lit. e"


class nachlass_verfallener_zinsen_faktor(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Faktor des Nachlasses verfallener Zinse (max 0.5 = Haelfte)"
    reference = "SR 282.11 Art. 13 lit. f"


# Computed variables

class eingriff_in_obligationaersrechte_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eingriffe in Obligationaersrechte sind grundsaetzlich zulaessig"
    reference = "SR 282.11 Art. 13"

    def formula(self, period, parameters):
        obligationen = self('gemeinwesen_hat_anleihensobligationen', period)
        ausserstande = self('gemeinwesen_ausserstande_verpflichtungen_zu_erfuellen', period)
        return obligationen * ausserstande


class amortisationsfrist_erstreckung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Erstreckung der Amortisationsfrist ist zulaessig (max 5 Jahre)"
    reference = "SR 282.11 Art. 13 lit. a"

    def formula(self, period, parameters):
        erstreckung = self('amortisationsfrist_erstreckung_jahre', period)
        grundsaetzlich = self('eingriff_in_obligationaersrechte_zulaessig', period)
        return grundsaetzlich * (erstreckung <= 5)


class stundung_kapital_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Stundung des Kapitals ist zulaessig (max 5 Jahre)"
    reference = "SR 282.11 Art. 13 lit. b"

    def formula(self, period, parameters):
        stundung = self('stundung_kapital_jahre', period)
        grundsaetzlich = self('eingriff_in_obligationaersrechte_zulaessig', period)
        return grundsaetzlich * (stundung <= 5)


class zinsfuss_herabsetzung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Herabsetzung des Zinsfusses ist zulaessig (bis zur Haelfte)"
    reference = "SR 282.11 Art. 13 lit. e"

    def formula(self, period, parameters):
        faktor = self('zinsfuss_herabsetzung_faktor', period)
        grundsaetzlich = self('eingriff_in_obligationaersrechte_zulaessig', period)
        return grundsaetzlich * (faktor >= 0.5)


class nachlass_zinsen_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Nachlass verfallener Zinse ist zulaessig (max Haelfte)"
    reference = "SR 282.11 Art. 13 lit. f"

    def formula(self, period, parameters):
        faktor = self('nachlass_verfallener_zinsen_faktor', period)
        grundsaetzlich = self('eingriff_in_obligationaersrechte_zulaessig', period)
        return grundsaetzlich * (faktor <= 0.5)
