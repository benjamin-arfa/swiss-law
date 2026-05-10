"""SR 935.61 Art. 8

Generated from: ch/935/de/935.61.md

Art. 8: Persönliche Voraussetzungen für den Registereintrag
1. Erfordernisse:
   a. Handlungsfähigkeit
   b. Keine strafrechtliche Verurteilung wegen mit Anwaltsberuf unvereinbarer
      Handlungen (es sei denn nicht mehr im Privatauszug)
   c. Keine Verlustscheine
   d. Unabhängige Berufsausübung; Anstellung nur bei Personen die selbst
      im Register eingetragen sind
2. Ausnahme: Anstellung bei anerkannter gemeinnütziger Organisation möglich,
   wenn a-c erfüllt und Tätigkeit auf Organisationszweck beschränkt
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class anwalt_ist_handlungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anwältin/Anwalt ist handlungsfähig"
    reference = "SR 935.61 Art. 8 Abs. 1 Bst. a"


class anwalt_keine_relevante_verurteilung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Keine strafrechtliche Verurteilung wegen Handlungen, "
        "die mit dem Anwaltsberuf nicht zu vereinbaren sind "
        "(oder nicht mehr im Privatauszug des Strafregisters)"
    )
    reference = "SR 935.61 Art. 8 Abs. 1 Bst. b"


class anwalt_keine_verlustscheine(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Keine Verlustscheine vorhanden"
    reference = "SR 935.61 Art. 8 Abs. 1 Bst. c"


class anwalt_unabhaengige_berufsausuebung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "In der Lage, den Anwaltsberuf unabhängig auszuüben; "
        "Anstellung nur bei im Register eingetragenen Personen"
    )
    reference = "SR 935.61 Art. 8 Abs. 1 Bst. d"


class anwalt_bei_gemeinnuetziger_organisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Angestellt bei anerkannter gemeinnütziger Organisation"
    reference = "SR 935.61 Art. 8 Abs. 2"


class anwalt_taetigkeit_auf_organisationszweck_beschraenkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Parteivertretung beschränkt sich strikte auf Mandate "
        "im Rahmen des Organisationszwecks"
    )
    reference = "SR 935.61 Art. 8 Abs. 2"


class persoenliche_voraussetzungen_registereintrag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Persönliche Voraussetzungen für Registereintrag erfüllt (Art. 8 BGFA)"
    reference = "SR 935.61 Art. 8"

    def formula(person, period, parameters):
        handlungsfaehig = person('anwalt_ist_handlungsfaehig', period)
        keine_verurteilung = person('anwalt_keine_relevante_verurteilung', period)
        keine_verlustscheine = person('anwalt_keine_verlustscheine', period)
        unabhaengig = person('anwalt_unabhaengige_berufsausuebung', period)
        bei_ngo = person('anwalt_bei_gemeinnuetziger_organisation', period)
        auf_zweck_beschraenkt = person('anwalt_taetigkeit_auf_organisationszweck_beschraenkt', period)

        # Standard path: all four conditions (Abs. 1)
        standard = handlungsfaehig * keine_verurteilung * keine_verlustscheine * unabhaengig

        # NGO exception path: a-c plus NGO conditions (Abs. 2)
        ngo_path = (
            handlungsfaehig * keine_verurteilung * keine_verlustscheine *
            bei_ngo * auf_zweck_beschraenkt
        )

        return standard + ngo_path - (standard * ngo_path)  # logical OR
