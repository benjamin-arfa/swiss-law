"""SR 833.11 Art. 1 & 2

Generated from: ch/833/de/833.11.md

Art. 1: Militär- und Zivilschutzdienst - Military and civil protection service:
- Covered: persons fulfilling military duty under MG and civil protection duty
- NOT covered: off-duty equipment maintenance, preparatory work

Art. 2: Berufsmilitär, Zeitmilitär und Instruktoren:
- Professional military: career officers, NCOs, soldiers, candidates, senior staff officers
- Temporary military: temporary officers, NCOs, soldiers
- BABS instructors: head of civil protection division, training leaders, instructors
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class mvv_im_militaerdienst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person leistet obligatorischen oder freiwilligen Militärdienst"
    reference = "SR 833.11 Art. 1 Abs. 1"


class mvv_im_zivilschutzdienst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person leistet obligatorischen oder freiwilligen Zivilschutzdienst"
    reference = "SR 833.11 Art. 1 Abs. 3"


class mvv_ausserdienstliche_pflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person erfüllt ausserdienstliche Pflichten (Bekleidung, Ausrüstung, Bewaffnung)"
    reference = "SR 833.11 Art. 1 Abs. 4"


class mvv_ist_berufsmilitaer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Berufsmilitär (Berufsoffizier, -unteroffizier, -soldat, Anwärter, höherer Stabsoffizier)"
    reference = "SR 833.11 Art. 2 Abs. 1"


class mvv_ist_zeitmilitaer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Zeitmilitär (Zeitoffizier, -unteroffizier, -soldat)"
    reference = "SR 833.11 Art. 2 Abs. 2"


class mvv_ist_babs_instruktor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Instruktor des Bundesamtes für Bevölkerungsschutz"
    reference = "SR 833.11 Art. 2 Abs. 3"


class mvv_bundeshaftung_grundlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Voraussetzungen der Bundeshaftung (Militärversicherung) sind erfüllt"
    reference = "SR 833.11 Art. 1"

    def formula(person, period, parameters):
        militaer = person('mvv_im_militaerdienst', period)
        zivilschutz = person('mvv_im_zivilschutzdienst', period)
        ausserdienstlich = person('mvv_ausserdienstliche_pflicht', period)
        # Covered if in military or civil protection service, but NOT if merely doing off-duty duties
        return (militaer + zivilschutz) * (1 - ausserdienstlich) > 0
