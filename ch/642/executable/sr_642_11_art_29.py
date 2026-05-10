"""SR 642.11 Art. 29

Generated from: ch/642/de/642.11.md

Art. 29 Rueckstellungen (Provisions):
1. Provisions charged to the profit and loss account are permitted for:
   a. existing obligations in the fiscal year whose amount is still undetermined;
   b. loss risks associated with current assets, particularly goods and debtors;
   c. other immediately threatening loss risks existing in the fiscal year;
   d. future R&D contracts with third parties, up to 10% of taxable business
      income, but no more than CHF 1,000,000 in total.
2. Previous provisions are added back to taxable business income insofar as
   they are no longer justified.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ifd_steuerbarer_geschaeftsertrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerbarer Geschaeftsertrag vor Rueckstellungen (CHF)"
    reference = "SR 642.11 Art. 29 Abs. 1 Bst. d"


class ifd_rueckstellung_verpflichtungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Rueckstellungen fuer bestehende Verpflichtungen unbestimmter Hoehe (CHF)"
    reference = "SR 642.11 Art. 29 Abs. 1 Bst. a"


class ifd_rueckstellung_verlustrisiken_umlauf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Rueckstellungen fuer Verlustrisiken auf Umlaufvermoegen (CHF)"
    reference = "SR 642.11 Art. 29 Abs. 1 Bst. b"


class ifd_rueckstellung_drohende_verluste(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Rueckstellungen fuer unmittelbar drohende Verlustrisiken (CHF)"
    reference = "SR 642.11 Art. 29 Abs. 1 Bst. c"


class ifd_fe_auftraege_dritte_geplant(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Geplante Forschungs- und Entwicklungsauftraege an Dritte (CHF)"
    reference = "SR 642.11 Art. 29 Abs. 1 Bst. d"


class ifd_rueckstellung_fe_auftraege(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zulassige Rueckstellung fuer F&E-Auftraege an Dritte (CHF)"
    reference = "SR 642.11 Art. 29 Abs. 1 Bst. d"

    def formula(person, period, parameters):
        geplant = person('ifd_fe_auftraege_dritte_geplant', period)
        ertrag = person('ifd_steuerbarer_geschaeftsertrag', period)

        p = parameters(period).sr_642_11

        # Max 10% of taxable business income
        plafond_prozent = ertrag * p.provision_rd_rate

        # Absolute cap of CHF 1,000,000
        plafond_absolut = p.provision_rd_max

        plafond = min_(plafond_prozent, plafond_absolut)
        return min_(geplant, max_(plafond, 0))


class ifd_rueckstellungen_nicht_mehr_begruendet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufzuloesende Rueckstellungen, die nicht mehr begruendet sind (CHF)"
    reference = "SR 642.11 Art. 29 Abs. 2"


class ifd_rueckstellungen_netto(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Netto-Effekt der Rueckstellungen auf den steuerbaren Ertrag (CHF, negativ = Abzug)"
    reference = "SR 642.11 Art. 29"

    def formula(person, period, parameters):
        verpflichtungen = person('ifd_rueckstellung_verpflichtungen', period)
        verlustrisiken = person('ifd_rueckstellung_verlustrisiken_umlauf', period)
        drohend = person('ifd_rueckstellung_drohende_verluste', period)
        fe = person('ifd_rueckstellung_fe_auftraege', period)
        aufzuloesen = person('ifd_rueckstellungen_nicht_mehr_begruendet', period)

        # Neue Rueckstellungen mindern, Aufloesungen erhoehen den Ertrag
        neue_rueckstellungen = verpflichtungen + verlustrisiken + drohend + fe
        return aufzuloesen - neue_rueckstellungen
