"""SR 351.6 Art. 12

Generated from: ch/351/de/351.6.md
Cost rules for cooperation with the International Criminal Court.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ersuchen_betrifft_zeugen_reisekosten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ersuchen betrifft Reisen/Sicherheit von Zeugen/Sachverstaendigen oder Uebergabe Inhaftierter"
    reference = "SR 351.6 Art. 12 Abs. 1 lit. a"


class uebersetzungskosten_anfallen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Uebersetzungs-, Dolmetsch- und Transkriptionskosten fallen an"
    reference = "SR 351.6 Art. 12 Abs. 1 lit. b"


class sachverstaendigengutachten_angefordert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gerichtshof hat Sachverstaendigengutachten oder -bericht angefordert"
    reference = "SR 351.6 Art. 12 Abs. 1 lit. d"


class ersuchen_kostenpflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ersuchen ist nicht unentgeltlich (Ausnahme von der Gratisregel)"
    reference = "SR 351.6 Art. 12 Abs. 1"

    def formula(person, period):
        zeugen = person('ersuchen_betrifft_zeugen_reisekosten', period)
        uebersetzung = person('uebersetzungskosten_anfallen', period)
        gutachten = person('sachverstaendigengutachten_angefordert', period)
        return zeugen + uebersetzung + gutachten


class haftkosten_bund_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Haftkosten die der Bund traegt in CHF"
    reference = "SR 351.6 Art. 12 Abs. 3"


class haft_angeordnet_von_zentralstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Haft wurde von der Zentralstelle angeordnet"
    reference = "SR 351.6 Art. 12 Abs. 3"


class kosten_zu_lasten_bund(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kosten gehen zu Lasten des Bundes (Haft + amtlicher Rechtsbeistand)"
    reference = "SR 351.6 Art. 12 Abs. 3"

    def formula(person, period):
        return person('haft_angeordnet_von_zentralstelle', period)
