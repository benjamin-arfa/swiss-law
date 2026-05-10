"""SR 641.10 Art. 30

Generated from: ch/641/de/641.10.md

Verjaehrung der Abgabeforderung:
1. Die Abgabeforderung verjaehrt fuenf Jahre nach Ablauf des Kalenderjahres,
   in dem sie entstanden ist.
2. Die Verjaehrung beginnt nicht / steht still wenn die Forderung
   sichergestellt oder gestundet ist oder kein Zahlungspflichtiger im Inland
   Wohnsitz hat.
3. Unterbrechung durch Anerkennung oder Amtshandlung.
4. Stillstand und Unterbrechung wirken gegenueber allen Zahlungspflichtigen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stg_abgabeforderung_entstehungsjahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Kalenderjahr, in dem die Abgabeforderung entstanden ist"
    reference = "SR 641.10 Art. 30 Abs. 1"


class stg_forderung_ist_sichergestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Abgabeforderung sichergestellt oder gestundet ist"
    reference = "SR 641.10 Art. 30 Abs. 2"


class stg_zahlungspflichtiger_im_inland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob mindestens ein Zahlungspflichtiger im Inland Wohnsitz hat"
    reference = "SR 641.10 Art. 30 Abs. 2"


class stg_verjaehrung_unterbrochen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Verjaehrung unterbrochen wurde (Anerkennung oder Amtshandlung)"
    reference = "SR 641.10 Art. 30 Abs. 3"


class stg_verjaehrung_steht_still(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Verjaehrung stillsteht"
    reference = "SR 641.10 Art. 30 Abs. 2"

    def formula(person, period, parameters):
        sichergestellt = person('stg_forderung_ist_sichergestellt', period)
        im_inland = person('stg_zahlungspflichtiger_im_inland', period)
        return sichergestellt + not_(im_inland) > 0


class stg_abgabeforderung_verjaehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Abgabeforderung verjaehrt ist"
    reference = "SR 641.10 Art. 30"

    def formula(person, period, parameters):
        entstehungsjahr = person('stg_abgabeforderung_entstehungsjahr', period)
        verjaehrungsfrist = parameters(period).sr_641_10.verjaehrungsfrist_jahre
        aktuelles_jahr = period.start.year

        # Verjaehrung tritt ein nach 5 Jahren nach Ablauf des Entstehungsjahres
        jahre_vergangen = aktuelles_jahr - entstehungsjahr
        frist_abgelaufen = jahre_vergangen > verjaehrungsfrist

        unterbrochen = person('stg_verjaehrung_unterbrochen', period.first_month)
        stillstand = person('stg_verjaehrung_steht_still', period.first_month)

        return frist_abgelaufen * not_(unterbrochen) * not_(stillstand)
