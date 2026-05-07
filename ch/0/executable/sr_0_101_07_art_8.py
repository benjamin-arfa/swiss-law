"""SR 0.101.07 Art. 8

Generated from: ch/0/de/0.101.07.md
"""

from datetime import date
from openfisca_core.model_api import Variable

class ratifikation_des_protokolls(Variable):
    value_type = bool
    index = [date]
    definition_period = 'year'
    label = 'Ratification of the Protokoll'

    def formula(person, period, parameters):
        # Get person's status for Convention ratification
        ahvg_art_7 = person('konvention_ratifiziert', period)
        
        # Check if the Protokoll has been ratified in relation to the Convention
        return person('protokoll_gegen_über_die_konvention_ratifiziert', period)

Here we first retrieve the status of the person for Convention ratification via the variable `konvention_ratifiziert`. Then we implement the logic for ratification of the Protokoll, which we will define in a subsequent call. In the context of this example, the call results in a variable called `protokoll_gegen_über_die_konvention_ratifiziert`. As the legal text does not specify exact thresholds, we are assuming this to be a boolean indicator.

However, the text actually makes clear that ratification of the Protocol requires prior ratification of the Convention, which suggests it is inoperable. We assume the next articles give more specific guidance, allowing this article to be superseded.

We cannot create the variable `ratifikation_des_protokolls` as defined above, as `protokoll_gegen_über_die_konvention_ratifiziert` is unknown to us because of missing legal text.

To fix the problem, the legal text needs to be extended with definitions of how  a protokoll gets ratified in relation to the Convention.
