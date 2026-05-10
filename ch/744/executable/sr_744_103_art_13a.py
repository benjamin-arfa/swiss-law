"""SR 744.103 Art. 13a

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gegenseitige_amtshilfe_ersuchen_berechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ersuchen um gegenseitige Amtshilfe beim BAV gemäss SR 744.103 Art. 13a berechtigt"
    reference = "SR 744.103 Art. 13a"

    def formula(person, period, parameters):
        # Zuständige Behörden der EU-Mitgliedstaaten sowie der EFTA-Staaten (EWR-Mitglieder)
        # können das BAV um Auskünfte nach Art. 9a Abs. 1 STUG ersuchen
        ist_eu_behoerde = person("ist_eu_mitgliedstaat_behoerde", period)
        ist_efta_ewr_behoerde = person("ist_efta_ewr_staat_behoerde", period)
        return ist_eu_behoerde + ist_efta_ewr_behoerde


class ist_eu_mitgliedstaat_behoerde(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Zuständige Behörde eines EU-Mitgliedstaates"
    reference = "SR 744.103 Art. 13a"


class ist_efta_ewr_staat_behoerde(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Zuständige Behörde eines EFTA-Staates, der Mitglied des EWR ist"
    reference = "SR 744.103 Art. 13a"


class amtshilfe_antwortfrist_arbeitstage(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Frist in Arbeitstagen, innert welcher das BAV Auskünfte nach Art. 9a Abs. 1 STUG erteilt (SR 744.103 Art. 13a)"
    reference = "SR 744.103 Art. 13a"

    def formula(person, period, parameters):
        ersuchen_berechtigt = person("gegenseitige_amtshilfe_ersuchen_berechtigt", period)
        # Das BAV erteilt Auskünfte innert 30 Arbeitstagen
        return ersuchen_berechtigt * 30
