"""SR 196.1 Art. 1

Generated from: ch/196/de/196.1.md

Gegenstand: Dieses Gesetz regelt die Sperrung, die Einziehung und die
Rueckerstattung von Vermoegenswerten auslaendischer politisch exponierter
Personen oder ihnen nahestehender Personen.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 1 is a declaratory provision defining the subject matter of the law.
# No computable rule can be derived.
