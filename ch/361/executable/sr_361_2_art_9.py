"""SR 361.2 Art. 9

Generated from: ch/361/de/361.2.md

Aufbewahrungsdauer: Verschiedene Fristen je nach Datenkategorie.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ipas_kategorie(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "IPAS-Datenkategorie (interpol, europol, nsis, afis_dna, vermisste, ausweise, ga)"
    reference = "SR 361.2 Art. 9"
    default_value = ""


class ipas_hit_geschaeft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Es handelt sich um ein Hit-Geschaeft nach Anhang 1"
    reference = "SR 361.2 Art. 9 Abs. 1bis"


class ipas_aufbewahrungsdauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsdauer der IPAS-Daten in Jahren"
    reference = "SR 361.2 Art. 9"

    def formula(person, period, parameters):
        kategorie = person('ipas_kategorie', period)
        hit = person('ipas_hit_geschaeft', period)

        # Art. 9 Abs. 4: Vermisste/Ausweise: 50 Jahre
        # Art. 9 Abs. 5: Interpol: 10 Jahre
        # Art. 9 Abs. 8: GA ohne Bezug: 3 Jahre
        # Art. 9 Abs. 1bis: Hit-Geschaefte: 5 Jahre nach letzter AFIS/DNA-Loeschung
        # Default / AFIS-DNA: synchron mit AFIS/DNA-System
        vermisste = where(kategorie == 'vermisste', 50, 0)
        ausweise = where(kategorie == 'ausweise', 50, 0)
        interpol = where(kategorie == 'interpol', 10, 0)
        ga = where(kategorie == 'ga', 3, 0)
        hit_dauer = where(hit, 5, 0)

        return vermisste + ausweise + interpol + ga + hit_dauer
