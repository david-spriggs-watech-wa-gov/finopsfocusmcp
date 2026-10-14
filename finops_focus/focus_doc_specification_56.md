---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/appendix/correction-handling-examples/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "44f5c4e3f8626481"
---
# 8.6 Examples: Correction Handling

This section provides examples of how correction handling may be implemented in alignment with the FOCUS specification. The examples are limited to illustrating correction handling for the Cost and Usage FOCUS dataset, and cover scenarios involving corrections to open and closed billing periods, as well as the various delivery mechanisms and correction styles supported by FOCUS.

The examples that follow are sectioned by Billing Period Status (i.e., "Open" or "Closed") and Billing Period Category (i.e., current open period, or previous open period, or closed):

| Billing Period Status | Billing Period Category | Description | 
|---|---|---|
| Open | Current Open | Examples of corrections to the current, open billing period. | 
| Open | Previous Open | Examples of corrections to a previous billing period that has not yet been closed. | 
| Closed | Closed | Examples of corrections to a closed billing period. | 

Within each of the sections above, the following four correction scenarios are demonstrated:

| Correction Scenario | Description | 
|---|---|
| **Partial Reallocation to Correct Resource** | Correcting misattributed costs between resources. | 
| **Late-Arriving Usage** | Accounting for omitted costs and usage incurred in a prior timeframe. | 
| **Itemized Cost-Only Corrections** | Reconciling minor cost drift with explicit adjustments per SKU. | 
| **Bulk Cost-Only Corrections** | Reconciling minor cost drift using a single, consolidated adjustment. | 

The example dataset artifacts provided in these scenarios demonstrate three distinct correction styles, each aligned with one of the supported delivery mechanisms:

| Correction Style | Delivery Mechanism | Description | 
|---|---|---|
| **Replacement** | Overwrite | Corrections are modeled through updates, additions, or omissions relative to the previous snapshot. This style reflects the latest state of data and does not retain historical correction records unless externally preserved. Net data volume is the lowest of the three correction styles as each dataset artifact supersedes previously delivered ones for the same delivery scope. | 
| **Delta** | Append | Corrections are represented by additive records that increment or decrement selected cost and quantity values. Original records remain unchanged, and reversals are optional. This style offers limited audit transparency. Net data volume is typically higher than Replacement but lower than Ledger as all delivered dataset artifacts are preserved. | 
| **Ledger** | Append | Corrections typically follow a two-step approach: reversal of the original record (if needed), and addition of a corrected record. Reversal is performed by creating a record with opposite cost and quantity values, while all other columns match the original. This style preserves full correction history and supports comprehensive auditability. Net data volume is typically the highest of the three correction styles as each correction requires explicit reversal and re-entry records. | 

## 8.6.1 Corrections to Open Billing Period

The following examples illustrate how corrections to open billing periods, including both current and previous open periods, may be represented in FOCUS Cost and Usage datasets, using various delivery mechanisms and correction styles.

Note: Corrections in this section apply to billing periods that are still open, whether current (Current Open-Period Correction Scenarios) or previous (Previous Open-Period Correction Scenarios). In the examples that follow, the InvoiceId column contains a provisional or placeholder value, even though the invoice has not yet been issued.

### 8.6.1.1 Current Open-Period Correction Scenarios

These scenarios address discrepancies related to charges from the July 2025 billing period. The discrepancies were identified on July 5th, 2025, while the July 2025 billing period was still open.

#### 8.6.1.1.1 Billing Period Alignment

Since the billing period is still open and invoices have not yet been issued, corrections can be applied without introducing retroactive semantics. The ChargeClass is set to null, and the BillingPeriodStart/End reflect the billing period in which the cost or usage was actually incurred (July).

#### 8.6.1.1.2 Correction Style

CrestNode delivers corrections using Replacement, Delta, and Ledger styles, each providing varying levels of traceability and auditability.

#### 8.6.1.1.3 Scenario 1: Current Open-Period Correction - Partial Reallocation to Correct Resource

On July 5th, 2025, CrestNode identified that a charge record for the current billing period (July 2025) was incorrectly attributed entirely to ResourceId `R-111`. In reality, only part of the cost and usage belonged to that resource, while the remainder pertained to ResourceId `R-222`.

Since the billing period was still open and invoices had not yet been issued, the correction was applied within the same billing period, allowing for more flexible correction mechanisms. To correct the misattribution, CrestNode had the option to use any of the following approaches:

