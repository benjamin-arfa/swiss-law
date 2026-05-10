"""SR 210 Art. 30b

Generated from: ch/de/210.md

Aenderung des Geschlechts im Personenstandsregister: Jede Person, die
innerlich fest davon ueberzeugt ist, nicht dem eingetragenen Geschlecht
zuzugehoeren, kann den Eintrag aendern lassen. Unter 16 oder unter
umfassender Beistandschaft: Zustimmung des gesetzlichen Vertreters noetig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kann_geschlechtseintrag_aendern(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person den Geschlechtseintrag selbstaendig aendern kann"
    reference = "SR 210 Art. 30b"

    def formula(person, period, parameters):
        alter_person = person('alter', period)
        unter_beistandschaft = person('unter_umfassender_beistandschaft', period)
        hat_zustimmung = person('hat_zustimmung_gesetzlicher_vertreter', period)

        mindestalter = parameters(period).zgb.geschlechtseintrag.mindestalter_ohne_zustimmung

        # Abs. 4: Unter 16 oder unter umfassender Beistandschaft ->
        # Zustimmung des gesetzlichen Vertreters erforderlich
        braucht_zustimmung = (alter_person < mindestalter) + unter_beistandschaft > 0

        # Kann aendern: entweder keine Zustimmung noetig, oder hat Zustimmung
        return not_(braucht_zustimmung) + (braucht_zustimmung * hat_zustimmung) > 0
