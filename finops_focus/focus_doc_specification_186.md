---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/sku-price-details/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "29dd60c7e47c6564"
---
# 3.1.60 SKU Price Details

SKU Price Details represent a list of *SKU Price* properties (key-value pairs) associated with a specific SKU Price ID. These properties include qualitative and quantitative properties of a *SKUs* (e.g., functionality and technical specifications), along with core stable pricing properties (e.g., pricing *periods*, tiers, etc.), excluding dynamic or negotiable pricing elements such as unit price amounts; currency (and related exchange rates); temporal validity (e.g., effective dates); and contract- or negotiation-specific factors (e.g., contract or account identifiers, and negotiable discounts).

The composition of properties associated with a specific *SKU Price* may differ across service providers and across *SKUs* within the same service provider. However, the exclusion of dynamic or negotiable pricing properties should ensure that all *charges* with the same SKU Price ID share the same SKU Price Details, i.e., that SKU Price Details remains consistent across different *billing periods* and *billing accounts* within a service provider.

SKU Price Details helps practitioners understand and distinguish *SKU Prices*, each identified by a SKU Price ID and associated with a used or purchased *resource* or *service*. It can also help determine the quantity of units for a property when it holds a numeric value (e.g., CoreCount), even when its unit differs from the one in which the *SKU* is priced and charged, thus supporting FinOps capabilities such as unit economics. Additionally, the SKU Price Details may be used to analyze costs based on pricing properties such as *periods* and tiers.

## 3.1.60.1 Requirements

SkuPriceDetails MUST adhere to the following requirements:

- SkuPriceDetails MUST be of type JSON Object (serialized as a String where necessary).
- SkuPriceDetails MUST conform to StringHandling requirements.
- SkuPriceDetails MUST conform to KeyValueFormat requirements.
- SkuPriceDetails property keys SHOULD conform to PascalCase format.
- SkuPriceDetails MUST adhere to the following nullability requirements:
  - SkuPriceDetails MUST be null when SkuPriceId is null.
  - SkuPriceDetails MAY be null when SkuPriceId is not null.
- When SkuPriceDetails is not null, SkuPriceDetails MUST adhere to the following requirements:
  - SkuPriceDetails MUST be associated with a given SkuPriceId.
  - SkuPriceDetails MUST include the FOCUS-defined SKU Price property when an equivalent property is included as a custom property.
  - SkuPriceDetails MUST NOT include properties that are not applicable to the corresponding SkuPriceId.
  - SkuPriceDetails SHOULD include all FOCUS-defined SKU Price properties listed below that are applicable to the corresponding SkuPriceId.
  - SkuPriceDetails SHOULD include all custom SKU Price properties that are applicable to the corresponding SkuPriceId when there is no equivalent FOCUS-defined property.
  - SkuPriceDetails MAY include properties that are already captured in other dedicated columns.
  - SkuPriceDetails properties for a given SkuPriceId MUST adhere to the following requirements:
    - Existing SkuPriceDetails properties SHOULD remain consistent over time.
    - Existing SkuPriceDetails properties SHOULD NOT be removed.
    - Additional SkuPriceDetails properties MAY be added over time.
  - Property key SHOULD remain consistent across comparable *SKUs* having that property, and the values for this key SHOULD remain in a consistent format.
  - Property key MUST begin with the string "x\_" unless it is a FOCUS-defined property.
  - Property value MUST represent the value for a single PricingUnit when the property holds a numeric value.
- FOCUS-defined SKU Price properties MUST adhere to the following requirements:
  - Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  - Property value MUST be of the type specified for that property.
  - Property value MUST represent the value for a single PricingUnit, denominated in the unit of measure specified for that property when the property holds a numeric value.

## 3.1.60.2 FOCUS-Defined Properties

The following keys should be used when applicable to facilitate cross-SKU and cross-service-provider queries for the same conceptual property. FOCUS-defined keys will appear in the list below and custom (e.g., service-provider-defined) keys will be prefixed with "x\_" to make them easy to identify as well as prevent collisions.

| Key | Description | Data Type | Unit of Measure (numeric) or example values (string) | 
|---|---|---|---|
| CoreCount | Number of physical or virtual CPUs available <sup>1</sup> | Numeric | Measure: Quantity of Cores | 
| DiskMaxIops | Storage maximum sustained input/output operations per second <sup>1</sup> | Numeric | Measure: Input/Output Operations per Second (IOPS) | 
| DiskSpace | Storage capacity available | Numeric | Measure: Gibibytes (GiB) | 
| DiskType | Kind of disk used | String | Examples: "SSD", "HDD", "NVMe" | 
| GpuCount | Number of GPUs available | Numeric | Measure: Quantity of GPUs | 
| InstanceType | Common name of the instance including size, shape, series, etc. | String | Examples: "m5d.2xlarge", "NC24rs\_v3", "P50" | 
| InstanceSeries | Common name for the series and/or generation of the instance | String | Examples: "M5", "Dadv5", "N2D" | 
| MemorySize | RAM allocated for processing | Numeric | Measure: Gibibytes (GiB <sup>2</sup>) | 
| NetworkMaxIops | Network maximum sustained input/output operations per second <sup>1</sup> | Numeric | Measure: Input/Output Operations per Second (IOPS) | 
| NetworkMaxThroughput | Network maximum sustained throughput for data transfer <sup>1</sup> | Numeric | Measure: Megabits per second (Mbps) | 
| OperatingSystem | Operating system family <sup>3</sup> | String | Examples: "Linux", "MacOS", "Windows" | 
| Redundancy | Level of redundancy offered by the SKU | String | Examples: "Local", "Zonal", "Global" | 
| StorageClass | Class or tier of storage provided | String | Examples: "Hot", "Archive", "Nearline" | 

Notes

<sup>1</sup> In the case of "burstable" SKUs offering variable levels of performance, the baseline or guaranteed value should be used.

<sup>2</sup> Memory manufacturers still commonly uses "GB" to refer to 2<sup>30</sup> bytes, which is known as GiB in other contexts.

<sup>3</sup> This is the operating system family of the SKU, if it's included with the SKU or the SKU only supports one type of operating system.

## 3.1.60.3 Examples

```
{
    "StorageClass": "Archive",
    "CoreCount": 4,
    "x_PremiumProcessing": true
}
```
## 3.1.60.6 Description

A set of properties of a SKU Price ID which are meaningful and common to all instances of that SKU Price ID.

## Constraints

| Property | Value | 
|---|---|
| Column Type | Dimension | 
| Feature Level | Conditional | 
| Allows Nulls | Yes | 
| Data Type | JSON | 
| Value Format | Key-Value Format |