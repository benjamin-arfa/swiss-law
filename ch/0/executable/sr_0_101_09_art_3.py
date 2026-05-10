"""SR 0.101.09 Art. 3

Generated from: ch/0/de/0.101.09.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class BindToProtocol(Variable):
    value_type = bool
    label = u"Has the protocol been signed with or without reservation?"
    entity = Person
    definition_period = YEAR

    def formula_1(ax, period, params):
        return (
            True if (
                np.any((ax('signed_protocol', period) == True))
                or
                np.any((ax('ratified_protocol', period) == True))
                or
                np.any((ax('accepted_protocol', period) == True))
                or
                np.any((ax('approved_protocol', period) == True))
            )
            else False
        )

    # Added parameter to control whether ratification counts
    def formula_signature_status(ax, period, params):
        return (
            True # if signed without reservation
            if (np.any((ax('signed_without_reservation', period) == True)))
            else
            (
                True # if signed with reservation and either accepted, approved, ratified
                if ((signed_with_reservation := np.any((ax('signed_with_reservation', period) == True)))
                    and 
                    (
                        np.any((ax('accepted_protocol', period) == True))
                        or
                        np.any((ax('approved_protocol', period) == True))
                        or
                        np.any((ax('ratified_protocol', period) == True))
                    ))
                else False
            )
        )
