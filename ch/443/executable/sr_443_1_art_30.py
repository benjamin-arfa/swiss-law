"""SR 443.1 Art. 30

Generated from: ch/443/de/443.1.md

Widerhandlung gegen Abgabevorschriften:
- Vorsatz: Busse bis 3x hinterzogene Abgabe
- Fahrlaessigkeit: Busse bis 1x hinterzogene Abgabe
- Versuch strafbar
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hinterzogene_abgabe_film(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag der hinterzogenen Abgabe (CHF)"
    reference = "SR 443.1 Art. 30 Abs. 1"


class vorsaetzliche_abgabehinterziehung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Abgabehinterziehung vorsaetzlich erfolgte"
    reference = "SR 443.1 Art. 30 Abs. 1"


class max_busse_abgabehinterziehung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse bei Abgabehinterziehung (CHF)"
    reference = "SR 443.1 Art. 30"

    def formula(person, period, parameters):
        betrag = person('hinterzogene_abgabe_film', period)
        vorsatz = person('vorsaetzliche_abgabehinterziehung', period)
        # Vorsatz: 3x, Fahrlaessigkeit: 1x
        return betrag * (vorsatz * 3 + (1 - vorsatz) * 1)
