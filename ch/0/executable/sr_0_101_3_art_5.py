"""SR 0.101.3 Art. 5

Generated from: ch/0/de/0.101.3.md
"""

from openfisca_core import variable 

class Immunität_Variable(Variable):
    entity = Person
    value_type = bool
    label = u"Is there a suspension of an individual's immunität?"
    definition period = CURRENT_YEAR
    definition = """
    # Is the person in any of the periods for which this variable is defined?
    self.has_suspension == u"TRUE"
    """

    formula = formula
    period = 'any'

Here, the class `Immunität_Variable` extends the `Variable` class in OpenFisca.

We must remember to handle each period separately and consider how 'period' affects the definition of 'immunität' - in this explanation for simplicity it has been ignored.

In real code, you would create the actual OpenFisca definition file for it and store it with your definitions.

Next, we will create a YAML parameter snippet that includes the rates and thresholds found in the article. Given that we've focused on the boolean nature and the conditions in the decision process, our current YAML parameters do not contain any particular thresholds as thresholds are not specified in the given excerpt.

In practice, you could use the YAML snippet to define any threshold values required to make decisions in the formula function, if they were available.
