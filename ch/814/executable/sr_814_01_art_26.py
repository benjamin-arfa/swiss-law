"""SR 814.01 Art. 26-28

Generated from: ch/fr/814/814.01.md

Art. 26: Controle autonome (Selbstkontrolle)
- Abs. 1: Prohibited to market substances that could threaten environment/humans.
- Abs. 2: Manufacturer/importer must exercise self-control.
Art. 27: Information du preneur (Information des Abnehmers)
- Must inform buyer of environmental properties and provide instructions.
Art. 28: Utilisation respectueuse (Umweltgerechte Verwendung)
- Abs. 1: Whoever uses substances must ensure no environmental threat.
- Abs. 2: Instructions of manufacturers/importers must be followed.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class usg_bringt_stoffe_in_verkehr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Stoffe in Verkehr bringt"
    reference = "SR 814.01 Art. 26 Abs. 1"


class usg_stoffe_umweltgefaehrdend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob die Stoffe umweltgefaehrdend sind (bestimmungsgemaesser Gebrauch)"
    reference = "SR 814.01 Art. 26 Abs. 1"


class usg_selbstkontrolle_durchgefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob der Hersteller/Importeur die Selbstkontrolle durchgefuehrt hat"
    reference = "SR 814.01 Art. 26 Abs. 2"


class usg_abnehmer_informiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob der Abnehmer ueber die Umwelteigenschaften informiert wurde"
    reference = "SR 814.01 Art. 27 Abs. 1"


class usg_inverkehrbringen_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Inverkehrbringen der Stoffe zulaessig ist"
    reference = "SR 814.01 Art. 26-27"

    def formula(person, period, parameters):
        in_verkehr = person('usg_bringt_stoffe_in_verkehr', period)
        gefaehrdend = person('usg_stoffe_umweltgefaehrdend', period)
        kontrolle = person('usg_selbstkontrolle_durchgefuehrt', period)
        informiert = person('usg_abnehmer_informiert', period)

        # Not marketing substances: not relevant
        # Marketing: must not be hazardous + self-control done + buyer informed
        return not_(in_verkehr) + (in_verkehr * not_(gefaehrdend) * kontrolle * informiert)
