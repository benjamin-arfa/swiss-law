"""SR 822.11 Art. 20a

Generated from: ch/822/de/822.11.md

Art. 20a: Feiertage
- Abs. 1: Bundesfeiertag ist den Sonntagen gleichgestellt; Kantone koennen
  max. 8 weitere Feiertage den Sonntagen gleichstellen
- Abs. 2: AN hat das Recht, an nicht kantonal anerkannten religioesen
  Feiertagen die Arbeit auszusetzen (Anzeige 3 Tage im Voraus)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arg_kantonale_feiertage_anzahl(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    default_value = 8
    label = "Anzahl kantonale Feiertage die Sonntagen gleichgestellt sind (max. 8)"
    reference = "SR 822.11 Art. 20a Abs. 1"


class arg_kantonale_feiertage_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl kantonaler Feiertage liegt innerhalb des gesetzlichen Rahmens"
    reference = "SR 822.11 Art. 20a Abs. 1"

    def formula(person, period, parameters):
        anzahl = person('arg_kantonale_feiertage_anzahl', period)
        return anzahl <= 8


class arg_religioeser_feiertag_arbeit_ausgesetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Arbeitnehmer setzt Arbeit an religioeser Feier aus (Art. 20a Abs. 2)"
    reference = "SR 822.11 Art. 20a Abs. 2"


class arg_religioeser_feiertag_anzeige_frist_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Arbeitnehmer hat Vorhaben mindestens 3 Tage im Voraus angezeigt"
    reference = "SR 822.11 Art. 20a Abs. 2"


class arg_religioeser_feiertag_recht_auf_arbeitsaussetzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitnehmer hat Recht auf Arbeitsaussetzung an religioeser Feier"
    reference = "SR 822.11 Art. 20a Abs. 2"

    def formula(person, period, parameters):
        ausgesetzt = person('arg_religioeser_feiertag_arbeit_ausgesetzt', period)
        frist = person('arg_religioeser_feiertag_anzeige_frist_eingehalten', period)
        return ausgesetzt * frist
