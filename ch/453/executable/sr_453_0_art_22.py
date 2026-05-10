"""SR 453.0 Art. 22

Generated from: ch/453/de/453.0.md
Ausnahmen - Gegenstaende zum privaten Gebrauch und Uebersiedlungsgut.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class exemplar_ist_nicht_lebend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exemplar ist nicht lebend"
    reference = "SR 453.0 Art. 22 Abs. 1"


class ist_privater_gebrauch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exemplar ist Gegenstand zum privaten Gebrauch im Reiseverkehr"
    reference = "SR 453.0 Art. 22 Abs. 2"


class ist_uebersiedlungsgut(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exemplar ist Uebersiedlungsgut (Wohnsitzverlegung oder 1 Jahr im Ausland)"
    reference = "SR 453.0 Art. 22 Abs. 3"


class exemplar_rechtmaessigen_ursprungs(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exemplar ist rechtmaessigen Ursprungs"
    reference = "SR 453.0 Art. 22 Abs. 1"


class exemplar_anhang_i_im_ausland_erworben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exemplar Anhang I, ausserhalb des Aufenthaltsstaates erworben, wird dorthin eingefuehrt"
    reference = "SR 453.0 Art. 22 Abs. 4 Bst. a"


class exemplar_im_vorerwerb(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exemplar wurde im Vorerwerb erworben (vor CITES-Anwendung)"
    reference = "SR 453.0 Art. 22 Abs. 5"


class ausnahme_bewilligungspflicht_privat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausnahme von Bewilligungs- und Anmeldepflicht fuer privaten Gebrauch/Uebersiedlung"
    reference = "SR 453.0 Art. 22"

    def formula(person, period, parameters):
        nicht_lebend = person('exemplar_ist_nicht_lebend', period)
        privat = person('ist_privater_gebrauch', period)
        uebersiedlung = person('ist_uebersiedlungsgut', period)
        rechtmaessig = person('exemplar_rechtmaessigen_ursprungs', period)
        anhang_i_ausland = person('exemplar_anhang_i_im_ausland_erworben', period)
        vorerwerb = person('exemplar_im_vorerwerb', period)

        grundsatz = nicht_lebend * (privat + uebersiedlung) * rechtmaessig

        # Abs. 4a: Ausnahme gilt NICHT fuer Anhang I im Ausland erworben
        # Abs. 5: Vorerwerb hebt Einschraenkung auf
        einschraenkung = anhang_i_ausland * not_(vorerwerb)

        return grundsatz * not_(einschraenkung)
