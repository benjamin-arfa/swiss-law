"""SR 614.0 Art. 1

Generated from: ch/614/de/614.0.md

Finanzkontrollgesetz (FKG) - Art. 1: Stellung der Eidgenössischen
Finanzkontrolle (EFK). Die EFK ist das oberste Finanzaufsichtsorgan des
Bundes, selbständig und unabhängig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_oberstes_finanzaufsichtsorgan(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Eidgenössische Finanzkontrolle ist das oberste Finanzaufsichtsorgan "
        "des Bundes (Art. 1 Abs. 1)"
    )
    reference = "SR 614.0 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        # Art. 1 Abs. 1: Die EFK ist das oberste Finanzaufsichtsorgan des Bundes.
        # Structural/declaratory provision.
        return person('ist_eidgenoessische_finanzkontrolle', period)


class ist_eidgenoessische_finanzkontrolle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entität ist die Eidgenössische Finanzkontrolle"
    reference = "SR 614.0 Art. 1"


class efk_unterstuetzt_bundesversammlung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK unterstützt die Bundesversammlung bei der Ausübung ihrer "
        "verfassungsmässigen Finanzkompetenzen und Oberaufsicht (Art. 1 Abs. 1 lit. a)"
    )
    reference = "SR 614.0 Art. 1 Abs. 1 lit. a"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_unterstuetzt_bundesrat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK unterstützt den Bundesrat bei der Ausübung seiner Aufsicht über "
        "die Bundesverwaltung (Art. 1 Abs. 1 lit. b)"
    )
    reference = "SR 614.0 Art. 1 Abs. 1 lit. b"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_ist_selbstaendig_und_unabhaengig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK ist im Rahmen der gesetzlichen Vorschriften selbständig und "
        "unabhängig (Art. 1 Abs. 2)"
    )
    reference = "SR 614.0 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class efk_kann_sonderauftrag_ablehnen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK kann Sonderauftrag ablehnen wenn Unabhängigkeit oder "
        "Revisionsprogramm gefährdet (Art. 1 Abs. 2)"
    )
    reference = "SR 614.0 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        ist_efk = person('ist_eidgenoessische_finanzkontrolle', period)
        gefaehrdet_unabhaengigkeit = person('sonderauftrag_gefaehrdet_unabhaengigkeit', period)
        gefaehrdet_programm = person('sonderauftrag_gefaehrdet_revisionsprogramm', period)
        return ist_efk * (gefaehrdet_unabhaengigkeit + gefaehrdet_programm)


class sonderauftrag_gefaehrdet_unabhaengigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sonderauftrag gefährdet die Unabhängigkeit und Unvoreingenommenheit der EFK"
    reference = "SR 614.0 Art. 1 Abs. 2"


class sonderauftrag_gefaehrdet_revisionsprogramm(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sonderauftrag gefährdet die Abwicklung des Revisionsprogrammes der EFK"
    reference = "SR 614.0 Art. 1 Abs. 2"


class efk_administrativ_efd_beigeordnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK ist administrativ dem Eidgenössischen Finanzdepartement "
        "beigeordnet (Art. 1 Abs. 3)"
    )
    reference = "SR 614.0 Art. 1 Abs. 3"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)
