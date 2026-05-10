"""SR 672.937.2 Art. 1

Generated from: ch/672/de/672.937.2.md

Bundesbeschluss über die Genehmigung eines Protokolls zur Änderung
des Doppelbesteuerungsabkommens zwischen der Schweiz und Griechenland
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


# --- Input variables ---

class dba_ch_gr_protokoll_genehmigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Protokoll vom 4. November 2010 zur Änderung des DBA CH-GR (SR 0.672.937.21) ist genehmigt"
    reference = "SR 672.937.2 Art. 1 Abs. 1"

    def formula_2011(person, period, parameters):
        return True


class dba_ch_gr_bundesrat_ratifizierung_ermaechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat ist ermächtigt, das Protokoll zum DBA CH-GR zu ratifizieren"
    reference = "SR 672.937.2 Art. 1 Abs. 2"

    def formula_2011(person, period, parameters):
        return True


class dba_ch_gr_amtshilfegesuch_auf_illegalen_daten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Amtshilfegesuch beruht auf illegal beschafften Daten"
    reference = "SR 672.937.2 Art. 1 Abs. 4"


class dba_ch_gr_steuerpflichtige_person_identifiziert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die steuerpflichtige Person ist identifiziert (auch auf andere Weise als durch Name und Adresse möglich)"
    reference = "SR 672.937.2 Art. 1 Abs. 4 lit. a"


class dba_ch_gr_informationsinhaber_angegeben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Name und Adresse des mutmasslichen Informationsinhabers sind angegeben, soweit bekannt"
    reference = "SR 672.937.2 Art. 1 Abs. 4 lit. b"


# --- Computed variables ---

class dba_ch_gr_fishing_expedition(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Amtshilfegesuch stellt eine unzulässige 'fishing expedition' dar"
    reference = "SR 672.937.2 Art. 1 Abs. 4"

    def formula(person, period, parameters):
        identifiziert = person('dba_ch_gr_steuerpflichtige_person_identifiziert', period)
        informationsinhaber = person('dba_ch_gr_informationsinhaber_angegeben', period)
        # Fishing expedition liegt vor, wenn die Person nicht identifiziert ist
        # oder der Informationsinhaber nicht angegeben ist
        return not_(identifiziert) + not_(informationsinhaber) > 0


class dba_ch_gr_amtshilfe_zulassig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schweiz entspricht dem Amtshilfegesuch gestützt auf das DBA CH-GR"
    reference = "SR 672.937.2 Art. 1 Abs. 4"

    def formula(person, period, parameters):
        keine_fishing = not_(person('dba_ch_gr_fishing_expedition', period))
        keine_illegalen_daten = not_(person('dba_ch_gr_amtshilfegesuch_auf_illegalen_daten', period))
        identifiziert = person('dba_ch_gr_steuerpflichtige_person_identifiziert', period)
        informationsinhaber = person('dba_ch_gr_informationsinhaber_angegeben', period)
        return keine_fishing * keine_illegalen_daten * identifiziert * informationsinhaber
