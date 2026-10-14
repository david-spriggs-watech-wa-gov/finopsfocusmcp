---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/features/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: a23064f74583b5c9
---
# 2 Supported Features

Note: The following section is informative and non-normative. It does not define requirements.


The FOCUS specification is designed to meet the needs of FinOps practitioners in numerous scenarios. The following section contains features supported by the FOCUS specification. This list does not represent all possible combinations or use of FOCUS data but does represent core capabilities that the FOCUS specification supports.

## Supported Feature List

| Feature | Description | 
|---|---|
| Account Structures | Supports breaking costs down by billing and sub-accounts to facilitate chargeback and budgeting scenarios. | 
| Billed Cost and Invoice Alignment | Ensures data is consistent with payable invoices regarding total cost and the period of time covered. | 
| Charge Categorization | Supports classification of charges including purchases, usage, tax, credits, and adjustments. | 
| Commit Usage and Under Usage | Tracks the usage and under-usage of commitment discounts and capacity reservations. | 
| Commitment Program Eligibility Details | Identifies which commitment programs each charge qualifies for, supporting coverage rate analysis and uncovered savings identification. | 
| Contract Commitments | Tracks commitments made via contractual agreements using identifiers joined between Cost and Usage and Contract Commitment datasets. | 
| Cost and Usage Attribution | Facilitates the inclusion of provider-defined or user-defined metadata (tags) at a row level for organizational analysis. | 
| Cost Comparison | Supports comparing Billed, Contracted, Effective, and List cost columns to identify savings or amortization. | 
| Custom Columns | Allows the inclusion of additional columns to facilitate reporting capabilities not covered by the standard specification. | 
| Data Generator-Calculated Split Cost Allocation | Enables tracking resources split by internal consumption metrics, common for shared clusters like Kubernetes. | 
| Data Granularity | Supports multiple levels of granularity, from high-level account charges down to individual resource-level data. | 
| Dataset Instance Metadata | Provides metadata describing dataset artifacts, unique identifiers, and alignment with specific FOCUS datasets. | 
| Effective Cost Analysis | Enables analysis of costs after discounts and the amortization of upfront fees to track spending trends. | 
| Invoice Reconciliation | Reconciles Cost and Usage records with Invoice Detail line items to validate that usage costs map back to invoiced amounts. | 
| Location | Provides structured data for regions and availability zones to analyze costs based on deployment geography. | 
| Marketplace Purchases | Supports analysis of marketplace purchase data and reporting Effective Cost for service provider usage. | 
| Participating Entity Identification | Allows identification of entities involved in hosting, invoicing, and data generation (e.g., Service Provider vs. Host Provider). | 
| Recency Metadata | Indicates what portion of a dataset is complete and how recently it was updated to inform FinOps functions like chargeback. | 
| Resource Usage | Enables tracking consumption by providing information on which resources were used, in what quantities, and with what units. | 
| Schema Metadata | Communicates important attributes about data structure, types, and versions to facilitate structure changes. | 
| Service Categorization | Standardizes the classification of services into high-level functional categories and granular subcategories. | 
| Service Provider Services | Aligns costs with familiar service and product offering names for easier reporting and verification. | 
| Verification, Comparison, and Fluctuation Tracking of Unit Prices | Facilitates verification of List and Contracted unit prices and tracks fluctuations over time. |