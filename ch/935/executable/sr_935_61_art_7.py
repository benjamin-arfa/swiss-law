"""SR 935.61 Art. 7

Generated from: ch/935/de/935.61.md

Art. 7: Fachliche Voraussetzungen für den Registereintrag
- Anwaltspatent erforderlich
- Patent erfordert:
  a. juristisches Studium mit Lizentiat/Master einer CH-Hochschule oder
     gleichwertiges Diplom eines Staates mit gegenseitiger Anerkennung
  b. mindestens einjähriges Praktikum in der Schweiz, abgeschlossen mit Examen
- Für Zulassung zum Praktikum genügt Bachelor
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_anwaltspatent(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verfügt über ein kantonales Anwaltspatent"
    reference = "SR 935.61 Art. 7 Abs. 1"


class juristisches_studium_abgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Juristisches Studium mit Lizentiat oder Master einer schweizerischen "
        "Hochschule oder gleichwertigem Diplom abgeschlossen"
    )
    reference = "SR 935.61 Art. 7 Abs. 1 Bst. a"


class anwaltspraktikum_abgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Mindestens einjähriges Praktikum in der Schweiz mit Examen "
        "über theoretische und praktische juristische Kenntnisse abgeschlossen"
    )
    reference = "SR 935.61 Art. 7 Abs. 1 Bst. b"


class anwaltspraktikum_dauer_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer des Anwaltspraktikums in Monaten"
    reference = "SR 935.61 Art. 7 Abs. 1 Bst. b"


class anwaltspraktikum_examen_bestanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anwaltsprüfung (Praktikumsexamen) bestanden"
    reference = "SR 935.61 Art. 7 Abs. 1 Bst. b"


class fachliche_voraussetzungen_anwaltspatent(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fachliche Voraussetzungen für Anwaltspatent erfüllt (Art. 7 BGFA)"
    reference = "SR 935.61 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        studium = person('juristisches_studium_abgeschlossen', period)
        praktikum_dauer = person('anwaltspraktikum_dauer_monate', period)
        examen = person('anwaltspraktikum_examen_bestanden', period)
        min_monate = parameters(period).sr_935_61.min_praktikum_monate
        praktikum_ok = (praktikum_dauer >= min_monate) * examen
        return studium * praktikum_ok
