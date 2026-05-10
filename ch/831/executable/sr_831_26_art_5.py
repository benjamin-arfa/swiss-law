"""SR 831.26 Art. 5

Generated from: ch/831/de/831.26.md

Recognition requirements for institutions:
a) Appropriate infrastructure, services, and qualified staff
b) Economically managed with standardized accounting
c) Transparent admission conditions
d) Written information to disabled persons and relatives
e) Respect personality rights (self-determination, privacy, etc.)
f) Remuneration for economically valuable work
g) Disability-related transport to/from workshops and day centres
h) Quality assurance
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class institution_hat_infrastruktur(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Institution verfuegt ueber beduerfnisgerechte Infrastruktur und Fachpersonal"
    reference = "SR 831.26 Art. 5 Abs. 1 Bst. a"


class institution_wirtschaftlich_gefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Institution wird wirtschaftlich mit einheitlicher Rechnungslegung gefuehrt"
    reference = "SR 831.26 Art. 5 Abs. 1 Bst. b"


class institution_aufnahmebedingungen_offen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufnahmebedingungen der Institution sind offengelegt"
    reference = "SR 831.26 Art. 5 Abs. 1 Bst. c"


class institution_schriftliche_information(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Institution informiert invalide Personen und Angehoerige schriftlich"
    reference = "SR 831.26 Art. 5 Abs. 1 Bst. d"


class institution_wahrt_persoenlichkeitsrechte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Institution wahrt Persoenlichkeitsrechte (Selbstbestimmung, Privatsphaere, etc.)"
    reference = "SR 831.26 Art. 5 Abs. 1 Bst. e"


class institution_entloehnt_invalide(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Institution entloehnt invalide Personen fuer wirtschaftlich verwertbare Taetigkeit"
    reference = "SR 831.26 Art. 5 Abs. 1 Bst. f"


class institution_sichert_transport(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Institution stellt behinderungsbedingte Fahrten sicher"
    reference = "SR 831.26 Art. 5 Abs. 1 Bst. g"


class institution_qualitaetssicherung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Institution gewaehrleistet Qualitaetssicherung"
    reference = "SR 831.26 Art. 5 Abs. 1 Bst. h"


class institution_anerkennungsvoraussetzungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Anerkennungsvoraussetzungen nach Art. 5 IFEG erfuellt sind"
    reference = "SR 831.26 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        infrastruktur = person('institution_hat_infrastruktur', period)
        wirtschaftlich = person('institution_wirtschaftlich_gefuehrt', period)
        aufnahme = person('institution_aufnahmebedingungen_offen', period)
        info = person('institution_schriftliche_information', period)
        rechte = person('institution_wahrt_persoenlichkeitsrechte', period)
        entlohnung = person('institution_entloehnt_invalide', period)
        transport = person('institution_sichert_transport', period)
        qualitaet = person('institution_qualitaetssicherung', period)

        return (
            infrastruktur * wirtschaftlich * aufnahme * info
            * rechte * entlohnung * transport * qualitaet
        )
