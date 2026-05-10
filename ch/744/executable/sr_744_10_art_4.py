"""SR 744.10 Art. 4

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strassentransportunternehmen_zuverlaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuverlässigkeit des Strassentransportunternehmens gemäss Art. 5"
    reference = "SR 744.10 Art. 4 Abs. 1 lit. a"


class strassentransportunternehmen_finanziell_leistungsfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Finanzielle Leistungsfähigkeit des Strassentransportunternehmens gemäss Art. 6"
    reference = "SR 744.10 Art. 4 Abs. 1 lit. b"


class strassentransportunternehmen_fachlich_geeignet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fachliche Eignung des Strassentransportunternehmens gemäss Art. 7"
    reference = "SR 744.10 Art. 4 Abs. 1 lit. c"


class strassentransportunternehmen_sitz_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tatsächlicher und dauerhafter Sitz des Unternehmens in der Schweiz"
    reference = "SR 744.10 Art. 4 Abs. 1 lit. d"


class ist_verkehrsleiter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Verkehrsleiter oder Verkehrsleiterin"
    reference = "SR 744.10 Art. 4 Abs. 3"


class verkehrsleiter_in_anstellungs_oder_auftragsverhaeltnis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter/in steht in einem Anstellungs- oder Auftragsverhältnis zum Unternehmen"
    reference = "SR 744.10 Art. 4 Abs. 2 lit. a"


class verkehrsleiter_wohnsitz_oder_arbeitsort_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter/in hat Wohnsitz oder Arbeitsort in der Schweiz"
    reference = "SR 744.10 Art. 4 Abs. 2 lit. b"


class verkehrsleiter_auftragsverhaeltnis_anzahl_unternehmen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl der Unternehmen, die der Verkehrsleiter/in im Auftragsverhältnis leitet"
    reference = "SR 744.10 Art. 4 Abs. 5"


class verkehrsleiter_auftragsverhaeltnis_anzahl_fahrzeuge(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesamtzahl der Fahrzeuge aller Unternehmen, die der Verkehrsleiter/in im Auftragsverhältnis leitet"
    reference = "SR 744.10 Art. 4 Abs. 5"


class verkehrsleiter_auftragsverhaeltnis_grenze_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter/in im Auftragsverhältnis überschreitet nicht die Höchstgrenze von 4 Unternehmen und 50 Fahrzeugen"
    reference = "SR 744.10 Art. 4 Abs. 5"

    def formula(person, period, parameters):
        anzahl_unternehmen = person('verkehrsleiter_auftragsverhaeltnis_anzahl_unternehmen', period)
        anzahl_fahrzeuge = person('verkehrsleiter_auftragsverhaeltnis_anzahl_fahrzeuge', period)
        return (anzahl_unternehmen <= 4) * (anzahl_fahrzeuge <= 50)


class verkehrsleiter_anforderungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verkehrsleiter/in erfüllt alle Anforderungen nach Art. 4 Abs. 2: Zuverlässigkeit, fachliche Eignung, Anstellungs-/Auftragsverhältnis und Wohnsitz/Arbeitsort in der Schweiz"
    reference = "SR 744.10 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        zuverlaessig = person('strassentransportunternehmen_zuverlaessig', period)
        fachlich_geeignet = person('strassentransportunternehmen_fachlich_geeignet', period)
        anstellungsverhaeltnis = person('verkehrsleiter_in_anstellungs_oder_auftragsverhaeltnis', period)
        wohnsitz_schweiz = person('verkehrsleiter_wohnsitz_oder_arbeitsort_schweiz', period)
        return zuverlaessig * fachlich_geeignet * anstellungsverhaeltnis * wohnsitz_schweiz


class zulassungsbewilligung_strassentransportunternehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzungen für die Zulassungsbewilligung als Strassentransportunternehmen erfüllt"
    reference = "SR 744.10 Art. 4"

    def formula(person, period, parameters):
        # Abs. 1: Grundvoraussetzungen für alle Antragsteller
        zuverlaessig = person('strassentransportunternehmen_zuverlaessig', period)
        finanziell_leistungsfaehig = person('strassentransportunternehmen_finanziell_leistungsfaehig', period)
        fachlich_geeignet = person('strassentransportunternehmen_fachlich_geeignet', period)
        sitz_in_schweiz = person('strassentransportunternehmen_sitz_in_schweiz', period)
        grundvoraussetzungen = zuverlaessig * finanziell_leistungsfaehig * fachlich_geeignet * sitz_in_schweiz

        # Abs. 2 und 3: Verkehrsleiter/in-Anforderungen müssen erfüllt sein
        verkehrsleiter_ok = person('verkehrsleiter_anforderungen_erfuellt', period)

        # Abs. 3: Natürliche Person muss selbst Verkehrsleiter/in sein
        ist_vl = person('ist_verkehrsleiter', period)

        return grundvoraussetzungen * verkehrsleiter_ok * ist_vl
