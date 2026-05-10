"""SR 952.02 Art. 4 — Finanzbereich

Generated from: ch/952/de/952.02.md

Im Finanzbereich taetig ist, wer:
a) Dienstleistungen fuer Finanzgeschaefte erbringt/vermittelt (Einlagen-,
   Kreditgeschaeft, Effektenhandel, Kapitalanlage, Vermoegensverwaltung,
   kryptobasierte Vermoegenswerte);
b) qualifizierte Beteiligungen ueberwiegend an Finanzunternehmen haelt
   (Holdinggesellschaft);
c) wesentliche Gruppengesellschaft nach Art. 3a ist.

Versicherungsbereich wird gleichgestellt, sofern keine abweichenden
Regelungen in BankV oder ERV.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bankv_erbringt_finanzdienstleistungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Erbringt/vermittelt Dienstleistungen fuer Finanzgeschaefte"
    reference = "SR 952.02 Art. 4 Abs. 1 lit. a"


class bankv_ist_finanz_holding(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Haelt qualifizierte Beteiligungen ueberwiegend an Finanzunternehmen"
    reference = "SR 952.02 Art. 4 Abs. 1 lit. b"


class bankv_ist_wesentliche_gruppengesellschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ist wesentliche Gruppengesellschaft nach Art. 3a BankV"
    reference = "SR 952.02 Art. 4 Abs. 1 lit. c"


class bankv_ist_versicherungsunternehmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut ist Versicherungsunternehmen"
    reference = "SR 952.02 Art. 4 Abs. 2"


class bankv_im_finanzbereich_taetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut ist im Finanzbereich taetig nach Art. 4 BankV"
    reference = "SR 952.02 Art. 4"

    def formula_2021(person, period, parameters):
        finanzdienstleistungen = person('bankv_erbringt_finanzdienstleistungen', period)
        holding = person('bankv_ist_finanz_holding', period)
        gruppengesellschaft = person('bankv_ist_wesentliche_gruppengesellschaft', period)
        versicherung = person('bankv_ist_versicherungsunternehmen', period)

        return (
            finanzdienstleistungen
            + holding
            + gruppengesellschaft
            + versicherung
        ) >= 1
