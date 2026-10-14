---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/appendix/json-object-examples/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "3c4b307904839aa0"
---
# 8.8 Examples: JSON Object

This section provides examples for the columns in the specification in the JSON Object Format.

## 8.8.1 Examples: Allocated Method Details

The JSON samples in the scenarios below each represent a single allocated record out of the multiple records derived from an origin record for that scenario. The sum AllocatedRatio will add up to 1 (100%) across all allocated records for an origin record, with the AllocatedRatio (or sum of AllocatedRatio) representing the allocated record's portion of the overall origin record.

### 8.8.1.1 Scenario 1: Single UsageUnit Value Used for Allocation

When only a single "UsageUnit" is used to calculate the allocation.

```
{
  "Elements" : [ {
    "AllocatedRatio" : 0.1,
    "UsageUnit" : "Hours",
    "UsageQuantity" : 300
    }
  ]
}
```
### 8.8.1.2 Scenario 2: Multiple UsageUnit Values Used for Allocation

When multiple "UsageUnit" values are used to calculate the allocation, another object is added to the "Elements" collection.

```
{
  "Elements": [
    {
      "AllocatedRatio": 0.05,
      "UsageUnit": "CPU",
      "UsageQuantity": 0.5
    },
    {
      "AllocatedRatio": 0.1,
      "UsageUnit": "Memory",
      "UsageQuantity": 4
    }
  ]
}
```
### 8.8.1.3 Scenario 3: Data Generator Omits Keys That are Not Required

This data generator does not wish to supply the "UsageUnit" or "UsageQuantity" keys but still provides cost allocation with some additional allocation method details. In this case, "UsageUnit" and "UsageQuantity" are omitted, and only the "AllocatedRatio" is supplied.

```
{
  "Elements" : [ {
    "AllocatedRatio" : 0.45
    }
  ]
}
```
### 8.8.1.4 Scenario 4: Additional Non-FOCUS Specified Properties

A data generator can add additional properties if they feel more context is helpful or necessary to the practitioner. In this scenario, the data generator is supplying additional context that shows only 0.5 of a unit was used. However, since 1 unit was requested by the service this allocation represents, the allocation is being charged at 1 regardless.

```
{
  "Elements": [
    {
      "AllocatedRatio": 0.6,
      "UsageUnit": "vCPU",
      "UsageQuantity": 1,
      "x_ReservedVCPU": 1,
      "x_UsedVCPU": 0.5,
      "x_AllocatedVCPU": 1
    }
  ]
}
```
## 8.8.2 Examples: Commitment Program Eligibility Details

The examples below are not exhaustive and may change over time. Service providers are the authoritative source for their *commitment programs*.

### 8.8.2.1 Aura Web (Partially Covered Compute Usage)

Scenario: A compute usage row that is partially covered by a Flexible Spend Plan. The eligibility column still reflects all programs this usage qualifies for, regardless of current coverage.

| ServiceProviderName | ServiceName | CommitmentProgramEligibilityDetails | 
|---|---|---|
| Aura Web | Compute | {"CommitmentPrograms": \[{"ProgramType": "Flexible Spend Plan"}, {"ProgramType": "Resource Reservation"}\]} | 

### 8.8.2.2 StackLens (Observability with Interval Spend Commitment)

Scenario: An observability platform usage row eligible for Monthly and Annual interval spend commitment pricing, offering lower effective rates than standard usage.

| ServiceProviderName | ServiceName | CommitmentProgramEligibilityDetails | 
|---|---|---|
| StackLens | Observability | {"CommitmentPrograms": \[{"ProgramType": "Monthly Interval Spend Commitment"}, {"ProgramType": "Annual Interval Spend Commitment"}\]} | 

### 8.8.2.3 LatticeScale (Ineligible Object Storage Usage)

Scenario: Standard object storage usage or a support fee, which is not eligible for any commitment program.

| ServiceProviderName | ServiceName | CommitmentProgramEligibilityDetails | 
|---|---|---|
| LatticeScale | ObjectStorage | null | 

### 8.8.2.4 Aura Web (Advance Resource Commitment-Eligible Compute Usage)

Scenario: A compute instance type and tenancy that are eligible for both discount-bearing programs and advance resource commitments. The eligibility column reflects all commitment constructs the usage qualifies for.

| ServiceProviderName | ServiceName | CommitmentProgramEligibilityDetails | 
|---|---|---|
| Aura Web | Compute | {"CommitmentPrograms": \[{"ProgramType": "Flexible Spend Plan"}, {"ProgramType": "Resource Reservation"}, {"ProgramType": "Advance Resource Commitment"}, {"ProgramType": "Zonal Resource Commitment"}\]} | 

### 8.8.2.5 Coverage Rate with Eligibility-Adjusted Denominator

This example demonstrates how to calculate an accurate *commitment* coverage rate using CommitmentProgramEligibilityDetails alongside CommitmentDiscountId.

Acme Corp runs compute workloads on Aura Web. Some usage is covered by a Resource Reservation, some is eligible but uncovered, and a support fee is ineligible for any *commitment program*.

