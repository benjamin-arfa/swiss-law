"""SR 816.11 Art. 4

Generated from: ch/816/de/816.11.md

Optionen der Patientinnen und Patienten: Umfassende Kontrollmoeglichkeiten
ueber das elektronische Patientendossier.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_vertraulichkeitsstufe_festgelegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Patientin festgelegt hat, welcher Stufe neue Daten zugeordnet werden"
    reference = "SR 816.11 Art. 4 Bst. a"


class hat_fachperson_ausgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Patientin einzelne Gesundheitsfachpersonen vom Zugriff ausgeschlossen hat"
    reference = "SR 816.11 Art. 4 Bst. b"


class hat_stellvertretung_benannt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Patientin eine Stellvertretung fuer das EPD benannt hat"
    reference = "SR 816.11 Art. 4 Bst. f"


class hat_notfallzugriff_erweitert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Patientin den Notfallzugriff auf eingeschraenkt zugaengliche Daten erweitert hat"
    reference = "SR 816.11 Art. 4 Bst. e"


class hat_notfallzugriff_ausgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Patientin den Notfallzugriff vollstaendig ausgeschlossen hat"
    reference = "SR 816.11 Art. 4 Bst. e"
