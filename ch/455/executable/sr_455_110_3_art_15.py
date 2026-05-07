"""SR 455.110.3 Art. 15

Generated from: ch/455/de/455.110.3.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class wasseroberflaeche_beschattet_anteil(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der beschatteten Wasseroberflaeche (0.0-1.0)"
    reference = "SR 455.110.3 Art. 15 Abs. 1"


class ist_wintermonat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aktueller Monat ist ein Wintermonat"
    reference = "SR 455.110.3 Art. 15 Abs. 1"


class wassertiefe_m(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Wassertiefe des Teiches in Metern"
    reference = "SR 455.110.3 Art. 15 Abs. 1"


class ufer_bestockt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewaesser hat bestocktes Ufer"
    reference = "SR 455.110.3 Art. 15 Abs. 1"


class fischbecken_beschattung_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beschattung der Wasseroberflaeche konform (min 10%) nach Art. 15 Abs. 1 SR 455.110.3"
    reference = "SR 455.110.3 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        anteil = person('wasseroberflaeche_beschattet_anteil', period)
        winter = person('ist_wintermonat', period)
        tiefe = person('wassertiefe_m', period)
        bestockt = person('ufer_bestockt', period)
        # Ausnahmen: Wintermonate, bestocktes Ufer, Tiefe > 2m
        ausnahme = winter + bestockt + (tiefe > 2.0)
        return (anteil >= 0.1) + ausnahme
