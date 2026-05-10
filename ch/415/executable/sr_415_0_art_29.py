"""SR 415.0 Art. 29

Generated from: ch/415/de/415.0.md

Gewerbliche Leistungen des BASPO.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class leistung_im_zusammenhang_mit_hauptaufgaben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbliche Leistung steht in engem Zusammenhang mit Hauptaufgaben des BASPO"
    reference = "SR 415.0 Art. 29 Abs. 1 Bst. a"


class leistung_beeintraechtigt_hauptaufgaben_nicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Leistung beeintraechtigt die Erfuellung der Hauptaufgaben nicht"
    reference = "SR 415.0 Art. 29 Abs. 1 Bst. b"


class leistung_erfordert_keine_bedeutenden_zusatzmittel(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Leistung erfordert keine bedeutenden zusaetzlichen Mittel"
    reference = "SR 415.0 Art. 29 Abs. 1 Bst. c"


# --- Computed variables ---

class baspo_gewerbliche_leistung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BASPO darf gewerbliche Leistung erbringen"
    reference = "SR 415.0 Art. 29 Abs. 1"

    def formula(person, period, parameters):
        zusammenhang = person('leistung_im_zusammenhang_mit_hauptaufgaben', period)
        nicht_beeintraechtigt = person('leistung_beeintraechtigt_hauptaufgaben_nicht', period)
        keine_zusatzmittel = person('leistung_erfordert_keine_bedeutenden_zusatzmittel', period)
        return zusammenhang * nicht_beeintraechtigt * keine_zusatzmittel
