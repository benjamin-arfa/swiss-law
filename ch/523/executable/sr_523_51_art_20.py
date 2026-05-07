"""SR 523.51 Art. 20

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class anmeldung_frist_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anmeldung durch den Kanton bis Ende der Kalenderwoche 41 erfolgt"
    reference = "SR 523.51 Art. 20 Abs. 1"


class anmeldung_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anmeldung ist gueltig (Zulassungsbedingungen erfuellt)"
    reference = "SR 523.51 Art. 20 Abs. 2"

    def formula(person, period, parameters):
        frist = person('anmeldung_frist_eingehalten', period)
        zulassung = person('zulassungsbedingungen_erfuellt', period)
        return frist * zulassung


class zulassungsbedingungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zulassungsbedingungen fuer das Modul sind erfuellt"
    reference = "SR 523.51 Art. 20 Abs. 2"
