"""SR 363.1 Art. 4a

Generated from: ch/363/de/363.1.md

Gebuehren im Zusammenhang mit der Anerkennung von Labors.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class labor_verfuegung_typ(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Typ der Verfuegung: erteilung, ablehnung, aenderung, sistierung, entzug"
    reference = "SR 363.1 Art. 4a Abs. 1"


class labor_verfuegung_gebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebuehr fuer die Verfuegung im Zusammenhang mit der Anerkennung (CHF)"
    reference = "SR 363.1 Art. 4a Abs. 1"

    def formula(person, period, parameters):
        typ = person('labor_verfuegung_typ', period)
        # Erteilung: 500, Ablehnung: 500, Aenderung: 200, Sistierung: 200, Entzug: 500
        gebuehr = select(
            [typ == 'erteilung', typ == 'ablehnung', typ == 'aenderung',
             typ == 'sistierung', typ == 'entzug'],
            [500.0, 500.0, 200.0, 200.0, 500.0],
            default=0.0
        )
        return gebuehr


class labor_aufsicht_stundensatz_administrativ(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Stundensatz fuer Mitarbeitende des administrativen Bereichs (CHF)"
    reference = "SR 363.1 Art. 4a Abs. 2 Bst. a"

    def formula(person, period, parameters):
        return person('labor_aufsicht_stundensatz_administrativ', period) * 0 + 97.0


class labor_aufsicht_stundensatz_fachlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Stundensatz fuer Mitarbeitende Planung/QM/DNA-Labor-Aufsicht (CHF)"
    reference = "SR 363.1 Art. 4a Abs. 2 Bst. b"

    def formula(person, period, parameters):
        return person('labor_aufsicht_stundensatz_fachlich', period) * 0 + 128.0
