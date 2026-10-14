---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/datasets/cost-and-usage/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: d3ea046423e3a86d
---
# 3.1 Cost and Usage

The Cost and Usage dataset is the primary dataset for FOCUS cost and usage data.

The specification for the Cost and Usage dataset defines a group of columns that provide qualitative values (such as dates, resource, and service provider information) categorized as "dimensions" and quantitative values (numeric values) categorized as "metrics" that can be used for performing various FinOps capabilities. Metrics are commonly used for aggregations (sum, multiplication, averaging etc.) and statistical operations within the dataset. Dimensions are commonly used to categorize, filter, and reveal details in your data when combined with metrics. The columns are presented in alphabetical order.

## Columns in this Dataset

| Column | Type | Level | Data Type | 
|---|---|---|---|
| Allocated Method ID | Dimension | Conditional | String | 
| Allocated Method Details | Dimension / Metric | Recommended | JSON | 
| Allocated Resource ID | Dimension | Conditional | String | 
| Allocated Resource Name | Dimension | Conditional | String | 
| Allocated Tags | Dimension | Conditional | JSON | 
| Availability Zone | Dimension | Recommended | String | 
| Billed Cost | Metric | Mandatory | Decimal | 
| Billing Account ID | Dimension | Mandatory | String | 
| Billing Account Name | Dimension | Mandatory | String | 
| Billing Account Type | Dimension | Conditional | String | 
| Billing Currency | Dimension | Mandatory | String | 
| Billing Period End | Dimension | Mandatory | Date/Time | 
| Billing Period Start | Dimension | Mandatory | Date/Time | 
| Capacity Reservation ID | Dimension | Conditional | String | 
| Capacity Reservation Status | Dimension | Conditional | String | 
| Charge Category | Dimension | Mandatory | String | 
| Charge Class | Dimension | Mandatory | String | 
| Charge Description | Dimension | Mandatory | String | 
| Charge Frequency | Dimension | Recommended | String | 
| Charge Period End | Dimension | Mandatory | Date/Time | 
| Charge Period Start | Dimension | Mandatory | Date/Time | 
| Commitment Discount Category | Dimension | Conditional | String | 
| Commitment Discount ID | Dimension | Conditional | String | 
| Commitment Discount Name | Dimension | Conditional | String | 
| Commitment Discount Quantity | Metric | Conditional | Decimal | 
| Commitment Discount Status | Dimension | Conditional | String | 
| Commitment Discount Type | Dimension | Conditional | String | 
| Commitment Discount Unit | Dimension | Conditional | String | 
| Commitment Program Eligibility Details | Dimension | Conditional | JSON | 
| Consumed Quantity | Metric | Conditional | Decimal | 
| Consumed Unit | Dimension | Conditional | String | 
| Contract Applied | Dimension / Metric | Conditional | JSON | 
| Contracted Cost | Metric | Mandatory | Decimal | 
| Contracted Unit Price | Metric | Conditional | Decimal | 
| Effective Cost | Metric | Mandatory | Decimal | 
| Host Provider Name | Dimension | Mandatory | String | 
| Invoice Detail ID | Dimension | Conditional | String | 
| Invoice ID | Dimension | Conditional | String | 
| Invoice Issuer Name | Dimension | Mandatory | String | 
| List Cost | Metric | Mandatory | Decimal | 
| List Unit Price | Metric | Conditional | Decimal | 
| Pricing Category | Dimension | Conditional | String | 
| Pricing Currency | Dimension | Conditional | String | 
| Pricing Currency Contracted Unit Price | Metric | Conditional | Decimal | 
| Pricing Currency Effective Cost | Metric | Conditional | Decimal | 
| Pricing Currency List Unit Price | Metric | Conditional | Decimal | 
| Pricing Quantity | Metric | Mandatory | Decimal | 
| Pricing Unit | Dimension | Mandatory | String | 
| Region ID | Dimension | Conditional | String | 
| Region Name | Dimension | Conditional | String | 
| Resource ID | Dimension | Conditional | String | 
| Resource Name | Dimension | Conditional | String | 
| Resource Type | Dimension | Conditional | String | 
| Service Provider Name | Dimension | Mandatory | String | 
| Service Category | Dimension | Mandatory | String | 
| Service Name | Dimension | Mandatory | String | 
| Service Subcategory | Dimension | Recommended | String | 
| SKU ID | Dimension | Conditional | String | 
| SKU Meter | Dimension | Conditional | String | 
| SKU Price Details | Dimension | Conditional | JSON | 
| SKU Price ID | Dimension | Conditional | String | 
| Sub Account ID | Dimension | Conditional | String | 
| Sub Account Name | Dimension | Conditional | String | 
| Sub Account Type | Dimension | Conditional | String | 
| Tags | Dimension | Conditional | JSON | 

