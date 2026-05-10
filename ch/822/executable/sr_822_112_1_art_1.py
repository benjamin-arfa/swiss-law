"""SR 822.112.1 Art. 1

Generated from: ch/822/de/822.112.1.md

Designation of train stations and airports as public transport centres
per Art. 27(1ter) ArG, where special working time rules apply:

Stations: Aarau, Baden, Basel Bad. Bhf, Basel SBB, Bellinzona, Bern,
Biel/Bienne, Brig, Buelach, Bulle, Burgdorf, Chur, Dietikon, Frauenfeld,
Fribourg/Freiburg, Geneve, Geneve-Aeroport, Lausanne, Lenzburg, Lugano,
Luzern, Morges, Neuchatel, Nyon, Olten, Renens, Schaffhausen, Sion,
Solothurn, St. Gallen, Thalwil, Thun, Uster, Vevey, Visp, Wil,
Winterthur, Yverdon-les-Bains, Zug, Zuerich Flughafen, Zuerich Altstetten,
Zuerich Enge, Zuerich HB, Zuerich Oerlikon, Zuerich Stadelhofen

Airports: Bern Belp, Geneve Cointrin, Lugano Agno, Sion,
St. Gallen Altenrhein, Zuerich Kloten
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class arg_arbeitsort_zentrum_ov(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Arbeitsort ein Bahnhof oder Flughafen ist, der als Zentrum des oeffentlichen Verkehrs gilt"
    reference = "SR 822.112.1 Art. 1"


class arg_arbeitsort_bahnhof_grosser_reiseverkehr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Arbeitsort ein Bahnhof mit grossem Reiseverkehr gemaess Art. 27 Abs. 1ter ArG ist"
    reference = "SR 822.112.1 Art. 1 Abs. 1"


class arg_arbeitsort_flughafen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Arbeitsort ein Flughafen gemaess Art. 27 Abs. 1ter ArG ist"
    reference = "SR 822.112.1 Art. 1 Abs. 2"


class arg_sonderregelung_arbeitszeit_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sonderregelung fuer Arbeitszeiten an Zentren des oeffentlichen Verkehrs anwendbar ist"
    reference = "SR 822.112.1 Art. 1"

    def formula(person, period, parameters):
        bahnhof = person('arg_arbeitsort_bahnhof_grosser_reiseverkehr', period)
        flughafen = person('arg_arbeitsort_flughafen', period)
        return bahnhof + flughafen
