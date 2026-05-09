"""SR 941.216 Art. 5 — Verfahren für das Inverkehrbringen

Audiometrieverordnung — Verordnung über audiometrische Messmittel.
Generated from: ch/de/941/941.216.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class hat_ordentliche_zulassung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfügt über eine ordentliche Zulassung nach Anhang 5 der Messmittelverordnung"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_5"


class hat_ersteichung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat eine Ersteichung nach Anhang 5 der Messmittelverordnung durchlaufen"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_5"


class darf_in_verkehr_gebracht_werden_941_216(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Audiometer oder Hörprüfkabine darf in Verkehr gebracht werden (SR 941.216 Art. 5 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_5"

    def formula(person, period, parameters):
        # Art. 5 Abs. 1: Audiometer und Hörprüfkabinen bedürfen einer
        # ordentlichen Zulassung und einer Ersteichung.
        zulassung = person('hat_ordentliche_zulassung', period)
        eichung = person('hat_ersteichung', period)
        return zulassung * eichung


class ist_neue_hoerpruefkabine_installiert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine neue Hörprüfkabine wurde installiert"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_5"


class abnahmemessung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bei neuer Hörprüfkabine ist eine Abnahmemessung durch METAS oder Eichstelle erforderlich (SR 941.216 Art. 5 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_5"

    def formula(person, period, parameters):
        # Art. 5 Abs. 2: Bei Installation einer neuen Hörprüfkabine muss
        # Abnahmemessung durch METAS oder Eichstelle erfolgen.
        return person('ist_neue_hoerpruefkabine_installiert', period)
