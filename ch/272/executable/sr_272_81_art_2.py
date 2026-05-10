"""SR 272.81 Art. 2

Generated from: ch/272/de/272.81.md

Einsatz von Videokonferenzen in Zivilverfahren: Abweichung von Art. 54 ZPO
erlaubt Videokonferenzen unter bestimmten Voraussetzungen (Einverstaendnis,
Risikogruppe, Dringlichkeit).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class parteien_einverstanden_videokonferenz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Parteien mit der Durchfuehrung per Videokonferenz einverstanden sind"
    reference = "SR 272.81 Art. 2 Abs. 1 Bst. a"


class partei_ist_besonders_gefaehrdet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Partei zu einer durch das Coronavirus besonders gefaehrdeten Kategorie gehoert"
    reference = "SR 272.81 Art. 2 Abs. 1 Bst. b"


class gerichtsmitglied_ist_gefaehrdet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Gerichtsmitglied zu einer gefaehrdeten Kategorie gehoert"
    reference = "SR 272.81 Art. 2 Abs. 1 Bst. c"


class besondere_dringlichkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine besondere Dringlichkeit besteht"
    reference = "SR 272.81 Art. 2 Abs. 1 Bst. d"


class wichtige_gruende_gegen_videokonferenz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob wichtige Gruende gegen eine Durchfuehrung per Videokonferenz sprechen"
    reference = "SR 272.81 Art. 2 Abs. 1"


class videokonferenz_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verhandlung mittels Videokonferenz durchgefuehrt werden darf"
    reference = "SR 272.81 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        einverstanden = person('parteien_einverstanden_videokonferenz', period)
        partei_gefaehrdet = person('partei_ist_besonders_gefaehrdet', period)
        gericht_gefaehrdet = person('gerichtsmitglied_ist_gefaehrdet', period)
        dringend = person('besondere_dringlichkeit', period)
        gegen = person('wichtige_gruende_gegen_videokonferenz', period)

        # Einverstaendnis reicht allein; Risikogruppe/Dringlichkeit nur ohne wichtige Gegengruende
        return (
            einverstanden
            + (partei_gefaehrdet * not_(gegen))
            + (gericht_gefaehrdet * not_(gegen))
            + dringend
        )