Three usage rows for a single charge period (2025-04-01):

1. **Uncovered compute** (Row 1): Eligible for Flexible Spend Plan and Resource Reservation, not currently covered. BilledCost and EffectiveCost are both $200.00.
2. **Covered compute** (Row 2): Covered by a Resource Reservation. CommitmentProgramEligibilityDetails is populated. BilledCost is $0.00; EffectiveCost is $150.00.
3. **Support fee** (Row 3): Not eligible for any *commitment program*. Both CommitmentProgramEligibilityDetails and CommitmentDiscountId are null. BilledCost and EffectiveCost are both $50.00.

By filtering the denominator to rows where `CommitmentProgramEligibilityDetails IS NOT NULL`, the $50.00 support fee is correctly excluded from the eligible population:

| Metric | Value | 
|---|---|
| Eligible denominator | Row 1 ($200.00) + Row 2 ($150.00) = $350.00 | 
| Covered numerator | Row 2 ($150.00) | 
| Coverage rate | `150 / 350` = **42.9%** | 

Row 3 (support fee) is correctly excluded because CommitmentProgramEligibilityDetails is null for ineligible charges.

### 8.8.2.6 Uncovered Eligible Spend by Program Type

This example demonstrates how to use CommitmentProgramEligibilityDetails to identify uncovered savings opportunities across *commitment program* types and providers.

Acme Corp runs compute workloads on Aura Web and uses StackLens for observability monitoring. Some Aura Web compute usage is covered by a Resource Reservation. StackLens usage is uncovered but eligible for Interval Spend Commitments at monthly or annual terms. A practitioner wants to answer: "Which *commitment program* and provider should I target for my next purchase?"

Six usage rows for a single charge period (2025-04-01):

1. **Uncovered compute** (Rows 1-2): Two Aura Web Compute rows eligible for both Flexible Spend Plan and Resource Reservation. BilledCost totals $500.00 across both rows.
2. **Covered compute** (Row 3): Aura Web Compute covered by an existing Resource Reservation. Filtered out by the query because CommitmentDiscountId is populated.
3. **Ineligible support** (Row 4): Aura Web Support with no CommitmentProgramEligibilityDetails. Filtered out because the column is null.
4. **Uncovered observability** (Rows 5-6): Two StackLens Observability rows eligible for Monthly Interval Spend Commitment and Annual Interval Spend Commitment. BilledCost totals $200.00.

To evaluate these purchasing options, the `CommitmentPrograms` JSON array must be flattened so each eligible program can be analyzed independently. By expanding the array (e.g., via `CROSS JOIN UNNEST`) and grouping the uncovered costs by `ServiceProviderName`, `ServiceName`, and `EligibleProgramType`, the practitioner gets the summary presented in the table below. A reference implementation is available in the eligible uncovered spend query supported feature.

| ServiceProviderName | ServiceName | EligibleProgramType | EligibleUncoveredCost | 
|---|---|---|---|
| Aura Web | Compute | Flexible Spend Plan | $500.00 | 
| Aura Web | Compute | Resource Reservation | $500.00 | 
| StackLens | Observability | Monthly Interval Spend Commitment | $200.00 | 
| StackLens | Observability | Annual Interval Spend Commitment | $200.00 | 

Aura Web Compute appears as $500.00 under both Flexible Spend Plan and Resource Reservation. This does not mean $1,000.00 is uncovered. The $500.00 is the same spend, and each program type represents an independent purchasing opportunity. Purchasing a Flexible Spend Plan would cover some or all of that $500.00, as would a Resource Reservation. The practitioner must choose between them (or split across both) based on flexibility requirements and discount depth.

The same logic applies to StackLens: $200.00 of observability spend could be covered by either a monthly or annual Interval Spend Commitment. The annual option typically offers a deeper discount in exchange for a longer commitment term.

The query uses BilledCost rather than EffectiveCost because all rows are uncovered (CommitmentDiscountId IS NULL). For uncovered usage, BilledCost equals EffectiveCost and reflects the actual amount paid.

## 8.8.3 Examples: Contract Applied

### 8.8.3.1 Scenario 1: Initial Contract Commitment

A single Cost and Usage charge represents the values stated on a contract and its three contract commitments agreed between a service provider and a customer:

1. 12345: Spend $500k overall. (This is the value of the contract, and thus ContractId = ContractCommitmentId.)
2. 23456: Spend $25k on a particular service.
3. 34567: Consume 100k compute hours on a particular resource type.

The Charge Category is denoted as Purchase, and the Contract ID, Resource ID, and Contract Commitment ID are all denoted as 12345.

```
{
  "ResourceId": "12345",
  "ChargeCategory": "Purchase",
  "BilledCost": 500000.00,
  "EffectiveCost": 0.00,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractId": "12345",
        "ContractCommitmentId": "12345",
        "ContractCommitmentAppliedCost": 500000.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "23456",
        "ContractCommitmentAppliedCost": 25000.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "34567",
        "ContractCommitmentAppliedQuantity": 100000.00,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
}
```
### 8.8.3.2 Scenario 2: Contract Commitment Usage with No Custom Columns

