"""SR 654.11 Art. 5 - Zuordnung laenderbezogener Berichte und Abrufverfahren

Generated from: ch/654/de/654.11.md

Cantons report UIDs to the ESTV within 2 months after year-end.
The ESTV assigns reports to cantons and provides online access
with two-factor authentication.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class kanton_uid_meldung_frist_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer die Meldung der UID durch die Kantone an die ESTV (Monate nach Jahresende)"
    reference = "SR 654.11 Art. 5 al. 1"
    default_value = 2


class bericht_kanton_zugeordnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der laenderbezogene Bericht wurde dem zustaendigen Kanton zugeordnet"
    reference = "SR 654.11 Art. 5 al. 2"


class abrufverfahren_zugaenglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bericht ist der kantonalen Steuerbehorde im Abrufverfahren zugaenglich"
    reference = "SR 654.11 Art. 5 al. 3"


class zwei_faktor_authentifizierung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zwei-Faktor-Authentifizierung mit physischem Merkmal ist erforderlich"
    reference = "SR 654.11 Art. 5 al. 4"
    default_value = True
