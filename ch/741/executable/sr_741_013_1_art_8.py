"""SR 741.013.1 Art. 8

Generated from: ch/741/de/741.013.1.md

VSKV-ASTRA: Sicherheitsabzug
Safety deductions from speed measurements depending on the measurement
method and the measured speed value.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity
import numpy as np

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class gemessene_geschwindigkeit(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Gemessener Geschwindigkeitswert in km/h (auf naechste ganze Zahl abgerundet)"
    reference = "SR 741.013.1 Art. 8"


class messart_code(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Messart-Code: 1=Radar, 2=Laser, 3=Radar in Kurven, 4=Moving-Radar, 5=Schwellendetektoren, 6=Abschnittsgeschwindigkeit, 7=Analoger Fahrtschreiber, 8=Digitaler Fahrtschreiber, 9=Datenaufzeichnungsgeraet"
    reference = "SR 741.013.1 Art. 8"


class sicherheitsabzug_radar(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Sicherheitsabzug bei Radarmessungen (Art. 8 Abs. 1 lit. a VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8 Abs. 1 lit. a"

    def formula(person, period, parameters):
        v = person("gemessene_geschwindigkeit", period)
        return np.select(
            [v <= 100, v <= 150, v > 150],
            [5.0, 6.0, 7.0],
            default=0.0
        )


class sicherheitsabzug_laser(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Sicherheitsabzug bei Lasermessungen (Art. 8 Abs. 1 lit. b VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8 Abs. 1 lit. b"

    def formula(person, period, parameters):
        v = person("gemessene_geschwindigkeit", period)
        return np.select(
            [v <= 100, v <= 150, v > 150],
            [3.0, 4.0, 5.0],
            default=0.0
        )


class sicherheitsabzug_radar_kurve(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Sicherheitsabzug bei stationaeren Radarmessungen in Kurven (Art. 8 Abs. 1 lit. c VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8 Abs. 1 lit. c"

    def formula(person, period, parameters):
        v = person("gemessene_geschwindigkeit", period)
        return np.where(v <= 100, 10.0, 14.0)


class sicherheitsabzug_moving_radar(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Sicherheitsabzug bei Moving-Radar (Art. 8 Abs. 1 lit. d VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8 Abs. 1 lit. d"

    def formula(person, period, parameters):
        v = person("gemessene_geschwindigkeit", period)
        return np.select(
            [v <= 100, v <= 150, v > 150],
            [7.0, 8.0, 9.0],
            default=0.0
        )


class sicherheitsabzug_schwellendetektoren(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Sicherheitsabzug bei Schwellendetektoren (Art. 8 Abs. 1 lit. e VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8 Abs. 1 lit. e"

    def formula(person, period, parameters):
        v = person("gemessene_geschwindigkeit", period)
        return np.select(
            [v <= 100, v <= 150, v > 150],
            [5.0, 6.0, 7.0],
            default=0.0
        )


class sicherheitsabzug_abschnitt(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Sicherheitsabzug bei Abschnittsgeschwindigkeitskontrollen (Art. 8 Abs. 1 lit. f VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8 Abs. 1 lit. f"

    def formula(person, period, parameters):
        v = person("gemessene_geschwindigkeit", period)
        return np.select(
            [v <= 100, v <= 150, v > 150],
            [5.0, 6.0, 7.0],
            default=0.0
        )


class sicherheitsabzug_fahrtschreiber_analog(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Sicherheitsabzug bei analogen Fahrtschreibern (Art. 8 Abs. 2 lit. a VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8 Abs. 2 lit. a"

    def formula(person, period, parameters):
        return 10.0


class sicherheitsabzug_fahrtschreiber_digital(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Sicherheitsabzug bei digitalen Fahrtschreibern (Art. 8 Abs. 2 lit. b VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8 Abs. 2 lit. b"

    def formula(person, period, parameters):
        return 6.0


class sicherheitsabzug_datenaufzeichnung(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Sicherheitsabzug bei Datenaufzeichnungsgeraeten (Art. 8 Abs. 2 lit. c VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8 Abs. 2 lit. c"

    def formula(person, period, parameters):
        return 14.0


class sicherheitsabzug(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Anwendbarer Sicherheitsabzug basierend auf Messart (Art. 8 VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8"

    def formula(person, period, parameters):
        messart = person("messart_code", period)
        return np.select(
            [
                messart == 1,
                messart == 2,
                messart == 3,
                messart == 4,
                messart == 5,
                messart == 6,
                messart == 7,
                messart == 8,
                messart == 9,
            ],
            [
                person("sicherheitsabzug_radar", period),
                person("sicherheitsabzug_laser", period),
                person("sicherheitsabzug_radar_kurve", period),
                person("sicherheitsabzug_moving_radar", period),
                person("sicherheitsabzug_schwellendetektoren", period),
                person("sicherheitsabzug_abschnitt", period),
                person("sicherheitsabzug_fahrtschreiber_analog", period),
                person("sicherheitsabzug_fahrtschreiber_digital", period),
                person("sicherheitsabzug_datenaufzeichnung", period),
            ],
            default=0.0
        )


class bereinigte_geschwindigkeit(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Bereinigte Geschwindigkeit nach Sicherheitsabzug (Art. 8 VSKV-ASTRA)"
    reference = "SR 741.013.1 Art. 8"

    def formula(person, period, parameters):
        v = person("gemessene_geschwindigkeit", period)
        abzug = person("sicherheitsabzug", period)
        return np.maximum(v - abzug, 0.0)
