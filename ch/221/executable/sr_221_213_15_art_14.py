"""SR 221.213.15 Art. 14

Generated from: ch/221/de/221.213.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antrag_aller_vertragsparteien_auf_ausserkraftsetzung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Vertragsparteien beantragen Ausserkraftsetzung"
    reference = "SR 221.213.15 Art. 14 Abs. 1 lit. a"


class voraussetzungen_nicht_mehr_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzungen zur Allgemeinverbindlicherklärung nicht mehr erfüllt"
    reference = "SR 221.213.15 Art. 14 Abs. 1 lit. b"


class vertrag_vorzeitig_aufgeloest(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Allgemeinverbindlich erklärter Vertrag vorzeitig aufgelöst"
    reference = "SR 221.213.15 Art. 14 Abs. 1 lit. c"


class allgemeinverbindlichkeit_befristet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Allgemeinverbindlicherklärung befristet ausgesprochen"
    reference = "SR 221.213.15 Art. 14 Abs. 2 lit. a"


class frist_abgelaufen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Frist der Allgemeinverbindlicherklärung abgelaufen"
    reference = "SR 221.213.15 Art. 14 Abs. 2 lit. a"


class geltungsdauer_vertrag_abgelaufen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Geltungsdauer des allgemeinverbindlich erklärten Vertrages abgelaufen"
    reference = "SR 221.213.15 Art. 14 Abs. 2 lit. b"


class allgemeinverbindlichkeit_ausser_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Allgemeinverbindlicherklärung wird ausser Kraft gesetzt"
    reference = "SR 221.213.15 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        antrag = person('antrag_aller_vertragsparteien_auf_ausserkraftsetzung', period)
        voraussetzungen = person('voraussetzungen_nicht_mehr_erfuellt', period)
        aufgeloest = person('vertrag_vorzeitig_aufgeloest', period)
        return antrag + voraussetzungen + aufgeloest


class allgemeinverbindlichkeit_dahingefallen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Allgemeinverbindlicherklärung fällt dahin"
    reference = "SR 221.213.15 Art. 14 Abs. 2"

    def formula(person, period, parameters):
        befristet = person('allgemeinverbindlichkeit_befristet', period)
        frist = person('frist_abgelaufen', period)
        geltungsdauer = person('geltungsdauer_vertrag_abgelaufen', period)
        return (befristet * frist) + geltungsdauer
