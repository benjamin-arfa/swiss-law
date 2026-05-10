"""SR 836.21 Art. 10 - Duration of entitlement after wage claim expires; coordination

Art. 10: After the employee's inability to work begins (Art. 324a OR), family
allowances continue for the current month plus 3 subsequent months.
Same for unpaid leave (par. 1bis). After interruption, entitlement resumes
from the 1st of the month work is resumed (par. 1ter).

Without wage entitlement, allowances continue during:
(a) maternity leave: max 16 weeks
(b) extended maternity (hospitalized newborn): max 22 weeks
(bbis) extended maternity (death of other parent): max 16 weeks
(bter) both extensions combined: max 24 weeks
(c) other parent's leave: max 2 weeks
(cbis) other parent's leave extended (death of mother): max 16 weeks
(cter) both extensions combined: max 24 weeks
(d) care leave for seriously ill/injured child: max 14 weeks
(e) adoption leave: 2 weeks
(f) youth leave (Art. 329e OR): during leave

After death of employee: current month + 3 months.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class arbeitsverhinderung_beginn_monat(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Month in which inability to work began (Art. 10 par. 1 FamZV)"
    default_value = 0


class monate_seit_arbeitsverhinderung(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Months elapsed since beginning of inability to work (Art. 10 par. 1 FamZV)"
    default_value = 0


class anspruch_famz_nach_lohnende(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Continued entitlement to family allowances after wage claim expires (Art. 10 par. 1 FamZV)"

    def formula(person, period, parameters):
        monate = person("monate_seit_arbeitsverhinderung", period)
        # Current month + 3 following months = up to 4 months total
        return monate <= 4


class unbezahlter_urlaub(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Employee is on unpaid leave (Art. 10 par. 1bis FamZV)"
    default_value = False


class monate_seit_unbezahltem_urlaub(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Months since unpaid leave began (Art. 10 par. 1bis FamZV)"
    default_value = 0


class anspruch_famz_unbezahlter_urlaub(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Continued entitlement during unpaid leave (Art. 10 par. 1bis FamZV)"

    def formula(person, period, parameters):
        urlaub = person("unbezahlter_urlaub", period)
        monate = person("monate_seit_unbezahltem_urlaub", period)
        return urlaub * (monate <= 4)


class wochen_mutterschaftsurlaub(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Weeks of maternity leave taken (Art. 10 par. 2 let. a FamZV)"
    default_value = 0


class neugeborenes_hospitalisiert(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Newborn is hospitalized (Art. 10 par. 2 let. b FamZV)"
    default_value = False


class anderer_elternteil_verstorben(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Other parent has died (Art. 10 par. 2 let. bbis FamZV)"
    default_value = False


class max_wochen_mutterschaftsurlaub(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Maximum weeks of maternity leave with family allowance entitlement (Art. 10 par. 2 FamZV)"

    def formula(person, period, parameters):
        hospitalisiert = person("neugeborenes_hospitalisiert", period)
        verstorben = person("anderer_elternteil_verstorben", period)

        # Base: 16 weeks (let. a)
        # Hospitalized newborn: 22 weeks (let. b)
        # Death of other parent: 16 weeks (let. bbis) - same as base
        # Both: 24 weeks (let. bter)
        return where(
            hospitalisiert * verstorben,
            24,
            where(
                hospitalisiert,
                22,
                16,
            ),
        )


class wochen_urlaub_anderer_elternteil(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Weeks of other parent's leave taken (Art. 10 par. 2 let. c FamZV)"
    default_value = 0


class mutter_verstorben(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Mother has died (Art. 10 par. 2 let. cbis FamZV)"
    default_value = False


class max_wochen_urlaub_anderer_elternteil(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Maximum weeks of other parent's leave with family allowance entitlement (Art. 10 par. 2 FamZV)"

    def formula(person, period, parameters):
        mutter_tod = person("mutter_verstorben", period)
        hospitalisiert = person("neugeborenes_hospitalisiert", period)

        # Base: 2 weeks (let. c)
        # Mother died: 16 weeks (let. cbis)
        # Mother died + hospitalized: 24 weeks (let. cter)
        return where(
            mutter_tod * hospitalisiert,
            24,
            where(
                mutter_tod,
                16,
                2,
            ),
        )


class wochen_betreuungsurlaub_kind(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Weeks of care leave for seriously ill/injured child (Art. 10 par. 2 let. d FamZV)"
    default_value = 0


class anspruch_famz_betreuungsurlaub(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Entitlement to family allowances during care leave (Art. 10 par. 2 let. d FamZV)"

    def formula(person, period, parameters):
        wochen = person("wochen_betreuungsurlaub_kind", period)
        return wochen <= 14
