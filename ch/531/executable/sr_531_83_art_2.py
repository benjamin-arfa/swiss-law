"""SR 531.83 Art. 2 — Verwendungsbeschränkung

Verordnung über die Beschränkung der Verwendung von Alteplase.
Generated from: ch/de/531/531.83.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class indikation_akuter_myokardinfarkt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verwendung für thrombolytische Therapie bei akutem Myokardinfarkt (SR 531.83 Art. 2 Abs. 1 lit. a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2022/439/de#art_2"


class indikation_lungenembolie(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verwendung für thrombolytische Behandlung bei akuter massiver Lungenembolie mit hämodynamischer Instabilität (SR 531.83 Art. 2 Abs. 1 lit. b)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2022/439/de#art_2"


class indikation_ischaemischer_hirnschlag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verwendung für thrombolytische Behandlung bei akutem ischämischem Hirnschlag (SR 531.83 Art. 2 Abs. 1 lit. c)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2022/439/de#art_2"


class alteplase_verwendung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verwendung von Alteplase > 2mg ist für eine registrierte Indikation zulässig (SR 531.83 Art. 2 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2022/439/de#art_2"

    def formula(person, period, parameters):
        # Art. 2 Abs. 1: Alteplase darf nur für die folgenden Indikationen
        # verwendet werden:
        # a) akuter Myokardinfarkt
        # b) akute massive Lungenembolie mit hämodynamischer Instabilität
        # c) akuter ischämischer Hirnschlag
        myokardinfarkt = person('indikation_akuter_myokardinfarkt', period)
        lungenembolie = person('indikation_lungenembolie', period)
        hirnschlag = person('indikation_ischaemischer_hirnschlag', period)
        return myokardinfarkt + lungenembolie + hirnschlag > 0


class ersatz_alteplase_2mg_durch_verduennung_verboten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Ersatz von Alteplase 2mg durch Verdünnung der höher dosierten Alteplase ist verboten (SR 531.83 Art. 2 Abs. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2022/439/de#art_2"

    def formula(person, period, parameters):
        # Art. 2 Abs. 3: Generelles Verbot.
        return True
