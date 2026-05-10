"""SR 731.31 Art. 17

Generated from: ch/731/de/731.31.md

Annual standby fee (Bereitstellungspauschale) for systemically critical
companies.  Composed of federal bond yield component + third-party costs.
Interest and risk surcharges paid during the year are deducted.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_bundesanleihe_rendite(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Rendite einer 4-jaehrigen Bundesanleihe (Anteil, mind. 0)"
    reference = "SR 731.31 Art. 17 Abs. 2 lit. a"


class firevo_verpflichtungskredit(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Verpflichtungskredit im Zeitpunkt des Inkrafttretens (CHF)"
    reference = "SR 731.31 Art. 17 Abs. 2 lit. a"


class firevo_drittkosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten fuer den Beizug Dritter fuer den Vollzug (CHF)"
    reference = "SR 731.31 Art. 17 Abs. 2 lit. b"


class firevo_bereitstellungspauschale_brutto(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bereitstellungspauschale brutto (CHF)"
    reference = "SR 731.31 Art. 17 Abs. 2"

    def formula(person, period, parameters):
        """Art. 17 Abs. 2:
        a. yield of 4-year federal bond * commitment credit (min 0%)
        b. plus third-party costs
        """
        rendite = person('firevo_bundesanleihe_rendite', period)
        kredit = person('firevo_verpflichtungskredit', period)
        drittkosten = person('firevo_drittkosten', period)

        rendite_component = max_(rendite, 0.0) * kredit
        return rendite_component + drittkosten


class firevo_bereitstellungspauschale_netto(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bereitstellungspauschale netto nach Abzug Zinsen/Risikozuschlaege (CHF)"
    reference = "SR 731.31 Art. 17 Abs. 3"

    def formula(person, period, parameters):
        """Art. 17 Abs. 3: Interest and risk surcharges paid in the year
        are deducted.  If they exceed the standby fee, fee is zero.
        """
        brutto = person('firevo_bereitstellungspauschale_brutto', period)
        zinsen_und_zuschlag = person('firevo_zinskosten_total', period)

        return max_(brutto - zinsen_und_zuschlag, 0.0)
