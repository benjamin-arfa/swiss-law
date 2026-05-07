"""SR 455.110.2 Art. 6

Generated from: ch/455/de/455.110.2.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class maximales_kontrollintervall_stunden(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximales Kontrollintervall bei Uebernachtung im Schlachtbetrieb in Stunden (Art. 6 Abs. 2 SR 455.110.2)"
    reference = "SR 455.110.2 Art. 6 Abs. 2"
    default_value = 12.0
    # Ueberwachung am Abend des Anlieferungstages und danach alle max. 12 Stunden
