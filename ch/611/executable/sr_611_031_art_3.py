"""SR 611.031 Art. 3

Generated from: ch/611/de/611.031.md

Gottfried-Keller-Stiftung - Art. 3: Verwendung der Erträge.
Erträge für Anschaffung bedeutender Kunstwerke und Erhaltung bestehender
Kunstwerke mit öffentlicher Zweckbestimmung. Sonderregel im Kriegsfall.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_bedeutendes_kunstwerk(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Werk ist ein bedeutendes Werk der bildenden Kunst des In- oder Auslands"
    reference = "SR 611.031 Art. 3 Abs. 1 lit. a"


class ist_zeitgenoessisches_kunstwerk(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kunstwerk ist zeitgenössisch"
    reference = "SR 611.031 Art. 3 Abs. 1 lit. a"


class ertraege_verwendbar_fuer_anschaffung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Erträge können für Anschaffung dieses Werks verwendet werden "
        "(Art. 3 Abs. 1 lit. a)"
    )
    reference = "SR 611.031 Art. 3 Abs. 1 lit. a"

    def formula(person, period, parameters):
        # Abs. 1 lit. a: Anschaffung bedeutender Werke der bildenden Kunst,
        # zeitgenössische nur ausnahmsweise
        bedeutend = person('ist_bedeutendes_kunstwerk', period)
        zeitgenoessisch = person('ist_zeitgenoessisches_kunstwerk', period)
        ausnahme_genehmigt = person('ausnahme_zeitgenoessisch_genehmigt', period)
        return bedeutend * (1 - zeitgenoessisch + zeitgenoessisch * ausnahme_genehmigt)


class ausnahme_zeitgenoessisch_genehmigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausnahme für zeitgenössisches Kunstwerk wurde genehmigt"
    reference = "SR 611.031 Art. 3 Abs. 1 lit. a"


class hat_oeffentliche_zweckbestimmung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kunstwerk hat eine dem Land dauerhaft gesicherte öffentliche Zweckbestimmung"
    reference = "SR 611.031 Art. 3 Abs. 1 lit. b"


class gelegenheit_zur_anschaffung_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gelegenheit zur Anschaffung nach lit. a bietet sich"
    reference = "SR 611.031 Art. 3 Abs. 2"


class ertraege_verwendbar_fuer_erhaltung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Erträge können für Erstellung/Erhaltung bestehender Kunstwerke "
        "verwendet werden (Art. 3 Abs. 1 lit. b / Abs. 2)"
    )
    reference = "SR 611.031 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        # Abs. 2: Nur wenn sich zu Anschaffungen nach lit. a keine Gelegenheit bietet
        # Höchstens die Hälfte des Jahresertrags
        hat_zweck = person('hat_oeffentliche_zweckbestimmung', period)
        keine_anschaffung = 1 - person('gelegenheit_zur_anschaffung_vorhanden', period)
        return hat_zweck * keine_anschaffung


class max_anteil_ertrag_fuer_erhaltung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Anteil des Jahresertrags für Erhaltung nach lit. b (Art. 3 Abs. 2)"
    reference = "SR 611.031 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        # Art. 3 Abs. 2: Höchstens die Hälfte des Jahresertrags
        return 0.5


class eidgenossenschaft_im_krieg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eidgenossenschaft ist mit dem Ausland in Krieg verwickelt"
    reference = "SR 611.031 Art. 3 Abs. 3"


class ertraege_fuer_verwundete_pflegebeduerftiger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Verfügbare Mittel sind für Pflege verwundeter und kranker "
        "Wehrmänner zu verwenden (Art. 3 Abs. 3)"
    )
    reference = "SR 611.031 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        return person('eidgenossenschaft_im_krieg', period)
