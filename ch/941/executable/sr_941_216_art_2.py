"""SR 941.216 Art. 2 — Geltungsbereich

Audiometrieverordnung — Verordnung über audiometrische Messmittel.
Generated from: ch/de/941/941.216.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_audiometer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein Audiometer (Messmittel zur Ermittlung der Hörschwelle, SR 941.216 Art. 2 lit. a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_2"


class ist_hoerpruefkabine(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine Hörprüfkabine (schallabsorbierend ausgekleidete Messkabine, SR 941.216 Art. 2 lit. b)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_2"


class verwendung_zu_gesundheitsrelevanten_zwecken(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wird für audiometrische Prüfungen zu gesundheitsrelevanten Zwecken verwendet"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_2"


class unterliegt_geltungsbereich_941_216(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterliegt dem Geltungsbereich der Audiometrieverordnung (SR 941.216 Art. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_2"

    def formula(person, period, parameters):
        # Art. 2: Unterstehen Messmittel für audiometrische Prüfungen zu
        # gesundheitsrelevanten Zwecken, namentlich Audiometer und Hörprüfkabinen.
        ist_audiometer = person('ist_audiometer', period)
        ist_kabine = person('ist_hoerpruefkabine', period)
        gesundheit = person('verwendung_zu_gesundheitsrelevanten_zwecken', period)
        return (ist_audiometer + ist_kabine > 0) * gesundheit
