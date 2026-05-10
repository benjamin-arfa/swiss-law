"""SR 251.6 Art. 8

Generated from: ch/251/de/251.6.md

Beschraenkungen betreffend die Vertragsaufloesung: Kuendigungsmodalitaeten
die als qualitativ schwerwiegende Beeintraechtigungen gelten.
- Befristete Vertraege >= 5 Jahre: Ankuendigung Nichtverlängerung min. 6 Monate
- Unbefristete Vertraege: Kuendigungsfrist min. 2 Jahre
- Unbefristete mit Begruendung und Entschaedigung: min. 1 Jahr
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vertrag_ist_befristet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Vertrag befristet ist"
    reference = "SR 251.6 Art. 8"


class vertragsdauer_jahre(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer des befristeten Vertrags in Jahren"
    reference = "SR 251.6 Art. 8 Bst. a"


class ankuendigungsfrist_nichtverlängerung_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Ankuendigungsfrist fuer die Nichtverlängerung in Monaten"
    reference = "SR 251.6 Art. 8 Bst. a"


class kuendigungsfrist_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Kuendigungsfrist bei unbefristetem Vertrag in Monaten"
    reference = "SR 251.6 Art. 8 Bst. b/c"


class kuendigung_schriftlich_begruendet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kuendigung schriftlich begruendet ist"
    reference = "SR 251.6 Art. 8 Bst. c"


class angemessene_entschaedigung_oder_umstrukturierung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine angemessene Entschaedigung gezahlt wird oder eine Umstrukturierung vorliegt"
    reference = "SR 251.6 Art. 8 Bst. c Ziff. 1-2"


class ist_schwerwiegende_beeintraechtigung_kuendigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vertragsaufloesungsbestimmungen eine schwerwiegende Wettbewerbsbeeintraechtigung darstellen"
    reference = "SR 251.6 Art. 8"

    def formula(person, period, parameters):
        befristet = person('vertrag_ist_befristet', period)
        dauer = person('vertragsdauer_jahre', period)
        ankuendigung = person('ankuendigungsfrist_nichtverlängerung_monate', period)
        kuendigung = person('kuendigungsfrist_monate', period)
        begruendet = person('kuendigung_schriftlich_begruendet', period)
        entschaedigung = person('angemessene_entschaedigung_oder_umstrukturierung', period)

        # Befristete Vertraege >= 5 Jahre: min. 6 Monate Ankuendigung
        befristet_verletzt = befristet * (dauer >= 5) * (ankuendigung < 6)

        # Unbefristete: min. 2 Jahre (24 Monate)
        unbefristet_standard_verletzt = not_(befristet) * (kuendigung < 24)

        # Unbefristete verkuerzt: min. 1 Jahr (12 Monate) mit Begruendung + Entschaedigung
        unbefristet_verkuerzt_ok = (
            not_(befristet)
            * begruendet
            * entschaedigung
            * (kuendigung >= 12)
        )

        # Schwerwiegend wenn befristet verletzt, oder unbefristet verletzt ohne verkuerzte Ausnahme
        return befristet_verletzt + (unbefristet_standard_verletzt * not_(unbefristet_verkuerzt_ok))
