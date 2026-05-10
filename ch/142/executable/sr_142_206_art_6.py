"""SR 142.206 Art. 6

Generated from: ch/142/de/142.206.md

Erfassung und Aktualisierung von Daten: Erstellung eines persoenlichen
EES-Dossiers, Erfassung von Ein-/Ausreise oder Einreiseverweigerung,
und Aktualisierung bestehender Daten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ees_kein_persoenliches_dossier_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob zur betreffenden Person noch kein persoenliches EES-Dossier erstellt wurde"
    reference = "SR 142.206 Art. 6 Abs. 1"


class ees_dossier_erstellen_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die abfragende Stelle ein persoenliches EES-Dossier erstellen darf"
    reference = "SR 142.206 Art. 6 Abs. 1"

    def formula_2022_05(person, period, parameters):
        return person('ees_kein_persoenliches_dossier_vorhanden', period)


class ees_einreise_ausreise_nicht_erfasst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Einreise- oder Ausreisezeitpunkt oder Einreiseverweigerung nicht im EES erfasst ist"
    reference = "SR 142.206 Art. 6 Abs. 2"


class ees_daten_aktualisieren_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob bestehende EES-Daten aktualisiert werden duerfen"
    reference = "SR 142.206 Art. 6 Abs. 3"

    def formula_2022_05(person, period, parameters):
        return not_(person('ees_kein_persoenliches_dossier_vorhanden', period))
