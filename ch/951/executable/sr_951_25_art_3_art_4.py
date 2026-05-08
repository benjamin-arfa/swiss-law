"""SR 951.25 Art. 3–4

Generated from: ch/951/de/951.25.md

Empfaenger von Finanzhilfen und Anerkennungsvoraussetzungen:
- Art. 3: Anerkannte Organisationen, die KMU Solidarbuergschaften fuer
  Bankkredite bereitstellen.
- Art. 4: Anerkennungsvoraussetzungen: nicht gewinnorientiert,
  branchenoffen, unabhaengig vom Kreditgeber, professionell gefuehrt,
  ueberkantonal taetig. Bundesrat kann Zahl beschraenken.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class kmu_buergschaft_org_nicht_gewinnorientiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Buergschaftsorganisation ist nicht gewinnorientiert (Art. 4 Abs. 1 lit. a)"
    reference = "SR 951.25 Art. 4 Abs. 1 lit. a"


class kmu_buergschaft_org_branchenoffen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Organisation steht Unternehmen aller Branchen offen (Art. 4 Abs. 1 lit. b)"
    reference = "SR 951.25 Art. 4 Abs. 1 lit. b"


class kmu_buergschaft_org_unabhaengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Organisation ist unabhaengig vom Kreditgeber (Art. 4 Abs. 1 lit. c)"
    reference = "SR 951.25 Art. 4 Abs. 1 lit. c"


class kmu_buergschaft_org_professionell(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Organisation wird professionell und effizient gefuehrt (Art. 4 Abs. 1 lit. d)"
    reference = "SR 951.25 Art. 4 Abs. 1 lit. d"


class kmu_buergschaft_org_ueberkantonal(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Organisation ist ueberkantonal taetig (Art. 4 Abs. 1 lit. e)"
    reference = "SR 951.25 Art. 4 Abs. 1 lit. e"


class kmu_buergschaft_org_anerkennungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Organisation erfuellt alle Anerkennungsvoraussetzungen nach Art. 4"
    reference = "SR 951.25 Art. 4"

    def formula_2007(person, period, parameters):
        return (
            person('kmu_buergschaft_org_nicht_gewinnorientiert', period)
            * person('kmu_buergschaft_org_branchenoffen', period)
            * person('kmu_buergschaft_org_unabhaengig', period)
            * person('kmu_buergschaft_org_professionell', period)
            * person('kmu_buergschaft_org_ueberkantonal', period)
        )
