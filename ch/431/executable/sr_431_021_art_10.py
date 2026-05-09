"""SR 431.021 Art. 10

Generated from: ch/431/de/431.021.md

Validierung der Daten fuer die Statistik - BFS betreibt Validierungsservice,
kontrolliert Vollstaendigkeit, Registerinhalt, Identifikatoren, EGID/EWID und Plausibilitaet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class datenlieferung_vollstaendig_validiert(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Vollstaendigkeit der Datenlieferung ist validiert"
    reference = "SR 431.021 Art. 10 Abs. 2 Bst. a"


class registerinhalt_vorhanden_validiert(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Registerinhalt nach Art. 6 RHG ist vorhanden"
    reference = "SR 431.021 Art. 10 Abs. 2 Bst. b"


class identifikatoren_korrekt_validiert(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Identifikatoren korrekt und Merkmalskatalog eingehalten"
    reference = "SR 431.021 Art. 10 Abs. 2 Bst. c"


class egid_korrekt_validiert(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "EGID korrekt und EWID plausibel gemaess GWR-Abgleich"
    reference = "SR 431.021 Art. 10 Abs. 2 Bst. d"


class personendaten_plausibel_validiert(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Plausibilitaet der Personendaten gemaess Plausibilisierungsregeln"
    reference = "SR 431.021 Art. 10 Abs. 2 Bst. e"


class validierung_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Alle Validierungspruefungen des BFS sind bestanden"
    reference = "SR 431.021 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('datenlieferung_vollstaendig_validiert', period) *
            person('registerinhalt_vorhanden_validiert', period) *
            person('identifikatoren_korrekt_validiert', period) *
            person('egid_korrekt_validiert', period) *
            person('personendaten_plausibel_validiert', period)
        )


class erneute_lieferung_verlangt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "BFS verlangt erneute Datenlieferung wegen Maengeln"
    reference = "SR 431.021 Art. 10 Abs. 5"

    def formula(person, period, parameters):
        return not_(person('validierung_bestanden', period))
