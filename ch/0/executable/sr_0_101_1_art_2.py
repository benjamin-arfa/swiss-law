"""SR 0.101.1 Art. 2

Generated from: ch/0/de/0.101.1.md
"""

from openfisca_core import Variable


class has_immunity(Variable):
    value_type = bool
    axis = "individual"
    default_unit = ""

    def formula(amodel, period, institutions, parameters):
        # Entities mentioned in Article 1, Paragraph 1 have immunity
        immunity_grants = amodel.council.entities.filter(person("mentioned_in_article1", period))

        # Entities mentioned in Article 1, Paragraph 1 do not have immunity if they have revealed their statements or documents to anyone outside the Commission or the Court
        revealed_entities = amodel.council.entities.filter(reveal_statements_or_documents(period))

        return amodel.elementwise_constant(True, entities=immunity_grants - revealed_entities)

Note: `reveal_statements_or_documents()` is a new formula function representing the decision logic in Article 2, 2.
