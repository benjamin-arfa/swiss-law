"""SR 941.216 Art. 7 — Nacheichung von Hörprüfkabinen

Audiometrieverordnung — Verordnung über audiometrische Messmittel.
Generated from: ch/de/941/941.216.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class nacheichung_hoerpruefkabine_intervall_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Intervall für Nacheichung von Hörprüfkabinen in Jahren (SR 941.216 Art. 7 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_7"

    def formula(person, period, parameters):
        # Art. 7 Abs. 1: Die Nacheichung von Hörprüfkabinen erfolgt alle sechs Jahre.
        return 6


class hoerpruefkabine_baulich_veraendert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Hörprüfkabine wurde baulich verändert"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_7"


class neue_abnahmemessung_nach_baulicher_aenderung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Neue Abnahmemessung nach baulicher Veränderung der Hörprüfkabine erforderlich (SR 941.216 Art. 7 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_7"

    def formula(person, period, parameters):
        # Art. 7 Abs. 2: Wird die Hörprüfkabine baulich verändert, muss eine
        # neue Abnahmemessung nach Art. 5 Abs. 2 durchgeführt werden.
        ist_kabine = person('ist_hoerpruefkabine', period)
        veraendert = person('hoerpruefkabine_baulich_veraendert', period)
        return ist_kabine * veraendert


class ist_hoerpruefkabine(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine Hörprüfkabine"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_7"
