"""SR 672.933.21 Art. 3 — Beschaffung der Informationen

Art. 3: Bei Übergabe der Informationen erlässt die ESTV eine Schlussverfügung.
Bei Verweigerung erlässt sie eine Verfügung mit 3-Monats-Frist zur Herausgabe.

Generated from: ch/672/de/672.933.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_switzerland.entities import Person


class informationsinhaber_uebergibt_informationen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Informationsinhaber übergibt verlangte Informationen an ESTV (SR 672.933.21 Art. 3 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_3"


class schlussverfuegung_erlassen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "ESTV erlässt Schlussverfügung (SR 672.933.21 Art. 3 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_3"

    def formula(person, period, parameters):
        return person('informationsinhaber_uebergibt_informationen', period)


class verfuegung_herausgabe_3_monate(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "ESTV erlässt Verfügung zur Herausgabe innert 3 Monaten (SR 672.933.21 Art. 3 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_3"

    def formula(person, period, parameters):
        # Art. 3 Abs. 2: Bei Verweigerung durch Informationsinhaber oder betroffene Person
        # erlässt ESTV Verfügung mit 3-Monats-Frist.
        benachrichtigt = person('informationsinhaber_benachrichtigt', period)
        uebergibt = person('informationsinhaber_uebergibt_informationen', period)
        return benachrichtigt * (1 - uebergibt)