- Replacement style correction, which replaced the original record attributed to R-111 with a corrected version, and introduced a new record for `R-222` to reflect the accurate resource attribution.
- Delta style correction, which used a decrement to reduce the cost from the incorrectly attributed resource (`R-111`), and an increment to assign the cost to the correct resource (`R-222`).
- Ledger style correction, which negated the original charge and introduced two new records (one for each resource) accurately reflecting the corrected cost and usage distribution.

CSV Examples:

- Original Dataset Artifact
- Replacement Dataset Artifact
- Delta Dataset Artifact
- Ledger Dataset Artifact

Note the following details in the example datasets:

- The correction is modeled using either Overwrite or Append mechanisms, as the billing period is still open and invoice has not yet been issued.
- Original Dataset includes:
  - A charge record attributed entirely to ResourceId `R-111`.
- Replacement style correction includes:
  - A replacement of the original record to reflect the corrected portion for `R-111`.
  - An additional record for `R-222` to account for the remaining portion of the cost and usage.
- Delta style correction includes:
  - A decrement record for `R-111`, reducing the cost previously misattributed to that resource.
  - An increment record for `R-222`, assigning the corresponding portion of the cost to the correct resource.
- Ledger style correction includes:
  - A reversal record for the original charge.
  - A corrected record for `R-111`.
  - A corrected record for `R-222`.
- Each correction record has ChargeClass set to null, indicating that it pertains to an open billing period and is not a retroactive correction to a previously closed billing period.
- Each correction record is assigned to the current billing period (July 2025).

#### 8.6.1.1.4 Scenario 2: Current Open-Period Correction - Late-Arriving Usage

On July 5th, 2025, CrestNode identified a cost incurred during the current billing period (ChargePeriodStart: `2025-07-01`) that was not included in the initial dataset.

Since the billing period was still open and invoices had not yet been issued, the correction was applied within the same billing period, allowing for more flexible correction mechanisms. To account for the previously omitted usage, CrestNode had the option to use either Overwrite or Append mechanisms, i.e.:

- Replacement style correction
- Delta style correction
- Ledger style correction

Regardless of the correction style used, the correction was realized by introducing a single increment record representing the late-arriving usage and associated cost.

CSV Examples:

Note the following details in the example datasets:

- The original dataset was incomplete and did not capture late-arriving usage and associated cost for July 2025.
- The correction may be modeled using either Overwrite or Append mechanisms, as the billing period is still open.
- All three correction styles (Replacement, Delta, and Ledger) introduce a single increment record representing the previously omitted usage and associated cost.
- The correction record has ChargeClass set to null, indicating that it pertains to an open billing period and is not a retroactive correction to a previously closed billing period.
- The correction record is assigned to the current billing period (July 2025).

#### 8.6.1.1.5 Scenario 3: Current Open-Period Correction - Itemized Cost-Only Corrections

On July 5th, 2025, CrestNode detected a minor cost discrepancy caused by accumulated rounding differences across multiple records spanning two distinct SkuPriceId values. While each individual record was correctly rounded, the aggregated cost differed slightly from the precise total, resulting in small drifts.

Since the billing period was still open and invoices had not yet been issued, the correction was applied within the same billing period, allowing for more flexible correction mechanisms. To reconcile this discrepancy, CrestNode had the option to use either Overwrite or Append mechanisms, i.e.:

- Replacement style correction
- Delta style correction
- Ledger style correction

Regardless of the correction style used, the correction was realized by introducing two itemized increment records, each representing a cost-only adjustment for one of the affected SkuPriceId values. Unlike bulk corrections, which consolidate adjustments into a single record without specifying a SkuPriceId, this approach explicitly itemizes the correction per SkuPriceId. Because the original records were individually correct and no single record requires reversal, the Ledger style correction does not include explicit reversals. In this case, the Ledger and Delta corrections are identical, as only additive records are needed to reconcile the accumulated drift.

Compared to the bulk correction approach, this method ensures transparency and traceability and is preferred when itemized correction is feasible.

CSV Examples:

- Original Dataset Artifact
- Replacement Dataset Artifact
- Delta Dataset Artifact
- Ledger Dataset Artifact

Note the following details in the example datasets:

- The original dataset was complete in terms of usage, but a minor cost discrepancy was identified due to accumulated rounding drift across multiple records spanning two SkuPriceId values.
- The correction may be modeled using either Overwrite or Append mechanisms, as the billing period is still open.
- All three correction styles (Replacement, Delta, and Ledger) introduce two itemized increment records representing cost-only adjustments.
- Each correction record explicitly references the affected SkuPriceId.
- Each correction record has ChargeClass set to null, indicating that it pertains to an open billing period and is not a retroactive correction to a previously closed billing period.
- Each correction record has ChargeCategory set to "Adjustment", which is the only valid value when both PricingQuantity and ChargeClass are null, due to the normative requirement that PricingQuantity must not be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
- Each correction record is assigned to the current billing period (July 2025).

