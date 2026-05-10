"""SR 913.211 Art. 7

Generated from: ch/913/de/913.211.md

Gemeinschaftliche Ökonomiegebäude:
- Unterstützung wenn: Gemeinschaft vom Kanton anerkannt,
  Mindest-SAK vorhanden, jeder Teilhaber bewirtschaftet Betrieb,
  Zusammenarbeitsvertrag abgeschlossen
- Mindestdauer Vertrag: 20 Jahre bei Beiträgen, Kreditlaufzeit bei nur Krediten
- Bei Austritt vor Fristablauf: anteilsmässige Rückzahlung
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gemeinschaft_kantonal_anerkannt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gemeinschaft von der kantonalen Stelle anerkannt ist"
    reference = "SR 913.211 Art. 7 Abs. 1 Bst. a"


class gemeinschaft_hat_mindest_sak(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gemeinschaft über den Mindestarbeitsbedarf an SAK verfügt"
    reference = "SR 913.211 Art. 7 Abs. 1 Bst. b"


class teilhaber_bewirtschaftet_betrieb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob jeder Teilhaber einen Betrieb mit erfüllten Voraussetzungen bewirtschaftet"
    reference = "SR 913.211 Art. 7 Abs. 1 Bst. c"


class zusammenarbeitsvertrag_abgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Zusammenarbeitsvertrag abgeschlossen wurde"
    reference = "SR 913.211 Art. 7 Abs. 1 Bst. d"


class unterstuetzung_mit_beitraegen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Unterstützung Beiträge umfasst (nicht nur Investitionskredite)"
    reference = "SR 913.211 Art. 7 Abs. 1 Bst. d"


class gemeinschaftliches_oekonomiegebaeude_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Voraussetzungen für Unterstützung gemeinschaftlicher Ökonomiegebäude erfüllt sind"
    reference = "SR 913.211 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('gemeinschaft_kantonal_anerkannt', period) *
            person('gemeinschaft_hat_mindest_sak', period) *
            person('teilhaber_bewirtschaftet_betrieb', period) *
            person('zusammenarbeitsvertrag_abgeschlossen', period)
        )


class mindestdauer_zusammenarbeitsvertrag_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Erforderliche Mindestdauer des Zusammenarbeitsvertrags in Jahren"
    reference = "SR 913.211 Art. 7 Abs. 1 Bst. d"

    def formula(person, period, parameters):
        import numpy as np
        mit_beitraegen = person('unterstuetzung_mit_beitraegen', period)
        min_dauer = parameters(period).sr_913_211.mindestdauer_vertrag_bei_beitraegen_jahre
        return np.where(mit_beitraegen, min_dauer, 0)
