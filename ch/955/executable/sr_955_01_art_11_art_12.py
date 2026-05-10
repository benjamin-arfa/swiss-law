"""SR 955.01 Art. 11–12

Generated from: ch/955/de/955.01.md

Wechsel zur berufmaessigen Taetigkeit und SRO-Anschluss:
- Art. 11: Bei Wechsel zur berufmaessigen Taetigkeit: unverzueglich
  GwG-Pflichten einhalten; innert 2 Monaten SRO-Anschlussgesuch.
  Bis Anschluss: nur Handlungen zur Vermoegenserhaltung.
- Art. 12: Bei Austritt/Ausschluss aus SRO: innert 2 Monaten
  Gesuch bei anderer SRO. Taetigkeit nur im Rahmen bestehender
  Geschaeftsbeziehungen. Ohne Gesuch/Anschluss: Taetigkeitsverbot.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gwv_wechsel_zu_berufmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person wechselt von nicht-berufmaessig zu berufmaessig"
    reference = "SR 955.01 Art. 11 Abs. 1"


class gwv_austritt_aus_sro(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist aus SRO ausgetreten oder ausgeschlossen"
    reference = "SR 955.01 Art. 12 Abs. 1"


class gwv_hat_sro_anschluss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist an eine SRO angeschlossen"
    reference = "SR 955.01 Art. 11, 12"


class gwv_sro_anschluss_frist_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer SRO-Anschlussgesuch (Monate)"
    reference = "SR 955.01 Art. 11 Abs. 1 lit. b / Art. 12 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np

        p = parameters(period).sr955_01
        return np.full(person.count, p.sro_anschluss_frist_monate)


class gwv_darf_taetig_sein(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person darf als Finanzintermediar taetig sein"
    reference = "SR 955.01 Art. 11, 12"

    def formula(person, period, parameters):
        import numpy as np

        hat_anschluss = person('gwv_hat_sro_anschluss', period)
        wechsel = person('gwv_wechsel_zu_berufmaessig', period)
        austritt = person('gwv_austritt_aus_sro', period)

        # Ohne SRO-Anschluss: nur bei Wechsel/Austritt in Uebergangsphase
        uebergang = wechsel + austritt
        return hat_anschluss + (np.logical_not(hat_anschluss) * uebergang)
