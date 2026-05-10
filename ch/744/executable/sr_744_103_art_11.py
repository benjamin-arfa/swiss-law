"""SR 744.103 Art. 11

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class original_zulassungsbewilligung_am_sitz_aufbewahrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Original der Zulassungsbewilligung wird vom Strassentransportunternehmen am Sitz aufbewahrt"
    reference = "SR 744.103 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_strassentransportunternehmen', period)


class kopie_zulassungsbewilligung_im_fahrzeug(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eine beglaubigte Kopie der Zulassungsbewilligung und die Fahrerbescheinigung werden im Fahrzeug mitgeführt"
    reference = "SR 744.103 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        im_konzessionierten_linienverkehr = person('fahrzeug_im_konzessionierten_linienverkehr', period)
        hat_beglaubigte_kopie = person('hat_beglaubigte_kopie_zulassungsbewilligung', period)
        hat_fahrerbescheinigung = person('hat_fahrerbescheinigung', period)
        return where(
            im_konzessionierten_linienverkehr,
            True,
            hat_beglaubigte_kopie * hat_fahrerbescheinigung
        )


class kopie_zulassungsbewilligung_vorweispflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beglaubigte Kopie der Zulassungsbewilligung und Fahrerbescheinigung sind den Kontrollorganen auf Verlangen vorzuweisen"
    reference = "SR 744.103 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        im_konzessionierten_linienverkehr = person('fahrzeug_im_konzessionierten_linienverkehr', period)
        return not_(im_konzessionierten_linienverkehr)


class fahrzeug_im_konzessionierten_linienverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Das Fahrzeug wird im konzessionierten Linienverkehr nach Art. 6 Bst. a der Verordnung über die Personenbeförderung eingesetzt (SR 745.11)"
    reference = "SR 744.103 Art. 11 Abs. 3"


class ist_strassentransportunternehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist ein Strassentransportunternehmen"
    reference = "SR 744.103 Art. 11"


class hat_beglaubigte_kopie_zulassungsbewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eine vom BAV oder von der zuständigen Behörde beglaubigte Kopie der Zulassungsbewilligung liegt im Fahrzeug vor"
    reference = "SR 744.103 Art. 11 Abs. 2"


class hat_fahrerbescheinigung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die Fahrerbescheinigung liegt im Fahrzeug vor"
    reference = "SR 744.103 Art. 11 Abs. 2"