#### 8.6.1.1.6 Scenario 4: Current Open-Period Correction - Bulk Cost-Only Corrections

On July 5th, 2025, CrestNode detected a minor cost discrepancy caused by accumulated rounding differences across multiple records spanning two distinct SkuPriceId values. While each individual record was correctly rounded, the aggregated cost differed slightly from the precise total, resulting in small drifts.

Since the billing period was still open and invoices had not yet been issued, the correction was applied within the same billing period, allowing for more flexible correction mechanisms. To reconcile this discrepancy, CrestNode had the option to use either Overwrite or Append mechanisms, i.e.:

- Replacement style correction
- Delta style correction
- Ledger style correction

Regardless of the correction style used, the correction was realized by introducing a single increment record representing the bulk cost-only adjustment. Unlike itemized corrections, this record did not specify a SkuPriceId, as the discrepancy spanned multiple SKU Price IDs. Because the original records were individually correct and no single record requires reversal, the Ledger style correction does not include explicit reversals. In this case, the Ledger and Delta corrections are identical, as only additive records are needed to reconcile the accumulated drift.

Compared to the itemized correction approach, this method sacrifices transparency and traceability, but is suitable when itemized correction is not feasible.

CSV Examples:

- Original Dataset Artifact
- Replacement Dataset Artifact
- Delta Dataset Artifact
- Ledger Dataset Artifact

Note the following details in the example datasets:

- The original dataset was complete in terms of usage, but a minor cost discrepancy was identified due to accumulated rounding drift across multiple records spanning two SkuPriceId values.
- The correction may be modeled using either Overwrite or Append mechanisms, as the billing period is still open.
- All three correction styles (Replacement, Delta, and Ledger) introduce a single increment record representing the bulk cost-only adjustment to reconcile the total drift.
- The correction record does not specify a SkuPriceId, as it spans multiple SKU Price IDs.
- The correction record has ChargeClass set to null, indicating that it pertains to an open billing period and is not a retroactive correction to a previously closed billing period.
- The correction record has ChargeCategory set to "Adjustment", which is the only valid value when both PricingQuantity and ChargeClass are null, due to the normative requirement that PricingQuantity must not be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
- The correction record is assigned to the current billing period (July 2025).

### 8.6.1.2 Previous Open-Period Correction Scenarios

These scenarios address discrepancies related to charges from the June 2025 billing period. The discrepancies were identified on July 5th, 2025, while the June 2025 billing period was still open.

#### 8.6.1.2.1 Billing Period Alignment

Although applied after the period had ended, these corrections do not introduce retroactive semantics, as the billing period was still open and invoices had not yet been issued when the corrections were applied. The ChargeClass is set to null, and the BillingPeriodStart/End reflect the billing period in which the cost or usage was originally incurred (June).

#### 8.6.1.2.2 Correction Style

CrestNode (acting as both the data generator and *invoice issuer*) delivers corrections using Replacement, Delta, and Ledger correction styles, offering varying levels of traceability and auditability.

#### 8.6.1.2.3 Scenario 1: Previous Open-Period Correction - Partial Reallocation to Correct Resource

This scenario is nearly identical to *Scenario 1: Current Open-Period Correction - Partial Reallocation to Correct Resource*. The only difference is that the original misattributed charge occurred in the previous billing period (June 2025), which has ended but has not yet been closed. The correction is applied before invoice issuance, using the same correction styles: Replacement, Delta, and Ledger.

CSV Examples:

- Original Dataset Artifact
- Replacement Dataset Artifact
- Delta Dataset Artifact
- Ledger Dataset Artifact

#### 8.6.1.2.4 Scenario 2: Previous Open-Period Correction - Late-Arriving Usage

This scenario is nearly identical to *Scenario 2: Current Open-Period Correction - Late-Arriving Usage*. The only difference is that the late-arriving usage pertains to the previous billing period (June 2025), which has ended but has not yet been closed. The correction is applied before invoice issuance, using the same correction styles: Replacement, Delta, and Ledger.

CSV Examples:

#### 8.6.1.2.5 Scenario 3: Previous Open-Period Correction - Itemized Cost-Only Corrections

