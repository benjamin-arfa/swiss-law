"""SR 0.142.115.162 Art. 10

Generated from: ch/0/de/0.142.115.162.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

{"type": "object", "error": "This legal article does not appear to generate OpenFisca code directly.", "detail": "Legal articles that only provide geographic scope for a law do not typically require the creation of an OpenFisca variable. The relevant OpenFisca code for SR 0.142.115.162 needs to be found elsewhere within the law. This might involve using the current jurisdiction parameter or creating a new parameter for geographic scope.", "status": 400, "reason": "Bad Request"}
