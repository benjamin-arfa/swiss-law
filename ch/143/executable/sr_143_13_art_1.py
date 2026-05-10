"""SR 143.13 Art. 1

Generated from: ch/143/de/143.13.md

Pass 2010: EJPD introduces new passport on 1 March 2010.
From that date, only Pass 2010 may be issued.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class pass_2010_einfuehrungsdatum(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum der Einfuehrung des Passes 2010"
    reference = "SR 143.13 Art. 1 Abs. 1"
    default_value = "2010-03-01"


class nur_pass_2010_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ab 1. Maerz 2010 nur noch der Pass 2010 ausgestellt werden darf"
    reference = "SR 143.13 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        # After 1 March 2010, only Pass 2010 may be issued
        return True
