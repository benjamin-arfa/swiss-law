"""SR 143.11 Art. 5

Generated from: ch/143/de/143.11.md

Gueltigkeitsdauer (Validity period) for Swiss identity documents:
- Adults (18+): 10 years for ordinary passport and ID card
- Minors (<18): 5 years
- Provisional passport: max 12 months
- 3+ losses within 5 years: validity reduced to 2 years
- Medical temporary fingerprint issues: passport validity 1 year
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

GUELTIGKEIT_ERWACHSENE_JAHRE = 10
GUELTIGKEIT_MINDERJAEHRIGE_JAHRE = 5
GUELTIGKEIT_PROVISORISCH_MONATE = 12
GUELTIGKEIT_VERLUST_JAHRE = 2
VERLUST_SCHWELLE = 3
VERLUST_ZEITRAUM_JAHRE = 5
GUELTIGKEIT_MEDIZINISCH_JAHRE = 1


class alter_bei_antrag(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person zum Zeitpunkt des Antrags"
    reference = "SR 143.11 Art. 5 Abs. 1"


class ist_provisorischer_pass(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wird ein provisorischer Pass beantragt"
    reference = "SR 143.11 Art. 5 Abs. 2"


class anzahl_verluste_5_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Verluste derselben Ausweisart innerhalb von 5 Jahren"
    reference = "SR 143.11 Art. 5 Abs. 3"
    default_value = 0


class sorgfalt_glaubhaft_dargelegt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person legt glaubhaft dar, dass Ausweise mit Sorgfalt behandelt wurden"
    reference = "SR 143.11 Art. 5 Abs. 3"


class fingerabdruck_medizinisch_temporaer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fingerabdruecke koennen aus temporaeren medizinischen Gruenden nicht erfasst werden"
    reference = "SR 143.11 Art. 12 Abs. 4"


class gueltigkeitsdauer_ausweis_jahre(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gueltigkeitsdauer des Ausweises in Jahren"
    reference = "SR 143.11 Art. 5"

    def formula(person, period):
        import numpy as np
        alter = person('alter_bei_antrag', period)
        provisorisch = person('ist_provisorischer_pass', period)
        verluste = person('anzahl_verluste_5_jahre', period)
        sorgfalt = person('sorgfalt_glaubhaft_dargelegt', period)
        medizinisch = person('fingerabdruck_medizinisch_temporaer', period)

        # Abs. 1: Standard-Gueltigkeitsdauer
        standard = np.where(
            alter >= 18,
            GUELTIGKEIT_ERWACHSENE_JAHRE,
            GUELTIGKEIT_MINDERJAEHRIGE_JAHRE
        )

        # Abs. 2: Provisorischer Pass max 12 Monate = 1 Jahr
        standard = np.where(provisorisch, GUELTIGKEIT_PROVISORISCH_MONATE / 12, standard)

        # Abs. 3: Verkuerzte Gueltigkeitsdauer bei >= 3 Verlusten (ohne Sorgfalt)
        verkuerzung_noetig = (verluste >= VERLUST_SCHWELLE) * (1 - sorgfalt)
        standard = np.where(verkuerzung_noetig, GUELTIGKEIT_VERLUST_JAHRE, standard)

        # Art. 12 Abs. 4: Temporaere medizinische Gruende = 1 Jahr
        standard = np.where(medizinisch, GUELTIGKEIT_MEDIZINISCH_JAHRE, standard)

        return standard.astype(float)
