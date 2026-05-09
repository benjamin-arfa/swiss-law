"""SR 836.2 Art. 11

Generated from: ch/836/de/836.2.md

Art. 11: Unterstellung - Subjection to the Family Allowances Act.
Abs. 1: Diesem Gesetz unterstehen:
  a. Arbeitgeber, die nach Art. 12 AHVG beitragspflichtig sind
  b. Arbeitnehmerinnen/Arbeitnehmer nicht beitragspflichtiger Arbeitgeber (Art. 6 AHVG)
  c. Personen nach Art. 12 Abs. 3 (Selbstaendigerwerbende, seit 1.1.2013)
Abs. 2: Nicht diesem Gesetz unterstehen Arbeitgeber und
Arbeitnehmer landwirtschaftlicher Betriebe (Art. 18).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_beitragspflichtiger_arbeitgeber_ahvg(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitgeber ist beitragspflichtig nach Art. 12 AHVG"
    reference = "SR 836.2 Art. 11 Abs. 1 lit. a"


class ist_arbeitnehmer_nicht_beitragspflichtiger_arbeitgeber(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitnehmer eines nicht beitragspflichtigen Arbeitgebers nach Art. 6 AHVG"
    reference = "SR 836.2 Art. 11 Abs. 1 lit. b"


class ist_selbstaendigerwerbend(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist selbstaendigerwerbend nach Art. 12 Abs. 3 FamZG"
    reference = "SR 836.2 Art. 11 Abs. 1 lit. c"


class ist_landwirtschaftlicher_arbeitgeber(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitgeber eines landwirtschaftlichen Betriebes (Art. 18)"
    reference = "SR 836.2 Art. 11 Abs. 2"


class ist_landwirtschaftlicher_arbeitnehmer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitnehmer eines landwirtschaftlichen Betriebes (Art. 18)"
    reference = "SR 836.2 Art. 11 Abs. 2"


class unterstellt_famzg(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person/Arbeitgeber ist dem FamZG unterstellt (Art. 11)"
    reference = "SR 836.2 Art. 11"

    def formula(person, period, parameters):
        ag_beitragspflichtig = person('ist_beitragspflichtiger_arbeitgeber_ahvg', period)
        an_nicht_beitragspflichtig = person('ist_arbeitnehmer_nicht_beitragspflichtiger_arbeitgeber', period)
        selbstaendig = person('ist_selbstaendigerwerbend', period)
        landw_ag = person('ist_landwirtschaftlicher_arbeitgeber', period)
        landw_an = person('ist_landwirtschaftlicher_arbeitnehmer', period)

        # Abs. 1: Unterstellt
        unterstellt = (ag_beitragspflichtig + an_nicht_beitragspflichtig + selbstaendig) > 0

        # Abs. 2: Nicht unterstellt wenn landwirtschaftlich
        nicht_landwirtschaftlich = (1 - landw_ag) * (1 - landw_an)

        return unterstellt * nicht_landwirtschaftlich
