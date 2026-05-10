"""SR 142.206 Art. 4

Generated from: ch/142/de/142.206.md

Abfrage zur Pruefung von Visumgesuchen und fuer Visumentscheide:
Abfrage ueber ORBIS anhand personenbezogener, Reisedokument-,
visumbezogener oder biometrischer Daten. Bei Treffer Zugang zu
Kategorien I-VI.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ees_abfrage_visumgesuch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine EES-Abfrage zur Pruefung eines Visumgesuchs erfolgt"
    reference = "SR 142.206 Art. 4 Abs. 1"


class ees_abfrage_personenbezogene_daten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die EES-Abfrage anhand personenbezogener Daten (Name, Geburtsdatum, Geschlecht, Staatsangehoerigkeit) erfolgt"
    reference = "SR 142.206 Art. 4 Abs. 1 Bst. a"


class ees_abfrage_reisedokument_daten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die EES-Abfrage anhand von Reisedokumentdaten (Art, Nummer, Code, Gueltigkeit) erfolgt"
    reference = "SR 142.206 Art. 4 Abs. 1 Bst. b"


class ees_abfrage_biometrische_daten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die EES-Abfrage anhand biometrischer Daten (Fingerabdruecke, Gesichtsbild) erfolgt"
    reference = "SR 142.206 Art. 4 Abs. 1 Bst. d"


class ees_treffer_gefunden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die EES-Suche einen Treffer ergeben hat"
    reference = "SR 142.206 Art. 4 Abs. 2"


class ees_zugang_kategorien_i_vi(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die zugangsberechtigte Stelle die Daten der Kategorien I-VI nach Anhang 2 abfragen darf"
    reference = "SR 142.206 Art. 4 Abs. 2"

    def formula_2022_05(person, period, parameters):
        return (
            person('ees_abfrage_visumgesuch', period)
            * person('ees_treffer_gefunden', period)
        )
