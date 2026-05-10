"""SR 614.0 Art. 11

Generated from: ch/614/de/614.0.md

Art. 11: Stellen für interne Revision der zentralen Bundesverwaltung -
Regelung der internen Revisionsstellen, ihrer Unabhängigkeit, Aufgaben,
Berichterstattung und Koordination mit der EFK.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_stelle_fuer_interne_revision(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entität ist eine Stelle für interne Revision der zentralen Bundesverwaltung"
    reference = "SR 614.0 Art. 11 Abs. 1"


class interne_revision_fachlich_unabhaengig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Stelle für interne Revision ist in der Erfüllung ihrer fachlichen "
        "Aufgaben selbstständig und unabhängig (Art. 11 Abs. 1)"
    )
    reference = "SR 614.0 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_stelle_fuer_interne_revision', period)


class geschaeftsordnung_genehmigt_durch_efk(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Geschäftsordnung der Stelle für interne Revision unterliegt "
        "der Genehmigung durch die EFK (Art. 11 Abs. 1)"
    )
    reference = "SR 614.0 Art. 11 Abs. 1"


class efk_beurteilt_wirksamkeit_interne_revision(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK beurteilt periodisch die Wirksamkeit der Stellen für interne "
        "Revision und sorgt für Koordination (Art. 11 Abs. 2)"
    )
    reference = "SR 614.0 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_eidgenoessische_finanzkontrolle', period)


class interne_revision_meldet_maengel_unverzueglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Stelle für interne Revision unterrichtet unverzüglich über Mängel "
        "von grundsätzlicher oder erheblicher finanzieller Bedeutung (Art. 11 Abs. 4)"
    )
    reference = "SR 614.0 Art. 11 Abs. 4"

    def formula(person, period, parameters):
        ist_revision = person('ist_stelle_fuer_interne_revision', period)
        mangel_grundsaetzlich = person('mangel_von_grundsaetzlicher_bedeutung', period)
        mangel_finanziell = person('mangel_von_erheblicher_finanzieller_bedeutung', period)
        return ist_revision * (mangel_grundsaetzlich + mangel_finanziell)


class mangel_von_grundsaetzlicher_bedeutung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Festgestellter Mangel ist von grundsätzlicher Bedeutung"
    reference = "SR 614.0 Art. 11 Abs. 4"


class mangel_von_erheblicher_finanzieller_bedeutung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Festgestellter Mangel ist von erheblicher finanzieller Bedeutung"
    reference = "SR 614.0 Art. 11 Abs. 4"
