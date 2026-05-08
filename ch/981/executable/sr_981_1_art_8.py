"""SR 981.1 Art. 8 - Festsetzung der Entschaedigungsbetraege

Generated from: ch/981/de/981.1.md

Uebersteigt die Gesamtsumme die Globalentschaedigung, werden die Betraege
entsprechend herabgesetzt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class globalentschaedigung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Verfuegbare Globalentschaedigung (CHF)"
    reference = "SR 981.1 Art. 8"


class gesamtsumme_entschaedigungen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtsumme aller Entschaedigungen (CHF)"
    reference = "SR 981.1 Art. 8"


class entschaedigung_im_abkommen_festgesetzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Entschaedigung ist im Abkommen zahlenmaaessig festgesetzt"
    reference = "SR 981.1 Art. 8"


class herabsetzungsfaktor(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Herabsetzungsfaktor wenn Gesamtsumme die Globalentschaedigung uebersteigt (0-1)"
    reference = "SR 981.1 Art. 8"

    def formula(self, period, parameters):
        globale = self('globalentschaedigung', period)
        gesamt = self('gesamtsumme_entschaedigungen', period)
        return where(gesamt > globale, globale / gesamt, 1.0)


class entschaedigungsbetrag_effektiv(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Effektiver Entschaedigungsbetrag nach allfaelliger Herabsetzung (CHF)"
    reference = "SR 981.1 Art. 8"

    def formula(self, period, parameters):
        schaden = self('schadenshoehe', period)
        faktor = self('herabsetzungsfaktor', period)
        festgesetzt = self('entschaedigung_im_abkommen_festgesetzt', period)
        # Im Abkommen festgesetzte Betraege werden nicht herabgesetzt
        return where(festgesetzt, schaden, schaden * faktor)
