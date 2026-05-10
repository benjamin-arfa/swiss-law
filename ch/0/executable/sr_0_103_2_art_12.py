"""SR 0.103.2 Art. 12

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unrestricted_residence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Unrestricted Residence in Switzerland in accordance to article 12 (SR 0.103.2)"

    def formula(person, period, parameters):
        works_outside_switzerland = person("works_outside_switzerland", period)
        resides_abroad = person("resides_abroad", period)
        
        # The conditions to restrict freedom of movement 
        national_security_condition = parameters(period).security.national_security_risks
        
        # All variables are combined as 'OR' with parameter security.public_order_risks 
        # because the formula should evaluate to true when any of the restrictions can be evaluated to true. 
        public_order_risks = (  # Evaluating as 'AND' if any restriction 'AND' public_order_risks 
            # Since one may not evaluate true (national_security) AND false (public_order) 
            parameters(period).security.public_order_risks
            ) 

        moves_within_swiss_territory = person("moves_within_swiss_territory", period)
        
        work_outside = (works_outside_switzerland | resides_abroad)
        # 
        return (  # All variables are combined as 'AND' to evaluate to true
            # Restrict or do nothing if restrictions may occur 
            # All variables and work_outside combined with 'OR' if restrictions cannot be evaluated to true
            not (national_security_condition & public_order_risks & (moves_within_swiss_territory | work_outside)) & (  # Using '|' for OR, 'and' for AND
            # Evaluating all restriction variables as individual boolean variables 
            national_security_condition | 
            public_order_risks | 
            parameters(period).social_health.disease_risks | 
            parameters(period).public_order.risks | 
            parameters(period).right_to_move.restrictions )
        )

# Adding metadata and description to parameters, in accordance to openfisca standard 
# so this can be exported into YAML.
parameter_yaml_1 = """#
# Variables for the implementation in OpenFisca.
#
# This file is part of the OpenFisca-CH project, and under the terms of the 
# AGPL- version 3 license.
#
# It describes the parameters and variables that are required to implement the
# calculation of the variables for social security contributions, such as the 
# one introduced with the present file.
#
# The parameters and variables described in this file are created when running
# python models/sri/params.py

security:
  national_security_risks:
    description: 'Nationale Sicherheitsrisiken'
    unit: boolean
    variable: sri.security.national_security_risks

  public_order_risks:
    description: 'Bedrohung der öffentlichen Sicherheit'
    unit: boolean
    variable: sri.public_order.risks

social_health:
  disease_risks:
    description: 'Volksgesundheitsrisiken'
    metadata:
      unit: boolean
      reference:
        - title: 'Article 12 SR 0.103.2'
          href: 'https://www.fedlex.admin.ch/eli/cc/63/837_843_843/de#art_12'
        - title: 'Article 12.2 SR 0.103.2'
          href: 'https://www.fedlex.admin.ch/eli/cc/63/837_843_843/de#art_12_2'
    variable: sri.social_health.disease_risks

public_order:
  risks:
    description: 'Bedrohung der öffentlichen Sicherheit'
    metadata:
      unit: boolean
      reference:
        - title: 'Article 12 SR 0.103.2'
          href: 'https://www.fedlex.admin.ch/eli/cc/63/837_843_843/de#art_12'
    variable: sri.public_order.risks

right_to_move:
  restrictions:
    description: 'Einschränkung des Rechtes auf freie Bewegung'
    unit: boolean
    variable: sri.right_to_move.restrictions

"""
