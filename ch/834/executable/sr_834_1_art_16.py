"""SR 834.1 Art. 16

Generated from: ch/834/de/834.1.md

Mindest- und Hoechstbetrag der Gesamtentschaedigung:

Abs. 1 - Ausbildungsdienste laengerer Dauer (Mindestbetrag % vom Hoechstbetrag):
  a. ohne Kinder: 45%
  b. mit einem Kind: 65%
  c. mit >= 2 Kindern: 70%

Abs. 2 - Durchdiener in Ausbildung fuer hoeheren Grad:
  a. ohne Kinder: 37%
  b. mit einem Kind: 55%
  c. mit >= 2 Kindern: 62%

Abs. 3 - Andere Dienste:
  a. ohne Kinder: 25%
  b. mit einem Kind: 40%
  c. mit >= 2 Kindern: 50%

Abs. 4: Grundentschaedigung wird gekuerzt, soweit sie 80% des Hoechstbetrags
  uebersteigt.
Abs. 5: Gesamtentschaedigung gekuerzt auf max(vordienstliches Einkommen,
  Hoechstbetrag), aber nicht unter Mindestbetraege.
Abs. 6: Gesamtentschaedigung = Grundentschaedigung + Kinderzulagen.
  Betreuungskosten- und Betriebszulagen werden immer ungekuerzt zusaetzlich
  ausgerichtet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eo_in_ausbildungsdienst_laengerer_dauer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist in Ausbildungsdienst laengerer Dauer (Art. 16 Abs. 1 EOG)"
    reference = "SR 834.1 Art. 16 Abs. 1"


class eo_ist_durchdiener_in_ausbildung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist Durchdiener in Ausbildung fuer hoeheren Grad (Art. 16 Abs. 2 EOG)"
    reference = "SR 834.1 Art. 16 Abs. 2"


class eo_mindestbetrag_gesamtentschaedigung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Mindestbetrag der taegl. Gesamtentschaedigung (CHF)"
    reference = "SR 834.1 Art. 16"

    def formula_2005(person, period, parameters):
        import numpy as np

        anzahl_kinder = person('eo_anzahl_kinder', period)
        in_ausb_lang = person('eo_in_ausbildungsdienst_laengerer_dauer', period)
        ist_durchdiener = person('eo_ist_durchdiener_in_ausbildung', period)

        p = parameters(period).sr834_1
        hoechstbetrag = p.hoechstbetrag_gesamtentschaedigung

        # Abs. 1: Ausbildungsdienste laengerer Dauer
        mindest_abs1 = np.select(
            [anzahl_kinder == 0, anzahl_kinder == 1, anzahl_kinder >= 2],
            [
                hoechstbetrag * p.mindest_ausb_lang_ohne_kinder,
                hoechstbetrag * p.mindest_ausb_lang_ein_kind,
                hoechstbetrag * p.mindest_ausb_lang_zwei_kinder,
            ],
            default=hoechstbetrag * p.mindest_ausb_lang_ohne_kinder
        )

        # Abs. 2: Durchdiener
        mindest_abs2 = np.select(
            [anzahl_kinder == 0, anzahl_kinder == 1, anzahl_kinder >= 2],
            [
                hoechstbetrag * p.mindest_durchdiener_ohne_kinder,
                hoechstbetrag * p.mindest_durchdiener_ein_kind,
                hoechstbetrag * p.mindest_durchdiener_zwei_kinder,
            ],
            default=hoechstbetrag * p.mindest_durchdiener_ohne_kinder
        )

        # Abs. 3: Andere Dienste
        mindest_abs3 = np.select(
            [anzahl_kinder == 0, anzahl_kinder == 1, anzahl_kinder >= 2],
            [
                hoechstbetrag * p.mindest_andere_ohne_kinder,
                hoechstbetrag * p.mindest_andere_ein_kind,
                hoechstbetrag * p.mindest_andere_zwei_kinder,
            ],
            default=hoechstbetrag * p.mindest_andere_ohne_kinder
        )

        return np.where(
            in_ausb_lang,
            mindest_abs1,
            np.where(ist_durchdiener, mindest_abs2, mindest_abs3)
        )


class eo_gesamtentschaedigung_taeglich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegl. Gesamtentschaedigung nach Art. 16 EOG (CHF)"
    reference = "SR 834.1 Art. 16"

    def formula_2005(person, period, parameters):
        import numpy as np

        grundentschaedigung_rs = person('eo_grundentschaedigung_rs', period)
        grundentschaedigung_andere = person('eo_grundentschaedigung_andere_dienste', period)
        in_rs = person('eo_in_rekrutenschule', period)
        in_zs = person('eo_in_grundausbildung_zivilschutz', period)
        kinderzulage = person('eo_kinderzulage_taeglich', period)
        einkommen = person('eo_vordienstliches_erwerbseinkommen_taeglich', period)
        mindestbetrag = person('eo_mindestbetrag_gesamtentschaedigung', period)

        p = parameters(period).sr834_1
        hoechstbetrag = p.hoechstbetrag_gesamtentschaedigung

        in_rs_oder_zs = (in_rs + in_zs) > 0
        grundentschaedigung = np.where(
            in_rs_oder_zs, grundentschaedigung_rs, grundentschaedigung_andere
        )

        # Abs. 4: Grundentschaedigung max 80% des Hoechstbetrags
        max_grund = hoechstbetrag * p.max_grundentschaedigung_anteil
        grundentschaedigung = np.minimum(grundentschaedigung, max_grund)

        # Abs. 6: Gesamtentschaedigung = Grundentschaedigung + Kinderzulagen
        gesamt = grundentschaedigung + kinderzulage

        # Abs. 5: Kuerzung auf max(vordienstl. Einkommen, Hoechstbetrag),
        # aber nicht unter Mindestbetrag
        obergrenze = np.maximum(einkommen, hoechstbetrag)
        gesamt = np.minimum(gesamt, obergrenze)
        gesamt = np.maximum(gesamt, mindestbetrag)

        return gesamt
