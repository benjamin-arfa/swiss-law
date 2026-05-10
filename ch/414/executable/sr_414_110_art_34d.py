"""SR 414.110 Art. 34d

Generated from: ch/414/de/414.110.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_schweizer_studierender(Variable):
    """Ob die Person Schweizer Staatsangehoerigkeit hat"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schweizer Studierender"
    reference = "SR 414.110 Art. 34d Abs. 2"
    default_value = False


class hat_wohnsitz_schweiz(Variable):
    """Ob die Person Wohnsitz in der Schweiz hat (nicht zum Studiumszweck)"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wohnsitz in der Schweiz (nicht zum Studiumszweck begruendet)"
    reference = "SR 414.110 Art. 34d Abs. 2"
    default_value = False


class wohnsitz_zum_studiumszweck(Variable):
    """Ob Wohnsitz in der Schweiz zum Zweck des Studiums begruendet wurde"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wohnsitz zum Zweck des Studiums begruendet"
    reference = "SR 414.110 Art. 34d Abs. 2bis"
    default_value = False


class studiengebuehr_inland(Variable):
    """Studiengebuehr fuer Schweizer / Auslaender mit Wohnsitz in der Schweiz"""
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Studiengebuehr fuer Inlandstudierende (sozialvertraeglich)"
    reference = "SR 414.110 Art. 34d Abs. 2"


class ist_auslaendischer_studierender_mit_erhoehter_gebuehr(Variable):
    """Ob die Person als auslaendischer Studierender hoeherer Gebuehr unterliegt"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Auslaendischer Studierender mit erhoehter Gebuehr"
    reference = "SR 414.110 Art. 34d Abs. 2bis"

    def formula(person, period, parameters):
        ist_schweizer = person('ist_schweizer_studierender', period)
        hat_wohnsitz = person('hat_wohnsitz_schweiz', period)
        zum_studium = person('wohnsitz_zum_studiumszweck', period)
        # Erhoehte Gebuehr fuer: Auslaender die zum Studium Wohnsitz begruenden
        # oder keinen Wohnsitz in der Schweiz haben
        auslaender = 1 - ist_schweizer
        kein_regulaerer_wohnsitz = (1 - hat_wohnsitz) + zum_studium
        return auslaender * (kein_regulaerer_wohnsitz > 0)


class mindest_studiengebuehr_auslaendisch(Variable):
    """Mindestens das Dreifache der Inlandsgebuehr fuer auslaendische Studierende"""
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mindeststudiengebuehr fuer auslaendische Studierende (3x Inland)"
    reference = "SR 414.110 Art. 34d Abs. 2bis"

    def formula(person, period, parameters):
        inland_gebuehr = person('studiengebuehr_inland', period)
        ist_erhoehte = person('ist_auslaendischer_studierender_mit_erhoehter_gebuehr', period)
        return ist_erhoehte * inland_gebuehr * 3
