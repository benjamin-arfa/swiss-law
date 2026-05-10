"""SR 950.1 Art. 25–26

Generated from: ch/950/de/950.1.md

Interessenkonflikte und Entschaedigungen durch Dritte:
- Art. 25: Organisatorische Vorkehrungen zur Vermeidung von
  Interessenkonflikten. Bei Unvermeidbarkeit: Offenlegung.
- Art. 26: Entschaedigungen von Dritten (Retrozessionen/Kickbacks):
  Nur zulaessig wenn (a) Kunde vorgaengig informiert und
  ausdruecklich verzichtet, oder (b) Entschaedigung vollumfaenglich
  an Kunden weitergegeben. Information muss Art und Umfang umfassen
  (oder Berechnungsgrundlagen falls Betrag nicht bestimmbar).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fidleg_interessenkonflikte_vorkehrungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Organisatorische Vorkehrungen gegen Interessenkonflikte getroffen"
    reference = "SR 950.1 Art. 25 Abs. 1"


class fidleg_interessenkonflikte_offengelegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unvermeidbare Interessenkonflikte offengelegt (Art. 25 Abs. 2)"
    reference = "SR 950.1 Art. 25 Abs. 2"


class fidleg_drittentschaedigung_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag der Entschaedigung von Dritten / Retrozessionen (CHF)"
    reference = "SR 950.1 Art. 26"


class fidleg_kunde_hat_verzichtet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kunde hat ausdruecklich auf Herausgabe der Drittentschaedigung verzichtet"
    reference = "SR 950.1 Art. 26 Abs. 1 lit. a"


class fidleg_entschaedigung_weitergegeben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Drittentschaedigung vollumfaenglich an Kunden weitergegeben"
    reference = "SR 950.1 Art. 26 Abs. 1 lit. b"


class fidleg_drittentschaedigung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Annahme der Drittentschaedigung ist zulaessig"
    reference = "SR 950.1 Art. 26"

    def formula_2020(person, period, parameters):
        import numpy as np

        betrag = person('fidleg_drittentschaedigung_betrag', period)
        verzichtet = person('fidleg_kunde_hat_verzichtet', period)
        weitergegeben = person('fidleg_entschaedigung_weitergegeben', period)

        # Kein Betrag -> zulaessig (nichts anzunehmen)
        kein_betrag = betrag <= 0
        # Lit. a: informiert und verzichtet ODER lit. b: weitergegeben
        return kein_betrag + (verzichtet + weitergegeben)


class fidleg_art_25_26_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Art. 25-26 Interessenkonflikte und Retrozessionen konform"
    reference = "SR 950.1 Art. 25–26"

    def formula_2020(person, period, parameters):
        vorkehrungen = person('fidleg_interessenkonflikte_vorkehrungen', period)
        zulaessig = person('fidleg_drittentschaedigung_zulaessig', period)

        return vorkehrungen * zulaessig
