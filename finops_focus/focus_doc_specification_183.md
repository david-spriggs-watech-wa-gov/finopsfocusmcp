---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/metadata/data-generator/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: fcac693974d334ec
---
# 5.1 Data Generator

The FOCUS metadata about the generator of the FOCUS data.

## 5.1.1 Requirements

DataGenerator adheres to the following requirements:

- DataGenerator MUST be present in the Metadata.
- DataGenerator MUST be of type Object.
- DataGenerator MUST NOT be null.

## 5.1.2 Metadata ID

DataGenerator

## 5.1.3 Metadata Name

Data Generator

## 5.1.4 Examples

For an example of the FOCUS Data Generator metadata please refer to: Data Generator Example.

## 5.1.5 Version Introduced

1.0

## 5.1.6 Data Generator

Human-readable name of the entity that generated the dataset instance. The Data Generator ensures the technical accuracy and delivery of the data.

DataGenerator property adheres to the following requirements:

- DataGenerator MUST be present in the Data Generator object.
- DataGenerator MUST be of type String.
- DataGenerator MUST conform to StringHandling requirements.
- DataGenerator MUST NOT be null.
- DataGenerator SHOULD reflect the entity that generated the *FOCUS dataset*.

### 5.1.6.1 Metadata ID

DataGenerator

### 5.1.6.2 Metadata Name

Data Generator

### 5.1.6.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Mandatory | 
| Allows nulls | False | 
| Data type | String | 
| Value format | \<not specified> | 

### 5.1.6.4 Version Introduced

1.0