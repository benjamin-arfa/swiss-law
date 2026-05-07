"""SR 0.142.116.822 Art. 4

Generated from: ch/0/de/0.142.116.822.md
"""

Note: In OpenFisca, we typically model a problem space with entities, variables, parameters, and functions. Given the nature of this article, we can define a set of variables to track the various categories of people and the documents they need to provide.

Below is an example:

from openfisca_core.model_api import *

class document_type(EntityEnum):
    LETTER = 1
    OFFICIAL_INVITATION = 2
    CERTIFICATE_OF_EMPLOYMENT = 3
    CONFIRMATION_OF_PARTICIPATION = 4

class document(Entity):
    category = EnumSelector(document_type)
    purpose = String(max_length=100)
    issued_to = String(max_length=100)
    issued_by = String(max_length=100)
    issued_date = Date

class visa_category(EntityEnum):
    OFFICIALS = 1
    BUSINESSPEOPLE = 2
    DRIVERS = 3
    # ... and so on

class person(Entity):
    name = String(max_length=100)
    birth_date = Date
    nationality = EnumSelector(['SRB', 'CH'])
    visa_category = EnumSelector(visa_category)
    documents = ListOf(document)

This example models the entities, variables, and relationships described in the article.
