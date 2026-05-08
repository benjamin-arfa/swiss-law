"""SR 746.1 Art. 1

Generated from: ch/746/de/746.1.md

Rohrleitungsgesetz (RLG) - Geltungsbereich.
Anwendbar auf Rohrleitungen zur Befoerderung von Erdoel, Erdgas oder
anderen fluessigen oder gasfoermigen Brenn- oder Treibstoffen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class unterliegt_rohrleitungsgesetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anlage unterliegt dem Rohrleitungsgesetz (RLG, SR 746.1)"
    reference = "SR 746.1 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        # Art. 1 Abs. 1: Anwendbar auf Rohrleitungen zur Befoerderung
        # von Erdoel, Erdgas oder anderen bezeichneten Stoffen.
        ist_rohrleitung = person('ist_rohrleitungsanlage', period)
        ist_ausgenommen = person('rohrleitungsgesetz_ausnahme', period)
        return ist_rohrleitung * ~ist_ausgenommen


class ist_rohrleitungsanlage(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anlage ist eine Rohrleitung zur Befoerderung von fluessigen oder gasfoermigen Brenn- oder Treibstoffen"
    reference = "SR 746.1 Art. 1 Abs. 1"


class rohrleitungsgesetz_ausnahme(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rohrleitung ist vom Gesetz ausgenommen (geringe Laenge, Teil einer Lagereinrichtung)"
    reference = "SR 746.1 Art. 1 Abs. 4"


class unterliegt_rohrleitungsgesetz_voll(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rohrleitung unterliegt dem RLG in vollem Umfang (Durchmesser/Betriebsdruck ueberschreiten Grenzwerte oder Landesgrenze kreuzend)"
    reference = "SR 746.1 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        # Art. 1 Abs. 2: Voll anwendbar auf Rohrleitungen deren
        # Durchmesser und Betriebsdruck eine bestimmte Groesse ueberschreiten
        # oder die Landesgrenze kreuzen.
        ueberschreitet_grenzwerte = person('rohrleitung_ueberschreitet_grenzwerte', period)
        kreuzt_landesgrenze = person('rohrleitung_kreuzt_landesgrenze', period)
        ist_rohrleitung = person('ist_rohrleitungsanlage', period)
        return ist_rohrleitung * (ueberschreitet_grenzwerte + kreuzt_landesgrenze)


class rohrleitung_ueberschreitet_grenzwerte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Durchmesser und Betriebsdruck der Rohrleitung ueberschreiten die vom Bundesrat festgesetzten Groessen"
    reference = "SR 746.1 Art. 1 Abs. 2 lit. a"


class rohrleitung_kreuzt_landesgrenze(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rohrleitung kreuzt die Landesgrenze"
    reference = "SR 746.1 Art. 1 Abs. 2 lit. b"
