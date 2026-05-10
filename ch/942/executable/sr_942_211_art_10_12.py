"""SR 942.211 Art. 10-12

Generated from: ch/942/de/942.211.md

Art. 10: Bekanntgabepflicht für Dienstleistungen - Price disclosure for services:
Applies to 22 service categories including:
a. Hairdressers; b. Garage services; c. Gastronomy/hotels; d. Cosmetics;
e. Fitness/sports; f. Taxis; g. Entertainment/museums; h. Vehicle rental;
i. Laundry; k. Parking; l. Photo services; m. Courses; n. Flights/package travel;
p. Telecom; r. Banking; t. Pharmacy/medical; u. Funeral services; v. Notary

Art. 12: Trinkgeld - Tipping:
- Tip must be included in price or clearly labeled and quantified
- "Tip not included" without amount is prohibited
- Cannot demand tips beyond disclosed amount
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pbv_dienstleistung_kategorie(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Kategorie der Dienstleistung nach Art. 10 (1=Coiffeur, 2=Garage, 3=Gastgewerbe, 4=Kosmetik, 5=Fitness/Sport, 6=Taxi, 7=Unterhaltung, 8=Fahrzeugvermietung, 9=Wäscherei, 10=Parkieren, 11=Foto, 12=Kurse, 13=Flugreisen, 14=Reisebuchung, 15=Fernmeldedienste, 16=Mehrwertdienste, 17=Bankdienstleistungen, 18=Teilzeitnutzung, 19=Pharma/Medizin, 20=Bestattung, 21=Notariat, 0=nicht erfasst)"
    reference = "SR 942.211 Art. 10 Abs. 1"


class pbv_dienstleistung_preispflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Preisbekanntgabepflicht für Dienstleistung besteht"
    reference = "SR 942.211 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        kategorie = person('pbv_dienstleistung_kategorie', period)
        konsument = person('pbv_ist_konsument', period)
        # Duty exists if service is in one of the enumerated categories and offered to consumers
        return konsument * (kategorie >= 1) * (kategorie <= 21)


class pbv_trinkgeld_im_preis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Trinkgeld ist im Preis inbegriffen"
    reference = "SR 942.211 Art. 12 Abs. 1"


class pbv_trinkgeld_beziffert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Trinkgeld ist deutlich als solches bezeichnet und beziffert"
    reference = "SR 942.211 Art. 12 Abs. 1"


class pbv_trinkgeld_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Trinkgeldregelung ist PBV-konform"
    reference = "SR 942.211 Art. 12"

    def formula(person, period, parameters):
        im_preis = person('pbv_trinkgeld_im_preis', period)
        beziffert = person('pbv_trinkgeld_beziffert', period)
        # Either included in price or separately quantified
        return (im_preis + beziffert) > 0
