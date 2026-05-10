"""SR 142.281.3 Art. 8

Generated from: ch/142/de/142.281.3.md

Berechnungsformel fuer die Platzkostenpauschale bei Umbauten:
1. Fuer jeden Bereich: Bereichsquadratmeter * Bereichspreis
2. Summe aller Produkte
3. Summe * Eingriffs- und Veraenderungsgrad
4. Produkt + Zuschlag Umgebung/Ausstattung + Sicherheitszuschlag * Eingriffs-/Veraenderungsgrad
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eingriffs_und_veraenderungsgrad(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eingriffs- und Veraenderungsgrad bei Umbauten (0 bis 1)"
    reference = "SR 142.281.3 Art. 8"


class platzkostenpauschale_umbau(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Platzkostenpauschale pro Haftplatz bei Umbau (CHF)"
    reference = "SR 142.281.3 Art. 8"

    def formula(person, period, parameters):
        summe = person('summe_bereichskosten_neubau', period)
        evg = person('eingriffs_und_veraenderungsgrad', period)
        zuschlag_umbau = person('zuschlag_umbau_umgebung_ausstattung', period)
        sicherheit = person('sicherheitszuschlag_pro_haftplatz', period)

        # Schritt 3: Summe * Eingriffs-/Veraenderungsgrad
        # Schritt 4: + Zuschlag + Sicherheitszuschlag * Grad
        return summe * evg + zuschlag_umbau + sicherheit * evg
