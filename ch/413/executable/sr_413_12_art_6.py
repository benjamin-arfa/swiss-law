"""SR 413.12 Art. 6

Generated from: ch/413/de/413.12.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_im_pruefungsjahr(Variable):
    """Alter das die Person im Pruefungsjahr erreicht"""
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter im Pruefungsjahr"
    reference = "SR 413.12 Art. 6"


class hat_besondere_gruende_alter(Variable):
    """Ob besondere Gruende vorliegen (z.B. Zuzug aus Ausland)"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Besondere Gruende fuer Unterschreitung des Mindestalters"
    reference = "SR 413.12 Art. 6"
    default_value = False


class hat_sbfi_bewilligung_alter(Variable):
    """Ob SBFI-Bewilligung fuer juengere Kandidaten vorliegt"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SBFI-Bewilligung fuer juengere Kandidaten"
    reference = "SR 413.12 Art. 6"
    default_value = False


class zulassung_maturitaetspruefung_alter(Variable):
    """Ob die Altersbedingung fuer Zulassung zur Maturitaetspruefung erfuellt ist"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Altersbedingung fuer Zulassung zur Gesamtpruefung/zweiten Teilpruefung"
    reference = "SR 413.12 Art. 6"

    def formula(person, period, parameters):
        alter = person('alter_im_pruefungsjahr', period)
        besondere_gruende = person('hat_besondere_gruende_alter', period)
        sbfi_bewilligung = person('hat_sbfi_bewilligung_alter', period)
        # Mindestens 18 Jahre alt im Pruefungsjahr
        alter_genuegend = alter >= 18
        # Oder: besondere Gruende + SBFI-Bewilligung
        ausnahme = besondere_gruende * sbfi_bewilligung
        return alter_genuegend + ausnahme * (1 - alter_genuegend)
