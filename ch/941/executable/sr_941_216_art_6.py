"""SR 941.216 Art. 6 — Nacheichung von Audiometern

Audiometrieverordnung — Verordnung über audiometrische Messmittel.
Generated from: ch/de/941/941.216.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class nacheichung_audiometer_intervall_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Intervall für Nacheichung von Audiometern in Jahren (SR 941.216 Art. 6 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_6"

    def formula(person, period, parameters):
        # Art. 6 Abs. 1: Audiometer müssen jährlich einer Nacheichung
        # unterzogen werden.
        return 1


class nacheichung_audiometer_faellig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Nacheichung des Audiometers ist fällig (SR 941.216 Art. 6 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_6"

    def formula(person, period, parameters):
        # Art. 6 Abs. 1: Jährliche Nacheichung erforderlich.
        # Art. 6 Abs. 2: Durchführung durch METAS oder Eichstelle.
        return person('ist_audiometer', period)


class ist_audiometer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein Audiometer"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_6"


class metas_kann_frist_aendern(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "METAS kann die Nacheichungsfristen verlängern oder verkürzen (SR 941.216 Art. 6 Abs. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2010/161/de#art_6"

    def formula(person, period, parameters):
        # Art. 6 Abs. 3: METAS kann Fristen ändern wenn messtechnische
        # Eigenschaften dies erlauben oder verlangen.
        return person('ist_audiometer', period)
