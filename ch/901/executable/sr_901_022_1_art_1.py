"""SR 901.022.1 Art. 1

Generated from: ch/901/de/901.022.1.md

Anwendungsgebiete fuer Steuererleichterungen: Definiert die Gemeinden
pro Kanton, die als Anwendungsgebiete gelten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


# Gemeindelisten nach Kanton fuer Steuererleichterungen
ANWENDUNGSGEBIETE = {
    'AG': ['Klingnau', 'Menziken', 'Reinach', 'Zurzach'],
    'AR': ['Buehler', 'Wolfhalden'],
    'AI': ['Gonten', 'Oberegg', 'Schlatt-Haslen'],
    'BE': [
        'Biglen', 'Corgemont', 'Court', 'Frutigen', 'Hasle bei Burgdorf',
        'Huttwil', 'Langnau im Emmental', 'Loveresse', 'Luetzelflueh',
        'Meiringen', 'Moutier', 'Oberdiessbach', 'Pery-La Heutte',
        'Reconvilier', 'Reichenbach im Kandertal', 'Ruegsau',
        'Schwarzenburg', 'Sonceboz-Sombeval', 'Sumiswald', 'Tavannes',
        'Tramelan', 'Worb',
    ],
    'BL': ['Oberdorf'],
    'FR': ['Billens-Hennens', 'Mezieres', 'Romont', 'Villaz'],
    'GL': ['Glarus', 'Glarus Sued'],
    'GR': [
        'Albula/Alvra', 'Bregaglia', 'Cazis', 'Disentis/Musteir',
        'Fideris', 'Furna', 'Ilanz/Glion', 'Jenaz', 'Kueblis', 'Luzein',
        'Poschiavo', 'Schiers', 'Schluein', 'Scuol',
        'Seewis im Praettigau', 'Thusis', 'Trun', 'Val Muestair', 'Zernez',
    ],
    'JU': [
        'Alle', 'Cornol', 'Courgenay', 'Courrendlin', 'Courroux',
        'Courtedoux', 'Courtetelle', 'Delemont', 'Haute-Sorne',
        'Les Bois', 'Porrentruy', 'Rossemaison', 'Saignelegier',
    ],
    'LU': ['Schuepfheim', 'Willisau', 'Wolhusen'],
    'NE': ['La Chaux-de-Fonds', 'Le Landeron', 'Le Locle', 'Val-de-Travers'],
    'SG': [
        'Ebnat-Kappel', 'Flums', 'Goldach', 'Mels', 'Rheineck',
        'Rorschach', 'Rorschacherberg', 'Uzwil', 'Wattwil',
    ],
    'SH': ['Hallau', 'Oberhallau', 'Siblingen', 'Trasadingen', 'Wilchingen'],
    'SO': ['Balsthal', 'Breitenbach'],
    'TG': ['Amriswil', 'Hefenhofen'],
    'TI': [
        'Ascona', 'Bellinzona', 'Biasca', 'Brione sopra Minusio',
        'Cadenazzo', 'Gordola', 'Locarno', 'Losone', 'Lumino', 'Minusio',
        'Muralto', 'Orselina', 'Tenero-Contra', 'Terre di Pedemonte',
    ],
    'UR': [
        'Altdorf', 'Buerglen', 'Erstfeld', 'Gurtnellen', 'Schattdorf',
        'Seedorf', 'Silenen',
    ],
    'VD': [
        'Aigle', 'Bex', 'Chateau-d\'Oex', 'Cheseaux-Noreaz', 'Cossonay',
        'Echallens', 'Grandson', 'Lavey-Morcles', 'Montagny-pres-Yverdon',
        'Moudon', 'Penthalaz', 'Rennaz', 'Sainte-Croix',
        'Valeyres-sous-Montagny', 'Vallorbe', 'Yverdon-les-Bains',
    ],
    'VS': [
        'Ardon', 'Bitsch', 'Brig-Glis', 'Collombey-Muraz', 'Conthey',
        'Dorenaz', 'Fully', 'Gampel-Bratsch', 'Leuk', 'Martigny',
        'Martigny-Combe', 'Massongex', 'Monthey', 'Naters', 'Niedergesteln',
        'Raron', 'Riddes', 'Saint-Leonard', 'Saint-Maurice', 'Saxon',
        'Sierre', 'Sion', 'St. Niklaus', 'Steg-Hohtenn',
        'Turtmann-Unterems', 'Vernayaz', 'Vetroz', 'Vouvry',
    ],
    'ZH': ['Bachenbuelach', 'Duernten', 'Rueti'],
}

# Flat set of all qualifying municipalities
ALLE_ANWENDUNGSGEBIETE = {g for lst in ANWENDUNGSGEBIETE.values() for g in lst}


class gemeinde_name(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Name der Gemeinde des Unternehmensstandorts"
    reference = "SR 901.022.1 Art. 1"
    default_value = ''


class ist_anwendungsgebiet_steuererleichterungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gemeinde als Anwendungsgebiet fuer Steuererleichterungen gilt"
    reference = "SR 901.022.1 Art. 1"
