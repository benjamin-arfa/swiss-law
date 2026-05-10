"""SR 211.412.110 Art. 2a

Generated from: ch/211/fr/211.412.110.md

Standard labor unit (UMOS) calculation: various factors per hectare/animal
for agricultural enterprises. Processing supplement 0.05 UMOS per 10,000 CHF.
Near-agriculture supplement capped at 0.4 UMOS. Minimum 0.8 UMOS required.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class odfr_surface_pommes_de_terre_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Surface de culture de pommes de terre en hectares"
    reference = "SR 211.412.110 Art. 2a al. 2 let. c"


class odfr_surface_petits_fruits_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Surface de petits fruits, baies, plantes medicinales et aromatiques en ha"
    reference = "SR 211.412.110 Art. 2a al. 2 let. d"


class odfr_surface_viticulture_vinification_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Surface de viticulture avec vinification en ha"
    reference = "SR 211.412.110 Art. 2a al. 2 let. e"


class odfr_surface_serres_fondations_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Surface de serres reposant sur des fondations permanentes en ha"
    reference = "SR 211.412.110 Art. 2a al. 2 let. f"


class odfr_surface_tunnels_chassis_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Surface de tunnels ou chassis en ha"
    reference = "SR 211.412.110 Art. 2a al. 2 let. g"


class odfr_surface_foret_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Surface de foret faisant partie de l'exploitation en ha"
    reference = "SR 211.412.110 Art. 2a al. 2 let. n"


class odfr_prestation_brute_transformation_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prestation brute de transformation/stockage/vente produits propres en CHF"
    reference = "SR 211.412.110 Art. 2a al. 6"


class odfr_prestation_brute_activites_proches_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prestation brute d'activites proches de l'agriculture en CHF"
    reference = "SR 211.412.110 Art. 2a al. 7"


class odfr_umos_base(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "UMOS de base selon les facteurs OTerm (al. 1)"
    reference = "SR 211.412.110 Art. 2a al. 1"


class odfr_umos_supplements_cultures(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "UMOS supplementaires pour cultures speciales"
    reference = "SR 211.412.110 Art. 2a al. 2"

    def formula(person, period, parameters):
        pommes_de_terre = person('odfr_surface_pommes_de_terre_ha', period) * 0.039
        petits_fruits = person('odfr_surface_petits_fruits_ha', period) * 0.323
        viticulture = person('odfr_surface_viticulture_vinification_ha', period) * 0.323
        serres = person('odfr_surface_serres_fondations_ha', period) * 0.969
        tunnels = person('odfr_surface_tunnels_chassis_ha', period) * 0.485
        foret = person('odfr_surface_foret_ha', period) * 0.013
        return pommes_de_terre + petits_fruits + viticulture + serres + tunnels + foret


class odfr_umos_supplement_transformation(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "UMOS supplementaires pour transformation/stockage/vente (0.05 par 10000 CHF)"
    reference = "SR 211.412.110 Art. 2a al. 6"

    def formula(person, period, parameters):
        prestation = person('odfr_prestation_brute_transformation_chf', period)
        return (prestation / 10000) * 0.05


class odfr_umos_supplement_activites_proches(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "UMOS supplementaires pour activites proches agriculture (plafond 0.4 UMOS)"
    reference = "SR 211.412.110 Art. 2a al. 7"

    def formula(person, period, parameters):
        prestation = person('odfr_prestation_brute_activites_proches_chf', period)
        supplement = (prestation / 10000) * 0.05
        return min_(supplement, 0.4)


class odfr_umos_activites_principales(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "UMOS des activites principales (al. 1 a 6)"
    reference = "SR 211.412.110 Art. 2a al. 8"

    def formula(person, period, parameters):
        base = person('odfr_umos_base', period)
        cultures = person('odfr_umos_supplements_cultures', period)
        transformation = person('odfr_umos_supplement_transformation', period)
        return base + cultures + transformation


class odfr_supplement_activites_proches_applicable(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le supplement activites proches est applicable (min 0.8 UMOS activites principales)"
    reference = "SR 211.412.110 Art. 2a al. 8"

    def formula(person, period, parameters):
        return person('odfr_umos_activites_principales', period) >= 0.8


class odfr_umos_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "UMOS total de l'exploitation agricole"
    reference = "SR 211.412.110 Art. 2a"

    def formula(person, period, parameters):
        principales = person('odfr_umos_activites_principales', period)
        proches = person('odfr_umos_supplement_activites_proches', period)
        applicable = person('supplement_activites_proches_applicable', period)
        return principales + where(applicable, proches, 0)
