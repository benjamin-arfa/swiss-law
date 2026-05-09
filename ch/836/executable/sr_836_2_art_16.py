"""SR 836.2 Art. 16

Generated from: ch/836/de/836.2.md

Art. 16: Finanzierung.
Abs. 1: Die Kantone regeln die Finanzierung der Familienzulagen
        und der Verwaltungskosten.
Abs. 2: Die Beitraege werden in Prozent des AHV-pflichtigen
        Einkommens berechnet.
Abs. 3: Die Kantone bestimmen, ob innerhalb einer FAK auf den
        AHV-pflichtigen Einkommen der Arbeitnehmer und der
        Selbstaendigerwerbenden der gleiche Beitragssatz erhoben wird.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ahv_pflichtiges_einkommen(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "AHV-pflichtiges Einkommen pro Monat"
    reference = "SR 836.2 Art. 16 Abs. 2"


class beitragssatz_familienzulage(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kantonaler Beitragssatz fuer Familienzulagen (in Prozent des AHV-pflichtigen Einkommens)"
    reference = "SR 836.2 Art. 16 Abs. 2"


class beitrag_familienzulage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Monatlicher Beitrag an die Familienausgleichskasse (Art. 16 FamZG)"
    reference = "SR 836.2 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        einkommen = person('ahv_pflichtiges_einkommen', period)
        satz = person('beitragssatz_familienzulage', period.this_year)
        # Beitraege in Prozent des AHV-pflichtigen Einkommens
        return einkommen * satz / 100
