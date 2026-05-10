"""SR 442.11 Art. 2a

Generated from: ch/442/de/442.11.md

Soziale Sicherheit der Kulturschaffenden: 12% der subventionierten
Arbeitsleistungen an Pensionskasse. Spesen werden nicht beruecksichtigt
(Pauschale 20%). Anteile unter 50 CHF werden nicht ueberwiesen.
Frist: 60 Tage nach positivem Entscheid. Verfall nach 5 Jahren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kulturschaffender_ahv_versichert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kulturschaffende bei der AHV versichert ist"
    reference = "SR 442.11 Art. 2a Abs. 1"


class subventionierte_arbeitsleistungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Subventionierte Arbeitsleistungen (CHF)"
    reference = "SR 442.11 Art. 2a Abs. 3"


class spesen_bekannt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Spesen mit vertretbarem Aufwand feststellbar sind"
    reference = "SR 442.11 Art. 2a Abs. 3"


class spesen_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag der Spesen und aehnlichen Kosten (CHF)"
    reference = "SR 442.11 Art. 2a Abs. 3"


class berechnungsgrundlage_soziale_sicherheit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Berechnungsgrundlage fuer den Anteil soziale Sicherheit (nach Abzug Spesen)"
    reference = "SR 442.11 Art. 2a Abs. 3"

    def formula(person, period, parameters):
        arbeitsleistungen = person('subventionierte_arbeitsleistungen', period)
        spesen_known = person('spesen_bekannt', period)
        spesen = person('spesen_betrag', period)
        # Wenn Spesen bekannt: Arbeitsleistungen - Spesen
        # Wenn nicht bekannt: Arbeitsleistungen - 20% pauschal
        pauschale = arbeitsleistungen * 0.20
        abzug = spesen_known * spesen + (1 - spesen_known) * pauschale
        return arbeitsleistungen - abzug


class beitrag_soziale_sicherheit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Beitrag an Pensionskasse/Vorsorge (12%, min 50 CHF, sonst 0)"
    reference = "SR 442.11 Art. 2a Abs. 3"

    def formula(person, period, parameters):
        grundlage = person('berechnungsgrundlage_soziale_sicherheit', period)
        ahv = person('kulturschaffender_ahv_versichert', period)
        beitrag = grundlage * 0.12
        # Anteile unter 50 CHF werden nicht ueberwiesen
        return ahv * beitrag * (beitrag >= 50)
