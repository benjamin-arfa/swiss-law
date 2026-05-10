"""SR 744.211 Art. 11

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class planvorlagen_zur_vernehmlassung_uebermittelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesamt übermittelt Unterlagen über neuen Fahrzeugtyp an kantonale Behörde zur Vernehmlassung"
    reference = "SR 744.211 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        neuer_fahrzeugtyp = person('neuer_fahrzeugtyp_trolleybus_oder_anhaenger', period)
        unterlagen_vollstaendig = person('unterlagen_art10_abs2_a_bis_e_vorhanden', period)
        return neuer_fahrzeugtyp * unterlagen_vollstaendig


class neuer_fahrzeugtyp_trolleybus_oder_anhaenger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrzeugtyp ist ein Trolleybus oder Anhänger (neuer Typ)"
    reference = "SR 744.211 Art. 11 Abs. 1"


class unterlagen_art10_abs2_a_bis_e_vorhanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterlagen gemäss Art. 10 Abs. 2 Bst. a–e sind vorhanden"
    reference = "SR 744.211 Art. 11 Abs. 1"


class abmessungen_oder_gewicht_ueberschreiten_motorwagen_normen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Abmessungen oder Gewicht des Fahrzeugs überschreiten die für Motorwagen geltenden Normen"
    reference = "SR 744.211 Art. 11 Abs. 2"


class kantonale_zustimmung_fuer_genehmigung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zustimmung der kantonalen Behörde ist Voraussetzung für Genehmigung des Bundesamtes"
    reference = "SR 744.211 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        return person('abmessungen_oder_gewicht_ueberschreiten_motorwagen_normen', period)


class vorlage_kantonaler_behoerde_zu_unterbreiten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorlage ist in jedem Fall der kantonalen Behörde zu unterbreiten (wegen Überschreitung der Normen)"
    reference = "SR 744.211 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        return person('abmessungen_oder_gewicht_ueberschreiten_motorwagen_normen', period)


class genehmigung_fuer_bestimmtes_netz_oder_strecke(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Genehmigung der Planvorlagen ist für ein bestimmtes Netz oder genau bezeichnete Strecken erteilt"
    reference = "SR 744.211 Art. 11 Abs. 3"

    def formula(person, period, parameters):
        netz_bezeichnet = person('netz_oder_strecke_genau_bezeichnet', period)
        genehmigung_erteilt = person('planvorlagen_genehmigung_erteilt', period)
        return netz_bezeichnet * genehmigung_erteilt


class netz_oder_strecke_genau_bezeichnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Netz oder die Strecke ist genau bezeichnet (Voraussetzung für Genehmigung)"
    reference = "SR 744.211 Art. 11 Abs. 3"


class planvorlagen_genehmigung_erteilt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Genehmigung der Planvorlagen durch das Bundesamt erteilt"
    reference = "SR 744.211 Art. 11 Abs. 3"


class vertrag_vor_plangenehmigung_abgeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bau- oder Lieferungsvertrag wurde vor Genehmigung der Planvorlagen abgeschlossen"
    reference = "SR 744.211 Art. 11 Abs. 4"


class vertrag_hat_keinen_anspruch_auf_beruecksichtigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vor Genehmigung abgeschlossene Verträge haben keinen Anspruch auf Berücksichtigung"
    reference = "SR 744.211 Art. 11 Abs. 4"

    def formula(person, period, parameters):
        return person('vertrag_vor_plangenehmigung_abgeschlossen', period)
