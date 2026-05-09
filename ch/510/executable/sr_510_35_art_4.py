"""SR 510.35 Art. 4 - Sperrbefehl

Generated from: ch/510/de/510.35.md

Durch Sperrbefehl koennen einzelne Gebaeude, Haeusergruppen, ganze
Ortschaften, Gemeinden und groessere Gebiete seuchenpolizeilich
gesperrt werden. Der Sperrbefehl bestimmt die konkreten Einschraenkungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class sperrgebiet_nicht_belegbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Sperrgebiet von militaerischen Schulen und Kursen nicht belegt, betreten oder durchfahren werden darf"
    reference = "SR 510.35 Art. 4 Abs. 1 lit. a"


class truppen_duerfen_sperrgebiet_nicht_verlassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Truppen und Wehrmaenner im Sperrgebiet dieses nicht verlassen duerfen"
    reference = "SR 510.35 Art. 4 Abs. 1 lit. b"


class wehrmaenner_duerfen_nicht_einruecken(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob im Sperrgebiet wohnhafte Wehrmaenner nicht einruecken duerfen"
    reference = "SR 510.35 Art. 4 Abs. 1 lit. d"


class militaerpostverkehr_eingeschraenkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Militaerpostverkehr eingeschraenkt ist"
    reference = "SR 510.35 Art. 4 Abs. 1 lit. h"
