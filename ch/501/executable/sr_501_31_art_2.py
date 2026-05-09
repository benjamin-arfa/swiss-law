"""SR 501.31 Art. 2 - Planung des Mitteleinsatzes

Generated from: ch/501/de/501.31.md

Die KSD-Partner planen und bereiten den Einsatz der verfuegbaren Mittel
fuer alle Lagen vor.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ksd_mitteleinsatz_geplant(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Einsatz der verfuegbaren Mittel fuer alle Lagen geplant und vorbereitet ist"
    reference = "SR 501.31 Art. 2"

    def formula(person, period, parameters):
        return person('ist_ksd_partner', period)
