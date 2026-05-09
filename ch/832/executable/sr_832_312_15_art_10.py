"""SR 832.312.15 Art. 10 – Erteilung des Kranführerausweises

Generated from: ch/832/de/832.312.15.md

Kranführerausweis (Kategorie A oder B) wird erteilt an Personen die:
a) das 18. Altersjahr vollendet haben
b) körperlich/geistig geeignet sind
c) die Ausbildung nach Art. 12 oder gleichwertige Ausbildung abgeschlossen haben
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

MINDESTALTER_KRANFUEHRERAUSWEIS = 18


class ausbildung_kranfuehrer_abgeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ausbildung zur Kranführerin/zum Kranführer nach Art. 12 oder gleichwertig abgeschlossen"
    reference = "SR 832.312.15 Art. 10 lit. c"


class anspruch_kranfuehrerausweis(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Erfüllt Voraussetzungen für einen Kranführerausweis"
    reference = "SR 832.312.15 Art. 10"

    def formula(person, period, parameters):
        alter = person('alter_jahre', period.this_year)
        geeignet = person('koerperlich_geistig_geeignet_kran', period.this_year)
        ausbildung = person('ausbildung_kranfuehrer_abgeschlossen', period)

        return (alter >= MINDESTALTER_KRANFUEHRERAUSWEIS) * geeignet * ausbildung
