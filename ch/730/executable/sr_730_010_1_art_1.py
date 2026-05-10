"""SR 730.010.1 Art. 1

Generated from: ch/730/fr/730.010.1.md

Art. 1 - Guarantee of origin for electricity:
1. Production period for recording electricity is 1 calendar month for
   installations >30 kVA (AC), or 1 month/quarter for others.
3. For fossil installations <=300 kVA commissioned before 2013-01-01
   with self-consumption <=20%, excess production may be recorded.
4. A guarantee of origin loses validity 12 months after the end of
   the corresponding production period (with spring extension rule).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ogom_periode_production_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Production recording period in months (1 for monthly, 3 for quarterly)"
    reference = "SR 730.010.1 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        puissance_kva = person('ogom_puissance_nominale_ca_kva', period)
        choix_trimestriel = person('ogom_choix_trimestriel', period)
        p = parameters(period).sr_730_010_1

        # >30 kVA: must be monthly (1 month)
        # <=30 kVA: monthly or quarterly at choice
        return where(
            puissance_kva > p.seuil_puissance_mensuelle_kva,
            1,
            where(choix_trimestriel, 3, 1)
        )


class ogom_puissance_nominale_ca_kva(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Nominal AC power of the installation (kVA)"
    reference = "SR 730.010.1 Art. 1"


class ogom_choix_trimestriel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the operator chose quarterly recording (only for <=30 kVA)"
    reference = "SR 730.010.1 Art. 1 Abs. 1"
    default_value = False


class ogom_excedent_fossile_admis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether fossil installation qualifies for excess production recording exception"
    reference = "SR 730.010.1 Art. 1 Abs. 3"

    def formula(person, period, parameters):
        puissance_raccordement_kva = person('ogom_puissance_raccordement_kva', period)
        mise_en_service_avant_2013 = person('ogom_mise_en_service_avant_2013', period)
        autoconsommation_pct = person('ogom_autoconsommation_pct', period)
        est_fossile = person('ogom_installation_fossile', period)
        p = parameters(period).sr_730_010_1

        return (
            est_fossile
            * mise_en_service_avant_2013
            * (puissance_raccordement_kva <= p.seuil_fossile_raccordement_kva)
            * (autoconsommation_pct <= p.seuil_fossile_autoconsommation_pct)
        )


class ogom_puissance_raccordement_kva(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Connection power of the installation (kVA)"
    reference = "SR 730.010.1 Art. 1 Abs. 3"


class ogom_mise_en_service_avant_2013(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the installation was commissioned before 1 January 2013"
    reference = "SR 730.010.1 Art. 1 Abs. 3"


class ogom_autoconsommation_pct(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Self-consumption as percentage of electricity produced (%)"
    reference = "SR 730.010.1 Art. 1 Abs. 3"


class ogom_installation_fossile(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the installation uses fossil energy sources"
    reference = "SR 730.010.1 Art. 1 Abs. 3"


class ogom_validite_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Validity duration of guarantee of origin in months after production period end"
    reference = "SR 730.010.1 Art. 1 Abs. 4"

    def formula(person, period, parameters):
        p = parameters(period).sr_730_010_1
        # Standard validity is 12 months; spring production gets extension to May next year
        return p.validite_go_mois + 0 * person('ogom_puissance_nominale_ca_kva', period)
