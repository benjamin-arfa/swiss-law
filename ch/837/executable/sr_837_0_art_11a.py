"""SR 837.0 Art. 11a

Generated from: ch/837/de/837.0.md

Art. 11a: Freiwillige Leistungen des Arbeitgebers bei Aufloesung des
Arbeitsverhaeltnisses (Voluntary employer benefits at termination)

Abs. 1: The loss of work is not countable as long as voluntary employer
benefits cover the loss of income resulting from the termination.

Abs. 2: Voluntary employer benefits are only considered insofar as they
exceed the annual maximum amount of insured income in mandatory accident
insurance (UVG maximum = CHF 148,200 as of 2024).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alv_freiwillige_leistungen_arbeitgeber(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Freiwillige Leistungen des Arbeitgebers bei Kuendigung (CHF)"
    reference = "SR 837.0 Art. 11a Abs. 1"


class alv_arbeitsausfall_durch_leistungen_gedeckt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitsausfall ist durch freiwillige Arbeitgeberleistungen gedeckt"
    reference = "SR 837.0 Art. 11a Abs. 1"


class alv_anrechenbare_freiwillige_leistungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare freiwillige Leistungen (nur Betrag ueber UVG-Hoechstbetrag)"
    reference = "SR 837.0 Art. 11a Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        leistungen = person('alv_freiwillige_leistungen_arbeitgeber', period)
        # Only amounts exceeding UVG maximum are considered (CHF 148,200)
        uvg_max = 148200.0
        return np.maximum(leistungen - uvg_max, 0.0)


class alv_wartefrist_freiwillige_leistungen_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Tage Wartefrist wegen freiwilliger Arbeitgeberleistungen"
    reference = "SR 837.0 Art. 11a"

    def formula(person, period, parameters):
        import numpy as np
        anrechenbar = person('alv_anrechenbare_freiwillige_leistungen', period)
        verdienst = person('alv_versicherter_verdienst', period)

        # Days covered = anrechenbare amount / daily insured income
        tagesverdienst = np.maximum(verdienst / 260.0, 1.0)  # avoid division by zero
        tage = np.floor(anrechenbar / tagesverdienst)
        return tage.astype(int)
