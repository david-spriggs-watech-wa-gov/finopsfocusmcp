---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/contract-commitment/contract-commitment-lifecycle-status/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2013-03-03"
fingerprint: f34a006cce675ab5
---
# 3.3.13 Contract Commitment Lifecycle Status

Dataset:
                    Contract Commitment

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    String

Since:
                    1.4

Contract Commitment Lifecycle Status represents the current lifecycle state of a *contract commitment*. The Status determines the applicability of the commitment to a specific period of Cost and Usage data.

## 3.3.13.1 Requirements

ContractCommitmentLifecycleStatus MUST adhere to the following requirements:

- ContractCommitmentLifecycleStatus MUST be of type String.
- ContractCommitmentLifecycleStatus MUST NOT be null.
- ContractCommitmentLifecycleStatus MUST be one of the allowed values.
- When a contract commitment record is modified in a way that requires a new ContractCommitmentID, ContractCommitmentLifecycleStatus for the previous record MUST be "Superseded".

## 3.3.13.2 Allowed Values

| Value | Sort Order | Description | 
|---|---|---|
| Proposed | 10 | The commitment is being negotiated or modeled; it has no legal or financial impact on current data. | 
| Pending | 20 | The commitment is finalized or signed, but the effective start date is in the future. | 
| Active | 30 | The commitment is currently in effect, and it has remaining value. | 
| Exhausted | 40 | The commitment is currently in effect, but its value has been fully consumed. | 
| Expired | 50 | The commitment is no longer active because it reached its scheduled end date. | 
| Canceled | 60 | The commitment is no longer active because it was terminated by either party prior to its scheduled end date. | 
| Superseded | 70 | The commitment is no longer active because it was replaced by a newer version prior to its scheduled end date. | 

## 3.3.13.5 Description

The current lifecycle state of a *contract commitment*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | No | 
| Data Type | String | 
| Value Format | Allowed values |