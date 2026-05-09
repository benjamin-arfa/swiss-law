"""SR 642.11 Art. 3

Generated from: ch/642/de/642.11.md

Art. 3 Persoenliche Zugehoerigkeit (Personal affiliation / Tax residency):
1. Natural persons are subject to tax based on personal affiliation if they
   have their tax domicile or tax residence in Switzerland.
2. Tax domicile exists when a person resides in Switzerland with the
   intention of permanent stay.
3. Tax residence exists when a person stays in Switzerland (ignoring
   temporary interruptions):
   a. for at least 30 days and pursues gainful employment;
   b. for at least 90 days without pursuing gainful employment.
4. No tax domicile/residence for persons domiciled abroad who only attend
   an educational institution or receive care in a medical facility.
5. Persons employed by the Confederation or another Swiss public-law entity
   abroad who are exempt from income taxes there are taxable at their place
   of origin.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_steuerrechtlichen_wohnsitz_ch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat steuerrechtlichen Wohnsitz in der Schweiz (Absicht dauernden Verbleibens)"
    reference = "SR 642.11 Art. 3 Abs. 2"


class aufenthaltstage_ch(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Aufenthaltstage in der Schweiz im Steuerjahr"
    reference = "SR 642.11 Art. 3 Abs. 3"


class erwerbstaetig_in_ch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person in der Schweiz eine Erwerbstaetigkeit ausubt"
    reference = "SR 642.11 Art. 3 Abs. 3 Bst. a"


class besucht_nur_lehranstalt_ch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person haelt sich nur zum Besuch einer Lehranstalt oder zur Pflege in einer Heilstaette in der Schweiz auf"
    reference = "SR 642.11 Art. 3 Abs. 4"


class wohnsitz_im_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat Wohnsitz im Ausland"
    reference = "SR 642.11 Art. 3 Abs. 4"


class hat_steuerrechtlichen_aufenthalt_ch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person hat steuerrechtlichen Aufenthalt in der Schweiz"
    reference = "SR 642.11 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        tage = person('aufenthaltstage_ch', period)
        erwerbstaetig = person('erwerbstaetig_in_ch', period)

        # Art. 3 Abs. 3 Bst. a: min. 30 Tage mit Erwerbstaetigkeit
        aufenthalt_erwerbstaetig = erwerbstaetig * (tage >= 30)

        # Art. 3 Abs. 3 Bst. b: min. 90 Tage ohne Erwerbstaetigkeit
        import numpy as np
        aufenthalt_nicht_erwerbstaetig = np.logical_not(erwerbstaetig) * (tage >= 90)

        return aufenthalt_erwerbstaetig + aufenthalt_nicht_erwerbstaetig


class steuerpflichtig_persoenliche_zugehoerigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist aufgrund persoenlicher Zugehoerigkeit in der Schweiz steuerpflichtig"
    reference = "SR 642.11 Art. 3"

    def formula(person, period, parameters):
        import numpy as np
        wohnsitz = person('hat_steuerrechtlichen_wohnsitz_ch', period)
        aufenthalt = person('hat_steuerrechtlichen_aufenthalt_ch', period)
        nur_lehranstalt = person('besucht_nur_lehranstalt_ch', period)
        ausland = person('wohnsitz_im_ausland', period)

        # Art. 3 Abs. 4: Ausnahme fuer Lehranstalt/Heilstaette bei Wohnsitz im Ausland
        ausnahme = ausland * nur_lehranstalt

        return (wohnsitz + aufenthalt) * np.logical_not(ausnahme)
