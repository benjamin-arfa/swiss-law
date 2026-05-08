"""SR 941.421.11 Art. 1

Generated from: ch/941/de/941.421.11.md

Art. 1: Freimengen und Konzentrationen
- Abs. 1: Vorlaeufer mit Zugangsbeschraenkungen duerfen ohne Bewilligung
  im Fachhandel abgegeben werden bis:
  a. Wasserstoffperoxid: 25 ml bei 35% Konzentration
  b. Nitromethan: 25 ml bei 100% Konzentration
- Abs. 2: Bei tieferen Konzentrationen erhoeht sich die Freimenge entsprechend.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vvsg_stoff_typ(Variable):
    """1 = Wasserstoffperoxid, 2 = Nitromethan"""
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Typ des Vorlaeufer-Stoffs (1=Wasserstoffperoxid, 2=Nitromethan)"
    reference = "SR 941.421.11 Art. 1 Abs. 1"


class vvsg_konzentration_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Konzentration des Vorlaeufer-Stoffs in Prozent"
    reference = "SR 941.421.11 Art. 1"


class vvsg_menge_ml(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Abgegebene Menge des Vorlaeufer-Stoffs in Millilitern"
    reference = "SR 941.421.11 Art. 1"


class vvsg_max_konzentration(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Referenz-Konzentration fuer den jeweiligen Stoff (%)"
    reference = "SR 941.421.11 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        stoff = person('vvsg_stoff_typ', period)
        return select(
            [stoff == 1, stoff == 2],
            [35.0, 100.0],
            default=0.0,
        )


class vvsg_freimenge_ml(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Freimenge ohne Erwerbs- oder Ausnahmebewilligung (ml), "
        "angepasst bei tieferer Konzentration"
    )
    reference = "SR 941.421.11 Art. 1"

    def formula(person, period, parameters):
        stoff = person('vvsg_stoff_typ', period)
        konzentration = person('vvsg_konzentration_prozent', period)
        max_konz = person('vvsg_max_konzentration', period)

        # Basis-Freimenge ist 25 ml bei Referenz-Konzentration
        basis_freimenge = parameters(period).vvsg.basis_freimenge_ml

        # Abs. 2: Bei tieferer Konzentration erhoeht sich die Freimenge
        # proportional: Freimenge = 25 ml * (max_konz / tatsaechliche_konz)
        freimenge = where(
            konzentration > 0,
            basis_freimenge * (max_konz / konzentration),
            0.0,
        )
        return freimenge


class vvsg_abgabe_ohne_bewilligung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Abgabe ohne Erwerbs- oder Ausnahmebewilligung zulaessig"
    reference = "SR 941.421.11 Art. 1"

    def formula(person, period, parameters):
        menge = person('vvsg_menge_ml', period)
        freimenge = person('vvsg_freimenge_ml', period)
        stoff = person('vvsg_stoff_typ', period)
        # Nur fuer bekannte Stoffe und innerhalb der Freimenge
        return (stoff > 0) * (menge <= freimenge)
