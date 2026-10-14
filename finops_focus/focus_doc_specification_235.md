---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-description/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: dcfa402e03ff587b
---
# 3.3.7 Contract Commitment Description

Dataset:
                    Contract Commitment

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    String

Since:
                    1.3

Contract Commitment Description provides a high-level context of a *contract commitment* without requiring additional discovery. Contract Commitment Description is a self-contained summary of the contract commitment's terms, which may not be sufficiently described by the other columns of the Contract Commitment dataset.

## 3.3.7.1 Requirements

ContractCommitmentDescription MUST adhere to the following requirements:

- ContractCommitmentDescription MUST be of type String.
- ContractCommitmentDescription MUST conform to StringHandling requirements.
- ContractCommitmentDescription SHOULD NOT be null.
- ContractCommitmentDescription maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

## 3.3.7.4 Description

The self-contained summary of the *contract commitment's* terms.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | \\\<not specified> |