---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/charge-class/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2017-01-03"
fingerprint: "4ec1042ac0534c07"
---
# 3.1.17 Charge Class

Dataset:
                    Cost and Usage

Column Type:
                    Dimension

Feature Level:
                    Mandatory

Data Type:
                    String

Since:
                    1.0

Charge Class indicates whether a *charge* represents a *correction* to a previously *closed billing period*. Charge Class is commonly used to differentiate such corrections from all other charges, including both regularly incurred *charges* and *corrections* to *open billing periods*.

## 3.1.17.1 Requirements

ChargeClass MUST adhere to the following requirements:

- ChargeClass MUST be of type String.
- ChargeClass MUST adhere to the following nullability requirements:
  - ChargeClass MUST be null when the *charge* does not represent a correction to a previously *closed billing period*.
  - ChargeClass MUST NOT be null when the *charge* represents a correction to a previously *closed billing period*.
- ChargeClass MUST be "Correction" when ChargeClass is not null.

## 3.1.17.2 Allowed Values

| Value | Description | 
|---|---|
| Correction | Correction to a previously *closed billing period* (e.g., refunds and credit modifications). | 

## 3.1.17.5 Description

Indicates whether a *charge* represents a correction to a previously *closed billing period*.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Mandatory | 
| Allows Nulls | Yes | 
| Data Type | String | 
| Value Format | Allowed values |