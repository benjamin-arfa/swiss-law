"""SR 0.101.3 Art. 11

Generated from: ch/0/de/0.101.3.md
"""

from openfisca_core.model_api import Variable

class Notifikation_des_EU_Mitgliedstaates(Variable):
    value_type = bool
    label = "Notifikation des EU-Mitgliedstaates"
    definition_period = "1J"

    def formula_1996_03_05(de, period, data):
        # Hier fehlt die Implementierung basierend auf dem Schweizerischen Gesetz und den Artikeln
        return de == True
