"""SR 235.1 Art. 9

Generated from: ch/235/de/235.1.md

Einschraenkung des Auskunftsrechts: Gruende fuer Verweigerung,
Einschraenkung oder Aufschiebung der Auskunft.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_auskunft_gesetz_schliesst_aus(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ein Gesetz im formellen Sinn sieht Ausschluss der Auskunft vor"
    reference = "SR 235.1 Art. 9 Abs. 1 lit. a"


class dsg_auskunft_interessen_dritter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ueberwiegende Interessen Dritter erfordern Einschraenkung"
    reference = "SR 235.1 Art. 9 Abs. 1 lit. b"


class dsg_auskunft_oeffentliche_sicherheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ueberwiegende oeffentliche Interessen (Sicherheit) erfordern Einschraenkung"
    reference = "SR 235.1 Art. 9 Abs. 2 lit. a"


class dsg_auskunft_strafuntersuchung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auskunft wuerde Zweck einer Strafuntersuchung in Frage stellen"
    reference = "SR 235.1 Art. 9 Abs. 2 lit. b"


class dsg_auskunft_eigene_interessen_privat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Eigene ueberwiegende Interessen des privaten Inhabers erfordern Einschraenkung"
    reference = "SR 235.1 Art. 9 Abs. 4"


class dsg_auskunft_eingeschraenkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auskunftsrecht ist eingeschraenkt/verweigert/aufgeschoben"
    reference = "SR 235.1 Art. 9"

    def formula(person, period, parameters):
        gesetz = person('dsg_auskunft_gesetz_schliesst_aus', period)
        dritte = person('dsg_auskunft_interessen_dritter', period)
        sicherheit = person('dsg_auskunft_oeffentliche_sicherheit', period)
        straf = person('dsg_auskunft_strafuntersuchung', period)
        privat = person('dsg_auskunft_eigene_interessen_privat', period)
        bundesorgan = person('dsg_bearbeitung_durch_bundesorgan', period)

        # Abs. 1: alle Inhaber (Gesetz oder Interessen Dritter)
        # Abs. 2: nur Bundesorgane (oeffentl. Sicherheit oder Strafuntersuchung)
        # Abs. 4: nur private Inhaber (eigene Interessen)
        return gesetz + dritte + (bundesorgan * (sicherheit + straf)) + (not_(bundesorgan) * privat) > 0
