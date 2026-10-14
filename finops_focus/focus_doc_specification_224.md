---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/appendix/commitment-discount-flexibility-examples/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2023-01-01"
fingerprint: "204f20534ec7e380"
---
# 8.3 Examples: Commitment Discount Flexibility

A usage-based *commitment discount* obligates a customer to a usage amount for one or more related SKUs in return for reduced rates. For example, when a usage-based *commitment discount* is purchased to cover a specific database SKU, this commitment will cover every hour over the period where at least one instance of this SKU is running. The usage-based commitment can cover 1 resource over the hour, or in the case of *commitment discount flexibility*, it can cover a portion of 1 resource or multiple resources at a time.

When mixing usage-based commitment discounts with and without *commitment discount flexibility* and *CommitmentDiscountQuantity* measured by time, it is important to differentiate the *CommitmentDiscountUnit* for each type of *commitment discount*. In each scenario below, *commitment discounts without commitment discount flexibility* applied use "Hour" as the *CommitmentDiscountUnit*, and conversely commitment discounts *with commitment discount flexibility* applied use "Normalized Hour" as the *CommitmentDiscountUnit*.

For more details on exactly how *commitment discounts* purchase and usage rows appear with and without *commitment discount flexibility*, see the following scenarios:

## 8.3.1 100% Utilization Without Commitment Discount Flexibility

### 8.3.1.1 Context

For this example, fictitious service provider, *LatticeScale*, offers the following SKU catalog which is used in the scenario below.

### 8.3.1.2 SKU Catalog

| Service | Sku Id | Sku Price Id | Sku Price Unit Price | Normalization Factor | 
|---|---|---|---|---|
| Compute | VM\_SMALL | VM\_SMALL\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $0.50 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $1.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $1.50 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $2.00 | 4 | 
| Compute | VM\_SMALL | VM\_SMALL\_COMMITTED\_HOUR | $0.50 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_COMMITTED\_HOUR | $1.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_COMMITTED\_HOUR | $1.50 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_COMMITTED\_HOUR | $2.00 | 4 | 
| Compute | VM\_SMALL | VM\_SMALL\_ON\_DEMAND\_HOUR | $1.00 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_ON\_DEMAND\_HOUR | $2.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_ON\_DEMAND\_HOUR | $3.00 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_ON\_DEMAND\_HOUR | $4.00 | 4 | 

The above SKU Catalog shows that this service provider only has 1 service that offers 4 virtual machine SKUs at various list rates, *commitment discount* rates, and normalization factors. Each SKU's normalization factor classifies its relative size to its *commitment discount* rate. Usage-based *commitment discounts* with *commitment discount flexibility* can fully cover any combination of 1 or more SKUs where the sum of their normalization factor is less than or equal to the normalization factor of the *commitment discount*.

### 8.3.1.3 Scenario

- 1 no upfront *commitment discount* is purchased for 1 year (2023) for 1 VM\_LARGE.
- 1 VM\_LARGE resource runs for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00.

### 8.3.1.4 Outcome

- 1 recurring, purchase record exists for 1 eligible "Hour" of the no upfront, *commitment discount* and incurs a $1.50 *BilledCost*.
- The *commitment discount* covers the first *charge period* for 1 VM\_LARGE resource incurring a $1.50 *EffectiveCost*.

## 8.3.2 0% Utilization Without Commitment Discount Flexibility

### 8.3.2.1 Context

For this example, fictitious service provider, *LatticeScale*, offers the following SKU catalog which is used in the scenario below.

### 8.3.2.2 SKU Catalog

| Service | Sku Id | Sku Price Id | Sku Price Unit Price | Normalization Factor | 
|---|---|---|---|---|
| Compute | VM\_SMALL | VM\_SMALL\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $0.50 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $1.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $1.50 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $2.00 | 4 | 
| Compute | VM\_SMALL | VM\_SMALL\_COMMITTED\_HOUR | $0.50 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_COMMITTED\_HOUR | $1.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_COMMITTED\_HOUR | $1.50 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_COMMITTED\_HOUR | $2.00 | 4 | 
| Compute | VM\_SMALL | VM\_SMALL\_ON\_DEMAND\_HOUR | $1.00 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_ON\_DEMAND\_HOUR | $2.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_ON\_DEMAND\_HOUR | $3.00 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_ON\_DEMAND\_HOUR | $4.00 | 4 | 

The above SKU Catalog shows that this service provider only has 1 service that offers 4 virtual machine SKUs at various list unit prices, *commitment discount* unit prices, and normalization factors. Each SKU's normalization factor classifies its relative size to its *commitment discount* unit price. Usage-based *commitment discounts* with *commitment discount flexibility* can fully cover any combination of 1 or more SKUs where the sum of their normalization factor is less than or equal to the normalization factor of the *commitment discount*.

### 8.3.2.3 Scenario

- 1 no upfront *commitment discount* is purchased for 1 year (2023) for 1 VM\_LARGE.
- 1 VM\_MEDIUM resource runs for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00.

### 8.3.2.4 Outcome

