"""SR 363.1 Art. 2

Generated from: ch/363/de/363.1.md

Analyselabors und ihre Anerkennung: Bedingungen fuer die Anerkennung
forensischer DNA-Analyselabors.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class labor_ist_akkreditiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Labor ist auf dem Gebiet der forensischen Genetik akkreditiert (SAS)"
    reference = "SR 363.1 Art. 2 Abs. 2 Bst. a"


class labor_erfuellt_qualitaetsanforderungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Labor erfuellt jederzeit die Leistungs- und Qualitaetsanforderungen"
    reference = "SR 363.1 Art. 2 Abs. 2 Bst. b"


class labor_ringversuche_bestanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Labor hat in den letzten 12 Monaten mindestens 4 Ringversuche erfolgreich bestanden"
    reference = "SR 363.1 Art. 2 Abs. 2 Bst. c"


class labor_fachliche_leitung_qualifiziert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fachliche Leitung hat Abschluss als Forensischer Genetiker SGRM oder gleichwertig"
    reference = "SR 363.1 Art. 2 Abs. 2 Bst. d"


class labor_geschaeftsfuehrung_guter_ruf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Geschaeftsfuehrung geniesst guten Ruf und bietet Gewaehr fuer einwandfreie Taetigkeit"
    reference = "SR 363.1 Art. 2 Abs. 2 Bst. e"


class labor_geschaeftsfuehrung_am_sitz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Geschaeftsfuehrung uebt Leitung am Sitz des Labors tatsaechlich und verantwortlich aus"
    reference = "SR 363.1 Art. 2 Abs. 2 Bst. f"


class labor_anerkennung_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Labor erfuellt alle Voraussetzungen fuer die Anerkennung durch das EJPD"
    reference = "SR 363.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        akkreditiert = person('labor_ist_akkreditiert', period)
        qualitaet = person('labor_erfuellt_qualitaetsanforderungen', period)
        ringversuche = person('labor_ringversuche_bestanden', period)
        leitung = person('labor_fachliche_leitung_qualifiziert', period)
        ruf = person('labor_geschaeftsfuehrung_guter_ruf', period)
        sitz = person('labor_geschaeftsfuehrung_am_sitz', period)
        return akkreditiert * qualitaet * ringversuche * leitung * ruf * sitz
