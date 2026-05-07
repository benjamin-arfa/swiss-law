"""SR 744.103 Art. 17

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class sr_744_103_art_17_aufhebung_strassentransportunternehmen_vo(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SR 744.103 Art. 17: Aufhebung der Verordnung vom 1. November 2000 über die Zulassung als Strassentransportunternehmen im Personen- und Güterverkehr"
    reference = "https://www.fedlex.admin.ch/eli/cc/2021/867/de#art_17"

    def formula(person, period, parameters):
        # Art. 17 is a purely procedural repeal provision.
        # The Verordnung vom 1. November 2000 (AS 2000 2890; 2003 2484; 2009 5959 Ziff. I 7)
        # über die Zulassung als Strassentransportunternehmen im Personen- und Güterverkehr
        # is repealed upon entry into force of SR 744.103.
        # This variable indicates that the repeal is in effect (always True once the law applies).
        return True
