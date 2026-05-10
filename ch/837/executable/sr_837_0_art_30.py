"""SR 837.0 Art. 30

Generated from: ch/837/de/837.0.md

Art. 30: Einstellung in der Anspruchsberechtigung
(Suspension of benefit entitlement)

- Abs. 1: The insured person's entitlement is suspended if they:
  a. became unemployed through own fault
  b. waived salary/compensation claims against former employer at the
     expense of insurance
  c. did not sufficiently seek suitable work
  d. did not comply with control requirements or instructions
  e. provided false/incomplete information or violated disclosure obligations
  f. wrongfully obtained or attempted to obtain unemployment benefits
  g. received daily allowances during a project planning phase (Art. 71a)
     but did not start self-employment through own fault

- Abs. 3: The suspension applies only to days for which eligibility
  conditions are met. It counts toward the maximum number of daily allowances
  (Art. 27). Duration is based on degree of fault, max 60 days per reason
  (25 days for Abs. 1g).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alv_einstellung_eigenverschulden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Durch eigenes Verschulden arbeitslos geworden (Art. 30 Abs. 1 Bst. a)"
    reference = "SR 837.0 Art. 30 Abs. 1 Bst. a"


class alv_einstellung_ungenuegend_bemuehungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Sich nicht genuegend um zumutbare Arbeit bemueht (Art. 30 Abs. 1 Bst. c)"
    reference = "SR 837.0 Art. 30 Abs. 1 Bst. c"


class alv_einstellung_kontrollverstoss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kontrollvorschriften/Weisungen nicht befolgt (Art. 30 Abs. 1 Bst. d)"
    reference = "SR 837.0 Art. 30 Abs. 1 Bst. d"


class alv_einstellung_unwahre_angaben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unwahre/unvollstaendige Angaben gemacht (Art. 30 Abs. 1 Bst. e)"
    reference = "SR 837.0 Art. 30 Abs. 1 Bst. e"


class alv_einstellungsgrund_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einstellungsgrund nach Art. 30 Abs. 1 AVIG vorhanden"
    reference = "SR 837.0 Art. 30 Abs. 1"

    def formula(person, period, parameters):
        eigenverschulden = person('alv_einstellung_eigenverschulden', period)
        bemuehungen = person('alv_einstellung_ungenuegend_bemuehungen', period)
        kontrolle = person('alv_einstellung_kontrollverstoss', period)
        angaben = person('alv_einstellung_unwahre_angaben', period)
        return eigenverschulden + bemuehungen + kontrolle + angaben


class alv_einstellung_verschuldensgrad(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Verschuldensgrad der Einstellung (1=leicht, 2=mittel, 3=schwer)"
    reference = "SR 837.0 Art. 30 Abs. 3"


class alv_einstellung_dauer_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Dauer der Einstellung in Tagen (max 60 je Grund)"
    reference = "SR 837.0 Art. 30 Abs. 3"

    def formula(person, period, parameters):
        grund = person('alv_einstellungsgrund_vorhanden', period)
        grad = person('alv_einstellung_verschuldensgrad', period)
        p = parameters(period).alv

        # Maximum 60 days per reason, scaled by degree of fault
        # Light ~1-15 days, medium ~16-30 days, severe ~31-60 days (typical practice)
        dauer = where(
            grad == 1,
            min_(15, p.einstellung_max_tage),
            where(
                grad == 2,
                min_(30, p.einstellung_max_tage),
                p.einstellung_max_tage
            )
        )
        return grund * dauer
