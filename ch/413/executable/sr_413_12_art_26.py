"""SR 413.12 Art. 26

Generated from: ch/413/de/413.12.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_erster_pruefungsversuch(Variable):
    """Ob dies der erste Pruefungsversuch ist"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erster Pruefungsversuch"
    reference = "SR 413.12 Art. 26 Abs. 1"
    default_value = True


class recht_auf_wiederholung(Variable):
    """Ob das Recht auf einen zweiten Pruefungsversuch besteht"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Recht auf Wiederholung der Pruefung"
    reference = "SR 413.12 Art. 26 Abs. 1"

    def formula(person, period, parameters):
        erster_versuch = person('ist_erster_pruefungsversuch', period)
        # Recht auf zweiten Versuch nach Ablegen der Gesamt-/beider Teilpruefungen
        return erster_versuch


class jahre_seit_erstem_versuch(Variable):
    """Anzahl Jahre seit Abschluss des ersten Pruefungsversuchs"""
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahre seit erstem Pruefungsversuch"
    reference = "SR 413.12 Art. 26 Abs. 3"


class noten_noch_gueltig(Variable):
    """Ob Noten >= 4 vom ersten Versuch noch gueltig sind (2-Jahres-Frist)"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Noten ab 4 vom ersten Versuch noch gueltig"
    reference = "SR 413.12 Art. 26 Abs. 3"

    def formula(person, period, parameters):
        jahre = person('jahre_seit_erstem_versuch', period)
        return jahre <= 2


class muss_maturaarbeit_wiederholen(Variable):
    """Ob die Maturaarbeit wiederholt werden muss (Note < 4 beim ersten Versuch)"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Maturaarbeit muss wiederholt werden"
    reference = "SR 413.12 Art. 26 Abs. 3"

    def formula(person, period, parameters):
        note = person('note_maturaarbeit', period)
        erster_versuch = person('ist_erster_pruefungsversuch', period)
        return (1 - erster_versuch) * (note < 4)
