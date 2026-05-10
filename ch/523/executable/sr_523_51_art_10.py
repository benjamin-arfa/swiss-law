"""SR 523.51 Art. 10

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class modul_durchschnittsnote(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Arithmetisches Mittel der Einzelleistungen des Moduls (gerundet auf halbe oder ganze Note)"
    reference = "SR 523.51 Art. 10 Abs. 1"


class praktikumsnote(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Note fuer das Praktikum"
    reference = "SR 523.51 Art. 10 Abs. 1"


class modul_erfolgreich_besucht(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Modul gilt als erfolgreich besucht"
    reference = "SR 523.51 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        durchschnitt = person('modul_durchschnittsnote', period)
        praktikum = person('praktikumsnote', period)
        # Pass if average >= 4.0 AND practical grade >= 4.0
        return (durchschnitt >= 4.0) * (praktikum >= 4.0)


class modul_kreditpunkte(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Kreditpunkte fuer das Modul (nur bei Erfolg vergeben)"
    reference = "SR 523.51 Art. 10 Abs. 2-3"

    def formula(person, period, parameters):
        erfolgreich = person('modul_erfolgreich_besucht', period)
        kreditpunkte_gemaess_beschreibung = person('modul_kreditpunkte_beschreibung', period)
        return where(erfolgreich, kreditpunkte_gemaess_beschreibung, 0.0)


class modul_kreditpunkte_beschreibung(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Kreditpunkte gemaess Modulbeschreibung"
    reference = "SR 523.51 Art. 10 Abs. 2"
