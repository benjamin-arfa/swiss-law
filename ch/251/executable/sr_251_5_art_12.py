"""SR 251.5 Art. 12

Generated from: ch/251/de/251.5.md

Reduktion der Sanktion: Bis zu 50% bei unaufgeforderter Mitwirkung,
bis zu 80% bei Lieferung von Informationen ueber weitere Verstoesse.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unaufgeforderte_mitwirkung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen unaufgefordert am Verfahren mitgewirkt hat"
    reference = "SR 251.5 Art. 12 Abs. 1"


class teilnahme_eingestellt_bei_vorlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Teilnahme am Verstoss bei Vorlage der Beweismittel eingestellt war"
    reference = "SR 251.5 Art. 12 Abs. 1"


class liefert_info_weitere_verstoesse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen Informationen ueber weitere Verstoesse nach Art. 5 Abs. 3/4 KG liefert"
    reference = "SR 251.5 Art. 12 Abs. 3"


class wichtigkeit_beitrag_verfahrenserfolg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Faktor fuer die Wichtigkeit des Beitrags zum Verfahrenserfolg (0.0 bis 1.0)"
    reference = "SR 251.5 Art. 12 Abs. 2"


class maximale_reduktion_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Reduktion der Sanktion in Prozent (50 oder 80)"
    reference = "SR 251.5 Art. 12"

    def formula(person, period, parameters):
        weitere = person('liefert_info_weitere_verstoesse', period)
        # 80% bei Informationen ueber weitere Verstoesse, sonst 50%
        return where(weitere, 80, 50)


class sanktion_nach_reduktion(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Sanktionsbetrag nach Anwendung der Kooperationsreduktion"
    reference = "SR 251.5 Art. 12"

    def formula(person, period, parameters):
        betrag = person('sanktion_endgueltig', period)
        mitwirkung = person('unaufgeforderte_mitwirkung', period)
        eingestellt = person('teilnahme_eingestellt_bei_vorlage', period)
        max_red = person('maximale_reduktion_prozent', period)
        wichtigkeit = person('wichtigkeit_beitrag_verfahrenserfolg', period)

        reduktion = mitwirkung * eingestellt * max_red * wichtigkeit / 100
        return betrag * (1 - reduktion)
