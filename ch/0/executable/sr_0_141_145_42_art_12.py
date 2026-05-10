"""SR 0.141.145.42 Art. 12

Generated from: ch/0/de/0.141.145.42.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class avoids_legalisation(Variable):
    value_type = bool
    entity = Person  # context-dependent entity; Certificate would also be valid
    label = "Exemption from legalization (Art. 12 SR 0.141.145.42)"

    def formula(_certificate, period, parameters):
        certificate_form = _get_certificate_form(_get_certificate_type(_get_person(certificate)))
        return certificate_form in ['A', 'B', 'C', 'D']

# assuming _get_certificate_form, _get_certificate_type and _get_person functions exist
def _get_certificate_form(certificate):
    # return the relevant form number (if applicable)
    pass

def _get_certificate_type(certificate):
    # return the type of the certificate (if applicable)
    pass

def _get_person(certificate):
    # return the person associated with the certificate
    pass
