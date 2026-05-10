"""SR 194.11 Art. 1 - Staendige Aufgaben der Landeskommunikation

Generated from: ch/194/de/194.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class eda_unterstuetzt_interessenwahrung_im_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das EDA unterstuetzt die Interessenwahrung der Schweiz im Ausland mit Oeffentlichkeitsarbeit (Landeskommunikation)"
    reference = "SR 194.11 Art. 1 Abs. 1"


class foerderung_visibilitaet_schweiz_im_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Foerderung der Visibilitaet der Schweiz im Ausland"
    reference = "SR 194.11 Art. 1 Abs. 2 lit. a"


class erklaerung_politischer_positionen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erklaerung der politischen Anliegen und Positionen der Schweiz gegenueber auslaendischer Oeffentlichkeit"
    reference = "SR 194.11 Art. 1 Abs. 2 lit. b"


class pflege_beziehungsnetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aufbau und Pflege des Beziehungsnetzes zu Entscheidungstraegern und Meinungsfuehrern im Ausland"
    reference = "SR 194.11 Art. 1 Abs. 2 lit. c"


# Computed variables

class landeskommunikation_aufgabe_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Landeskommunikation umfasst mindestens eine der staendigen Aufgaben"
    reference = "SR 194.11 Art. 1 Abs. 2"

    def formula(self, period, parameters):
        visibilitaet = self('foerderung_visibilitaet_schweiz_im_ausland', period)
        positionen = self('erklaerung_politischer_positionen', period)
        beziehungen = self('pflege_beziehungsnetz', period)
        return visibilitaet + positionen + beziehungen > 0
