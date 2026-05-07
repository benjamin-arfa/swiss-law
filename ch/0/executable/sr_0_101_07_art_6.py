"""SR 0.101.07 Art. 6

Generated from: ch/0/de/0.101.07.md
"""

from openfisca_core import Variable

class TerritoryBoundByProtocol(Variable):
    value_type = bool
    label = "Whether the territory is bound by the protocol"
    definition period = "P1Y"
    definition_entity = "Country"
    definition_variable = "territory"

    formula = """
        if the country has ratified the protocol, then
            if the territory is one of the territories explicitly mentioned in the ratification document, then
                return true
            else if one of the following conditions is true:
                the country has made a declaration extending the protocol to this territory,
                the country has made a declaration amending the application of the protocol to include this territory,
            then
                return true
            else
                return false
        else
            return false
    """
