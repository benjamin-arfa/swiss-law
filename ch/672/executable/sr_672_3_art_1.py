"""SR 672.3 Art. 1 — Gegenstand der Anerkennung

Bundesgesetz über die Anerkennung privater Vereinbarungen zur Vermeidung der Doppelbesteuerung.
Generated from: ch/de/672/672.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_private_vereinbarung_doppelbesteuerung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine Vereinbarung zwischen privaten Einrichtungen zur Vermeidung der Doppelbesteuerung"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_1"


class staatsvertrag_fuer_regelungsgegenstand_ausgeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Abschluss eines Staatsvertrags ist für denselben Regelungsgegenstand ausgeschlossen"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_1"


class bundesrat_kann_vereinbarung_anerkennen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat ist ermächtigt, die Vereinbarung anzuerkennen (SR 672.3 Art. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_1"

    def formula(person, period, parameters):
        # Art. 1: Der Bundesrat wird ermächtigt, private Vereinbarungen zur
        # Vermeidung der Doppelbesteuerung anzuerkennen, wenn für denselben
        # Regelungsgegenstand der Abschluss eines Staatsvertrags ausgeschlossen ist.
        ist_vereinbarung = person('ist_private_vereinbarung_doppelbesteuerung', period)
        kein_staatsvertrag = person('staatsvertrag_fuer_regelungsgegenstand_ausgeschlossen', period)
        return ist_vereinbarung * kein_staatsvertrag
