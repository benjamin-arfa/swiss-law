"""SR 362.0 Art. 15

Generated from: ch/362/de/362.0.md

Austausch von Zusatzinformationen: SIRENE bureau must exchange supplementary
information within 12 hours. Immediate action required for terrorism-related
alerts, arrest warrants, vulnerable persons, and urgent alerts.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

FRIST_ZUSATZINFO_STUNDEN = 12  # spätestens innerhalb von 12 Stunden


class ist_ausschreibung_terrorismus(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ausschreibung steht im Zusammenhang mit terroristischer Straftat"
    reference = "SR 362.0 Art. 15 Abs. 1bis lit. a"


class ist_ausschreibung_festnahme_auslieferung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ausschreibung zur Festnahme zum Zweck der Auslieferung"
    reference = "SR 362.0 Art. 15 Abs. 1bis lit. b"


class ist_ausschreibung_schutzbeduerftig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ausschreibung einer schutzbeduerftigen Person"
    reference = "SR 362.0 Art. 15 Abs. 1bis lit. c"


class ist_ausschreibung_dringend_art33(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dringend gekennzeichnete Ausschreibung nach Art. 33"
    reference = "SR 362.0 Art. 15 Abs. 1bis lit. d"


class erfordert_umgehendes_handeln(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "SIRENE-Buero muss umgehend handeln (kein Aufschub)"
    reference = "SR 362.0 Art. 15 Abs. 1bis"

    def formula(person, period):
        return (
            person('ist_ausschreibung_terrorismus', period) +
            person('ist_ausschreibung_festnahme_auslieferung', period) +
            person('ist_ausschreibung_schutzbeduerftig', period) +
            person('ist_ausschreibung_dringend_art33', period)
        ) > 0


class max_frist_zusatzinfo_austausch_stunden(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Maximale Frist fuer Austausch von Zusatzinformationen (Stunden)"
    reference = "SR 362.0 Art. 15 Abs. 1, 1bis"

    def formula(person, period):
        import numpy as np
        umgehend = person('erfordert_umgehendes_handeln', period)
        # Umgehend = so schnell wie moeglich (approximiert als 1 Stunde),
        # Standard = spätestens 12 Stunden
        return np.where(umgehend, 1.0, FRIST_ZUSATZINFO_STUNDEN)
