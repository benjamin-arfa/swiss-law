"""SR 822.115.2 Art. 1

Generated from: ch/822/de/822.115.2.md

Art. 1: Gefaehrliche Arbeiten fuer Jugendliche
Folgende Arbeiten gelten fuer Jugendliche als gefaehrlich:
a. Arbeiten, welche die physische oder psychische Leistungsfaehigkeit uebersteigen
b. Arbeiten mit Risiko physischen, psychischen, moralischen oder sexuellen Missbrauchs
c. Arbeiten in belastenden Arbeitszeitsystemen (z.B. Akkordarbeit)
d. Arbeiten mit gesundheitsgefaehrdenden physikalischen Einwirkungen
   (ionisierende Strahlung, Ueberdruck, extreme Temperaturen, Laerm)
e. Arbeiten mit biologischen Agenzien (Gruppen 3 und 4)
f. Arbeiten mit gesundheitsgefaehrdenden chemischen Agenzien (R39, R42, R43, R40, R45, R46, R48, R60, R61)
g. Arbeiten mit unfallgefaehrlichen Maschinen/Werkzeugen
h. Arbeiten mit erheblicher Brand-/Explosions-/Vergiftungsgefahr
i. Arbeiten unter Tag, unter Wasser, in gefaehrlichen Hoehen, engen Raeumen
j. Arbeiten mit gefaehrlichen Tieren
k. Industrielles Schlachten von Tieren
l. Sortieren von Altmaterial, ungereinigter Waesche, Haaren/Borsten/Fellen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jarg_arbeit_uebersteigt_leistungsfaehigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit uebersteigt physische oder psychische Leistungsfaehigkeit Jugendlicher"
    reference = "SR 822.115.2 Art. 1 Bst. a"


class jarg_arbeit_missbrauchsrisiko(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit mit Risiko physischen, psychischen, moralischen oder sexuellen Missbrauchs"
    reference = "SR 822.115.2 Art. 1 Bst. b"


class jarg_arbeit_belastendes_zeitsystem(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit in belastendem Arbeitszeitsystem (z.B. Akkordarbeit)"
    reference = "SR 822.115.2 Art. 1 Bst. c"


class jarg_arbeit_physikalische_einwirkungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = (
        "Arbeit mit gesundheitsgefaehrdenden physikalischen Einwirkungen "
        "(Strahlung, Ueberdruck, extreme Temperatur, Laerm)"
    )
    reference = "SR 822.115.2 Art. 1 Bst. d"


class jarg_arbeit_biologische_agenzien(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit mit gesundheitsgefaehrdenden biologischen Agenzien (Gruppen 3/4)"
    reference = "SR 822.115.2 Art. 1 Bst. e"


class jarg_arbeit_chemische_agenzien(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit mit gesundheitsgefaehrdenden chemischen Agenzien (R39-R61)"
    reference = "SR 822.115.2 Art. 1 Bst. f"


class jarg_arbeit_unfallgefaehrliche_maschinen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit mit unfallgefaehrlichen Maschinen, Ausruestungen oder Werkzeugen"
    reference = "SR 822.115.2 Art. 1 Bst. g"


class jarg_arbeit_brand_explosionsgefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit mit erheblicher Brand-, Explosions-, Unfall- oder Vergiftungsgefahr"
    reference = "SR 822.115.2 Art. 1 Bst. h"


class jarg_arbeit_gefaehrliche_umgebung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit unter Tag, unter Wasser, in gefaehrlichen Hoehen, engen Raeumen oder bei Einsturzgefahr"
    reference = "SR 822.115.2 Art. 1 Bst. i"


class jarg_arbeit_gefaehrliche_tiere(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit mit gefaehrlichen Tieren"
    reference = "SR 822.115.2 Art. 1 Bst. j"


class jarg_arbeit_industrielles_schlachten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Industrielles Schlachten von Tieren"
    reference = "SR 822.115.2 Art. 1 Bst. k"


class jarg_arbeit_altmaterial_sortierung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Sortieren von Altmaterial, ungereinigter Waesche, Haaren/Borsten/Fellen"
    reference = "SR 822.115.2 Art. 1 Bst. l"


class jarg_gefaehrliche_arbeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit gilt als gefaehrlich fuer Jugendliche nach Art. 1 der Verordnung"
    reference = "SR 822.115.2 Art. 1"

    def formula(person, period, parameters):
        return (
            person('jarg_arbeit_uebersteigt_leistungsfaehigkeit', period)
            + person('jarg_arbeit_missbrauchsrisiko', period)
            + person('jarg_arbeit_belastendes_zeitsystem', period)
            + person('jarg_arbeit_physikalische_einwirkungen', period)
            + person('jarg_arbeit_biologische_agenzien', period)
            + person('jarg_arbeit_chemische_agenzien', period)
            + person('jarg_arbeit_unfallgefaehrliche_maschinen', period)
            + person('jarg_arbeit_brand_explosionsgefahr', period)
            + person('jarg_arbeit_gefaehrliche_umgebung', period)
            + person('jarg_arbeit_gefaehrliche_tiere', period)
            + person('jarg_arbeit_industrielles_schlachten', period)
            + person('jarg_arbeit_altmaterial_sortierung', period)
        ) > 0
