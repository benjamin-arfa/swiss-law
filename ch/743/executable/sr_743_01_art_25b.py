"""SR 743.01 Art. 25b

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Ausuebung einer sicherheitsrelevanten Taetigkeit
in dienstunfaehigem Zustand.
Angetrunken: Busse (oder bis 3 Jahre Freiheitsstrafe bei qualifizierter BAK).
Betaeubungsmittel/andere Gruende: Freiheitsstrafe bis 3 Jahre oder Geldstrafe.
Vorgesetzte: gleiche Strafandrohung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class seilbahn_person_qualifizierte_blutalkoholkonzentration(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine qualifizierte Blutalkoholkonzentration vorliegt"
    reference = "SR 743.01 Art. 25b Abs. 1"


class seilbahn_person_sicherheitsrelevante_taetigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person eine sicherheitsrelevante Taetigkeit im Seilbahnbereich ausuebte"
    reference = "SR 743.01 Art. 25b"


class seilbahn_strafe_dienstunfaehig_taetigkeit(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Strafandrohung bei Ausuebung sicherheitsrelevanter Taetigkeit in dienstunfaehigem Zustand"
    reference = "SR 743.01 Art. 25b"

    def formula(person, period, parameters):
        import numpy as np
        taetigkeit = person('seilbahn_person_sicherheitsrelevante_taetigkeit', period)
        alkohol = person('seilbahn_person_unter_alkoholeinfluss', period)
        qualifiziert = person('seilbahn_person_qualifizierte_blutalkoholkonzentration', period)
        betaeubung = person('seilbahn_person_unter_betaeubungsmitteleinfluss', period)
        sonstige = person('seilbahn_person_sonstige_leistungsminderung', period)

        return np.where(
            ~taetigkeit, 'keine_strafe',
            np.where(
                alkohol & ~qualifiziert, 'busse',
                np.where(
                    alkohol & qualifiziert, 'freiheitsstrafe_bis_3_jahre_oder_geldstrafe',
                    np.where(
                        betaeubung | sonstige, 'freiheitsstrafe_bis_3_jahre_oder_geldstrafe',
                        'keine_strafe'
                    )
                )
            )
        )
