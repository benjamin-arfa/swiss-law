"""SR 143.1 Art. 2 - Inhalt des Ausweises (Content of Identity Document)

Generated from: ch/143/de/143.1.md

Mandatory data fields for every Swiss identity document:
name, first names, sex, date of birth, place of origin, nationality,
height, signature, photograph, issuing authority, issue date,
expiry date, document number and type.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ausweis_hat_pflichtdaten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Ausweis alle Pflichtdaten nach Art. 2 Abs. 1 enthaelt"
    reference = "SR 143.1 Art. 2 Abs. 1"


class ausweis_hat_datenchip(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Ausweis mit einem Datenchip versehen ist"
    reference = "SR 143.1 Art. 2 Abs. 2bis"


class ausweis_hat_biometrische_daten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Datenchip Gesichtsbild und Fingerabdruecke enthaelt"
    reference = "SR 143.1 Art. 2 Abs. 2bis"

    def formula(person, period, parameters):
        return person('ausweis_hat_datenchip', period)


class identitaetskarte_ohne_chip_beantragbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Identitaetskarte ohne Chip beantragt werden kann"
    reference = "SR 143.1 Art. 2 Abs. 2ter"

    def formula(person, period, parameters):
        # Bundesrat muss sicherstellen, dass auch eine ID ohne Chip beantragt werden kann
        return True
