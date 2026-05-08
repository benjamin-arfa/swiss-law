"""SR 743.01 Art. 22

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Aufsichtsbehoerde.
BAV fuer Seilbahnen mit Bundeskonzession,
kantonale Behoerde fuer andere Seilbahnen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class seilbahn_aufsichtsbehoerde(Variable):
    value_type = str
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Zustaendige Aufsichtsbehoerde (BAV oder Kanton)"
    reference = "SR 743.01 Art. 22"

    def formula(organisation, period, parameters):
        import numpy as np
        bundeskonzession = organisation('seilbahn_bundeskonzession', period)
        return np.where(bundeskonzession, 'BAV', 'kanton')
