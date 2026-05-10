"""SR 642.11 Art. 6

Generated from: ch/642/de/642.11.md

Art. 6 Umfang der Steuerpflicht (Scope of tax liability):
1. With personal affiliation, tax liability is unlimited; however it does
   not extend to business establishments, permanent establishments and
   real estate abroad.
2. With economic affiliation, tax liability is limited to those parts of
   income for which a tax liability exists in Switzerland under Art. 4/5.
   At minimum, income earned in Switzerland must be taxed.
3. Delimitation with respect to business establishments, permanent
   establishments and real estate abroad follows federal law principles
   on intercantonal double taxation. Loss-recapture rule applies within
   7 following years.
4. Persons taxable under Art. 3(5) pay tax on income for which they are
   exempt abroad under international treaties.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class steuerpflicht_unbeschraenkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Unbeschraenkte Steuerpflicht (persoenliche Zugehoerigkeit, Art. 6 Abs. 1 DBG)"
    reference = "SR 642.11 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        # Unbeschraenkte Steuerpflicht bei persoenlicher Zugehoerigkeit
        return person('steuerpflichtig_persoenliche_zugehoerigkeit', period)


class steuerpflicht_beschraenkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Beschraenkte Steuerpflicht (wirtschaftliche Zugehoerigkeit, Art. 6 Abs. 2 DBG)"
    reference = "SR 642.11 Art. 6 Abs. 2"


class hat_geschaeftsbetrieb_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat Geschaeftsbetrieb/Betriebsstaette/Grundstuecke im Ausland"
    reference = "SR 642.11 Art. 6 Abs. 1"


class einkommen_in_ch_erzielt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "In der Schweiz erzieltes Einkommen (CHF) - Minimum bei beschraenkter Steuerpflicht"
    reference = "SR 642.11 Art. 6 Abs. 2"


class verlust_auslaendische_betriebsstaette(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verluste aus auslaendischer Betriebsstaette, mit inlaendischen Gewinnen verrechnet (CHF)"
    reference = "SR 642.11 Art. 6 Abs. 3"


class gewinn_auslaendische_betriebsstaette(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewinne aus auslaendischer Betriebsstaette in den Folgejahren (CHF)"
    reference = "SR 642.11 Art. 6 Abs. 3"


class steuerbares_einkommen_umfang(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerbares Einkommen nach Umfang der Steuerpflicht (CHF)"
    reference = "SR 642.11 Art. 6"

    def formula(person, period, parameters):
        unbeschraenkt = person('steuerpflicht_unbeschraenkt', period)
        einkommen_ch = person('einkommen_in_ch_erzielt', period)
        gesamteinkommen = person('steuerbares_gesamteinkommen', period)

        # Art. 6 Abs. 1: Bei persoenlicher Zugehoerigkeit: gesamtes Einkommen
        # (ohne auslaendische Betriebsstaetten/Grundstuecke)
        # Art. 6 Abs. 2: Bei wirtschaftlicher Zugehoerigkeit: mindestens
        # das in der Schweiz erzielte Einkommen
        return where(unbeschraenkt, gesamteinkommen, einkommen_ch)
