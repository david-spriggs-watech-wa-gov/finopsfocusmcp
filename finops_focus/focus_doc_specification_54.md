---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/invoice-detail/invoice-issue-date/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2013-04-03"
fingerprint: "7d72f8ca00297839"
---
# 3.4.13 Invoice Issue Date

Dataset:
                    Invoice Detail

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    Date/Time

Since:
                    1.4

Invoice Issue Date is the date the invoice was issued by the *invoice issuer*. This date serves as the official point of record for the billing document, determining the beginning of payment terms and providing a key reference point for financial audits and period closing processes.

## 3.4.13.1 Requirements

InvoiceIssueDate MUST adhere to the following requirements:

- InvoiceIssueDate MUST be of type Date/Time.
- InvoiceIssueDate MUST conform to DateTimeFormat requirements.
- InvoiceIssueDate MAY be null.
- InvoiceIssueDate MUST represent the official date of issuance for the corresponding InvoiceId.

## 3.4.13.4 Description

The date the invoice was issued by the invoice issuer.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | Date/Time | 
| Value Format | Date/Time Format |