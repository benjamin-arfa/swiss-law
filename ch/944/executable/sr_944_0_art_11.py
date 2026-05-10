"""SR 944.0 Art. 11

Generated from: ch/944/de/944.0.md

Strafbare Handlungen:
- Busse bei vorsätzlichem Verstoss gegen Deklarationsvorschriften (Art. 4)
  oder gegen Auskunftspflicht (Art. 8 Abs. 2)
- Fahrlässiges Handeln: Busse bis 2000 CHF
- Besonders leichte Fälle: Verzicht auf Bestrafung möglich
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verstoesst_gegen_deklarationsvorschrift(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob gegen eine Deklarationsvorschrift nach Art. 4 verstossen wurde"
    reference = "SR 944.0 Art. 11 Abs. 1 Bst. a"


class verletzt_auskunftspflicht_kig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Auskunftspflicht nach Art. 8 Abs. 2 nicht erfüllt wurde"
    reference = "SR 944.0 Art. 11 Abs. 1 Bst. b"


class handelt_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Handlung vorsätzlich erfolgte"
    reference = "SR 944.0 Art. 11 Abs. 1"


class handelt_fahrlaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Handlung fahrlässig erfolgte"
    reference = "SR 944.0 Art. 11 Abs. 2"


class ist_besonders_leichter_fall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein besonders leichter Fall vorliegt"
    reference = "SR 944.0 Art. 11 Abs. 3"


class busse_kig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse nach KIG Art. 11"
    reference = "SR 944.0 Art. 11"

    def formula(person, period, parameters):
        import numpy as np
        deklaration = person('verstoesst_gegen_deklarationsvorschrift', period)
        auskunft = person('verletzt_auskunftspflicht_kig', period)
        vorsatz = person('handelt_vorsaetzlich', period)
        fahrlaessig = person('handelt_fahrlaessig', period)
        leicht = person('ist_besonders_leichter_fall', period)

        hat_verstoss = np.maximum(deklaration, auskunft)
        max_busse_fahrlaessig = parameters(period).sr_944_0.busse_fahrlaessig_max

        # Besonders leichte Fälle: keine Busse
        # Fahrlässig: max 2000 CHF
        # Vorsätzlich: Busse (unbeschränkt nach StGB-Grundsätzen, hier max markiert)
        busse = np.where(
            leicht, 0,
            np.where(
                fahrlaessig * hat_verstoss,
                max_busse_fahrlaessig,
                np.where(
                    vorsatz * hat_verstoss,
                    max_busse_fahrlaessig,  # Minimum; actual amount is judicial discretion
                    0
                )
            )
        )
        return busse
