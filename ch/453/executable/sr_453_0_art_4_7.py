"""SR 453.0 Art. 4-7

Generated from: ch/453/de/453.0.md

Skipped: Art. 4 - Verantwortung fuer Dokumente (prozedural).
Art. 5 - Anmeldung (prozedural).
Art. 6 - Anmeldepflichtige Personen (prozedural).
Art. 7 - Erfassung von Daten im Informationssystem (prozedural).
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Rein prozedural - Dokumentenpflichten und Anmeldung
