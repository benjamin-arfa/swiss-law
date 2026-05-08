"""SR 950.1 Art. 28–29

Generated from: ch/950/de/950.1.md

Beraterregister:
- Art. 28: Registrierungspflicht fuer Kundenberaterinnen/-berater
  von inlaendischen Finanzdienstleistern (die nicht nach Finanzmarkt-
  gesetzen beaufsichtigt sind) und auslaendischen Finanzdienstleistern.
- Art. 29: Registrierungsvoraussetzungen: ausreichende Kenntnisse der
  Verhaltensregeln (Art. 7-20), notwendige Fachkenntnisse,
  Berufshaftpflicht oder gleichwertige Sicherheiten,
  Anschluss an Ombudsstelle.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class fidleg_ist_kundenberater(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist Kundenberaterin/Kundenberater"
    reference = "SR 950.1 Art. 28 Abs. 1"


class fidleg_berater_beaufsichtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Finanzdienstleister ist prudenziell beaufsichtigt"
    reference = "SR 950.1 Art. 28 Abs. 1"


class fidleg_berater_registrierungspflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kundenberater ist registrierungspflichtig (Art. 28)"
    reference = "SR 950.1 Art. 28"

    def formula_2020(person, period, parameters):
        import numpy as np

        ist_berater = person('fidleg_ist_kundenberater', period)
        beaufsichtigt = person('fidleg_berater_beaufsichtigt', period)

        # Registrierungspflichtig wenn Berater und nicht beaufsichtigt
        return ist_berater * np.logical_not(beaufsichtigt)


class fidleg_berater_hat_kenntnisse_verhaltensregeln(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Berater hat Kenntnisse der Verhaltensregeln (Art. 7-20)"
    reference = "SR 950.1 Art. 29 Abs. 1 lit. a"


class fidleg_berater_hat_fachkenntnisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Berater verfuegt ueber notwendige Fachkenntnisse"
    reference = "SR 950.1 Art. 29 Abs. 1 lit. a"


class fidleg_berater_hat_haftpflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Berater hat Berufshaftpflicht oder Sicherheiten"
    reference = "SR 950.1 Art. 29 Abs. 1 lit. b"


class fidleg_berater_hat_ombudsstelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Berater/Finanzdienstleister ist an Ombudsstelle angeschlossen"
    reference = "SR 950.1 Art. 29 Abs. 1 lit. c"


class fidleg_berater_registrierungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Berater erfuellt alle Registrierungsvoraussetzungen (Art. 29)"
    reference = "SR 950.1 Art. 29"

    def formula_2020(person, period, parameters):
        return (
            person('fidleg_berater_hat_kenntnisse_verhaltensregeln', period)
            * person('fidleg_berater_hat_fachkenntnisse', period)
            * person('fidleg_berater_hat_haftpflicht', period)
            * person('fidleg_berater_hat_ombudsstelle', period)
        )
