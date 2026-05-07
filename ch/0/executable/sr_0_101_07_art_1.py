"""SR 0.101.07 Art. 1

Generated from: ch/0/de/0.101.07.md
"""

from openfisca_core.variables import Variable
from openfisca_core.periods import ETD

class person_received_expulsion_decision(Variable):
    value_type = bool
    entity = Person
    definition_period = ETD
    reference = "Art. 1 SR 0.101.07"

    def formula(person, period, parameters):
        # Legal order made
        has_legal_order = person("has_legal_order", period)  # to be defined separately
        # Provided opportunity to
        # a) Gründe vorzubringen
        has_grund_vorzubringen = person("has_grund_vorzubringen", period)  # to be defined separately
        # b) Fallen prüfen
        has_fall_prufen = person("has_fall_prufen", period)  # to be defined separately
        # c) Sich vertreten
        has_sich_vertreten = person("has_sich_vertreten", period)  # to be defined separately
        # No need to exercise rights if
        # a) Im Interesse der öffentlichen Ordnung
        public_interest = person("public_interest", period)  # to be defined separately
        # b) Gründe der nationalen Sicherheit
        national_security = person("national_security", period)  # to be defined separately

        return (
            not (has_legal_order
                 and has_grund_vorzubringen
                 and has_fall_prufen
                 and has_sich_vertreten)
            and (public_interest or national_security)
        )
The variable `person_received_expulsion_decision` represents the key concept of the legal article. It will be true if the individual has not been given the opportunity to exercise their rights or if the expulsion is in the public interest or national security.