- 1 recurring, purchase record exists for 1 eligible "Hour" of the no upfront, *commitment discount* and incurs a $1.50 *BilledCost*.
- The VM\_LARGE *commitment discount* is unused for the corresponding *charge period* because no VM\_LARGE resources are running and incurs a $1.50 *EffectiveCost*.
- 1 hour of on-demand usage is incurred by the VM\_MEDIUM resource and incurs a $2.00 *BilledCost* and *EffectiveCost*.

## 8.3.3 100% Utilization with Commitment Discount Flexibility with 1 Resource

### 8.3.3.1 Context

For this example, fictitious service provider, *LatticeScale*, offers the following SKU catalog which is used in the scenario below.

### 8.3.3.2 SKU Catalog

| Service | Sku Id | Sku Price Id | Sku Price Unit Price | Normalization Factor | 
|---|---|---|---|---|
| Compute | VM\_SMALL | VM\_SMALL\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $0.50 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $1.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $1.50 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $2.00 | 4 | 
| Compute | VM\_SMALL | VM\_SMALL\_COMMITTED\_HOUR | $0.50 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_COMMITTED\_HOUR | $1.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_COMMITTED\_HOUR | $1.50 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_COMMITTED\_HOUR | $2.00 | 4 | 
| Compute | VM\_SMALL | VM\_SMALL\_ON\_DEMAND\_HOUR | $1.00 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_ON\_DEMAND\_HOUR | $2.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_ON\_DEMAND\_HOUR | $3.00 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_ON\_DEMAND\_HOUR | $4.00 | 4 | 

The above SKU catalog shows that this service provider only has 1 service that offers 4 virtual machine SKUs at various list rates, *commitment discount* rates, and normalization factors. Each SKU's normalization factor classifies its relative size to its *commitment discount* rate. Usage-based *commitment discounts* with *commitment discount flexibility* can fully cover any combination of 1 or more SKUs where the sum of their normalization factor is less than or equal to the normalization factor of the *commitment discount*.

### 8.3.3.3 Scenario

- 1 no upfront *commitment discount* is purchased for 1 year (2023) for 1 VM\_SMALL which has a normalization factor of 1.
- 1 VM\_LARGE resource runs for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00 with a normalization factor of 4.

### 8.3.3.4 Outcome

- 1 recurring, purchase record exists for 1 eligible "Normalized Hour" of the no upfront, *commitment discount* and incurs a $0.50 *BilledCost*.
- The VM\_SMALL *commitment discount* is fully utilized within the corresponding *charge period*, covers 25% of the VM\_LARGE resource, and incurs a $0.50 *EffectiveCost*.
- The VM\_LARGE resource incurs an additional, on-demand $2.25 *BilledCost* and *EffectiveCost*.

## 8.3.4 100% Utilization with Commitment Discount Flexibility with 2 Resources

### 8.3.4.1 Context

For this example, fictitious service provider, *LatticeScale*, offers the following SKU catalog which is used in the scenario below.

### 8.3.4.2 SKU Catalog

| Service | Sku Id | Sku Price Id | Sku Price Unit Price | Normalization Factor | 
|---|---|---|---|---|
| Compute | VM\_SMALL | VM\_SMALL\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $0.50 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $1.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $1.50 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_COMMITTED\_PURCHASE\_NO\_UPFRONT | $2.00 | 4 | 
| Compute | VM\_SMALL | VM\_SMALL\_COMMITTED\_HOUR | $0.50 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_COMMITTED\_HOUR | $1.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_COMMITTED\_HOUR | $1.50 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_COMMITTED\_HOUR | $2.00 | 4 | 
| Compute | VM\_SMALL | VM\_SMALL\_ON\_DEMAND\_HOUR | $1.00 | 1 | 
| Compute | VM\_MEDIUM | VM\_MEDIUM\_ON\_DEMAND\_HOUR | $2.00 | 2 | 
| Compute | VM\_LARGE | VM\_LARGE\_ON\_DEMAND\_HOUR | $3.00 | 3 | 
| Compute | VM\_XLARGE | VM\_XLARGE\_ON\_DEMAND\_HOUR | $4.00 | 4 | 

The above SKU Catalog shows that this service provider only has 1 service that offers 4 virtual machine SKUs at various list rates, *commitment discount* rates, and normalization factors. Each SKU's normalization factor classifies its relative size to its *commitment discount* rate. Usage-based *commitment discounts* with *commitment discount flexibility* can fully cover any combination of 1 or more SKUs where the sum of their normalization factor is less than or equal to the normalization factor of the *commitment discount*.

### 8.3.4.3 Scenario

- 1 no upfront *commitment discount* is purchased for 1 year (2023) for 1 VM\_XLARGE which has a normalization factor of 8.
- 2 VM\_MEDIUM resources run for 1 hour from 2023-01-01T00:00:00 to 2023-01-01T01:00:00 with a normalization factor of 4 for each.

### 8.3.4.4 Outcome

- 1 recurring, purchase record exists for 1 eligible "Normalized Hour" for a no upfront, *commitment discount* and incurs a $2.00 *BilledCost*.
- With *commitment discount flexibility*, 1 *commitment discount* for a VM\_XLARGE covers 2 VM\_MEDIUM resources within the corresponding *charge period* and incurs a $2.00 total *EffectiveCost*.
  - 1 *commitment discount* with a normalization factor of 8 covers 2 resources with normalization factors of 4 (i.e 4 + 4 = 8).