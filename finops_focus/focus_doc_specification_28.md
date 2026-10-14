---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/appendix/commitment-program-eligibility-details-examples/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: aa23336f462779c9
---
# 8.4 Examples: Commitment Program Eligibility Details

Note: The following examples are informative and non-normative. They do not define requirements.


This section demonstrates how CommitmentProgramEligibilityDetails interacts with other columns for *capacity reservation* programs. For discount-bearing program SQL queries, see the Commitment Program Eligibility Details supported feature.

## 8.4.1 Capacity Reservation Eligible Spend

This example demonstrates how CommitmentProgramEligibilityDetails interacts with CapacityReservationId and CapacityReservationStatus for *capacity reservation* programs. Unlike discount-bearing *commitment programs*, capacity reservations secure resource availability and are tracked via their own columns rather than the *commitment discount* columns.

Acme Corp runs compute workloads on Aura Web and holds an Advance Resource Commitment (cr-arc-acme-001) for a single charge period (2025-04-01). The `ProgramType` values "Advance Resource Commitment" and "Zonal Resource Commitment" are illustrative and do not correspond to a specific provider's program names.

This example focuses on Usage rows. Purchase rows for the reservation itself are not shown.

Four usage rows for the period:

1. **Used capacity** (Row 1): Compute usage consuming the reservation. CapacityReservationStatus is "Used". BilledCost and EffectiveCost are both $180.00.
2. **Unused capacity** (Row 2): Reserved capacity that went idle. CapacityReservationStatus is "Unused". BilledCost and EffectiveCost are both $70.00. Unlike *commitment discount* unused rows (where BilledCost is $0.00 because the purchase is invoiced separately), capacity reservation rows reflect the cost of reserved capacity whether consumed or not.
3. **Eligible but unreserved** (Row 3): Compute usage eligible for a Zonal Resource Commitment but no reservation is active. CapacityReservationId and CapacityReservationStatus are null. BilledCost and EffectiveCost are both $120.00 at standard pricing.
4. **Ineligible** (Row 4): A support fee with no *commitment program* eligibility. CommitmentProgramEligibilityDetails is null.

CommitmentProgramEligibilityDetails is populated on both Used and Unused rows (Rows 1 and 2). The column requirement states that CommitmentProgramEligibilityDetails "MUST NOT be null when a charge is eligible for a commitment program, regardless of whether a commitment was actually applied to the charge." The underlying resource type remains eligible for the program regardless of utilization status.

The capacity reservation query filters on CommitmentProgramEligibilityDetails and specific `ProgramType` values. Row 4 is excluded because CommitmentProgramEligibilityDetails is null. Rows 1 through 3 appear in the output, grouped by `ProgramType` and CapacityReservationStatus, allowing practitioners to see used, unused, and unreserved eligible spend separately.