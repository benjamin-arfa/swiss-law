"""SR 641.10 Art. 11

Generated from: ch/641/de/641.10.md

Faelligkeit der Emissionsabgabe:
a. Genossenschaftsanteile: 30 Tage nach Geschaeftsabschluss
b. Beteiligungsrechte: 30 Tage nach Ablauf des Vierteljahres, in dem die
   Abgabeforderung entstanden ist
c. In allen anderen Faellen: 30 Tage nach Entstehung der Abgabeforderung
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class stg_emissionsabgabe_art(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Art der Emissionsabgabe: 1=Genossenschaftsanteile, 2=Beteiligungsrechte, 3=andere"
    reference = "SR 641.10 Art. 11"


class stg_abgabeforderung_entstehungstag(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Tag im Monat, an dem die Abgabeforderung entstanden ist"
    reference = "SR 641.10 Art. 7"


class stg_geschaeftsabschluss_tag(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Tag im Monat des Geschaeftsabschlusses (fuer Genossenschaften)"
    reference = "SR 641.10 Art. 11 Bst. a"


class stg_emissionsabgabe_faelligkeitsfrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist in Tagen bis zur Faelligkeit der Emissionsabgabe"
    reference = "SR 641.10 Art. 11"

    def formula(person, period, parameters):
        frist = parameters(period).sr_641_10.faelligkeitsfrist_tage
        # The due date is always 30 days after the relevant event
        # (business closing, quarter end, or claim arising)
        return frist + 0 * person('stg_emissionsabgabe_art', period)