This scenario is nearly identical to *Scenario 3: Current Open-Period Correction - Itemized Cost-Only Corrections*. The only difference is that the original cost discrepancy occurred in the previous billing period (June 2025), which has ended but has not yet been closed. The correction is applied before invoice issuance, using the same correction styles: Replacement, Delta, and Ledger.

CSV Examples:

- Original Dataset Artifact
- Replacement Dataset Artifact
- Delta Dataset Artifact
- Ledger Dataset Artifact

#### 8.6.1.2.6 Scenario 4: Previous Open-Period Correction - Bulk Cost-Only Corrections

This scenario is nearly identical to *Scenario 4: Current Open-Period Correction - Bulk Cost-Only Corrections*. The only difference is that the original cost discrepancy occurred in the previous billing period (June 2025), which has ended but has not yet been closed. The correction is applied before invoice issuance, using the same correction styles: Replacement, Delta, and Ledger.

CSV Examples:

- Original Dataset Artifact
- Replacement Dataset Artifact
- Delta Dataset Artifact
- Ledger Dataset Artifact

## 8.6.2 Corrections to Closed Billing Period

The following examples illustrate how corrections to previously closed billing periods may be represented in FOCUS Cost and Usage dataset artifacts, using delivery mechanisms and correction styles that preserve invoice integrity and auditability.

### 8.6.2.1 Closed-Period Correction Scenarios

These scenarios address discrepancies related to charges from the May 2025 billing period after it was closed and invoiced by the issuer CrestNode on June 8th, 2025. The discrepancies were identified on July 5th, 2025. At that time, the June 2025 billing period was still open.

#### 8.6.2.1.1 Billing Period Alignment

Corrections are applied to the open billing period rather than modifying the closed one. The ChargeClass is set to "Correction", and the BillingPeriodStart/End reflect the current open period (June). However, the ChargePeriodStart/End remain mapped to the original timeframe (May) to preserve the historical accuracy of when the cost was incurred.

#### 8.6.2.1.2 Correction Style

While the Overwrite mechanism is permissible when it doesn't impact issued invoices, CrestNode defaults to the Append mechanism (Delta and Ledger styles) for all closed period corrections. This preference prioritizes auditability and traceability, ensuring that downstream consumers - particularly those managing chargeback - receive a clear, additive history of changes.

#### 8.6.2.1.3 Scenario 1: Closed-Period Correction - Partial Reallocation to Correct Resource

On July 5th, 2025, CrestNode identified that a charge record previously invoiced for May 2025 was incorrectly attributed entirely to ResourceId `R-111`. In reality, only part of the cost and usage belonged to that resource, while the remainder pertained to ResourceId `R-222`.

To correct this misattribution, CrestNode provisioned a reallocation correction using Append mechanisms. The correction was realized either through a Delta style correction, which redistributed the cost between resources using increment and decrement records, or through a Ledger style correction, which negated the original charge and introduced corrected records for each resource.

**Note:***Replacement (i.e., Overwrite delivery mechanism) could have been applied in this scenario because the reallocation would not affect invoice reconciliation and would not require additional invoices. However, CrestNode chose Append to preserve traceability and auditability while ensuring that downstream processes, in particular chargeback, receive timely and accurate cost attribution.*

CSV Examples:

Note the following details in the example datasets:

- The original dataset was delivered before the billing period was closed and includes a charge record that was part of the finalized invoice for May 2025.
- Correction records have ChargeClass set to "Correction", indicating they reallocate cost from a previously closed billing period.
- Original Dataset includes:
  - A charge record attributed entirely to ResourceId `R-111`.
- Delta style correction includes:
  - A decrement record for `R-111`, reducing the cost previously misattributed to that resource.
  - An increment record for `R-222`, assigning the corresponding portion of the cost to the correct resource.
- Ledger style correction includes:
  - A reversal record for the original charge.
  - A corrected record for `R-111`.
  - A corrected record for `R-222`.

#### 8.6.2.1.4 Scenario 2: Closed-Period Correction - Late-Arriving Usage

On July 5th, 2025, CrestNode identified a cost that was incurred during May 2025 (ChargePeriodStart: `2025-05-01`) but was not included in the finalized invoice issued on June 8th, 2025. Since the May billing period was closed, the correction was delivered in the next open billing period (e.g., June or July).

To account for the previously omitted usage, CrestNode provisioned a correction using Append mechanisms. The correction was realized by introducing a single increment record in both Delta style correction and Ledger style correction formats, representing the late-arriving cost and usage.

CSV Examples:

