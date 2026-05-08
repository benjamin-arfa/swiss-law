"""SR 816.11 Art. 1

Generated from: ch/816/de/816.11.md

Vertraulichkeitsstufen: Patientin/Patient kann medizinische Daten des
elektronischen Patientendossiers drei Vertraulichkeitsstufen zuordnen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


# Enum-like encoding: 1=normal, 2=eingeschraenkt, 3=geheim
class epd_vertraulichkeitsstufe(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Vertraulichkeitsstufe der medizinischen Daten (1=normal, 2=eingeschraenkt, 3=geheim)"
    reference = "SR 816.11 Art. 1 Abs. 1"


class hat_vertraulichkeitsstufe_gewaehlt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Patientin/der Patient eine Vertraulichkeitsstufe gewaehlt hat"
    reference = "SR 816.11 Art. 1 Abs. 2"


class epd_vertraulichkeitsstufe_effektiv(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Effektive Vertraulichkeitsstufe (Default: 1=normal zugaenglich)"
    reference = "SR 816.11 Art. 1"

    def formula(person, period, parameters):
        gewaehlt = person('hat_vertraulichkeitsstufe_gewaehlt', period)
        stufe = person('epd_vertraulichkeitsstufe', period)
        # Default ist 'normal zugaenglich' (1) wenn keine Zuordnung vorgenommen
        return gewaehlt * stufe + (1 - gewaehlt) * 1
