"""SR 831.20 Art. 28a

Generated from: ch/831/de/831.20.md

Art. 28a Bemessung des Invaliditaetsgrades (Assessment of the degree of disability):
1. For employed insured persons, the degree of disability is assessed according
   to Art. 16 ATSG (income comparison method): comparison of the income that
   could be earned without disability (Valideneinkommen) with the income that
   can still be earned with disability (Invalideneinkommen).
2. For non-employed insured persons active in their field of activity and
   for whom employment is not reasonable, the degree is based on the extent
   to which they are unable to carry out their activities.
3. For partly employed insured persons or those working unpaid in the spouse's
   business, the disability degree is determined using Art. 16 ATSG for the
   employment portion, and using para. 2 for the activity portion. The
   respective shares must be established and the disability degree assessed
   for both areas (mixed method).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_valideneinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkommen das ohne Invaliditaet erzielt werden koennte (Valideneinkommen, CHF)"
    reference = "SR 831.20 Art. 28a Abs. 1"


class iv_invalideneinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkommen das trotz Invaliditaet noch erzielt werden kann (Invalideneinkommen, CHF)"
    reference = "SR 831.20 Art. 28a Abs. 1"


class iv_ist_erwerbstaetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherte Person ist (teil-)erwerbstaetig"
    reference = "SR 831.20 Art. 28a Abs. 1"


class iv_anteil_erwerbstaetigkeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Erwerbstaetigkeit bei teilweiser Erwerbstaetigkeit (0.0-1.0)"
    reference = "SR 831.20 Art. 28a Abs. 3"
    default_value = 1.0


class iv_einschraenkung_aufgabenbereich_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einschraenkung im Aufgabenbereich in Prozent (0-100)"
    reference = "SR 831.20 Art. 28a Abs. 2"


class iv_invaliditaetsgrad_erwerbstaetige(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Invaliditaetsgrad nach Einkommensvergleich fuer erwerbstaetige Versicherte (Prozent)"
    reference = "SR 831.20 Art. 28a Abs. 1"

    def formula(person, period, parameters):
        validen = person('iv_valideneinkommen', period)
        invaliden = person('iv_invalideneinkommen', period)

        # Art. 16 ATSG: (Valideneinkommen - Invalideneinkommen) / Valideneinkommen * 100
        return where(validen > 0,
                     max_((validen - invaliden) / validen * 100, 0),
                     0)


class iv_invaliditaetsgrad_gemischt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Invaliditaetsgrad nach gemischter Methode (Prozent)"
    reference = "SR 831.20 Art. 28a Abs. 3"

    def formula(person, period, parameters):
        ist_erwerbstaetig = person('iv_ist_erwerbstaetig', period)
        anteil_erwerb = person('iv_anteil_erwerbstaetigkeit', period)
        iv_grad_erwerb = person('iv_invaliditaetsgrad_erwerbstaetige', period)
        einschraenkung_aufgabe = person('iv_einschraenkung_aufgabenbereich_prozent', period)

        anteil_aufgabe = 1.0 - anteil_erwerb

        # Art. 28a Abs. 3: Gewichteter Invaliditaetsgrad
        # Erwerbsanteil: nach Einkommensvergleich
        # Aufgabenbereichsanteil: nach Einschraenkung
        gemischt = (anteil_erwerb * iv_grad_erwerb) + (anteil_aufgabe * einschraenkung_aufgabe)

        # Vollerwerbstaetig: nur Einkommensvergleich
        # Nicht erwerbstaetig: nur Aufgabenbereich
        return where(ist_erwerbstaetig,
                     where(anteil_erwerb >= 1.0,
                           iv_grad_erwerb,
                           gemischt),
                     einschraenkung_aufgabe)
