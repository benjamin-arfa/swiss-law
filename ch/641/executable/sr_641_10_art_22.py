"""SR 641.10 Art. 22

Generated from: ch/641/de/641.10.md

Versicherungspraemienabgabe - Ausnahmen:
Von der Abgabe ausgenommen sind Praemienzahlungen fuer:
a. nichtrückkaufsfaehige Lebensversicherung / rueckkaufsfaehige mit
   periodischer Praemienzahlung
abis. Lebensversicherung fuer berufliche Vorsorge (BVG)
ater. Lebensversicherung mit Versicherungsnehmer im Ausland
b. Kranken- und Invaliditaetsversicherung
c. Unfallversicherung
d. Transportversicherung fuer Gueter
e. Elementarschaeden an Kulturland
f. Arbeitslosenversicherung
g. Hagelversicherung
h. Viehversicherung
i. Rueckversicherung
k. Kaskoversicherung fuer bestimmte Luftfahrzeuge/Schiffe im Ausland
l. Feuer/Diebstahl/Glas/Wasser/Kredit/Maschinen/Schmuck wenn Sache im Ausland
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class stg_versicherungsart(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Art der Versicherung: 1=Leben nicht-rueckkaufsfaehig, 2=Leben rueckkaufsfaehig periodisch, 3=Leben BVG, 4=Leben Ausland, 5=Kranken/Invaliditaet, 6=Unfall, 7=Transport, 8=Elementarschaeden, 9=Arbeitslosigkeit, 10=Hagel, 11=Vieh, 12=Rueck, 13=Kasko Ausland, 14=Sachversicherung Ausland, 15=Leben steuerbar, 99=andere steuerbar"
    reference = "SR 641.10 Art. 22"


class stg_versicherung_praemie_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Versicherungspraemie von der Stempelabgabe befreit ist"
    reference = "SR 641.10 Art. 22"

    def formula(person, period, parameters):
        art = person('stg_versicherungsart', period)
        # Befreit sind Arten 1-14 (alle Ausnahmen)
        # Nicht befreit: 15=steuerbare Lebensversicherung, 99=andere steuerbare
        return art <= 14
