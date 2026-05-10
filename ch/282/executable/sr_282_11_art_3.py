"""SR 282.11 Art. 3 - Nachlassvertragsrecht

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class beiratschaft_angeordnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine Beiratschaft wurde angeordnet"
    reference = "SR 282.11 Art. 3 Abs. 2"


class beiratschaft_hat_in_angemessener_frist_zum_ziel_gefuehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Beiratschaft hat in angemessener Frist zum Ziel gefuehrt"
    reference = "SR 282.11 Art. 3 Abs. 2"


class zustimmende_glaeubiger_anteil(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der zustimmenden Glaeubiger an den anwesenden Glaeubigern"
    reference = "SR 282.11 Art. 3 Abs. 3"


class zustimmende_forderungen_anteil_vertreten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der zustimmenden Forderungen an den vertretenen Forderungen"
    reference = "SR 282.11 Art. 3 Abs. 3"


class zustimmende_forderungen_anteil_gesamt(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der zustimmenden Forderungen an allen nicht pfandgedeckten Forderungen"
    reference = "SR 282.11 Art. 3 Abs. 3"


# Computed variables

class nachlassvertrag_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ein Nachlassvertrag darf zugelassen werden"
    reference = "SR 282.11 Art. 3 Abs. 2"

    def formula(self, period, parameters):
        beiratschaft = self('beiratschaft_angeordnet', period)
        ziel = self('beiratschaft_hat_in_angemessener_frist_zum_ziel_gefuehrt', period)
        # Nur wenn Beiratschaft angeordnet und nicht zum Ziel gefuehrt hat
        return beiratschaft * (1 - ziel)


class glaeubigerbeschluss_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beschluss ueber Eingriffe in Glaeubigerrechte ist gueltig"
    reference = "SR 282.11 Art. 3 Abs. 3"

    def formula(self, period, parameters):
        anteil_glaeubiger = self('zustimmende_glaeubiger_anteil', period)
        anteil_vertreten = self('zustimmende_forderungen_anteil_vertreten', period)
        anteil_gesamt = self('zustimmende_forderungen_anteil_gesamt', period)
        # Zwei Drittel der anwesenden Glaeubiger UND deren Forderungen
        # zwei Drittel der vertretenen, mindestens Haelfte aller nicht pfandgedeckten
        return (anteil_glaeubiger >= 2/3) * (anteil_vertreten >= 2/3) * (anteil_gesamt >= 0.5)
