"""SR 857.51 Art. 2

Generated from: ch/857/de/857.51.md

Veroeffentlichung: Kantone veroeffentlichen Anerkennung und Verzeichnis
der Beratungsstellen. Das Bundesamt veroeffentlicht ein Gesamtverzeichnis.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class schwangerschaftsberatungsstelle_verzeichnis_veroeffentlicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hat der Kanton das Verzeichnis der anerkannten Beratungsstellen veroeffentlicht?"
    reference = "SR 857.51 Art. 2 Abs. 1"


class schwangerschaftsberatungsstelle_bundesamt_informiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Wurde die Anerkennung und das Verzeichnis dem Bundesamt fuer Gesundheit mitgeteilt?"
    reference = "SR 857.51 Art. 2 Abs. 2"


class schwangerschaftsberatungsstelle_gesamtverzeichnis_veroeffentlicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hat das Bundesamt das Gesamtverzeichnis der anerkannten Beratungsstellen veroeffentlicht?"
    reference = "SR 857.51 Art. 2 Abs. 3"
