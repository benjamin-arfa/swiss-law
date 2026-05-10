"""SR 128.51 Art. 12

Generated from: ch/128/de/128.51.md

Ausnahmen von der Meldepflicht: Exemptions from the mandatory reporting
obligation based on size, type, and specific thresholds.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_hochschule(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation eine Hochschule nach Art. 74b Abs. 1 Bst. a ISG ist"
    reference = "SR 128.51 Art. 12 Abs. 1 Bst. a"


class anzahl_studierende(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Studierende der Hochschule"
    reference = "SR 128.51 Art. 12 Abs. 1 Bst. a"


class ist_energieunternehmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation ein Unternehmen nach Art. 74b Abs. 1 Bst. d ISG ist"
    reference = "SR 128.51 Art. 12 Abs. 1 Bst. b"


class muss_schutzniveau_a_oder_b_einhalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen Schutzniveau A oder B einhalten muss"
    reference = "SR 128.51 Art. 12 Abs. 1 Bst. b Ziff. 1"


class transportierte_energie_gwh(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Im Durchschnitt der letzten 5 Jahre transportierte Energie in GWh/Jahr"
    reference = "SR 128.51 Art. 12 Abs. 1 Bst. b Ziff. 2"


class ist_transportunternehmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation ein Eisenbahn-/Seilbahn-/Trolleybus-/Autobus-/Schifffahrtsunternehmen ist"
    reference = "SR 128.51 Art. 12 Abs. 1 Bst. c"


class hat_systemaufgaben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen mit Systemaufgaben nach Art. 37 EBG beauftragt ist"
    reference = "SR 128.51 Art. 12 Abs. 1 Bst. c Ziff. 1"


class erbringt_bestellte_angebote(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen durch Bund und Kantone bestellte Angebote erbringt"
    reference = "SR 128.51 Art. 12 Abs. 1 Bst. c Ziff. 2"


class infrastrukturkonzession_oeffentliches_interesse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Infrastrukturkonzession wegen oeffentlichem Interesse erteilt wurde"
    reference = "SR 128.51 Art. 12 Abs. 1 Bst. c Ziff. 3"


class anzahl_beschaeftigte_bereich(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl der im betroffenen Bereich beschaeftigten Personen"
    reference = "SR 128.51 Art. 12 Abs. 2"


class jahresumsatz_bereich_mio(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahresumsatz oder Jahresbilanzsumme im betroffenen Bereich in Mio. CHF"
    reference = "SR 128.51 Art. 12 Abs. 2"


class ist_behoerde_nach_art_74b_abs1_bst_ghlp(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation unter Art. 74b Abs. 1 Bst. g, h, l oder p ISG faellt"
    reference = "SR 128.51 Art. 12 Abs. 2"


class von_meldepflicht_ausgenommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation von der Meldepflicht ausgenommen ist"
    reference = "SR 128.51 Art. 12"

    def formula(person, period, parameters):
        import numpy as np

        # Hochschulen mit < 2000 Studierenden
        hochschule_ausnahme = person('ist_hochschule', period) * (person('anzahl_studierende', period) < 2000)

        # Energieunternehmen unter Schwelle
        energie_strom_ausnahme = (
            person('ist_energieunternehmen', period)
            * np.logical_not(person('muss_schutzniveau_a_oder_b_einhalten', period))
        )
        energie_gas_ausnahme = (
            person('ist_energieunternehmen', period)
            * (person('transportierte_energie_gwh', period) < 400)
        )

        # Transportunternehmen ohne Systemaufgaben etc.
        transport_ausnahme = (
            person('ist_transportunternehmen', period)
            * np.logical_not(person('hat_systemaufgaben', period))
            * np.logical_not(person('erbringt_bestellte_angebote', period))
            * np.logical_not(person('infrastrukturkonzession_oeffentliches_interesse', period))
        )

        # KMU-Ausnahme fuer Bst. g, h, l, p
        kmu_ausnahme = (
            person('ist_behoerde_nach_art_74b_abs1_bst_ghlp', period)
            * (person('anzahl_beschaeftigte_bereich', period) < 50)
            * (person('jahresumsatz_bereich_mio', period) < 10)
        )

        return (hochschule_ausnahme + energie_strom_ausnahme + energie_gas_ausnahme
                + transport_ausnahme + kmu_ausnahme) > 0
