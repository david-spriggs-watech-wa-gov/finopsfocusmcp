---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: d8ea803935645a69
---
1. Specification
2. v1.4
3. Columns

# Columns

123 columns

| Name | Dataset | Type | Feature Level | Data Type | Since | 
|---|---|---|---|---|---|
| Billing Period Created | Billing Period | Dimension | Mandatory | Date/Time | 1.4 | 
| Billing Period End | Billing Period | Dimension | Mandatory | Date/Time | 1.4 | 
| Billing Period Last Updated | Billing Period | Dimension | Mandatory | Date/Time | 1.4 | 
| Billing Period Start | Billing Period | Dimension | Mandatory | Date/Time | 1.4 | 
| Billing Period Status | Billing Period | Dimension | Mandatory | String | 1.4 | 
| Invoice Issuer Name | Billing Period | Dimension | Mandatory | String | 1.4 | 
| Billing Currency | Contract Commitment | Dimension | Mandatory | String | 1.3 | 
| Contract Commitment Applicability | Contract Commitment | Dimension / Metric | Mandatory | JSON | 1.4 | 
| Contract Commitment Benefit Category | Contract Commitment | Dimension | Mandatory | String | 1.4 | 
| Contract Commitment Category | Contract Commitment | Dimension | Mandatory | String | 1.3 | 
| Contract Commitment Cost | Contract Commitment | Metric | Mandatory | Decimal | 1.3 | 
| Contract Commitment Created | Contract Commitment | Dimension | Mandatory | Date/Time | 1.4 | 
| Contract Commitment Description | Contract Commitment | Dimension | Mandatory | String | 1.3 | 
| Contract Commitment Discount Percentage | Contract Commitment | Metric | Mandatory | Decimal | 1.4 | 
| Contract Commitment Duration Type | Contract Commitment | Dimension | Mandatory | String | 1.4 | 
| Contract Commitment Fulfillment Interval | Contract Commitment | Dimension | Mandatory | String | 1.4 | 
| Contract Commitment ID | Contract Commitment | Dimension | Mandatory | String | 1.3 | 
| Contract Commitment Last Updated | Contract Commitment | Dimension | Mandatory | Date/Time | 1.4 | 
| Contract Commitment Lifecycle Status | Contract Commitment | Dimension | Mandatory | String | 1.4 | 
| Contract Commitment Model | Contract Commitment | Dimension | Mandatory | String | 1.4 | 
| Contract Commitment Offer Category | Contract Commitment | Dimension | Mandatory | String | 1.4 | 
| Contract Commitment Payment Interval | Contract Commitment | Dimension | Mandatory | String | 1.4 | 
| Contract Commitment Payment Model | Contract Commitment | Dimension | Mandatory | String | 1.4 | 
| Contract Commitment Payment Upfront Percentage | Contract Commitment | Metric | Conditional | Decimal | 1.4 | 
| Contract Commitment Period End | Contract Commitment | Dimension | Mandatory | Date/Time | 1.3 | 
| Contract Commitment Period Start | Contract Commitment | Dimension | Mandatory | Date/Time | 1.3 | 
| Contract Commitment Quantity | Contract Commitment | Metric | Mandatory | Decimal | 1.3 | 
| Contract Commitment Type | Contract Commitment | Dimension | Mandatory | String | 1.3 | 
| Contract Commitment Unit | Contract Commitment | Dimension | Mandatory | String | 1.3 | 
| Contract ID | Contract Commitment | Dimension | Mandatory | String | 1.3 | 
| Contract Period End | Contract Commitment | Dimension | Mandatory | Date/Time | 1.3 | 
| Contract Period Start | Contract Commitment | Dimension | Mandatory | Date/Time | 1.3 | 
| Invoice Issuer Name | Contract Commitment | Dimension | Mandatory | String | 1.4 | 
| Pricing Currency | Contract Commitment | Dimension | Conditional | String | 1.4 | 
| Pricing Currency Contract Commitment Cost | Contract Commitment | Metric | Conditional | Decimal | 1.4 | 
| Service Provider Name | Contract Commitment | Dimension | Mandatory | String | 1.4 | 
| Allocated Method ID | Cost and Usage | Dimension | Conditional | String | 1.3 | 
| Allocated Method Details | Cost and Usage | Dimension / Metric | Recommended | JSON | 1.3 | 
| Allocated Resource ID | Cost and Usage | Dimension | Conditional | String | 1.3 | 
| Allocated Resource Name | Cost and Usage | Dimension | Conditional | String | 1.3 | 
| Allocated Tags | Cost and Usage | Dimension | Conditional | JSON | 1.3 | 
| Availability Zone | Cost and Usage | Dimension | Recommended | String | 0.5 | 
| Billed Cost | Cost and Usage | Metric | Mandatory | Decimal | 0.5 | 
| Billing Account ID | Cost and Usage | Dimension | Mandatory | String | 0.5 | 
| Billing Account Name | Cost and Usage | Dimension | Mandatory | String | 0.5 | 
| Billing Account Type | Cost and Usage | Dimension | Conditional | String | 1.2 | 
| Billing Currency | Cost and Usage | Dimension | Mandatory | String | 0.5 | 
| Billing Period End | Cost and Usage | Dimension | Mandatory | Date/Time | 0.5 | 
| Billing Period Start | Cost and Usage | Dimension | Mandatory | Date/Time | 0.5 | 
| Capacity Reservation ID | Cost and Usage | Dimension | Conditional | String | 1.1 | 
| Capacity Reservation Status | Cost and Usage | Dimension | Conditional | String | 1.1 | 
| Charge Category | Cost and Usage | Dimension | Mandatory | String | 0.5 | 
| Charge Class | Cost and Usage | Dimension | Mandatory | String | 1.0 | 
| Charge Description | Cost and Usage | Dimension | Mandatory | String | 1.0-preview | 
| Charge Frequency | Cost and Usage | Dimension | Recommended | String | 1.0-preview | 
| Charge Period End | Cost and Usage | Dimension | Mandatory | Date/Time | 0.5 | 
| Charge Period Start | Cost and Usage | Dimension | Mandatory | Date/Time | 0.5 | 
| Commitment Discount Category | Cost and Usage | Dimension | Conditional | String | 1.0-preview | 
| Commitment Discount ID | Cost and Usage | Dimension | Conditional | String | 1.0-preview | 
| Commitment Discount Name | Cost and Usage | Dimension | Conditional | String | 1.0-preview | 
| Commitment Discount Quantity | Cost and Usage | Metric | Conditional | Decimal | 1.1 | 
| Commitment Discount Status | Cost and Usage | Dimension | Conditional | String | 1.0 | 
| Commitment Discount Type | Cost and Usage | Dimension | Conditional | String | 1.0-preview | 
| Commitment Discount Unit | Cost and Usage | Dimension | Conditional | String | 1.1 | 
| Commitment Program Eligibility Details | Cost and Usage | Dimension | Conditional | JSON | 1.4 | 
| Consumed Quantity | Cost and Usage | Metric | Conditional | Decimal | 1.0 | 
| Consumed Unit | Cost and Usage | Dimension | Conditional | String | 1.0 | 
| Contract Applied | Cost and Usage | Dimension / Metric | Conditional | JSON | 1.3 | 
| Contracted Cost | Cost and Usage | Metric | Mandatory | Decimal | 1.0 | 
| Contracted Unit Price | Cost and Usage | Metric | Conditional | Decimal | 1.0 | 
| Effective Cost | Cost and Usage | Metric | Mandatory | Decimal | 0.5 | 
| Host Provider Name | Cost and Usage | Dimension | Mandatory | String | 1.3 | 
| Invoice Detail ID | Cost and Usage | Dimension | Conditional | String | 1.4 | 
| Invoice ID | Cost and Usage | Dimension | Conditional | String | 1.2 | 
| Invoice Issuer Name | Cost and Usage | Dimension | Mandatory | String | 0.5 | 
| List Cost | Cost and Usage | Metric | Mandatory | Decimal | 1.0-preview | 
| List Unit Price | Cost and Usage | Metric | Conditional | Decimal | 1.0-preview | 
| Pricing Category | Cost and Usage | Dimension | Conditional | String | 1.0-preview | 
| Pricing Currency | Cost and Usage | Dimension | Conditional | String | 1.2 | 
| Pricing Currency Contracted Unit Price | Cost and Usage | Metric | Conditional | Decimal | 1.2 | 
| Pricing Currency Effective Cost | Cost and Usage | Metric | Conditional | Decimal | 1.2 | 
| Pricing Currency List Unit Price | Cost and Usage | Metric | Conditional | Decimal | 1.2 | 
| Pricing Quantity | Cost and Usage | Metric | Mandatory | Decimal | 1.0-preview | 
| Pricing Unit | Cost and Usage | Dimension | Mandatory | String | 1.0-preview | 
| Region ID | Cost and Usage | Dimension | Conditional | String | 1.0 | 
| Region Name | Cost and Usage | Dimension | Conditional | String | 1.0 | 
| Resource ID | Cost and Usage | Dimension | Conditional | String | 0.5 | 
| Resource Name | Cost and Usage | Dimension | Conditional | String | 0.5 | 
| Resource Type | Cost and Usage | Dimension | Conditional | String | 1.0-preview | 
| Service Provider Name | Cost and Usage | Dimension | Mandatory | String | 1.3 Introduced as a replacement for the removed ProviderName column | 
| Service Category | Cost and Usage | Dimension | Mandatory | String | 0.5 | 
| Service Name | Cost and Usage | Dimension | Mandatory | String | 0.5 | 
| Service Subcategory | Cost and Usage | Dimension | Recommended | String | 1.1 | 
| SKU ID | Cost and Usage | Dimension | Conditional | String | 1.0-preview | 
| SKU Meter | Cost and Usage | Dimension | Conditional | String | 1.1 | 
| SKU Price Details | Cost and Usage | Dimension | Conditional | JSON | 1.1 | 
| SKU Price ID | Cost and Usage | Dimension | Conditional | String | 1.0-preview | 
| Sub Account ID | Cost and Usage | Dimension | Conditional | String | 0.5 | 
| Sub Account Name | Cost and Usage | Dimension | Conditional | String | 0.5 | 
| Sub Account Type | Cost and Usage | Dimension | Conditional | String | 1.2 | 
| Tags | Cost and Usage | Dimension | Conditional | JSON | 1.0-preview | 
| Billed Cost | Invoice Detail | Metric | Mandatory | Decimal | 1.4 | 
| Billing Account ID | Invoice Detail | Dimension | Mandatory | String | 1.4 | 
| Billing Currency | Invoice Detail | Dimension | Mandatory | String | 1.4 | 
| Billing Period End | Invoice Detail | Dimension | Mandatory | Date/Time | 1.4 | 
| Billing Period Start | Invoice Detail | Dimension | Mandatory | Date/Time | 1.4 | 
| Charge Category | Invoice Detail | Dimension | Mandatory | String | 1.4 | 
| Invoice Detail Created | Invoice Detail | Dimension | Mandatory | Date/Time | 1.4 | 
| Invoice Detail Description | Invoice Detail | Dimension | Mandatory | String | 1.4 | 
| Invoice Detail Grain | Invoice Detail | Dimension | Mandatory | JSON | 1.4 | 
| Invoice Detail ID | Invoice Detail | Dimension | Mandatory | String | 1.4 | 
| Invoice Detail Last Updated | Invoice Detail | Dimension | Mandatory | Date/Time | 1.4 | 
| Invoice ID | Invoice Detail | Dimension | Mandatory | String | 1.4 | 
| Invoice Issue Date | Invoice Detail | Dimension | Mandatory | Date/Time | 1.4 | 
| Invoice Issuer Name | Invoice Detail | Dimension | Mandatory | String | 1.4 | 
| Invoice Issue Status | Invoice Detail | Dimension | Mandatory | String | 1.4 | 
| Payment Currency | Invoice Detail | Dimension | Conditional | String | 1.4 | 
| Payment Currency Billed Cost | Invoice Detail | Metric | Conditional | Decimal | 1.4 | 
| Payment Currency Invoice Detail ID | Invoice Detail | Dimension | Conditional | String | 1.4 | 
| Payment Due Date | Invoice Detail | Dimension | Mandatory | Date/Time | 1.4 | 
| Payment Terms | Invoice Detail | Dimension | Mandatory | String | 1.4 | 
| Purchase Order Number | Invoice Detail | Dimension | Conditional | String | 1.4 | 
| Reference Invoice ID | Invoice Detail | Dimension | Mandatory | String | 1.4 |