---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-payment-interval/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2016-03-03"
fingerprint: "9661e00ab6a576bf"
---
# 3.3.16 Contract Commitment Payment Interval

Contract Commitment Payment Interval represents the frequency by which a *contract commitment* is invoiced. For payment models involving deferred financial obligations, the Payment Interval denotes the ongoing billing cycle. For models paid upfront, the Payment Interval denotes the single settlement event.

Note: Do not confuse the Contract Commitment Payment Interval with the Contract Commitment Fulfillment Interval. For example, a spend-based commitment discount may have an Hourly Fulfillment Interval (usage reset) but a Monthly Payment Interval (billing cycle).

## 3.3.16.1 Requirements

ContractCommitmentPaymentInterval MUST adhere to the following requirements:

- ContractCommitmentPaymentInterval MUST be of type String.
- ContractCommitmentPaymentInterval MUST NOT be null.
- ContractCommitmentPaymentInterval MUST be one of the allowed values.
- ContractCommitmentPaymentInterval MUST be "One-Time" when ContractCommitmentPaymentModel is "All Upfront".
- ContractCommitmentPaymentInterval SHOULD represent a time granularity equal to or lesser than the time granularity represented by ContractCommitmentDurationType.

## 3.3.16.2 Allowed Values

| Value | Sort Order | Description | Typical Use Case | 
|---|---|---|---|
| One-Time | 10 | A single invoice is generated for the entire obligation. | All Upfront models (e.g., 3yr All-Upfront RI) or single-invoice arrears paid at the end of a term. | 
| Monthly | 20 | Invoices for the deferred balance are generated once per month. | No Upfront Savings Plans or Monthly SaaS. | 
| Quarterly | 30 | Invoices for the deferred balance are generated every three months. | Partial Upfront deals with 90-day true-ups. | 
| Semi-Annual | 40 | Invoices for the deferred balance are generated every six months. | Split-payment agreements. | 
| Annual | 50 | Invoices for the deferred balance are generated once per year. | Partial Upfront EAs billed yearly. | 
| Custom | 60 | Hourly/Daily or other irregular cycles. | Irregular bridge contracts or non-standard terms. | 

## 3.3.16.5 Description

Represents the frequency by which a *contract commitment* is invoiced.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | Allowed values |