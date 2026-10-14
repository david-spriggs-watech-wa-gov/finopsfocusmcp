---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/datasets/contract-commitment/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "92fa002f75ebcc6c"
---
# 3.3 Contract Commitment

Columns:
                    30

Since:
                    1.3

The Contract Commitment dataset is a supporting dataset that describes the terms of contracts agreed between a service provider and a customer.

## Columns in this Dataset

| Column | Type | Level | Data Type | 
|---|---|---|---|
| Billing Currency | Dimension | Mandatory | String | 
| Contract Commitment Applicability | Dimension / Metric | Mandatory | JSON | 
| Contract Commitment Benefit Category | Dimension | Mandatory | String | 
| Contract Commitment Category | Dimension | Mandatory | String | 
| Contract Commitment Cost | Metric | Mandatory | Decimal | 
| Contract Commitment Created | Dimension | Mandatory | Date/Time | 
| Contract Commitment Description | Dimension | Mandatory | String | 
| Contract Commitment Discount Percentage | Metric | Mandatory | Decimal | 
| Contract Commitment Duration Type | Dimension | Mandatory | String | 
| Contract Commitment Fulfillment Interval | Dimension | Mandatory | String | 
| Contract Commitment ID | Dimension | Mandatory | String | 
| Contract Commitment Last Updated | Dimension | Mandatory | Date/Time | 
| Contract Commitment Lifecycle Status | Dimension | Mandatory | String | 
| Contract Commitment Model | Dimension | Mandatory | String | 
| Contract Commitment Offer Category | Dimension | Mandatory | String | 
| Contract Commitment Payment Interval | Dimension | Mandatory | String | 
| Contract Commitment Payment Model | Dimension | Mandatory | String | 
| Contract Commitment Payment Upfront Percentage | Metric | Conditional | Decimal | 
| Contract Commitment Period End | Dimension | Mandatory | Date/Time | 
| Contract Commitment Period Start | Dimension | Mandatory | Date/Time | 
| Contract Commitment Quantity | Metric | Mandatory | Decimal | 
| Contract Commitment Type | Dimension | Mandatory | String | 
| Contract Commitment Unit | Dimension | Mandatory | String | 
| Contract ID | Dimension | Mandatory | String | 
| Contract Period End | Dimension | Mandatory | Date/Time | 
| Contract Period Start | Dimension | Mandatory | Date/Time | 
| Invoice Issuer Name | Dimension | Mandatory | String | 
| Pricing Currency | Dimension | Conditional | String | 
| Pricing Currency Contract Commitment Cost | Metric | Conditional | Decimal | 
| Service Provider Name | Dimension | Mandatory | String | 

## Relationships

The Contract Commitment dataset can be joined to the Cost and Usage dataset through the use of Contract Commitment ID.

- In the Contract Commitment dataset, Contract Commitment ID is a column.
- In the Cost and Usage dataset, Contract Commitment ID is a property within a JSON object array provided in Contract Applied column.

| Dataset A | Dataset A Column | Dataset B | Dataset B Column | 
|---|---|---|---|
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Applied | 

## Requirements

ContractCommitment MUST adhere to the following requirements:

- ContractCommitment MUST be present when the service provider supports *contract commitments*.
- ContractCommitment column presence MUST adhere to the following requirements:
  - ContractCommitment MUST include BillingCurrency.
  - ContractCommitment MUST include ContractCommitmentApplicability.
  - ContractCommitment MUST include ContractCommitmentBenefitCategory.
  - ContractCommitment MUST include ContractCommitmentCategory.
  - ContractCommitment MUST include ContractCommitmentCost.
  - ContractCommitment MUST include ContractCommitmentCreated.
  - ContractCommitment MUST include ContractCommitmentDescription.
  - ContractCommitment MUST include ContractCommitmentDiscountPercentage.
  - ContractCommitment MUST include ContractCommitmentDurationType.
  - ContractCommitment MUST include ContractCommitmentFulfillmentInterval.
  - ContractCommitment MUST include ContractCommitmentId.
  - ContractCommitment MUST include ContractCommitmentLastUpdated.
  - ContractCommitment MUST include ContractCommitmentLifecycleStatus.
  - ContractCommitment MUST include ContractCommitmentModel.
  - ContractCommitment MUST include ContractCommitmentOfferCategory.
  - ContractCommitment MUST include ContractCommitmentPaymentInterval.
  - ContractCommitment MUST include ContractCommitmentPaymentModel.
  - ContractCommitment MUST include ContractCommitmentPaymentUpfrontPercentage when the service provider offers "Partial Upfront" payment models.
  - ContractCommitment MUST include ContractCommitmentPeriodEnd.
  - ContractCommitment MUST include ContractCommitmentPeriodStart.
  - ContractCommitment MUST include ContractCommitmentQuantity.
  - ContractCommitment MUST include ContractCommitmentType.
  - ContractCommitment MUST include ContractCommitmentUnit.
  - ContractCommitment MUST include ContractId.
  - ContractCommitment MUST include ContractPeriodEnd.
  - ContractCommitment MUST include ContractPeriodStart.
  - ContractCommitment MUST include InvoiceIssuerName.
  - ContractCommitment MUST include PricingCurrency when the service provider supports pricing and billing in different currencies.
  - ContractCommitment MUST include PricingCurrencyContractCommitmentCost when the service provider supports pricing and billing in different currencies.
  - ContractCommitment MUST include ServiceProviderName.
- ContractCommitment MUST conform to CorrectionHandling requirements.
- ContractCommitment MUST conform to DatasetCompleteness requirements.
- ContractCommitment MUST conform to DatasetConfiguration requirements.
- ContractCommitment MUST conform to DeliveryHandling requirements.
- ContractCommitment *FOCUS columns* MUST conform to FocusColumnHandling requirements.
- ContractCommitment *FOCUS columns* MUST conform to NullHandling requirements.
- ContractCommitment *custom columns* MUST conform to CustomColumnHandling requirements.

## Description

Describes the terms of contracts agreed between a service provider and a customer.