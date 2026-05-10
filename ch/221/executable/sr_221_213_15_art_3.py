"""SR 221.213.15 Art. 3

Generated from: ch/221/de/221.213.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verband_seit_mindestens_zehn_jahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verband besteht seit mindestens zehn Jahren mit Hauptzweck Vermieter-/Mieterinteressen"
    reference = "SR 221.213.15 Art. 3 Abs. 2 lit. a"


class anteil_mietende_oder_vermietende(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der vertretenen Mietenden oder Vermietenden im Geltungsbereich (0-1)"
    reference = "SR 221.213.15 Art. 3 Abs. 2 lit. b"


class anteil_einzelmietvertraege(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der Einzelmietverträge, die Mitglieder direkt oder indirekt zeichnen (0-1)"
    reference = "SR 221.213.15 Art. 3 Abs. 2 lit. b"


class verband_ist_repraesentativ(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verband ist repräsentativ im Sinne von Art. 3 Abs. 2"
    reference = "SR 221.213.15 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        seit_zehn_jahren = person('verband_seit_mindestens_zehn_jahren', period)
        anteil_mietende = person('anteil_mietende_oder_vermietende', period)
        anteil_vertraege = person('anteil_einzelmietvertraege', period)
        mitgliedschafts_kriterium = (anteil_mietende >= 0.05) + (anteil_vertraege >= 0.10)
        return seit_zehn_jahren * mitgliedschafts_kriterium


class rahmenmietvertrag_bietet_gleichwertigen_schutz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rahmenmietvertrag bietet mindestens gleichwertigen Schutz vor Missbrauch"
    reference = "SR 221.213.15 Art. 3 Abs. 1 lit. b"


class rahmenmietvertrag_nicht_gegen_zwingendes_recht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rahmenmietvertrag widerspricht nicht dem übrigen zwingenden Recht"
    reference = "SR 221.213.15 Art. 3 Abs. 1 lit. c"


class abweichung_von_zwingendem_recht_bewilligbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Abweichung von zwingenden Mietrechtsbestimmungen kann bewilligt werden"
    reference = "SR 221.213.15 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        repraesentativ = person('verband_ist_repraesentativ', period)
        gleichwertiger_schutz = person('rahmenmietvertrag_bietet_gleichwertigen_schutz', period)
        nicht_gegen_recht = person('rahmenmietvertrag_nicht_gegen_zwingendes_recht', period)
        return repraesentativ * gleichwertiger_schutz * nicht_gegen_recht
