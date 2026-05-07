"""SR 0.103.3 Art. 4

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
class no_evasion_tax_benefit(Reduction):
    def filter(self, benefits):
        # This would only return true if evasion is considered a crime, indirect implication.
        return True
