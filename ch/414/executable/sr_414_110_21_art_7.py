"""SR 414.110.21 Art. 7

Generated from: ch/414/de/414.110.21.md

Entschaedigung und Auslagenersatz der ETH-Beschwerdekommission:
2. Praesident: Pauschale CHF 18'000/Jahr
   Vizepraesident: Pauschale CHF 6'000/Jahr
3. Pauschalen decken alle Aufwendungen (ausser Auslagenersatz)
4. Weitere Mitglieder: CHF 500/Sitzung + CHF 250 Aktenstudium
   Bei Zirkularverfahren: pauschal CHF 500
   ETH-Bereich-Angestellte erhalten keine Entschaedigung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vethbk_anzahl_sitzungen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Sitzungen, an denen das Mitglied teilgenommen hat"
    reference = "SR 414.110.21 Art. 7 Abs. 4"


class vethbk_anzahl_zirkularverfahren(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Zirkularverfahren, an denen das Mitglied teilgenommen hat"
    reference = "SR 414.110.21 Art. 7 Abs. 4"


class vethbk_ist_eth_bereich_angestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Mitglied im ETH-Bereich angestellt ist"
    reference = "SR 414.110.21 Art. 7 Abs. 4"


class vethbk_entschaedigung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche Entschaedigung des Kommissionsmitglieds (CHF)"
    reference = "SR 414.110.21 Art. 7"

    def formula(person, period, parameters):
        ist_praesident = person('vethbk_ist_praesident', period.first_month)
        ist_vize = person('vethbk_ist_vizepraesident', period.first_month)
        ist_eth_angestellt = person('vethbk_ist_eth_bereich_angestellt', period.first_month)
        anzahl_sitzungen = person('vethbk_anzahl_sitzungen', period)
        anzahl_zirkular = person('vethbk_anzahl_zirkularverfahren', period)

        p = parameters(period).sr_414_110_21
        pauschale_praesident = p.pauschale_praesident
        pauschale_vize = p.pauschale_vizepraesident
        taggeld_sitzung = p.taggeld_sitzung
        aktenstudium = p.aktenstudium_zuschlag
        zirkular_pauschale = p.zirkular_pauschale

        # Praesident und Vize erhalten Jahrespauschalen
        entschaedigung_praesidium = (
            ist_praesident * pauschale_praesident
            + ist_vize * pauschale_vize
        )

        # Weitere Mitglieder: Taggeld + Aktenstudium pro Sitzung,
        # oder Pauschale pro Zirkularverfahren
        ist_weiteres_mitglied = not_(ist_praesident) * not_(ist_vize)
        entschaedigung_sitzung = anzahl_sitzungen * (taggeld_sitzung + aktenstudium)
        entschaedigung_zirkular = anzahl_zirkular * zirkular_pauschale
        entschaedigung_weitere = ist_weiteres_mitglied * (
            entschaedigung_sitzung + entschaedigung_zirkular
        )

        # ETH-Bereich-Angestellte erhalten als weitere Mitglieder keine Entschaedigung
        entschaedigung_weitere = where(
            ist_eth_angestellt * ist_weiteres_mitglied,
            0,
            entschaedigung_weitere
        )

        return entschaedigung_praesidium + entschaedigung_weitere
