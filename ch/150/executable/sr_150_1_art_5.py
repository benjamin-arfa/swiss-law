"""SR 150.1 Art. 5

Generated from: ch/150/de/150.1.md

Zusammensetzung: 12 Mitglieder, Fachleute mit Kompetenzen in Medizin,
Psychiatrie, Recht, interkulturellem Bereich oder Freiheitsentzug.
Angemessene Vertretung beider Geschlechter und der Sprachregionen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class anzahl_kommissionsmitglieder(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Mitglieder der Kommission zur Verhuetung von Folter"
    reference = "SR 150.1 Art. 5 Abs. 1"
    default_value = 12
