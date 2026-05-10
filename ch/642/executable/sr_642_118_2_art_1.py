"""SR 642.118.2 Art. 1

Generated from: ch/642/de/642.118.2.md

Art. 1: Anwendbare Quellensteuertarife - Classification of withholding tax
tariff codes based on civil status, employment status, and residency.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class quellensteuer_zivilstand(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Zivilstand: 1=ledig, 2=verheiratet, 3=geschieden, 4=getrennt, 5=verwitwet"
    reference = "SR 642.118.2 Art. 1 Abs. 1"


class quellensteuer_ehepartner_erwerbstaetig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ehepartner ist ebenfalls erwerbstaetig"
    reference = "SR 642.118.2 Art. 1 Abs. 1 Bst. c"


class quellensteuer_lebt_mit_kindern(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Lebt mit Kindern oder unterstuetzungsbeduerftigen Personen im gleichen Haushalt"
    reference = "SR 642.118.2 Art. 1 Abs. 1 Bst. h"


class quellensteuer_ist_grenzgaenger_de(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Grenzgaenger/in nach DBA-D (Deutschland)"
    reference = "SR 642.118.2 Art. 1 Abs. 1 Bst. i-m"


class quellensteuer_ist_grenzgaenger_it(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Grenzgaenger/in nach Grenzgaengerabkommen CH-IT"
    reference = "SR 642.118.2 Art. 1 Abs. 1 Bst. n-r"


class quellensteuer_bezieht_ahv_leistungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bezieht Leistungen nach Art. 18 Abs. 3 AHVG (Tarifcode D)"
    reference = "SR 642.118.2 Art. 1 Abs. 1 Bst. d"


class quellensteuer_vereinfachtes_verfahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wird im vereinfachten Abrechnungsverfahren besteuert (Tarifcode E)"
    reference = "SR 642.118.2 Art. 1 Abs. 1 Bst. e"


class quellensteuer_ersatzeinkuenfte_nicht_ueber_arbeitgeber(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bezieht Ersatzeinkuenfte nicht ueber Arbeitgeber (Tarifcode G)"
    reference = "SR 642.118.2 Art. 1 Abs. 1 Bst. g"


class quellensteuer_tarifcode(Variable):
    value_type = str
    max_length = 1
    entity = Person
    definition_period = YEAR
    label = "Quellensteuer-Tarifcode (A-V)"
    reference = "SR 642.118.2 Art. 1"

    def formula(person, period, parameters):
        zivilstand = person('quellensteuer_zivilstand', period)
        ehepartner_erwerb = person('quellensteuer_ehepartner_erwerbstaetig', period)
        mit_kindern = person('quellensteuer_lebt_mit_kindern', period)
        grenzgaenger_de = person('quellensteuer_ist_grenzgaenger_de', period)
        grenzgaenger_it = person('quellensteuer_ist_grenzgaenger_it', period)
        ahv_leistungen = person('quellensteuer_bezieht_ahv_leistungen', period)
        vereinfacht = person('quellensteuer_vereinfachtes_verfahren', period)
        ersatz_nicht_ag = person('quellensteuer_ersatzeinkuenfte_nicht_ueber_arbeitgeber', period)

        verheiratet = (zivilstand == 2)
        alleinstehend = (zivilstand == 1) + (zivilstand == 3) + (zivilstand == 4) + (zivilstand == 5)

        # Base tariff codes for non-cross-border workers
        # D: AHV benefit recipients
        # E: simplified procedure
        # G: replacement income not via employer
        # H: single with children
        # B: married, one earner
        # C: married, both earners
        # A: single without children
        base_code = where(ahv_leistungen, 'D',
                   where(vereinfacht, 'E',
                   where(ersatz_nicht_ag, 'G',
                   where(alleinstehend * mit_kindern, 'H',
                   where(verheiratet * ~ehepartner_erwerb, 'B',
                   where(verheiratet * ehepartner_erwerb, 'C',
                   'A'))))))

        # German cross-border workers: L/M/N/P/Q map to A/B/C/H/G
        de_code = where(ahv_leistungen, 'D',
                  where(alleinstehend * mit_kindern, 'P',
                  where(verheiratet * ~ehepartner_erwerb, 'M',
                  where(verheiratet * ehepartner_erwerb, 'N',
                  where(ersatz_nicht_ag, 'Q',
                  'L')))))

        # Italian cross-border workers: R/S/T/U/V map to A/B/C/H/G
        it_code = where(alleinstehend * mit_kindern, 'U',
                  where(verheiratet * ~ehepartner_erwerb, 'S',
                  where(verheiratet * ehepartner_erwerb, 'T',
                  where(ersatz_nicht_ag, 'V',
                  'R'))))

        return where(grenzgaenger_it, it_code,
               where(grenzgaenger_de, de_code,
               base_code))
