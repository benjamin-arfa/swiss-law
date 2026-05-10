"""SR 823.113 Art. 4

Generated from: ch/823/de/823.113.md

Vermittlungsprovision für künstlerische und ähnliche Darbietungen:
- Gruppen/Orchester: max. 8%
- Cabaret-Tänzerinnen: max. 8%
- Alleinmusiker/Alleinunterhalter/Artisten/Schauspieler: max. 10%
- Darf 5% der Brutto-Gage des ersten Jahresengagements nicht übersteigen
- Bei Vertragsdauer < 6 Arbeitstage: Erhöhung um max. 25%, Minimum 80 CHF
- Bei Auslandvermittlung: Erhöhung um max. 50%, aber nicht mehr als Mehrkosten
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kuenstler_kategorie(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Kategorie der künstlerischen Darbietung"
    reference = "SR 823.113 Art. 4 Abs. 1"
    # gruppen_orchester, cabaret, solo_kuenstler


class brutto_gage_erstes_jahresengagement(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Brutto-Gage aus dem ersten Jahresengagement"
    reference = "SR 823.113 Art. 4 Abs. 2"


class vertragsdauer_arbeitstage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Vertragsdauer in Arbeitstagen"
    reference = "SR 823.113 Art. 4 Abs. 3"


class ist_auslandvermittlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vermittlung ins Ausland erfolgt"
    reference = "SR 823.113 Art. 4 Abs. 4"


class vermittlungsprovision_kuenstler(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermittlungsprovision für künstlerische und ähnliche Darbietungen"
    reference = "SR 823.113 Art. 4"

    def formula(person, period, parameters):
        import numpy as np
        kategorie = person('kuenstler_kategorie', period)
        gage = person('brutto_gage_erstes_jahresengagement', period)
        tage = person('vertragsdauer_arbeitstage', period)
        ausland = person('ist_auslandvermittlung', period)

        params = parameters(period).sr_823_113

        # Base rate depends on category
        satz = np.where(
            np.isin(kategorie, ['gruppen_orchester', 'cabaret']),
            params.provision_gruppen_cabaret,
            np.where(
                kategorie == 'solo_kuenstler',
                params.provision_solo_kuenstler,
                0
            )
        )

        # Short engagement surcharge (< 6 days: +25%)
        kurz_zuschlag = np.where(
            tage < params.kurzengagement_schwelle_tage,
            params.kurzengagement_zuschlag,
            0
        )
        effektiver_satz = satz * (1 + kurz_zuschlag)

        provision = gage * effektiver_satz

        # Minimum 80 CHF for short engagements
        provision = np.where(
            tage < params.kurzengagement_schwelle_tage,
            np.maximum(provision, params.provision_minimum),
            provision
        )

        # Cap at 5% of first annual gross
        cap = gage * params.provision_jahresgage_cap
        provision = np.minimum(provision, cap)

        # Foreign placement surcharge (max +50%)
        provision = np.where(
            ausland,
            provision * (1 + params.ausland_zuschlag_max),
            provision
        )

        return provision
