"""SR 0.102.1 Art. 5

Generated from: ch/0/de/0.102.1.md
"""

from dateutil.relativedelta import relativedelta
from openfisca_core.model_api import *
from openfisca_switzerland.entities import *
import calendar


class protocol_entry_into_force_date(Variable):
    value_type = date
    label = "Entry into force date of the European Charter protocol"
    definition_period = YEAR
    data_uses = "protocol_signature_date", "protocol_ratification_date"

    def formula(person, period, parameters, protocol_signature_date, protocol_ratification_date):
        num_signing_countries = parameters(period).protocol.num_signing_countries
        min_signature_date = "1 01 2023"  # fixed date
        required_signatures = 8
        protocol_signatures_count = (
            person("protocol_signatures", period).cumsum() if "protocol_signatures" in person.resources else 0
        )

        early_entry_into_force_date = ""
        if protocol_signatures_count >= required_signatures:
            days_required = 3 * 30
            if parameters(period).entity.protocol_signatures_date
                <= parameters(period).entity.protocol_ratification_date
                    + relativedelta(months=+9):

                early_entry_into_force_date = (
                    parameters(period).entity.protocol_signature_date
                    + relativedelta(months=+3)
                )
                earliest_ratification_date = (
                    (parameters(period).entity.protocol_signature_date
                        + relativedelta(months=+3))
                    + relativedelta(
                        month=calendar.monthrange(
                            int(protocol_signature_date + relativedelta(months=+3)).year,
                            calendar.month(-1)
                        )[1] - 1
                    )
                )
                latest_ratification_date = (
                    earliest_ratification_date + relativedelta(days=1)
                )
            else:
                earliest_ratification_date = (
                    (parameters(period).entity.protocol_signature_date
                        + relativedelta(months=+3))
                    + relativedelta(
                        month=calendar.monthrange(
                            int(parameters(period).entity.protocol_signature_date
                                + relativedelta(months=+3)).year,
                            calendar.month(-1)
                        )[1] - 1
                    )
                )
                early_entry_into_force_date = earliest_ratification_date

        late_entry_into_force_date = date.min
        late_entity_id = "late protocol signatory"
        if person.legal_entity == late_entity_id:
            late_protocol_signature_count = protocol_signatures_count + 1

            days_required = 3 * 30
            signatories_signed_up_to = (
                protocol_signatures_count
                if protocol_signatures_count < required_signatures else required_signatures
            )
            late_entity_signature_date = (
                parameters(period).entity.protocol_signature_date if not protocol_signatures_count else (
                    parameters(period).entity.protocol_signatures_dates[signatories_signed_up_to].date()
                )
            )
            late_entry_into_force_date = (
                late_entity_signature_date
                + relativedelta(months=+3)
            )

        return min(
            early_entry_into_force_date.date() if early_entry_into_force_date else date.min,
            late_entry_into_force_date.date()
        )


class signature_date(Variable):
    value_type = date
    label = "Protocol signature date for the entity"


class ratification_date(Variable):
    value_type = date
    label = "Date when the entity signified it has ratified the Protocol"
