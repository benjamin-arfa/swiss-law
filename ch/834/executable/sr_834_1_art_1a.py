"""SR 834.1 Art. 1a

Generated from: ch/834/de/834.1.md

Anspruchsberechtigte Dienstleistende:
- Abs. 1: Personen in der Armee/Rotkreuzdienst haben Anspruch auf
  Entschaedigung fuer jeden besoldeten Diensttag.
- Abs. 2: Zivildienstleistende haben Anspruch fuer jeden anrechenbaren Tag.
- Abs. 3: Schutzdienstleistende haben Anspruch fuer jeden ganzen Tag mit Sold.
- Abs. 4: J+S-Kaderbildungskurse und Jungschuetzenleiterkurse gleichgestellt.
- Abs. 4bis: Anspruch erlischt mit ganzer AHV-Altersrente oder Referenzalter.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import DAY, MONTH, YEAR


class eo_leistet_militaerdienst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person leistet Militaerdienst oder Rotkreuzdienst (Art. 1a Abs. 1 EOG)"
    reference = "SR 834.1 Art. 1a Abs. 1"


class eo_leistet_zivildienst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person leistet Zivildienst (Art. 1a Abs. 2 EOG)"
    reference = "SR 834.1 Art. 1a Abs. 2"


class eo_leistet_schutzdienst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person leistet Schutzdienst (Art. 1a Abs. 3 EOG)"
    reference = "SR 834.1 Art. 1a Abs. 3"


class eo_leistet_js_kaderbildung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person nimmt an J+S-Kaderbildung oder Jungschuetzenleiterkurs teil (Art. 1a Abs. 4 EOG)"
    reference = "SR 834.1 Art. 1a Abs. 4"


class eo_bezieht_ganze_ahv_altersrente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person bezieht ganze AHV-Altersrente (Art. 1a Abs. 4bis EOG)"
    reference = "SR 834.1 Art. 1a Abs. 4bis"


class eo_hat_referenzalter_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person hat das AHV-Referenzalter erreicht (Art. 21 Abs. 1 AHVG)"
    reference = "SR 834.1 Art. 1a Abs. 4bis"


class eo_besoldete_diensttage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl besoldete Diensttage im Monat"
    reference = "SR 834.1 Art. 1a"


class eo_ist_dienstleistend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist Dienstleistende/r im Sinne von Art. 1a Abs. 5 EOG"
    reference = "SR 834.1 Art. 1a Abs. 5"

    def formula_2005(person, period, parameters):
        militaer = person('eo_leistet_militaerdienst', period)
        zivil = person('eo_leistet_zivildienst', period)
        schutz = person('eo_leistet_schutzdienst', period)
        js = person('eo_leistet_js_kaderbildung', period)
        ganze_rente = person('eo_bezieht_ganze_ahv_altersrente', period)
        referenzalter = person('eo_hat_referenzalter_erreicht', period)

        ist_dienstleistend = militaer + zivil + schutz + js > 0

        # Abs. 4bis: Anspruch erlischt mit ganzer Altersrente oder Referenzalter
        anspruch_erloschen = ganze_rente + referenzalter > 0

        return ist_dienstleistend * not_(anspruch_erloschen)