## Relationships

The Cost and Usage dataset can be joined to the Contract Commitment dataset through the use of the Contract Commitment ID.

- In the Cost and Usage dataset, Contract Commitment ID is a property within a JSON object array provided in Contract Applied column.
- In the Contract Commitment dataset, Contract Commitment ID is a column.

| Dataset A | Dataset A Column | Dataset B | Dataset B Column | 
|---|---|---|---|
| Cost and Usage | Contract Applied | Contract Commitment | Contract Commitment ID | 

## Requirements

CostAndUsage MUST adhere to the following requirements:

- CostAndUsage MUST be present.
- CostAndUsage column presence MUST adhere to the following requirements:
  - CostAndUsage SHOULD include AllocatedMethodDetails when the data generator supports data generator-calculated split cost allocation.
  - CostAndUsage MUST include AllocatedMethodId when the data generator supports data generator-calculated split cost allocation.
  - CostAndUsage MUST include AllocatedResourceId when the data generator supports data generator-calculated split cost allocation.
  - CostAndUsage MUST include AllocatedResourceName when the data generator supports data generator-calculated split cost allocation.
  - CostAndUsage MUST include AllocatedTags when the data generator supports data generator-calculated split cost allocation.
  - CostAndUsage SHOULD include AvailabilityZone when the host provider supports deploying resources or services within an *availability zone*.
  - CostAndUsage MUST include BilledCost.
  - CostAndUsage MUST include BillingAccountId.
  - CostAndUsage MUST include BillingAccountName.
  - CostAndUsage MUST include BillingAccountType when the *invoice issuer* supports more than one possible BillingAccountType value.
  - CostAndUsage MUST include BillingCurrency.
  - CostAndUsage MUST include BillingPeriodEnd.
  - CostAndUsage MUST include BillingPeriodStart.
  - CostAndUsage MUST include CapacityReservationId when the service provider supports *capacity reservations*.
  - CostAndUsage MUST include CapacityReservationStatus when the service provider supports *capacity reservations*.
  - CostAndUsage MUST include ChargeCategory.
  - CostAndUsage MUST include ChargeClass.
  - CostAndUsage MUST include ChargeDescription.
  - CostAndUsage SHOULD include ChargeFrequency.
  - CostAndUsage MUST include ChargePeriodEnd.
  - CostAndUsage MUST include ChargePeriodStart.
  - CostAndUsage MUST include CommitmentDiscountCategory when the service provider supports *commitment discounts*.
  - CostAndUsage MUST include CommitmentDiscountId when the service provider supports *commitment discounts*.
  - CostAndUsage MUST include CommitmentDiscountName when the service provider supports *commitment discounts*.
  - CostAndUsage MUST include CommitmentDiscountQuantity when the service provider supports *commitment discounts*.
  - CostAndUsage MUST include CommitmentDiscountStatus when the service provider supports *commitment discounts*.
  - CostAndUsage MUST include CommitmentDiscountType when the service provider supports *commitment discounts*.
  - CostAndUsage MUST include CommitmentDiscountUnit when the service provider supports *commitment discounts*.
  - CostAndUsage MUST include CommitmentProgramEligibilityDetails when the service provider supports at least one *commitment program*.
  - CostAndUsage MUST include ConsumedQuantity when the service provider supports the measurement of usage.
  - CostAndUsage MUST include ConsumedUnit when the service provider supports the measurement of usage.
  - CostAndUsage MUST include ContractApplied when the service provider supports *contract commitments*.
  - CostAndUsage MUST include ContractedCost.
  - CostAndUsage MUST include ContractedUnitPrice when the service provider supports negotiated pricing concepts.
  - CostAndUsage MUST include EffectiveCost.
  - CostAndUsage MUST include HostProviderName.
  - CostAndUsage MUST include InvoiceDetailId when the invoice issuer supports payable invoices.
  - CostAndUsage MUST include InvoiceId when the invoice issuer supports payable invoices.
  - CostAndUsage MUST include InvoiceIssuerName.
  - CostAndUsage MUST include ListCost.
  - CostAndUsage MUST include ListUnitPrice when the service provider publishes unit prices exclusive of discounts.
  - CostAndUsage MUST include PricingCategory when the service provider supports more than one pricing category across all *SKUs*.
  - CostAndUsage MUST include PricingCurrency when the service provider supports pricing and billing in different currencies.
  - CostAndUsage MUST adhere to the following PricingCurrencyContractedUnitPrice presence requirements:
    - CostAndUsage MUST include PricingCurrencyContractedUnitPrice when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
    - CostAndUsage SHOULD include PricingCurrencyContractedUnitPrice when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
    - CostAndUsage MAY include PricingCurrencyContractedUnitPrice in all other cases.
  - CostAndUsage MUST adhere to the following PricingCurrencyEffectiveCost presence requirements:
    - CostAndUsage MUST include PricingCurrencyEffectiveCost when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
    - CostAndUsage SHOULD include PricingCurrencyEffectiveCost when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
    - CostAndUsage MAY include PricingCurrencyEffectiveCost in all other cases.
  - CostAndUsage MUST adhere to the following PricingCurrencyListUnitPrice presence requirements:
    - CostAndUsage MUST include PricingCurrencyListUnitPrice when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
    - CostAndUsage SHOULD include PricingCurrencyListUnitPrice when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
    - CostAndUsage MAY include PricingCurrencyListUnitPrice in all other cases.
  - CostAndUsage MUST include PricingQuantity.
  - CostAndUsage MUST include PricingUnit.
  - CostAndUsage MUST include RegionId when the host provider supports deploying resources or services within a region.
  - CostAndUsage MUST include RegionName when the host provider supports deploying resources or services within a region.
  - CostAndUsage MUST include ResourceId when the service provider supports billing based on provisioned *resources*.
  - CostAndUsage MUST include ResourceName when the service provider supports billing based on provisioned resources.
  - CostAndUsage MUST include ResourceType when the service provider supports billing based on provisioned *resources* and supports assigning types to *resources*.
  - CostAndUsage MUST include ServiceCategory.
  - CostAndUsage MUST include ServiceName.
  - CostAndUsage MUST include ServiceProviderName.
  - CostAndUsage SHOULD include ServiceSubcategory.
  - CostAndUsage MUST include SkuId when the service provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.
  - CostAndUsage MUST include SkuMeter when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.
  - CostAndUsage MUST include SkuPriceDetails when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.
  - CostAndUsage MUST include SkuPriceId when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.
  - CostAndUsage MUST include SubAccountId when the service provider supports a *sub account* construct.
  - CostAndUsage MUST include SubAccountName when the service provider supports a *sub account* construct.
  - CostAndUsage MUST include SubAccountType when the service provider supports more than one possible SubAccountType value.
  - CostAndUsage MUST include Tags when the data generator supports setting user or provider-defined tags.
  - CostAndUsage SHOULD include *custom columns* needed to identify all applied discounts when *FOCUS columns* are not sufficient.
