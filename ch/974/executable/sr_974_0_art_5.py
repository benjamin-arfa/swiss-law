"""SR 974.0 Art. 5

Generated from: ch/974/de/974.0.md

Ziele der Entwicklungszusammenarbeit:
- Unterstützt Entwicklungsländer bei der Verbesserung der Lebensbedingungen
- In erster Linie ärmere Entwicklungsländer, Regionen und Bevölkerungsgruppen
- Fördert: ländliche Entwicklung, Ernährungslage, Handwerk/Kleinindustrie,
  Arbeitsplätze, ökologisches/demografisches Gleichgewicht
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_entwicklungsland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Land als Entwicklungsland gilt"
    reference = "SR 974.0 Art. 5 Abs. 1"


class ist_aermeres_entwicklungsland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Land zu den ärmeren Entwicklungsländern gehört (Priorität)"
    reference = "SR 974.0 Art. 5 Abs. 2"


class foerderbereich(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Förderbereich: laendliche_entwicklung, ernaehrung, handwerk, arbeitsplaetze, oekologie"
    reference = "SR 974.0 Art. 5 Abs. 2"


class hat_prioritaet_fuer_foerderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Vorhaben Priorität für Förderung hat (ärmere Länder)"
    reference = "SR 974.0 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_aermeres_entwicklungsland', period)
