"""SR 141.0 Art. 38 - Einbezug von Kindern (Entlassung)

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unter_elterlicher_sorge_der_entlassenen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind steht unter der elterlichen Sorge der entlassenen Person"
    reference = "SR 141.0 Art. 38 Abs. 1 lit. a"


class kind_hat_keinen_aufenthalt_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind hat keinen Aufenthalt in der Schweiz"
    reference = "SR 141.0 Art. 38 Abs. 1 lit. b"


class kind_besitzt_andere_staatsangehoerigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind besitzt eine andere Staatsangehoerigkeit oder hat eine zugesichert bekommen"
    reference = "SR 141.0 Art. 38 Abs. 1 lit. c"


class kind_ueber_16_stimmt_zu(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Kind ueber 16 Jahren stimmt der Entlassung schriftlich zu"
    reference = "SR 141.0 Art. 38 Abs. 2"


class kind_wird_in_entlassung_einbezogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das minderjaehrige Kind wird in die Entlassung einbezogen"
    reference = "SR 141.0 Art. 38"

    def formula(self, period, parameters):
        sorge = self('unter_elterlicher_sorge_der_entlassenen', period)
        kein_aufenthalt = self('kind_hat_keinen_aufenthalt_schweiz', period)
        andere_staat = self('kind_besitzt_andere_staatsangehoerigkeit', period)
        alter = self('alter_des_kindes', period)
        zustimmung = self('kind_ueber_16_stimmt_zu', period)

        grundvoraussetzungen = sorge * kein_aufenthalt * andere_staat

        # Kinder ueber 16 brauchen Zustimmung
        unter_16 = alter < 16
        ueber_16_mit_zustimmung = (alter >= 16) * zustimmung

        return grundvoraussetzungen * (unter_16 + ueber_16_mit_zustimmung > 0)
