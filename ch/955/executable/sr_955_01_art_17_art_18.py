"""SR 955.01 Art. 17–18

Generated from: ch/955/de/955.01.md

Sorgfaltspflichten fuer Haendlerinnen und Haendler:
- Art. 17: Identifizierung der Vertragspartei (Name, Adresse,
  Geburtsdatum, Staatsangehoerigkeit) anhand amtlichen Ausweises.
  Vertretung: Stellvertreter muss Angaben machen.
- Art. 18: Feststellung wirtschaftlich berechtigte Person.
  Bei juristischen Personen: natuerliche Personen mit >=25%
  Stimmen/Kapital oder sonstige Kontrolle.
  Keine BO identifizierbar -> oberstes Leitungsmitglied.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gwv_haendler_identifizierung_erfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Identifizierung der Vertragspartei nach Art. 17 durchgefuehrt"
    reference = "SR 955.01 Art. 17"


class gwv_haendler_ausweis_kontrolliert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Amtlicher Ausweis mit Fotografie kontrolliert und kopiert"
    reference = "SR 955.01 Art. 17 Abs. 3"


class gwv_haendler_vertragspartei_ist_bo(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vertragspartei ist selbst wirtschaftlich berechtigt"
    reference = "SR 955.01 Art. 18 Abs. 1"


class gwv_bo_beteiligung_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Beteiligung der wirtschaftlich berechtigten Person (Prozent)"
    reference = "SR 955.01 Art. 18 Abs. 2 lit. b Ziff. 1"


class gwv_haendler_bo_festgestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Wirtschaftlich berechtigte Person korrekt festgestellt"
    reference = "SR 955.01 Art. 18"

    def formula(person, period, parameters):
        ist_bo = person('gwv_haendler_vertragspartei_ist_bo', period)
        beteiligung = person('gwv_bo_beteiligung_prozent', period)
        p = parameters(period).sr955_01

        # Art. 18 Abs. 2 lit. b: >=25% = wirtschaftlich berechtigt
        hat_qualif_beteiligung = beteiligung >= p.bo_beteiligung_schwelle  # 25.0

        return ist_bo + hat_qualif_beteiligung


class gwv_haendler_sorgfaltspflichten_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Haendler hat Sorgfaltspflichten nach Art. 17-18 erfuellt"
    reference = "SR 955.01 Art. 17–18"

    def formula(person, period, parameters):
        identifiziert = person('gwv_haendler_identifizierung_erfolgt', period)
        ausweis = person('gwv_haendler_ausweis_kontrolliert', period)
        bo = person('gwv_haendler_bo_festgestellt', period)

        return identifiziert * ausweis * bo