Note the following details in the example datasets:

- The original dataset was delivered before the billing period was closed.
- The late-arriving cost was incurred during May 2025 but was not captured in the original dataset and was therefore not reflected in the invoice for May 2025, issued on June 8th, 2025.
- The correction introduces a new charge record to account for this previously omitted cost.
- The correction record is assigned to the next open billing period (e.g., June 2025).
- The correction record has ChargeClass set to "Correction", indicating it accounts for usage from a previously closed billing period.
- Both Delta style and Ledger style corrections use a single increment record to represent the late-arriving usage and associated cost.

#### 8.6.2.1.5 Scenario 3: Closed-Period Correction - Itemized Cost-Only Corrections

On July 5th, 2025, CrestNode detected a minor cost discrepancy caused by accumulated rounding differences across multiple previously invoiced records spanning several different SkuPriceId values. While each individual record was correctly rounded, the aggregated cost differed slightly from the precise total, resulting in a small drift.

To reconcile this discrepancy, CrestNode provisioned a cost-only correction using Append mechanism. In both Delta style correction and Ledger style correction formats, the correction was realized by introducing two itemized increment records, each representing a cost-only adjustment for one of the affected SkuPriceId values. Unlike bulk corrections, which consolidate adjustments into a single record without specifying a SkuPriceId, this approach explicitly itemizes the correction per SkuPriceId. Because the original records were individually correct and no single record requires reversal, the Ledger style correction does not include explicit reversals. In this case, the Ledger and Delta corrections are identical, as only additive records are needed to reconcile the accumulated drift.

Compared to the bulk correction approach, this method ensures transparency and traceability and is preferred when itemized correction is feasible.

CSV Examples:

Note the following details in the example datasets:

- The original dataset was delivered before the billing period was closed.
- The original records were correctly rounded individually, but a minor discrepancy was later identified due to accumulated rounding drift across multiple records spanning two SkuPriceId values.
- The discrepancies were not captured in the original dataset and therefore were not reflected in the invoice for May 2025, issued on June 8th, 2025.
- Both Delta style and Ledger style corrections introduce two itemized increment records representing cost-only adjustments.
- Each correction record is assigned to the next open billing period (e.g., June 2025).
- Each correction record has ChargeClass set to "Correction", indicating it reconciles cost discrepancies from a previously closed billing period.
- Each correction record is itemized and explicitly references the relevant SkuPriceId.
- Each correction record has ChargeCategory set to "Adjustment". While in this case "Usage" might be more precise and is permitted (since ChargeClass is "Correction"), "Adjustment" was selected to denote a cost-only correction due to a rounding error.

#### 8.6.2.1.6 Scenario 4: Closed-Period Correction - Bulk Cost-Only Corrections

On July 5th, 2025, CrestNode detected a minor cost discrepancy caused by accumulated rounding differences across multiple previously invoiced records spanning several different SkuPriceId values. While each individual record was correctly rounded, the aggregated cost differed slightly from the precise total, resulting in a small drift.

To reconcile this discrepancy, CrestNode provisioned a bulk cost-only correction using Append mechanism. The correction was realized by introducing a single increment record in both Delta style correction and Ledger style correction formats, representing the bulk cost-only adjustment. Unlike itemized corrections, this bulk record did not specify a SkuPriceId, as the discrepancy spanned multiple SKU Price IDs. Because the original records were individually correct and no single record requires reversal, the Ledger style correction does not include explicit reversals. In this case, the Ledger and Delta corrections are identical, as only additive records are needed to reconcile the accumulated drift.

CSV Examples:

Note the following details in the example datasets:

- The original dataset was delivered before the billing period was closed.
- The original records were correctly rounded individually, but a minor discrepancy was later identified due to accumulated rounding drift across multiple records spanning two SkuPriceId values.
- The discrepancies were not captured in the original dataset and therefore were not reflected in the invoice for May 2025, issued on June 8th, 2025.
- Both Delta style and Ledger style corrections introduce a bulk cost-only record to reconcile the total drift and ensure invoice accuracy.
- The correction record is assigned to the next open billing period (e.g., June 2025).
- The correction record has ChargeClass set to "Correction", indicating it reconciles cost discrepancies from a previously closed billing period.
- The correction record does not specify a SkuPriceId, as it spans multiple SKU Price IDs.
- The correction record has ChargeCategory set to "Adjustment". While in this case "Usage" might be more precise and is permitted (since ChargeClass is "Correction"), "Adjustment" was selected to denote a cost-only correction due to a rounding error.