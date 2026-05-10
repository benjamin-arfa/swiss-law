"""SR 744.103 Art. 13

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class auslaendische_behoerde_kontaktstelle_gemeldet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausländische Behörde hat dem BAV eine Kontaktstelle mitgeteilt (Art. 13 Abs. 1)"
    reference = "SR 744.103 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        return person('kontaktstelle_benannt_und_gemeldet', period)


class kontaktstelle_benannt_und_gemeldet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Als Kontaktstelle benannt und dem BAV mitgeteilt"
    reference = "SR 744.103 Art. 13 Abs. 1"


class kontaktstelle_nach_eu_verordnung_1071_2009_art18(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Von EU-Mitgliedstaat oder EFTA-EWR-Staat benannte Kontaktstelle "
        "gemäss Art. 18 Abs. 1 der Verordnung (EG) Nr. 1071/2009"
    )
    reference = "SR 744.103 Art. 13 Abs. 2"


class ist_eu_oder_efta_ewr_staat_kontaktstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kontaktstelle eines EU-Mitgliedstaats oder eines EFTA-Staats im EWR"
    reference = "SR 744.103 Art. 13 Abs. 2"

    def formula(person, period, parameters):
        return person('kontaktstelle_nach_eu_verordnung_1071_2009_art18', period)


class bav_abrufverfahren_zugang_berechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Zugang im Abrufverfahren zu STUG-Daten (Art. 9 Abs. 3 Bst. a, d, e) "
        "gemäss Art. 13 BAV-Verordnung 744.103"
    )
    reference = "SR 744.103 Art. 13"

    def formula(person, period, parameters):
        # Abs. 1: BAV kann Zugang gewähren wenn Kontaktstelle gemeldet
        kontaktstelle_gemeldet = person('auslaendische_behoerde_kontaktstelle_gemeldet', period)

        # Abs. 2: Zugang haben die nach Art. 18 Abs. 1 VO (EG) 1071/2009
        # von EU- bzw. EFTA-EWR-Staaten benannten Kontaktstellen
        eu_efta_ewr_kontaktstelle = person('ist_eu_oder_efta_ewr_staat_kontaktstelle', period)

        return kontaktstelle_gemeldet * eu_efta_ewr_kontaktstelle
