"""SR 0.101.09 Art. 2

Generated from: ch/0/de/0.101.09.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

Here is a possible OpenFisca variable that inherits from Variable and implements a formula method, using a Python dictionary to reflect the titles of the articles of the protocols.

class ProtocolsVariable(Variable):
    def label(self):
        return "Protocols"
    
    def entity_class(self):
        return Person
    
    def define_parameters(self):
        parameters = self.init_parameters()
        titles = {
            1: ["..."],
            2: ["..."],
            3: ["..."],
            4: ["...", "Absatz 3)],
            5: ["...", "Absatz 3),", "Absatz 5)"],
            6: ["...", "Absatz 2)"],
            7: ["...", "Absatz 4),", "Absatz 6),"],
            8: ["..."]
        }
        for key, value in titles.items():
            parameters.add(parameter.ScalarParameter(
                key=str(key)+".title",
                default=value,
                title="Title of Article " + str(key),
                range=self.period
            ))
        return parameters

    def formula(self, period, parameters):
        title_1 = parameters[str(1)+".title"](period)
        title_2 = parameters[str(2)+".title"](period)
        title_3 = parameters[str(3)+".title"](period)
        title_4 = parameters[str(4)+".title"](period)
        title_5 = parameters[str(5)+".title"](period)
        # titles are concatenated here, for simplicity. In a real-world application, formatting would be more complex.
        return ', '.join([title_1, title_2, title_3, title_4, title_5])
