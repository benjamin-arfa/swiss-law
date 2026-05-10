"""SR 742.101 Art. 6

Generated from: ch/742/de/742.101.md

Erteilung, Aenderung und Erneuerung der Infrastrukturkonzession:
- Abs. 1: Bundesrat erteilt Konzession bei oeffentlichem Interesse oder
  eigenwirtschaftlichem Betrieb.
- Abs. 2: Zusaetzliche Voraussetzungen: keine entgegenstehenden oeffentlichen
  Interessen, Erschliessungsfunktion, Handelsregistereintrag.
- Abs. 5: Konzession wird fuer hoechstens 50 Jahre erteilt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class oeffentliches_interesse_infrastruktur(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein oeffentliches Interesse am Bau und Betrieb der Infrastruktur besteht"
    reference = "SR 742.101 Art. 6 Abs. 1 Bst. a"


class eigenwirtschaftlicher_betrieb_erwartet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein eigenwirtschaftlicher Betrieb erwartet werden kann"
    reference = "SR 742.101 Art. 6 Abs. 1 Bst. b"


class wesentliche_oeffentliche_interessen_entgegen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob wesentliche oeffentliche Interessen (Raumplanung, Umwelt, etc.) entgegenstehen"
    reference = "SR 742.101 Art. 6 Abs. 2 Bst. a"


class erfuellt_erschliessungsvoraussetzungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Erschliessungsvoraussetzungen nach Art. 11 PBG erfuellt sind"
    reference = "SR 742.101 Art. 6 Abs. 2 Bst. b"


class im_handelsregister_eingetragen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen im Handelsregister eingetragen ist"
    reference = "SR 742.101 Art. 6 Abs. 2 Bst. c"


class konzession_grundvoraussetzung_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Grundvoraussetzung fuer die Konzessionserteilung erfuellt ist (Art. 6 Abs. 1)"
    reference = "SR 742.101 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        oeffentlich = person('oeffentliches_interesse_infrastruktur', period)
        eigenwirtschaftlich = person('eigenwirtschaftlicher_betrieb_erwartet', period)
        return oeffentlich + eigenwirtschaftlich > 0


class konzession_zusatzvoraussetzungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die zusaetzlichen Voraussetzungen fuer die Konzessionserteilung erfuellt sind (Art. 6 Abs. 2)"
    reference = "SR 742.101 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        keine_entgegenstehenden = np.logical_not(
            person('wesentliche_oeffentliche_interessen_entgegen', period)
        )
        erschliessung = person('erfuellt_erschliessungsvoraussetzungen', period)
        handelsregister = person('im_handelsregister_eingetragen', period)
        return keine_entgegenstehenden * erschliessung * handelsregister


class infrastrukturkonzession_erteilbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Infrastrukturkonzession erteilt werden kann"
    reference = "SR 742.101 Art. 6"

    def formula(person, period, parameters):
        grund = person('konzession_grundvoraussetzung_erfuellt', period)
        zusatz = person('konzession_zusatzvoraussetzungen_erfuellt', period)
        return grund * zusatz


class konzession_maximale_dauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Dauer der Infrastrukturkonzession (Jahre)"
    reference = "SR 742.101 Art. 6 Abs. 5"

    def formula(person, period, parameters):
        return parameters(period).sr_742_101.konzession_max_dauer_jahre
