"""SR 322.1 Art. 7

Generated from: ch/322/de/322.1.md

Wahl der Richter: Praesidenten, Richter und Ersatzrichter werden vom
Bundesrat fuer eine Amtsdauer von vier Jahren gewaehlt. Als Richter
werden Angehoerige der Armee oder des Grenzwachtkorps gewaehlt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_militaerrichter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Militaerrichter gewaehlt ist"
    reference = "SR 322.1 Art. 7 Abs. 1"


class ist_angehoeriger_grenzwachtkorps(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Angehoerige des Grenzwachtkorps ist"
    reference = "SR 322.1 Art. 7 Abs. 2"


class waehlbar_als_militaerrichter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Richter oder Ersatzrichter am Militaergericht waehlbar ist"
    reference = "SR 322.1 Art. 7 Abs. 2"

    def formula_2009(person, period, parameters):
        """Fassung gemaess BG vom 3. Okt. 2008, in Kraft seit 1. Maerz 2009."""
        ist_armee = person('ist_angehoeriger_der_armee_justiz', period)
        ist_grenzwacht = person('ist_angehoeriger_grenzwachtkorps', period)
        return (ist_armee + ist_grenzwacht) > 0
