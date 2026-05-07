"""SR 0.142.116.702 Art. 11

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# This is an international treaty and does not appear to have any relevance to the Swiss OpenFisca implementation.
# It is primarily of relevance to the governance of an international agreement between the Swiss Confederation and the Government of St. Lucia.
# Variables and parameters are only included in the corresponding YAML file for international treaties relevant to Swiss OpenFisca.