Assume the contract commitment as described in Scenario 1. Assume that only 50% of cost and usage gets applied to the contract commitments, per the contract terms.

A single Cost and Usage charge for `myResource1` carries Effective Cost of 30 (denominated in USD) and Consumed Quantity of 1 (denominated in compute hours). The Charge Category is denoted as Usage.

This applies to the contract commitments in the following manner:

```
{
  "ResourceId": "myResource1",
  "ChargeCategory": "Usage",
  "BilledCost": 0.00,
  "EffectiveCost": 30.00,
  "ConsumedQuantity": 1,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractId": "12345",
        "ContractCommitmentId": "12345",
        "ContractCommitmentAppliedCost": 15.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "23456",
        "ContractCommitmentAppliedCost": 15.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "34567",
        "ContractCommitmentAppliedQuantity": 0.50,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
}
```
### 8.8.3.3 Scenario 3: Contract Commitment Usage with Custom Columns

The same as Scenario 2, except a custom key-value pair `x_ContractCommitmentCostBalance` is provided by the data generator. This datapoint represents the value remaining on a given contract commitment.

```
{
  "ResourceId": "myResource1",
  "ChargeCategory": "Usage",
  "BilledCost": 0.00,
  "EffectiveCost": 30.00,
  "ConsumedQuantity": 1,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractId": "12345",
        "ContractCommitmentId": "12345",
        "ContractCommitmentAppliedCost": 15.00,
        "x_ContractCommitmentCostBalance": 499985.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "23456",
        "ContractCommitmentAppliedCost": 15.00,
        "x_ContractCommitmentCostBalance": 24985.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "34567",
        "ContractCommitmentAppliedQuantity": 0.50,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
}
```
## 8.8.4 Examples: Contract Commitment Applicability

This section describes examples for the Contract Commitment Applicability column in the Contract Commitment dataset.

### 8.8.4.1 Global Scope and Applicability

If the commitment is 100% applicable to all resources, the `Applicability` object can be omitted entirely.

```
{
  "IsGlobalScope": true
}
```
### 8.8.4.2 Global Scope with Specific Exceptions

Organization-wide coverage **except** for Database services running in BillingAccountId 123456789012.

```
{
  "IsGlobalScope": true,
  "ExclusionOperator": "And",
  "Exclusions": [
    {
      "Dimension": "BillingAccountId",
      "Operator": "In",
      "Values": ["123456789012"]
    },
    {
      "Dimension": "ServiceCategory",
      "Operator": "In",
      "Values": ["Database"]
    }
  ]
}
```
### 8.8.4.3 Regional Scope

A commitment purchased for a specific region (e.g., `us-east-1`). Since `IsGlobalScope` and `IsComplexScope` are omitted, they default to `false`, requiring the inclusion block.

```
{
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"]
    }
  ]
}
```
### 8.8.4.4 Custom Scope

A commitment that is only applicable to a specific value (Pay-As-You-Go) for a custom entity (x\_BillingModel) in the `us-east-1` region.

```
{
  "InclusionOperator": "And",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"]
    },
    {
      "Dimension": "x_BillingModel",
      "Operator": "In",
      "Values": ["Pay-As-You-Go"]
    }
  ]
}
```
### 8.8.4.5 Regional Compute Commitment with Exceptions

Applies to Compute services in either `us-east-1` or `us-west-2`, excluding any resources tagged with an `Environment` of `Sandbox`.

```
{
  "InclusionOperator": "And",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1", "us-west-2"]
    },
    {
      "Dimension": "ServiceCategory",
      "Operator": "In",
      "Values": ["Compute"]
    }
  ],
  "ExclusionOperator": "Or",
  "Exclusions": [
    {
      "Dimension": "Tags",
      "Operator": "Contains",
      "Values": ["\"Environment\": \"Sandbox\""]
    }
  ]
}
```
### 8.8.4.6 Regional Applicability

A commitment that applies fully to `us-east-1` but only 50% of cost and usage in `us-west-2` is eligible. Note the differing applicability percentages in the two regions.

```
{
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"]
    },
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-west-2"],
      "Applicability": {
        "Cost": 0.5,
        "Usage": 0.5
      }
    }
  ]
}
```
### 8.8.4.7 Granular Applicability (Partial Object)

A scenario where 100% of Marketplace **Usage** counts toward a volume commitment, but only 50% of the **Cost** is applicable for financial credit. The engine defaults the missing `Usage` key to `1.0`.

```
{
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "InvoiceIssuerName",
      "Operator": "In",
      "Values": ["Cloud Marketplace"],
      "Applicability": {
        "Cost": 0.5
      }
    }
  ]
}
```
### 8.8.4.8 Complex Fallback

A commitment with dynamic or conditional logic that requires calculation against the total aggregate of cost or usage.

```
{
  "IsComplexScope": true
}
```