---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/appendix/invoice-and-billing-period-handling/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "3d54d5f334211241"
---
# 8.13 Invoice and Billing Period Handling

## 8.13.1 Overview

A primary use case for FinOps practitioners is the reconciliation of invoices and usage statements. In FOCUS, this process is supported through *FOCUS datasets*, notably the Cost and Usage, Invoice Detail, and Billing Period datasets.

In the context of FOCUS, successful *invoice reconciliation* relies on all monetary data appearing on an invoice or usage statement (including non-usage charges such as taxes, credits, refunds, support, training, and marketplace transactions) being accurately captured and categorized in these datasets.

Without this fundamental alignment, downstream processes like financial reporting and chargeback become unreliable.

### 8.13.1.1 Invoice Reconciliation and Issuance

Before an *invoice is issued*, i.e., before the Invoice Issue Status in the Invoice Detail dataset transitions to "Issued", data generators typically perform internal *invoice reconciliation* to ensure consistency between the invoice, the Invoice Detail dataset, and the Cost and Usage dataset.

At the conclusion of this process, a key objective is for the aggregated Billed Costs in the Invoice Detail dataset for a given Invoice Detail ID to align with the payable amounts presented on the corresponding invoice line items. This alignment is performed across Invoice ID, Invoice Detail ID, and Invoice Issuer.

Similarly, practitioners rely on the aggregated Billed Costs in the Invoice Detail dataset to reconcile with the aggregated Billed Costs in the Cost and Usage dataset for the same identifiers, subject to Rounding Variance Tolerance.

Practitioners may perform *invoice reconciliation* independently by verifying that invoice line items align with data delivered in *FOCUS dataset artifacts*, particularly Cost and Usage, Invoice Detail, and Billing Period.

Once an invoice is issued, it becomes an authoritative financial document, and the information it contains is expected not to change.

*Corrections* related to *issued invoices* (i.e., updates, additions, or omissions of underlying records in Cost and Usage, Invoice Detail, and Billing Period datasets) are permitted in accordance with the Invoice Issue Status requirements, as well as the Billed Cost requirements in both Invoice Detail and Cost and Usage datasets. In other words, such *corrections* are typically performed upon explicit request or approval by the customer, provided that they do not compromise the integrity of the issued invoice.

*Corrections* to underlying records that do not impact *invoice reconciliation* are allowed regardless of Invoice Issue Status. However, even in this case, they may reduce auditability and traceability or affect downstream processes (e.g., cost allocation, chargeback, reporting).

### 8.13.1.2 Open and Closed Billing Periods

A *closed billing period* represents a billing period for which all anticipated invoices have been successfully issued by the designated *invoice issuers*, and no additional invoices are generally expected to be associated with that period, except where explicitly requested or approved by the customer. In contrast, an *open billing period* remains subject to ongoing billing activities until it is formally closed.

The Billing Period dataset provides the necessary context to determine the status of each billing period for a specific invoice issuer. Since invoice issuer and *billing period*-related columns are present in all three *FOCUS datasets* (Billing Period, Cost and Usage, and Invoice Detail), records across the three datasets can be consistently associated with the corresponding billing cycles.

*Corrections* related to *closed billing periods* (i.e., updates; additions; or omissions of underlying records in Cost and Usage, Invoice Detail, and Billing Period *FOCUS datasets*) are permitted in accordance with the Billing Period Status requirements, as well as the Billed Cost requirements in both Invoice Detail and Cost and Usage datasets. In other words, such *corrections* are typically performed upon explicit request or approval by the customer, provided that they do not compromise the integrity of the *closed billing period*.

*Corrections* to underlying records that do not impact the integrity of the *closed billing period* or *invoice reconciliation*, such as informational or metadata updates, are allowed regardless of Billing Period Status.

If the original *closed billing period* is not reopened, corrections that require issuing additional invoices are best represented by associating them with a subsequent *open billing period*. This approach preserves historical financial accuracy, ensures clear temporal boundaries between billing cycles, and guarantees that all corrections are transparently tracked and auditable in future periods.