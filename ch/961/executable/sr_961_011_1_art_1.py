"""SR 961.011.1 Art. 1, 5 — Fortune liée et réserves légales

Generated from: ch/961/fr/961.011.1.md

OS-FINMA — Tied assets supplement and legal reserves:
- Art. 1 al. 1: Tied assets supplement (debit):
  (a) Life insurance: 1% of technical provisions
  (b) Non-life insurance: 4% of technical provisions (min 100,000 CHF)
- Art. 1 al. 2: Supplement waived if insurer bears no investment risk (life only)
- Art. 5: Legal reserve attribution from profit:
  Life insurers: >= 10% of annual profit
  Other insurers: >= 20% of annual profit
  Until reserve fund reaches 50% of statutory capital
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class provisions_techniques_vie(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Provisions techniques (assurance sur la vie) retenues pour le débit (CHF)"
    reference = "SR 961.011.1 Art. 1 al. 1 let. a"


class provisions_techniques_dommages(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Provisions techniques (assurance dommages) selon OS Art. 68 al. 1 let. a et b (CHF)"
    reference = "SR 961.011.1 Art. 1 al. 1 let. b"


class supporte_risque_placement_vie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'entreprise supporte un risque de placement (assurance vie)"
    reference = "SR 961.011.1 Art. 1 al. 2"


class supplement_fortune_liee(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Supplément de fortune liée (CHF)"
    reference = "SR 961.011.1 Art. 1"

    def formula(person, period, parameters):
        p = parameters(period).sr_961_011_1
        prov_vie = person('provisions_techniques_vie', period)
        prov_dom = person('provisions_techniques_dommages', period)
        risque_placement = person('supporte_risque_placement_vie', period)

        # Life: 1% (waived if no investment risk)
        sup_vie = prov_vie * p.taux_supplement_vie * risque_placement

        # Non-life: 4% but minimum 100,000 CHF
        import numpy
        sup_dom_calc = prov_dom * p.taux_supplement_dommages
        sup_dom = numpy.where(
            prov_dom > 0,
            numpy.maximum(sup_dom_calc, p.minimum_supplement_dommages),
            0.0
        )

        return sup_vie + sup_dom


class est_assureur_vie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Exploite l'assurance sur la vie"
    reference = "SR 961.011.1 Art. 5"


class benefice_annuel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bénéfice annuel de l'entreprise d'assurance (CHF)"
    reference = "SR 961.011.1 Art. 5"


class fonds_reserve_actuel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Fonds de réserve légal actuel (CHF)"
    reference = "SR 961.011.1 Art. 5"


class capital_statutaire(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Capital statutaire de l'entreprise (CHF)"
    reference = "SR 961.011.1 Art. 5"


class attribution_reserve_legale_minimum(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Attribution minimum aux réserves légales issues du bénéfice (CHF)"
    reference = "SR 961.011.1 Art. 5"

    def formula(person, period, parameters):
        p = parameters(period).sr_961_011_1
        benefice = person('benefice_annuel', period)
        reserve = person('fonds_reserve_actuel', period)
        capital = person('capital_statutaire', period)
        vie = person('est_assureur_vie', period)

        import numpy
        # 10% for life, 20% for others
        taux = numpy.where(vie, p.taux_reserve_vie, p.taux_reserve_autres)

        # Until reserve reaches 50% of statutory capital
        seuil = capital * p.seuil_reserve_capital
        besoin = numpy.maximum(seuil - reserve, 0.0)

        attribution = benefice * taux
        return numpy.minimum(attribution, besoin)
