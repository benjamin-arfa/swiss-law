"""SR 950.1 Art. 4–5

Generated from: ch/950/de/950.1.md

Kundensegmentierung und Opting-out/Opting-in:
- Art. 4: Drei Kundensegmente: (a) Privatkundinnen/-kunden,
  (b) professionelle Kunden, (c) institutionelle Kunden.
  Professionelle Kunden: Finanzintermediaere, Versicherungen,
  oeffentlich-rechtliche Koerperschaften, Vorsorgeeinrichtungen
  mit professioneller Tresorerie, grosse Unternehmen.
  Institutionelle Kunden: beaufsichtigte Institute, Zentralbanken,
  nationale/supranationale oeffentlich-rechtliche Koerperschaften.
- Art. 5: Opting-out: Vermoegende Privatkunden (>2 Mio. CHF oder
  >500'000 CHF mit Kenntnissen) koennen professionellen Status
  waehlen. Opting-in: Professionelle koennen Privatkundenschutz
  beanspruchen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fidleg_kunde_ist_privatkunde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist Privatkunde (Art. 4 Abs. 1 lit. a)"
    reference = "SR 950.1 Art. 4 Abs. 1 lit. a"


class fidleg_kunde_ist_professionell(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist professioneller Kunde (Art. 4 Abs. 1 lit. b)"
    reference = "SR 950.1 Art. 4 Abs. 1 lit. b"


class fidleg_kunde_ist_institutionell(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist institutioneller Kunde (Art. 4 Abs. 1 lit. c)"
    reference = "SR 950.1 Art. 4 Abs. 1 lit. c"


class fidleg_vermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Vermoegen des Kunden (CHF)"
    reference = "SR 950.1 Art. 5 Abs. 1"


class fidleg_hat_finanzkenntnisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kunde verfuegt ueber erforderliche Finanzkenntnisse"
    reference = "SR 950.1 Art. 5 Abs. 1"


class fidleg_opting_out_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Privatkunde ist berechtigt zum Opting-out (professioneller Status)"
    reference = "SR 950.1 Art. 5 Abs. 1"

    def formula_2020(person, period, parameters):
        vermoegen = person('fidleg_vermoegen', period)
        kenntnisse = person('fidleg_hat_finanzkenntnisse', period)
        ist_privat = person('fidleg_kunde_ist_privatkunde', period)

        p = parameters(period).sr950_1
        # Opting-out: >2 Mio. CHF oder >500'000 mit Kenntnissen
        schwelle_hoch = p.opting_out_vermoegen_hoch
        schwelle_niedrig = p.opting_out_vermoegen_niedrig

        return ist_privat * (
            (vermoegen > schwelle_hoch)
            + ((vermoegen > schwelle_niedrig) * kenntnisse)
        )


class fidleg_effektives_kundensegment(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Effektives Kundensegment (1=Privat, 2=Professionell, 3=Institutionell)"
    reference = "SR 950.1 Art. 4–5"

    def formula_2020(person, period, parameters):
        import numpy as np

        institutionell = person('fidleg_kunde_ist_institutionell', period)
        professionell = person('fidleg_kunde_ist_professionell', period)

        return np.where(
            institutionell, 3,
            np.where(professionell, 2, 1)
        )
