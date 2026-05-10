"""SR 414.110.21 Art. 19

Generated from: ch/414/de/414.110.21.md

Beschlussfassung der ETH-Beschwerdekommission:
1. Beschlussfaehig mit mindestens 4 Mitgliedern anwesend.
   Beschluesse mit einfachem Mehr der Anwesenden.
2. Zirkularweg: Mehrheit aller Kommissionsmitglieder erforderlich.
3. Mitglieder sind zur Stimmabgabe verpflichtet.
4. Bei Stimmengleichheit gibt die Stimme des Praesidenten den Ausschlag.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vethbk_anzahl_anwesende(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl anwesender Kommissionsmitglieder"
    reference = "SR 414.110.21 Art. 19 Abs. 1"


class vethbk_ist_zirkularverfahren_abstimmung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Abstimmung im Zirkularverfahren stattfindet"
    reference = "SR 414.110.21 Art. 19 Abs. 2"


class vethbk_ja_stimmen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Ja-Stimmen"
    reference = "SR 414.110.21 Art. 19"


class vethbk_praesident_stimmt_ja(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Praesident mit Ja stimmt (Stichentscheid)"
    reference = "SR 414.110.21 Art. 19 Abs. 4"


class vethbk_ist_beschlussfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Kommission beschlussfaehig ist"
    reference = "SR 414.110.21 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        anwesende = person('vethbk_anzahl_anwesende', period)
        quorum = parameters(period).sr_414_110_21.quorum
        return anwesende >= quorum


class vethbk_beschluss_angenommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Beschluss angenommen ist"
    reference = "SR 414.110.21 Art. 19"

    def formula(person, period, parameters):
        ist_zirkular = person('vethbk_ist_zirkularverfahren_abstimmung', period)
        ja_stimmen = person('vethbk_ja_stimmen', period)
        anwesende = person('vethbk_anzahl_anwesende', period)
        praesident_ja = person('vethbk_praesident_stimmt_ja', period)
        total_mitglieder = parameters(period).sr_414_110_21.total_mitglieder

        # Sitzung: einfaches Mehr der Anwesenden
        nein_stimmen_sitzung = anwesende - ja_stimmen
        angenommen_sitzung = where(
            ja_stimmen > nein_stimmen_sitzung,
            True,
            where(
                ja_stimmen == nein_stimmen_sitzung,
                praesident_ja,  # Stichentscheid
                False
            )
        )

        # Zirkular: Mehrheit aller Mitglieder
        angenommen_zirkular = ja_stimmen > (total_mitglieder / 2)

        beschlussfaehig = person('vethbk_ist_beschlussfaehig', period)

        return beschlussfaehig * where(
            ist_zirkular,
            angenommen_zirkular,
            angenommen_sitzung
        )
