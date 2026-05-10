"""SR 831.232.51 Art. 7

Generated from: ch/831/de/831.232.51.md

Art. 7: Gebrauchstraining, Reparatur und Betrieb - Training, repair
and operation of aids.

Abs. 1: Insurance covers costs of training for the use of an aid.

Abs. 2: Insurance covers repair, adjustment, and partial renewal costs
for aids provided by the insurance (if used with due care), unless a
third party is liable for damages. A cost share may be charged.

Abs. 3: Annual contribution for operation and maintenance costs: up to
CHF 485 maximum (unless annex specifies otherwise). Motor vehicle
operation costs are NOT covered.

Abs. 4: Monthly contribution for keeping a guide dog (amount per annex).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hvi_gebrauchstraining_kosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten fuer Gebrauchstraining des Hilfsmittels"
    reference = "SR 831.232.51 Art. 7 Abs. 1"


class hvi_reparaturkosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Reparaturkosten fuer von der IV abgegebenes Hilfsmittel"
    reference = "SR 831.232.51 Art. 7 Abs. 2"


class hvi_dritter_ersatzpflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ein Dritter ist fuer den Schaden ersatzpflichtig"
    reference = "SR 831.232.51 Art. 7 Abs. 2"


class hvi_sorgfaeltig_gebraucht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hilfsmittel wurde sorgfaeltig gebraucht"
    reference = "SR 831.232.51 Art. 7 Abs. 2"


class hvi_reparaturkostenuebernahme(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Von der IV uebernommene Reparaturkosten (Art. 7 Abs. 2 HVI)"
    reference = "SR 831.232.51 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        kosten = person('hvi_reparaturkosten', period)
        dritter = person('hvi_dritter_ersatzpflichtig', period)
        sorgfaeltig = person('hvi_sorgfaeltig_gebraucht', period)
        # Insurance covers costs if: careful use AND no third party liable
        return kosten * sorgfaeltig * not_(dritter)


class hvi_betriebskosten_effektiv(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Effektive jaehrliche Betriebs- und Unterhaltskosten des Hilfsmittels"
    reference = "SR 831.232.51 Art. 7 Abs. 3"


class hvi_ist_motorfahrzeug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hilfsmittel ist ein Motorfahrzeug"
    reference = "SR 831.232.51 Art. 7 Abs. 3"


class hvi_betriebskostenbeitrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher Beitrag an Betriebs- und Unterhaltskosten (max. CHF 485, Art. 7 Abs. 3 HVI)"
    reference = "SR 831.232.51 Art. 7 Abs. 3"

    def formula(person, period, parameters):
        effektiv = person('hvi_betriebskosten_effektiv', period)
        motorfahrzeug = person('hvi_ist_motorfahrzeug', period)
        max_beitrag = 485
        # No contribution for motor vehicles; otherwise min(actual, 485)
        return not_(motorfahrzeug) * min_(effektiv, max_beitrag)
