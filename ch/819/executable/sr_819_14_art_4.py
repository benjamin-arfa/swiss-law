"""SR 819.14 Art. 4

Generated from: ch/819/de/819.14.md

Art. 4 Konformitaetsbewertungsstellen:
1. Conformity assessment bodies must be:
   a. accredited under the Accreditation and Designation Ordinance (SR 946.512); or
   b. recognized by Switzerland under an international agreement; or
   c. otherwise authorized by federal law.
1bis. Bodies performing assessments under EU Machinery Regulation 2023/1230
     must be accredited and meet Art. 30 requirements.
2. Bodies must inform competent federal authorities when type-examination
   certificates or QA system approvals are suspended, revoked, or restricted.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class maschv_stelle_akkreditiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Konformitaetsbewertungsstelle akkreditiert ist (SR 946.512)"
    reference = "SR 819.14 Art. 4 Abs. 1 Bst. a"


class maschv_stelle_international_anerkannt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Stelle im Rahmen eines internationalen Abkommens anerkannt ist"
    reference = "SR 819.14 Art. 4 Abs. 1 Bst. b"


class maschv_stelle_anderweitig_ermaechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Stelle durch Bundesrecht anderweitig ermaechtigt ist"
    reference = "SR 819.14 Art. 4 Abs. 1 Bst. c"


class maschv_stelle_zugelassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Konformitaetsbewertungsstelle zugelassen ist"
    reference = "SR 819.14 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        akkreditiert = person('maschv_stelle_akkreditiert', period)
        anerkannt = person('maschv_stelle_international_anerkannt', period)
        ermaechtigt = person('maschv_stelle_anderweitig_ermaechtigt', period)
        return akkreditiert + anerkannt + ermaechtigt
