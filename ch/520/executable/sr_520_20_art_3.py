"""SR 520.20 Art. 3

Generated from: ch/520/de/520.20.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class notlage_im_asylbereich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Es liegt eine Notlage im Asylbereich vor"
    reference = "SR 520.20 Art. 3 Abs. 1 lit. a"


class keine_anderen_unterbringungsmoeglichkeiten(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Keine anderen Unterbringungsmoeglichkeiten zu annehmbaren Bedingungen verfuegbar"
    reference = "SR 520.20 Art. 3 Abs. 1 lit. b"


class schutzdienstpflichtige_im_einsatz(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Schutzdienstpflichtige sind zur Bewaeltigung der Notlage im Asylbereich im Einsatz"
    reference = "SR 520.20 Art. 3 Abs. 1 lit. c"


class schutzanlage_nicht_fuer_zivilschutz_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die Schutzanlagen und Liegestellen sind fuer den Zivilschutz nicht zwingend erforderlich"
    reference = "SR 520.20 Art. 3 Abs. 1 lit. d"


class armee_benoetigt_schutzanlage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die Armee benoetigt die Schutzanlage zur Erfuellung ihrer Aufgaben"
    reference = "SR 520.20 Art. 3 Abs. 2"


class requisition_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Alle Voraussetzungen fuer die Requisition sind erfuellt"
    reference = "SR 520.20 Art. 3"

    def formula(person, period, parameters):
        notlage = person('notlage_im_asylbereich', period)
        keine_alternative = person('keine_anderen_unterbringungsmoeglichkeiten', period)
        einsatz = person('schutzdienstpflichtige_im_einsatz', period)
        nicht_zivilschutz = person('schutzanlage_nicht_fuer_zivilschutz_erforderlich', period)
        nicht_armee = not_(person('armee_benoetigt_schutzanlage', period))

        return notlage * keine_alternative * einsatz * nicht_zivilschutz * nicht_armee
