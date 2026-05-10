"""SR 955.01 Art. 12a–12b

Generated from: ch/955/de/955.01.md

Verbot des Abbruchs und Abbruch der Geschaeftsbeziehung:
- Art. 12a: Kein Abbruch, wenn Meldepflicht-Voraussetzungen erfuellt.
  Verbot des Rueckzugs bedeutender Vermoegenswerte bei bevorstehenden
  behoerdlichen Sicherstellungsmassnahmen.
- Art. 12b: Abbruch moeglich wenn Meldestelle innert 40 Arbeitstagen
  Weiterleitung mitteilt und keine Verfuegung innert 5 Arbeitstagen.
  Oder wenn nach Meldung keine Verfuegung innert 5 Arbeitstagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gwv_hat_meldung_erstattet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Finanzintermediar hat Meldung nach Art. 9 GwG erstattet"
    reference = "SR 955.01 Art. 12a Abs. 1"


class gwv_behoerdliche_massnahmen_bevorstehend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Behoerdliche Sicherstellungsmassnahmen stehen bevor"
    reference = "SR 955.01 Art. 12a Abs. 2"


class gwv_darf_geschaeftsbeziehung_abbrechen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Geschaeftsbeziehung darf abgebrochen werden"
    reference = "SR 955.01 Art. 12a, 12b"

    def formula_2023(person, period, parameters):
        import numpy as np

        hat_gemeldet = person('gwv_hat_meldung_erstattet', period)
        massnahmen = person('gwv_behoerdliche_massnahmen_bevorstehend', period)

        # Art. 12a: Kein Abbruch bei Meldepflicht oder bevorstehenden Massnahmen
        verbot = hat_gemeldet + massnahmen
        return np.logical_not(verbot)


class gwv_meldestelle_mitteilung_frist_arbeitstage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer Mitteilung Meldestelle nach Meldung (Arbeitstage)"
    reference = "SR 955.01 Art. 12b Abs. 1 lit. a"

    def formula_2023(person, period, parameters):
        import numpy as np

        p = parameters(period).sr955_01
        return np.full(person.count, p.meldestelle_mitteilung_frist)


class gwv_strafverfolgung_verfuegung_frist_arbeitstage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer Verfuegung Strafverfolgung nach Mitteilung (Arbeitstage)"
    reference = "SR 955.01 Art. 12b Abs. 1 lit. a"

    def formula_2023(person, period, parameters):
        import numpy as np

        p = parameters(period).sr955_01
        return np.full(person.count, p.strafverfolgung_verfuegung_frist)
