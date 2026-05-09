"""SR 915.8 Art. 3

Generated from: ch/915/de/915.8.md

FKINV - Art. 3: Hoehe der Finanzhilfe und anrechenbare Kosten.
Max. 80% der anrechenbaren Kosten, jaehrliche Zusprechung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class fkinv_anrechenbare_kosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = (
        "Anrechenbare und vom BLW anerkannte Kosten fuer Aufbau und Betrieb "
        "des Kompetenz- und Innovationsnetzwerks (Art. 3 Abs. 1)"
    )
    reference = "SR 915.8 Art. 3 Abs. 1"


class fkinv_finanzhilfe_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoehe der Finanzhilfe, max. 80% der anrechenbaren Kosten (Art. 3 Abs. 1)"
    reference = "SR 915.8 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        # Art. 3 Abs. 1: Die Finanzhilfe betraegt hoechstens 80 Prozent
        # der anrechenbaren Kosten.
        anrechenbare_kosten = person('fkinv_anrechenbare_kosten', period)
        max_anteil = 0.80
        return anrechenbare_kosten * max_anteil


class fkinv_personalkosten_anrechenbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Personalkosten sind anrechenbare Kosten (Art. 3 Abs. 3 lit. a)"
    reference = "SR 915.8 Art. 3 Abs. 3 lit. a"


class fkinv_sachkosten_anrechenbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sachkosten sind anrechenbare Kosten (Art. 3 Abs. 3 lit. b)"
    reference = "SR 915.8 Art. 3 Abs. 3 lit. b"


class fkinv_mietkosten_anrechenbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mietkosten fuer benoetigte Raeume sind anrechenbare Kosten (Art. 3 Abs. 3 lit. c)"
    reference = "SR 915.8 Art. 3 Abs. 3 lit. c"


class fkinv_technik_infrastruktur_anrechenbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kosten fuer technische Infrastruktur sind anrechenbare Kosten (Art. 3 Abs. 3 lit. d)"
    reference = "SR 915.8 Art. 3 Abs. 3 lit. d"


class fkinv_baukosten_nicht_anrechenbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kosten fuer Bau oder Erwerb von Raeumlichkeiten sind nicht anrechenbar (Art. 3 Abs. 4 lit. a)"
    reference = "SR 915.8 Art. 3 Abs. 4 lit. a"

    def formula(person, period, parameters):
        # Art. 3 Abs. 4 lit. a: Always true - building costs are never eligible.
        return person('fkinv_finanzhilfe_voraussetzungen_erfuellt', period) * 0 + 1


class fkinv_eigenleistungen_subventioniert_nicht_anrechenbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Eigenleistungen von ueberwiegend vom Bund subventionierten Organisationen "
        "sind nicht anrechenbar (Art. 3 Abs. 4 lit. b)"
    )
    reference = "SR 915.8 Art. 3 Abs. 4 lit. b"

    def formula(person, period, parameters):
        # Art. 3 Abs. 4 lit. b: Always true as a principle.
        return person('fkinv_finanzhilfe_voraussetzungen_erfuellt', period) * 0 + 1
