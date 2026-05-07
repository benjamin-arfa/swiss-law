"""SR 641.10 Art. 6

Generated from: ch/641/de/641.10.md

Art. 6 Ausnahmen (Exemptions) from the emission levy:
- Non-profit entities with max 6% dividend cap (a)
- Mergers, conversions, spin-offs (abis)
- Public-purpose entities in public hands (ater)
- Cooperatives with total contributions <= CHF 1,000,000 (b)
- Public transport companies from public investment (c)
- Participation rights from prior premiums already taxed (d)
- Foundation/increase of company with total contributions <= CHF 1,000,000 (h)
- Collective investment scheme units (i)
- Rehabilitation/restructuring up to CHF 10,000,000 (k)
- Bank conversion capital approved by FINMA (l)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class stg_gemeinnuetzig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the entity is non-profit with max 6% dividend cap per Art. 6 Abs. 1 Bst. a"
    reference = "SR 641.10 Art. 6 Abs. 1 Bst. a"


class stg_fusion_umwandlung_spaltung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether participation rights arise from merger/conversion/spin-off"
    reference = "SR 641.10 Art. 6 Abs. 1 Bst. abis"


class stg_gesamtleistung_gesellschafter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Total contributions by shareholders/cooperative members (CHF)"
    reference = "SR 641.10 Art. 6 Abs. 1 Bst. b, h"


class stg_ist_genossenschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the entity is a cooperative (Genossenschaft)"
    reference = "SR 641.10 Art. 6 Abs. 1 Bst. b"


class stg_ist_sanierung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether the issuance is part of a restructuring (Sanierung)"
    reference = "SR 641.10 Art. 6 Abs. 1 Bst. k"


class stg_emissionsabgabe_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether the entity is exempt from emission levy"
    reference = "SR 641.10 Art. 6"

    def formula(person, period, parameters):
        gemeinnuetzig = person('stg_gemeinnuetzig', period.this_year)
        fusion = person('stg_fusion_umwandlung_spaltung', period)
        gesamtleistung = person('stg_gesamtleistung_gesellschafter', period)
        ist_genossenschaft = person('stg_ist_genossenschaft', period.this_year)
        ist_sanierung = person('stg_ist_sanierung', period)

        schwelle_gruendung = parameters(period).sr_641_10.befreiung_schwelle_gruendung
        schwelle_sanierung = parameters(period).sr_641_10.befreiung_schwelle_sanierung

        # Art. 6(a): non-profit exempt
        # Art. 6(abis): mergers/conversions exempt
        # Art. 6(b): cooperatives with contributions <= 1M exempt
        genossen_befreit = ist_genossenschaft * (gesamtleistung <= schwelle_gruendung)
        # Art. 6(h): AG/GmbH with contributions <= 1M exempt
        gruendung_befreit = not_(ist_genossenschaft) * (gesamtleistung <= schwelle_gruendung)
        # Art. 6(k): restructuring with contributions <= 10M exempt
        sanierung_befreit = ist_sanierung * (gesamtleistung <= schwelle_sanierung)

        return (gemeinnuetzig + fusion + genossen_befreit + gruendung_befreit
                + sanierung_befreit)
