"""SR 919.118 Art. 10c

Generated from: ch/919/de/919.118.md

Methode zur Berechnung der Risiken durch den Einsatz von Pflanzenschutzmitteln.

Abs. 1: Gesamtrisiko = Summe der Einzelrisiken pro Wirkstoff.
Abs. 2: Risikowerte basieren auf Menge und Toxizitaet (Oberflaeche/Natur)
         bzw. Metabolitenbelastung (Grundwasser).
Abs. 3: Jaehrliche Berechnung:
  a. Oberflaechengewaesser: Risikowert * Flaeche * Expositionsfaktor
  b. Naturnahe Lebensraeume: Risikowert * Flaeche * Expositionsfaktor
  c. Grundwasser: Risikowert * Flaeche
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class psm_risikowert_wasserorganismen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Risikowert eines Wirkstoffs fuer Wasserorganismen"
    reference = "SR 919.118 Art. 10c Abs. 2 Bst. a"


class psm_risikowert_nichtzielorganismen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Risikowert eines Wirkstoffs fuer Nichtzielorganismen"
    reference = "SR 919.118 Art. 10c Abs. 2 Bst. a"


class psm_risikowert_grundwasser(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Risikowert fuer potenzielle Metabolitenbelastung im Grundwasser"
    reference = "SR 919.118 Art. 10c Abs. 2 Bst. b"


class psm_behandelte_flaeche(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mit Pflanzenschutzmittel behandelte Flaeche (ha)"
    reference = "SR 919.118 Art. 10c Abs. 3"


class psm_expositionsfaktor(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Von Anwendungsbedingungen abhaengiger Expositionsfaktor"
    reference = "SR 919.118 Art. 10c Abs. 3"


class psm_risiko_oberflaechengewaesser(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliches Risiko fuer Oberflaechengewaesser pro Wirkstoff"
    reference = "SR 919.118 Art. 10c Abs. 3 Bst. a"

    def formula(person, period, parameters):
        risikowert = person('psm_risikowert_wasserorganismen', period)
        flaeche = person('psm_behandelte_flaeche', period)
        expositionsfaktor = person('psm_expositionsfaktor', period)
        return risikowert * flaeche * expositionsfaktor


class psm_risiko_naturnahe_lebensraeume(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliches Risiko fuer naturnahe Lebensraeume pro Wirkstoff"
    reference = "SR 919.118 Art. 10c Abs. 3 Bst. b"

    def formula(person, period, parameters):
        risikowert = person('psm_risikowert_nichtzielorganismen', period)
        flaeche = person('psm_behandelte_flaeche', period)
        expositionsfaktor = person('psm_expositionsfaktor', period)
        return risikowert * flaeche * expositionsfaktor


class psm_risiko_grundwasser(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliches Risiko fuer Grundwasser pro Wirkstoff"
    reference = "SR 919.118 Art. 10c Abs. 3 Bst. c"

    def formula(person, period, parameters):
        risikowert = person('psm_risikowert_grundwasser', period)
        flaeche = person('psm_behandelte_flaeche', period)
        return risikowert * flaeche