- CostAndUsage MUST conform to CorrectionHandling requirements.
- CostAndUsage MUST conform to DatasetCompleteness requirements.
- CostAndUsage MUST conform to DatasetConfiguration requirements.
- CostAndUsage MUST conform to DeliveryHandling requirements.
- CostAndUsage MUST include *charges* representing unused portions of a *commitment* when the *commitment* is not fully utilized.
- CostAndUsage MUST include separate *charges* representing discounted and non-discounted portions when a discount applies to only a portion of the originally incurred *charge*.
- When the data generator supports data generator-calculated split cost allocation, CostAndUsage MUST adhere to the following requirements:
  - CostAndUsage MUST have its data generator-calculated split cost allocation method documented and accessible to practitioners.
  - CostAndUsage SHOULD offer data generator-calculated split cost allocation on an opt-in basis.
  - CostAndUsage MAY contain records for concepts not related to resource usage, when it aligns with the documented data generator-calculated split cost allocation method.
  - CostAndUsage MAY contain records for unused or unallocated usage from the *origin charge* as separate *allocated charges*, when it aligns with the documented data generator-calculated split cost allocation method.
  - CostAndUsage MAY contain *allocated charges* with apportioned costs for unused or unallocated usage, when it aligns with the documented data generator-calculated split cost allocation method.
- CostAndUsage SHOULD reflect all applied discounts in *charges* they pertain to.
- CostAndUsage SHOULD NOT represent applied discounts as separate negating or offsetting *charges*.
- CostAndUsage *FOCUS columns* MUST conform to DataGeneratorCalculatedSplitCostAllocationHandling requirements when the data generator supports data generator-calculated split cost allocation.
- CostAndUsage *FOCUS columns* MUST conform to FocusColumnHandling requirements.
- CostAndUsage *FOCUS columns* MUST conform to NullHandling requirements.
- CostAndUsage *custom columns* MUST conform to CustomColumnHandling requirements.