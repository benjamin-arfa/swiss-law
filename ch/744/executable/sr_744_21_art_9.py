"""SR 744.21 Art. 9

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class technische_normalisierung_vorschriften_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat kann Vorschriften über technische Normalisierung der Anlagen und Fahrzeuge erlassen (SR 744.21 Art. 9)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1985/577_577_577/de#art_9"

    def formula(person, period, parameters):
        # Art. 9: The Federal Council may issue technical standardisation regulations
        # after consulting the cantons concerned and licensed companies.
        # This is a purely enabling/procedural provision granting regulatory power;
        # no individual eligibility condition applies — always true as a standing authority.
        return True
