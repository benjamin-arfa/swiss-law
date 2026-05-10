"""SR 235.1 Art. 11a

Generated from: ch/235/de/235.1.md

Register der Datensammlungen: Meldepflicht fuer Datensammlungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_inhaber_ist_bundesorgan(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Inhaber der Datensammlung ist ein Bundesorgan"
    reference = "SR 235.1 Art. 11a Abs. 2"


class dsg_regelmaessig_besonders_schuetzenswert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Regelmaessig besonders schuetzenswerte Personendaten oder Persoenlichkeitsprofile werden bearbeitet"
    reference = "SR 235.1 Art. 11a Abs. 3 lit. a"


class dsg_regelmaessig_bekanntgabe_dritte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Regelmaessig Personendaten an Dritte bekannt gegeben"
    reference = "SR 235.1 Art. 11a Abs. 3 lit. b"


class dsg_gesetzliche_bearbeitungspflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten werden aufgrund gesetzlicher Verpflichtung bearbeitet (private Personen)"
    reference = "SR 235.1 Art. 11a Abs. 5 lit. a"


class dsg_datenschutzverantwortlicher_bestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Unabhaengiger Datenschutzverantwortlicher wurde bezeichnet"
    reference = "SR 235.1 Art. 11a Abs. 5 lit. e"


class dsg_datenschutz_qualitaetszeichen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Datenschutz-Qualitaetszeichen durch Zertifizierung erworben"
    reference = "SR 235.1 Art. 11a Abs. 5 lit. f"


class dsg_meldepflicht_datensammlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Datensammlung muss beim Beauftragten angemeldet werden"
    reference = "SR 235.1 Art. 11a"

    def formula(person, period, parameters):
        bundesorgan = person('dsg_inhaber_ist_bundesorgan', period)
        besonders = person('dsg_regelmaessig_besonders_schuetzenswert', period)
        dritte = person('dsg_regelmaessig_bekanntgabe_dritte', period)
        gesetzl = person('dsg_gesetzliche_bearbeitungspflicht', period)
        dsv = person('dsg_datenschutzverantwortlicher_bestellt', period)
        qual = person('dsg_datenschutz_qualitaetszeichen', period)

        # Bundesorgane: immer meldepflichtig (Abs. 2)
        # Private: meldepflichtig wenn Abs. 3 a oder b (Abs. 3)
        # Ausnahmen Abs. 5: gesetzl. Pflicht, DSV bestellt, Qualitaetszeichen
        privat_pflichtig = not_(bundesorgan) * (besonders + dritte > 0)
        ausnahme = gesetzl + dsv + qual > 0
        privat_meldepflichtig = privat_pflichtig * not_(ausnahme)

        return bundesorgan + privat_meldepflichtig > 0
