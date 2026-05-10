"""SR 150.21 Art. 4

Generated from: ch/150/de/150.21.md

Bearbeitungsfristen: Netzwerksuche umgehend nach Erhalt eines
vollstaendigen Gesuchs. Frist fuer Rueckmeldung: 6 Arbeitstage.
Verkuerzung bei Dringlichkeit, Verlaengerung bei besonderem Aufwand.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_gesuch_vollstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Informationsgesuch vollstaendig ist"
    reference = "SR 150.21 Art. 4 Abs. 1"


class ist_besonders_dringlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Anfrage besonders dringlich ist"
    reference = "SR 150.21 Art. 4 Abs. 3"


class ist_besonders_aufwendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Suche besonders aufwendig ist"
    reference = "SR 150.21 Art. 4 Abs. 3"


class rueckmeldungsfrist_arbeitstage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer die Rueckmeldung in Arbeitstagen"
    reference = "SR 150.21 Art. 4 Abs. 3"

    def formula(person, period, parameters):
        # Standard: 6 Arbeitstage
        standard = 6
        # Bei Dringlichkeit kann verkuerzt werden (hier: 3 Tage als Beispiel)
        # Bei Aufwand kann verlaengert werden (hier unveraendert, da kontextabhaengig)
        dringlich = person('ist_besonders_dringlich', period)
        return where(dringlich, 3, standard)
