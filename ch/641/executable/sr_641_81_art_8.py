"""SR 641.81 Art. 8 - Tarif (Tariff rates)

Heavy Vehicle Tax Act (SVAG) - Tariff rates for heavy vehicle tax.
Art. 8 Abs. 1:
  a) Min 0.6 Rappen, max 2.5 Rappen per km per tonne gross weight
  b) If general max weight raised to 40t: max 3 Rappen; for vehicles <=28t
     may be reduced by up to 1/5
  c) Emission-based: average tariff applies, higher for above-avg emissions,
     lower for below-avg emissions

Generated from: ch/641/de/641.81.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class svag_tarif_rappen_pro_km_tonne(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Applicable tariff rate in Rappen per km per tonne (SR 641.81 Art. 8)"
    reference = "SR 641.81 Art. 8"

    def formula(person, period, parameters):
        gewicht = person("svag_hoechstzulaessiges_gesamtgewicht", period)
        emissions_kategorie = person("svag_emissions_kategorie", period)

        # Base tariff: between 0.6 and 2.5 Rappen (standard), up to 3.0 Rappen
        # if max weight raised to 40 tonnes
        basis_tarif = 2.5

        # Vehicles up to 28 tonnes may get up to 1/5 reduction
        reduktion_bis_28t = where(gewicht <= 28.0, basis_tarif * 0.2, 0.0)

        # Emission-based adjustment: +/- around the average
        # 0 = average, 1 = above average, -1 = below average
        emissions_anpassung = where(
            emissions_kategorie > 0, 0.3,
            where(emissions_kategorie < 0, -0.3, 0.0)
        )

        tarif = basis_tarif - reduktion_bis_28t + emissions_anpassung

        # Enforce legal bounds: min 0.6, max 3.0 Rappen
        tarif = max_(tarif, 0.6)
        tarif = min_(tarif, 3.0)

        return tarif


class svag_emissions_kategorie(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Vehicle emission category: -1=below avg, 0=average, 1=above avg (SR 641.81 Art. 8 Abs. 1 lit. c)"
    reference = "SR 641.81 Art. 8"
    default_value = 0


class svag_abgabe_leistungsabhaengig(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Performance-based heavy vehicle tax in CHF (SR 641.81 Art. 8)"
    reference = "SR 641.81 Art. 8"

    def formula(person, period, parameters):
        km = person("svag_gefahrene_kilometer", period)
        gewicht = person("svag_hoechstzulaessiges_gesamtgewicht", period)
        tarif_rappen = person("svag_tarif_rappen_pro_km_tonne", period)
        ist_personentransport = person("svag_fahrzeug_personentransport", period)

        # Leistungsabhaengige Abgabe: tarif * km * gewicht / 100 (Rappen to CHF)
        abgabe = tarif_rappen * km * gewicht / 100.0

        # For passenger transport, flat-rate applies instead (Art. 4)
        return where(ist_personentransport, 0.0, abgabe)
