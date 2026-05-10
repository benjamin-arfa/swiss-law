"""SR 192.121 Art. 22

Generated from: ch/192/de/192.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_bei_einreise_als_begleitperson(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter bei Einreise als berechtigte Begleitperson"
    reference = "SR 192.121 Art. 22"

class erleichterter_arbeitsmarktzugang(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erleichterter Zugang zum Arbeitsmarkt fuer Begleitpersonen (Art. 22 Abs. 1)"
    reference = "SR 192.121 Art. 22"

    def formula(person, period, parameters):
        berechtigt = person('berechtigung_begleitung_abs1', period)
        haushalt = person('lebt_im_gemeinsamen_haushalt', period)
        wohnt_ch = person('wohnt_in_schweiz', period)
        return berechtigt * haushalt * wohnt_ch

class erleichterter_arbeitsmarktzugang_kind(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erleichterter Arbeitsmarktzugang fuer Kinder bis 25 (Einreise vor 21, Art. 22 Abs. 1 lit. d-e)"
    reference = "SR 192.121 Art. 22"

    def formula(person, period, parameters):
        kind = person('ist_kind_hauptberechtigte', period)
        alter = person('alter', period)
        alter_einreise = person('alter_bei_einreise_als_begleitperson', period)
        haushalt = person('lebt_im_gemeinsamen_haushalt', period)
        return kind * (alter_einreise < 21) * (alter <= 25) * haushalt

class erwerbseinkommen_begleitperson_steuerpflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erwerbseinkommen der Begleitperson in der Schweiz steuerpflichtig (Art. 22 Abs. 6)"
    reference = "SR 192.121 Art. 22"

    def formula(person, period, parameters):
        return person('erleichterter_arbeitsmarktzugang', period) * person('nebenerwerbstaetig', period)
