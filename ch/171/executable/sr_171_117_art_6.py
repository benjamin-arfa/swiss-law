"""SR 171.117 Art. 6

Generated from: ch/171/de/171.117.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- IPU Delegation ---

class anzahl_nr_ipu(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Nationalratsmitglieder in der IPU-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return 5


class anzahl_sr_ipu(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ständeratsmitglieder in der IPU-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return 3


# --- PV-ER Delegation ---

class anzahl_nr_pv_er(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Nationalratsmitglieder in der PV-ER-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        return 4


class anzahl_sr_pv_er(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ständeratsmitglieder in der PV-ER-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        return 2


class anzahl_ersatz_nr_pv_er(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ersatzmitglieder Nationalrat in der PV-ER-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        return 4


class anzahl_ersatz_sr_pv_er(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ersatzmitglieder Ständerat in der PV-ER-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        return 2


# --- EFTA/EU Delegation ---

class anzahl_nr_efta_eu(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Nationalratsmitglieder in der EFTA/EU-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        return 3


class anzahl_sr_efta_eu(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ständeratsmitglieder in der EFTA/EU-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        return 2


# --- APF Delegation ---

class anzahl_nr_apf(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Nationalratsmitglieder in der APF-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. d"

    def formula(person, period, parameters):
        return 3


class anzahl_sr_apf(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ständeratsmitglieder in der APF-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. d"

    def formula(person, period, parameters):
        return 2


# --- PV-OSZE Delegation ---

class anzahl_nr_pv_osze(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Nationalratsmitglieder in der PV-OSZE-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. e"

    def formula(person, period, parameters):
        return 3


class anzahl_sr_pv_osze(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ständeratsmitglieder in der PV-OSZE-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. e"

    def formula(person, period, parameters):
        return 3


# --- PV-NATO Delegation ---

class anzahl_nr_pv_nato(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Nationalratsmitglieder in der PV-NATO-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. f"

    def formula(person, period, parameters):
        return 2


class anzahl_sr_pv_nato(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ständeratsmitglieder in der PV-NATO-Delegation"
    reference = "SR 171.117 Art. 6 Abs. 1 Bst. f"

    def formula(person, period, parameters):
        return 2


# --- PD-OECD Delegation ---

class anzahl_nr_pd_oecd(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Nationalratsmitglieder in der PD-OECD"
    reference = "SR 171.117 Art. 6 Abs. 1bis"

    def formula(person, period, parameters):
        return 2


class anzahl_sr_pd_oecd(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ständeratsmitglieder in der PD-OECD"
    reference = "SR 171.117 Art. 6 Abs. 1bis"

    def formula(person, period, parameters):
        return 2


# --- Nachbarländer-Delegationen ---

class anzahl_nr_nachbarlaender_delegation(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Nationalratsmitglieder in Delegationen zu Nachbarländer-Parlamenten"
    reference = "SR 171.117 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        return 3


class anzahl_sr_nachbarlaender_delegation(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ständeratsmitglieder in Delegationen zu Nachbarländer-Parlamenten"
    reference = "SR 171.117 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        return 2


class anzahl_ersatz_nr_nachbarlaender(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ersatzmitglieder Nationalrat in Nachbarländer-Delegationen"
    reference = "SR 171.117 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        return 3


class anzahl_ersatz_sr_nachbarlaender(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ersatzmitglieder Ständerat in Nachbarländer-Delegationen"
    reference = "SR 171.117 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        return 2
