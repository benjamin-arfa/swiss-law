"""SR 811.212 Art. 1

Generated from: ch/811/de/811.212.md

Gegenstand der GesBKV:
- Regelt berufsspezifische Kompetenzen für Gesundheitsberufe nach GesBG
- Periodische Überprüfung der Kompetenzen
- Erlass von Akkreditierungsstandards
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_gesundheitsberuf_nach_gesbg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Beruf ein Gesundheitsberuf nach GesBG ist"
    reference = "SR 811.212 Art. 1"


class studiengang_typ(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Typ des Studiengangs: pflege, physiotherapie, ergotherapie, hebamme, ernaehrung, optometrie, osteopathie"
    reference = "SR 811.212 Art. 2-8"


class hat_studienabschluss_gesbg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Studienabschluss nach GesBG vorliegt"
    reference = "SR 811.212 Art. 1 Bst. a"
