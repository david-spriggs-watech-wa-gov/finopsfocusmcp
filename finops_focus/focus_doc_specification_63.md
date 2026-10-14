---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/appendix/discount-handling/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: bfdf037f679b9803
---
# 8.1 Discount Handling

While *service providers* may use different terms and mechanisms to describe and represent discounts in their native datasets, FOCUS represents discounts as reduced pricing reflected directly in the *charges* they pertain to, rather than as separate offsetting *charges*. Unlike discounts, *credits* are financial incentives or allowances represented as separate *charges* unrelated to other *charges*.

In Cost and Usage, cost and unit price columns reflect the effect of discounts. Discounts associated with *contract commitments* are further identified and attributed using the Contract Applied column (also serves as an association to the Contract Commitment dataset), as well as *commitment discount*-specific columns. *Custom columns* may be used when needed to further identify or describe discounts.

For additional context and related normative requirements associated with discount handling, refer to the following specification sections:

| Concept | Description | Entity | Specification Location | 
|---|---|---|---|
| **General dataset rules** | Handling unused portions, splitting discounted charges, and avoiding negating rows | Dataset | CostAndUsage | 
| **Effect of discounts** | Reflecting reduced pricing from discounts | Column | CostAndUsage.BilledCost CostAndUsage.EffectiveCost CostAndUsage.ContractedCost CostAndUsage.ListCost CostAndUsage.ContractedUnitPrice CostAndUsage.ListUnitPrice | 
| **Commitment Discount specifics** | Identification and utilization of *commitment discounts* | Column | CostAndUsage.CommitmentDiscountId CostAndUsage.CommitmentDiscountStatus | 
| **Resource tracking** | Identifying the exact resource that received the commitment discount | Column | CostAndUsage.ResourceId | 
| **Contract allocations** | Associating a charge with specific contract commitments | Column | CostAndUsage.ContractApplied |