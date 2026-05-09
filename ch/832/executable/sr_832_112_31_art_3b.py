"""SR 832.112.31 Art. 3b

Generated from: ch/832/de/832.112.31.md

Art. 3b: Verfahren zur Kostenuebernahme bei Fortsetzung der Therapie
nach 40 Sitzungen.
- Abs. 1: Soll die Psychotherapie nach 40 Sitzungen fortgesetzt werden,
  muss der Arzt dem Vertrauensarzt berichten (Art, Setting, Verlauf,
  Ergebnisse, Vorschlag zur Fortsetzung).
- Abs. 4: Der Versicherer teilt innerhalb von 15 Arbeitstagen nach
  Eingang des Berichts mit, ob die Kosten weiter uebernommen werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class klv_psychotherapie_vertrauensarzt_bericht_eingereicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bericht an Vertrauensarzt fuer Fortsetzung der Psychotherapie eingereicht"
    reference = "SR 832.112.31 Art. 3b Abs. 1"


class klv_psychotherapie_fortsetzung_bewilligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Fortsetzung der Psychotherapie durch Versicherer bewilligt"
    reference = "SR 832.112.31 Art. 3b Abs. 4"


class klv_psychotherapie_antwortfrist_arbeitstage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer Antwort des Versicherers in Arbeitstagen"
    reference = "SR 832.112.31 Art. 3b Abs. 4"

    def formula(person, period, parameters):
        # Art. 3b Abs. 4: Innerhalb von 15 Arbeitstagen
        return 15


class klv_psychotherapie_kostenuebernahme_nach_40(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kostenuebernahme fuer Psychotherapie nach 40 Sitzungen"
    reference = "SR 832.112.31 Art. 3b"

    def formula(person, period, parameters):
        sitzungen = person('klv_psychotherapie_sitzungen_absolviert', period.this_year)
        bericht = person('klv_psychotherapie_vertrauensarzt_bericht_eingereicht', period)
        bewilligt = person('klv_psychotherapie_fortsetzung_bewilligt', period)
        # Nach 40 Sitzungen: Bericht muss eingereicht und Fortsetzung bewilligt sein
        return (sitzungen >= 40) * bericht * bewilligt
