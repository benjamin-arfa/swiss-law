"""SR 641.10 Art. 17

Generated from: ch/641/de/641.10.md

Umsatzabgabe - Abgabepflicht:
1. Abgabepflichtig ist der Effektenhaendler.
2. Er schuldet eine halbe Abgabe:
   a. wenn er vermittelt: fuer jede Vertragspartei, die sich nicht als
      registrierter Effektenhaendler oder befreiter Anleger ausweist
   b. wenn er Vertragspartei ist: fuer sich selbst und die Gegenpartei
3. Der Effektenhaendler gilt als Vermittler wenn er zu Originalbedingungen
   abrechnet, Gelegenheit nachweist, oder Urkunden am Tag des Erwerbs
   weiterveaeussert.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stg_ist_effektenhaendler(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person ein Effektenhaendler nach Art. 13 Abs. 3 ist"
    reference = "SR 641.10 Art. 13 Abs. 3"


class stg_ist_vermittler(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Effektenhaendler als Vermittler gilt (Art. 17 Abs. 3)"
    reference = "SR 641.10 Art. 17 Abs. 3"


class stg_gegenpartei_ist_registriert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Gegenpartei ein registrierter Effektenhaendler oder befreiter Anleger ist"
    reference = "SR 641.10 Art. 17 Abs. 2"


class stg_anzahl_nicht_registrierte_parteien(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl nicht-registrierter Vertragsparteien (0, 1 oder 2)"
    reference = "SR 641.10 Art. 17 Abs. 2"


class stg_umsatzabgabe_halbe_abgaben(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl halber Abgaben, die der Effektenhaendler schuldet"
    reference = "SR 641.10 Art. 17 Abs. 2"

    def formula(person, period, parameters):
        ist_effektenhaendler = person('stg_ist_effektenhaendler', period)
        ist_vermittler = person('stg_ist_vermittler', period)
        gegenpartei_registriert = person('stg_gegenpartei_ist_registriert', period)
        anzahl_nicht_reg = person('stg_anzahl_nicht_registrierte_parteien', period)

        # Vermittler: eine halbe Abgabe pro nicht-registrierte Partei
        halbe_als_vermittler = anzahl_nicht_reg * 1.0

        # Vertragspartei: halbe Abgabe fuer sich + halbe fuer Gegenpartei
        # wenn Gegenpartei nicht registriert
        halbe_als_partei = 1.0 + where(gegenpartei_registriert, 0, 1.0)

        return ist_effektenhaendler * where(
            ist_vermittler,
            halbe_als_vermittler,
            halbe_als_partei
        )


class stg_umsatzabgabe_geschuldet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Vom Effektenhaendler geschuldete Umsatzabgabe (CHF)"
    reference = "SR 641.10 Art. 17"

    def formula(person, period, parameters):
        halbe_abgaben = person('stg_umsatzabgabe_halbe_abgaben', period)
        volle_abgabe = person('stg_umsatzabgabe_betrag', period)
        return halbe_abgaben * volle_abgabe * 0.5
