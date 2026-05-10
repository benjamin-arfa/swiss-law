"""SR 744.10 Art. 13

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_744_10_art_13_bundesrat_vollzug(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SR 744.10 Art. 13 – Vollzug: Der Bundesrat erlässt die Ausführungsvorschriften."
    reference = "https://www.fedlex.admin.ch/eli/cc/2009/680/de#art_13"

    def formula(person, period, parameters):
        # Art. 13 delegates the authority to issue implementing provisions to the
        # Federal Council. This is a purely procedural norm with no individual
        # applicability condition; the article is in force from 1 January 2010.
        return period.start.year >= 2010
