---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/appendix/commitment-discounts/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2010-02-08"
fingerprint: "266a746e7ce7f2d1"
---
# 8.2 Examples: Commitment Discounts

This appendix section defines the concept of a *commitment discount*. It then lays out a series of FOCUS dataset examples.

## 8.2.1 Overview

A *commitment discount* is a billing discount model that offers reduced rates on preselected *SKUs* in exchange for an obligated usage or spend amount over a specified *period*. *Commitment discounts* typically consist of purchase and usage records within cost and usage datasets.

Usage-based *commitment discounts* obligate a customer to a predetermined amount of usage over a specified *period*. In some cases, usage-based *commitment discounts* also feature *commitment discount flexibility* which may expand the types of *resources* that a *commitment discount* can cover. It is important to note when mixing *commitment discounts* with and without *commitment discount flexibility*, the CommitmentDiscountUnit should reflect this difference.

Spend-based *commitment discounts* obligate a customer to a predetermined amount of spend over a specified *period*. In the usage examples below, each *row* measures the monetary amount of the hourly commit consumed by the *commitment discount*, so the CommitmentDiscountUnit chosen is "USD", or the *billing currency*.

### 8.2.1.1 Purchasing

While customers are bound to the *period* of a *commitment discount*, service providers offer some or all of the following payment options before and/or during the *period*:

- *All Upfront* - The *commitment discount* is paid in full before the *period* begins.
- *No Upfront* - The *commitment discount* is paid on a repeated basis, typically over each *billing period* of the *period*.
- *Partial Upfront* - Some of the *commitment discount* is paid before the *period* begins, and the rest is paid repeatedly over the *period*.

For example, if a customer buys a 1-year, spend-based *commitment discount* with a $1.00 hourly commit and pays with the partial option, the *commitment discount's* payment consists of a one-time purchase in the beginning of the *period and* monthly recurring purchases. The one-time payment covers half of the annual commitment (Flexible Spend Plans are half, Resource Reservations are a portion of the cost), while the recurring payment covers the remaining half and is calculated based on the exact number of hours in each *billing period*:

1. *One-Time* - $4,380 (24 hours × 365 days × $1.00 × 0.5)
2. *Recurring* - $336.00 for February (672 hours in the month × $1.00 × 0.5)

### 8.2.1.2 Usage

Commitment discounts follow a "use-it-or-lose-it" model where the *amortization* of a *commitment discount's* purchase applies evenly to eligible *resources* over each *charge period* of the *period*.

For example, if a customer buys a spend-based *commitment discount* with a $1.00 hourly commit in January (31 days), only $1.00 is eligible for consumption for each hourly *charge period*. If a customer has eligible *resources* running during this *charge period*, an amount of up to $1.00 will be allocated to these *resources*. Conversely, if a customer does not have eligible *resources* running that fully take advantage of this $1.00 during this *charge period*, then some or all of this amount will go to waste.

## 8.2.2 Data Generator Scenarios

Below are tables listing some common commitment discount scenarios for a few prominent FOCUS data generators.

### 8.2.2.1 Data Generator Scenarios: Aura Web

| Scenario | What You'll Learn | 
|---|---|
| Resource Reservation - All Upfront | How a single large upfront purchase amortizes across usage rows. BilledCost=0 on usage rows; EffectiveCost carries the amortized value. Usage-based commitment ( `CommitmentDiscountCategory=Usage`). | 
| Resource Reservation - Partial Upfront | How partial upfront splits into two purchase rows: one `One-Time` and one `Recurring`. Demonstrates the hybrid payment model for Resource Reservations (RRs). | 
| Flexible Spend Plan - All Upfront | How Flexible Spend Plans (FSPs) differ from RRs: `CommitmentDiscountCategory=Spend` (dollar-based) instead of `Usage` (instance-based). Quantities measured in USD, not instance hours. | 
| Flexible Spend Plan - Partial Upfront | The partial upfront pattern applied to FSPs. Two purchase rows (one-time + recurring) mirror the RR partial model but with spend-based commitment fields. | 
| Flexible Spend Plan - No Upfront | The no-upfront model: only a `Recurring` purchase row, no initial capital outlay. Compare the higher effective rate against all-upfront and partial-upfront variants. | 
| Flexible Spend Plan - 100% Utilization with Overage | What happens when demand exceeds commitment capacity. Committed hours apply the effective unit price; overage hours spill to standard pricing at full list price ( `PricingCategory=Standard`). | 
| Flexible Spend Plan - 75% Utilization | Moderate underutilization: 18 hours `Used`, 6 hours `Unused`. Unused rows carry EffectiveCost with null resource fields, representing wasted spend. | 
| Flexible Spend Plan - 50% Utilization | Significant underutilization: 12 hours `Used`, 12 hours `Unused`. Half the commitment value is wasted - key pattern for identifying commitment right-sizing opportunities. | 
| Flexible Spend Plan - 0% Utilization | Worst case: commitment purchased but never applied. All 24 hours show `Unused` status. EffectiveCost accrues entirely as waste. | 

### 8.2.2.2 Data Generator Scenarios: CrestNode

| Scenario | What You'll Learn | 
|---|---|
| Resource Reservation - All Upfront | CrestNode's usage-based reservation model in FOCUS format. Compare structure and rates against Aura Web Resource Reservations. | 
| Resource Reservation - No Upfront | CrestNode no-upfront reservations with monthly recurring payments only. Note the higher effective rate vs all-upfront, reflecting the deferred-payment premium. | 
| Flexible Spend Plan - All Upfront | CrestNode's spend-based Flexible Spend Plan ( `CommitmentDiscountCategory=Spend`). Compare against CrestNode Resource Reservations and Aura Web Flexible Spend Plans. | 

### 8.2.2.3 Data Generator Scenarios: LatticeScale

| Scenario | What You'll Learn | 
|---|---|
| Resource Reservation - No Upfront | LatticeScale's usage-based commitment: `CommitmentDiscountCategory=Usage`, quantities in `Hours`. Monthly billing only (no upfront option). Deepest discount. | 
| Dynamic Compute Commitment - No Upfront | LatticeScale's spend-based commitment: `CommitmentDiscountCategory=Spend`, quantities in `USD`. Monthly recurring billing, no upfront payment. Compare against Aura Web and CrestNode. | 

## 8.2.3 Aura Web Resource Reservation - All Upfront - 100% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | All Upfront | 
| Commitment Discount Category | Usage | 
| Utilization | 100% | 
| Hours Generated | 24 | 
| Annual Commitment | $402,960.00 | 
| List Unit Price | $69.00/hour | 

### 8.2.3.1 Scenario Description

This example shows an **Aura Web Resource Reservation**, which is a commitment (with a Commitment Discount Category of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

### 8.2.3.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $402,960.00 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $1,104.00 | 
| **Total** | 25 | **$402,960.00** | **$1,104.00** | 

### 8.2.3.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.3.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 1 (commitment units) | 

**For usage-based commitments:** CommitmentDiscountQuantity represents the quantity of resources (e.g., instance hours), not a dollar amount. For a 1-hour reservation, CommitmentDiscountQuantity = 1.

#### 8.2.3.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $69.00 | 
| **ContractedUnitPrice** | Negotiated unit price | $69.00 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.3.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $402,960.00 | $0.00 | $402,960.00 | 
| **Used Row** | $0.00 | $46.00 | $69.00 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

### 8.2.3.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | One-Time | One-time upfront payment | 
| BilledCost | $402,960.00 | Full annual commitment payment | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 1 | One commitment unit purchased | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 8760.00 | Total commitment capacity for the 1-year term (1 instance-hr/hr × 8,760 hrs/yr) | 
| CommitmentDiscountUnit | Hours | Unit of commitment capacity (usage-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase | 

### 8.2.3.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $46.00 | Amortized cost (annual / hours) | 
| ListCost | $69.00 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 1 | Commitment units applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | auraweb:compute:us-east-1:123456789012:resource-reserv... | Links usage to purchase | 
| SkuId | AURAWEB-USEAST1-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

## 8.2.4 Aura Web Resource Reservation - Partial Upfront - 100% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | Partial Upfront | 
| Commitment Discount Category | Usage | 
| Utilization | 100% | 
| Hours Generated | 24 | 
| Annual Commitment | $440,014.80 | 
| List Unit Price | $75.35/hour | 

### 8.2.4.1 Scenario Description

This example shows an **Aura Web Resource Reservation**, which is a commitment (with a Commitment Discount Category of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **Partial Upfront** payment option combines an initial upfront payment with a reduced recurring monthly fee. This results in two Purchase rows: one One-Time for the upfront portion and one Recurring for the monthly fee, both with zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

### 8.2.4.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 2 | $236,884.68 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $1,205.52 | 
| **Total** | 26 | **$236,884.68** | **$1,205.52** | 

### 8.2.4.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.4.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 1 (commitment units) | 

**For usage-based commitments:** CommitmentDiscountQuantity represents the quantity of resources (e.g., instance hours), not a dollar amount. For a 1-hour reservation, CommitmentDiscountQuantity = 1.

#### 8.2.4.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $75.35 | 
| **ContractedUnitPrice** | Negotiated unit price | $75.35 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.4.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row (One-Time)** | $220,007.40 | $0.00 | $220,007.40 | 
| **Purchase Row (Recurring)** | $16,877.28 | $0.00 | $16,877.28 | 
| **Used Row** | $0.00 | $50.23 | $75.35 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

### 8.2.4.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | One-Time | One-time upfront payment | 
| BilledCost | $220,007.40 | Upfront portion (50% of annual commitment) | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 1 | One commitment unit purchased | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 8760.00 | Full commitment capacity for the 1-year term (1 instance-hr/hr × 8,760 hrs/yr) | 
| CommitmentDiscountUnit | Hours | Unit of commitment capacity (usage-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase | 

### 8.2.4.5 Recurring Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | Recurring | Monthly recurring fee | 
| BilledCost | $16,877.28 | Monthly portion (hourly rate / 2 × 672 hours in Feb) | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 1 | One commitment unit purchased | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 672.00 | Commitment capacity for Feb (1 instance-hr/hr × 672 hrs) | 
| CommitmentDiscountUnit | Hours | Unit of commitment capacity (usage-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-RECURRING | Price point for recurring purchase | 

### 8.2.4.6 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $50.23 | Amortized cost (annual / hours) | 
| ListCost | $75.35 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 1 | Commitment units applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | auraweb:compute:us-east-1:123456789012:resource-reserv... | Links usage to purchase | 
| SkuId | AURAWEB-USEAST1-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

## 8.2.5 Aura Web Flexible Spend Plan - All Upfront - 100% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | All Upfront | 
| Commitment Discount Category | Spend | 
| Utilization | 100% | 
| Hours Generated | 24 | 
| Annual Commitment | $628,004.40 | 
| List Unit Price | $107.54/hour | 

### 8.2.5.1 Scenario Description

This example shows an **Aura Web Flexible Spend Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

### 8.2.5.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $628,004.40 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $1,720.56 | 
| **Total** | 25 | **$628,004.40** | **$1,720.56** | 

### 8.2.5.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.5.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 71.69 (USD) | 

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $71.69/hour commitment, this value is $71.69.

#### 8.2.5.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $107.54 | 
| **ContractedUnitPrice** | Negotiated unit price | $107.54 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.5.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $628,004.40 | $0.00 | $628,004.40 | 
| **Used Row** | $0.00 | $71.69 | $107.54 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

### 8.2.5.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | One-Time | One-time upfront payment | 
| BilledCost | $628,004.40 | Full annual commitment payment | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 628,004.40 | Total commitment in USD (PricingUnit = USD) | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 628,004.40 | Full annual commitment ($71.69/hr × 8,760 hrs) | 
| CommitmentDiscountUnit | USD | Unit of commitment capacity (spend-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase | 

### 8.2.5.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $71.69 | Amortized cost (annual / hours) | 
| ListCost | $107.54 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 71.69 | Hourly commitment spend applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | auraweb:flexspend::123456789012:flexspendplan/fsp-... | Links usage to purchase | 
| SkuId | AURAWEB-USEAST1-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

## 8.2.6 Aura Web Flexible Spend Plan - Partial Upfront - 100% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | Partial Upfront | 
| Commitment Discount Category | Spend | 
| Utilization | 100% | 
| Hours Generated | 24 | 
| Annual Commitment | $447,986.40 | 
| List Unit Price | $76.71/hour | 

### 8.2.6.1 Scenario Description

This example shows an **Aura Web Flexible Spend Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **Partial Upfront** payment option combines an initial upfront payment with a reduced recurring monthly fee. This results in two Purchase rows: one One-Time for the upfront portion and one Recurring for the monthly fee, both with zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

### 8.2.6.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 2 | $241,176.24 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $1,227.36 | 
| **Total** | 26 | **$241,176.24** | **$1,227.36** | 

### 8.2.6.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.6.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 51.14 (USD) | 

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $51.14/hour commitment, this value is $51.14.

#### 8.2.6.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $76.71 | 
| **ContractedUnitPrice** | Negotiated unit price | $76.71 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.6.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row (One-Time)** | $223,993.20 | $0.00 | $223,993.20 | 
| **Purchase Row (Recurring)** | $17,183.04 | $0.00 | $17,183.04 | 
| **Used Row** | $0.00 | $51.14 | $76.71 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

### 8.2.6.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | One-Time | One-time upfront payment | 
| BilledCost | $223,993.20 | Upfront portion (50% of annual commitment) | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 223,993.20 | Upfront portion in USD (PricingUnit = USD) | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 447,986.40 | Full annual commitment capacity ($51.14/hr × 8,760 hrs) | 
| CommitmentDiscountUnit | USD | Unit of commitment capacity (spend-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase | 

### 8.2.6.5 Recurring Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | Recurring | Monthly recurring fee | 
| BilledCost | $17,183.04 | Monthly portion (hourly rate / 2 × 672 hours in Feb) | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 17,183.04 | Monthly portion in USD (PricingUnit = USD) | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 34,366.08 | Full monthly commitment capacity ($51.14/hr × 672 hrs) | 
| CommitmentDiscountUnit | USD | Unit of commitment capacity (spend-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-RECURRING | Price point for recurring purchase | 

### 8.2.6.6 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $51.14 | Amortized cost (annual / hours) | 
| ListCost | $76.71 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 51.14 | Hourly commitment spend applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | auraweb:flexspend::123456789012:flexspendplan/fsp-... | Links usage to purchase | 
| SkuId | AURAWEB-USEAST1-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

## 8.2.7 Aura Web Flexible Spend Plan - No Upfront - 100% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | No Upfront | 
| Commitment Discount Category | Spend | 
| Utilization | 100% | 
| Hours Generated | 24 | 
| Annual Commitment | $462,966.00 | 
| List Unit Price | $79.28/hour | 

### 8.2.7.1 Scenario Description

This example shows an **Aura Web Flexible Spend Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **No Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

### 8.2.7.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $35,515.20 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $1,268.40 | 
| **Total** | 25 | **$35,515.20** | **$1,268.40** | 

### 8.2.7.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.7.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 52.85 (USD) | 

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $52.85/hour commitment, this value is $52.85.

#### 8.2.7.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $79.28 | 
| **ContractedUnitPrice** | Negotiated unit price | $79.28 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.7.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $35,515.20 | $0.00 | $35,515.20 | 
| **Used Row** | $0.00 | $52.85 | $79.28 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

### 8.2.7.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | Recurring | Monthly recurring fee | 
| BilledCost | $35,515.20 | Monthly recurring payment (hourly rate × 672 hours in Feb) | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 35,515.20 | Total commitment in USD (PricingUnit = USD) | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 35,515.20 | Commitment capacity for Feb ($52.85/hr × 672 hrs) | 
| CommitmentDiscountUnit | USD | Unit of commitment capacity (spend-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-MONTHLY | Price point for recurring purchase | 

### 8.2.7.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $52.85 | Amortized cost (annual / hours) | 
| ListCost | $79.28 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 52.85 | Hourly commitment spend applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | auraweb:flexspend::123456789012:flexspendplan/fsp-... | Links usage to purchase | 
| SkuId | AURAWEB-USEAST1-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

## 8.2.8 Aura Web Flexible Spend Plan - All Upfront - 100% Utilization with Overage

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | All Upfront | 
| Commitment Discount Category | Spend | 
| Utilization | 100% (with overage to standard pricing) | 
| Hours Generated | 24 committed + 12 standard overflow | 
| Annual Commitment | $211,992.00 | 
| List Unit Price | $36.30/hour | 

### 8.2.8.1 Scenario Description

This example shows an **Aura Web Flexible Spend Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **100% utilization with overage** where demand exceeds commitment capacity. The 24 Used rows represent full utilization of the commitment. The 12 Standard rows represent compute usage beyond the commitment that spills to standard pricing. Standard pricing rows have no CommitmentDiscountStatus, PricingCategory='Standard', and BilledCost=EffectiveCost at the full list price.

### 8.2.8.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $211,992.00 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $580.80 | 
| Usage (Standard) | 12 | $435.60 | $435.60 | 
| **Total** | 37 | **$212,427.60** | **$1,016.40** | 

### 8.2.8.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.8.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 24.20 (USD) | 

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $24.20/hour commitment, this value is $24.20.

#### 8.2.8.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | Standard | 
|---|---|---|---|
| **ListUnitPrice** | List (public) unit price | $36.30 | $36.30 | 
| **ContractedUnitPrice** | Negotiated unit price | $36.30 | $36.30 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.8.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $211,992.00 | $0.00 | $211,992.00 | 
| **Used Row** | $0.00 | $24.20 | $36.30 | 
| **Standard Row** | $36.30 | $36.30 | $36.30 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.
- **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

### 8.2.8.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | One-Time | One-time upfront payment | 
| BilledCost | $211,992.00 | Full annual commitment payment | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 211,992.00 | Total commitment in USD (PricingUnit = USD) | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 211,992.00 | Full annual commitment ($24.20/hr × 8,760 hrs) | 
| CommitmentDiscountUnit | USD | Unit of commitment capacity (spend-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase | 

### 8.2.8.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $24.20 | Amortized cost (annual / hours) | 
| ListCost | $36.30 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 24.20 | Hourly commitment spend applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | auraweb:flexspend::123456789012:flexspendplan/fsp-... | Links usage to purchase | 
| SkuId | AURAWEB-USEAST1-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

### 8.2.8.6 Standard Pricing Usage Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute consumption (standard pricing) | 
| PricingCategory | Standard | No discount applied | 
| BilledCost | $36.30 | Same as ListCost, no negotiation/commitments | 
| EffectiveCost | $36.30 | Same as BilledCost, no pre/post payments | 
| ListCost | $36.30 | Public, non-negotiated cost | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours consumed | 
| CommitmentDiscountQuantity | null | **No commitment applied** | 
| CommitmentDiscountStatus | null | No commitment | 
| CommitmentDiscountId | null | No associated commitment | 
| ContractedUnitPrice | $36.30 | Equals ListUnitPrice (no negotiated discount) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-ONDEMAND | Standard (on-demand) resource SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-ONDEMAND-STANDARD | Price point for standard pricing | 

## 8.2.9 Aura Web Flexible Spend Plan - All Upfront - 75% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | All Upfront | 
| Commitment Discount Category | Spend | 
| Utilization | 75% | 
| Hours Generated | 24 | 
| Annual Commitment | $459,024.00 | 
| List Unit Price | $78.60/hour | 

### 8.2.9.1 Scenario Description

This example shows an **Aura Web Flexible Spend Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **underutilization** at 75% where only 18 of 24 commitment hours are consumed. The remaining 6 hours appear as 'Unused' rows with CommitmentDiscountStatus='Unused'. These unused rows still have EffectiveCost to reflect the wasted commitment value.

### 8.2.9.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $459,024.00 | $0.00 | 
| Usage (Used) | 18 | $0.00 | $943.20 | 
| Usage (Unused) | 6 | $0.00 | $314.40 | 
| **Total** | 25 | **$459,024.00** | **$1,257.60** | 

### 8.2.9.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.9.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 52.40 (USD) | 

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $52.40/hour commitment, this value is $52.40.

#### 8.2.9.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $78.60 | 
| **ContractedUnitPrice** | Negotiated unit price | $78.60 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.9.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $459,024.00 | $0.00 | $459,024.00 | 
| **Used Row** | $0.00 | $52.40 | $78.60 | 
| **Unused Row** | $0.00 | $52.40 | $52.40 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.
- **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.

### 8.2.9.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | One-Time | One-time upfront payment | 
| BilledCost | $459,024.00 | Full annual commitment payment | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 459,024.00 | Total commitment in USD (PricingUnit = USD) | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 459,024.00 | Full annual commitment ($52.40/hr × 8,760 hrs) | 
| CommitmentDiscountUnit | USD | Unit of commitment capacity (spend-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase | 

### 8.2.9.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $52.40 | Amortized cost (annual / hours) | 
| ListCost | $78.60 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 52.40 | Hourly commitment spend applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | auraweb:flexspend::123456789012:flexspendplan/fsp-... | Links usage to purchase | 
| SkuId | AURAWEB-USEAST1-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

### 8.2.9.6 Unused Commitment Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Represents commitment capacity | 
| BilledCost | $0.00 | No additional billing (already paid at purchase) | 
| EffectiveCost | $52.40 | **Wasted value** - lost commitment | 
| PricingQuantity | 52.40 | Hourly commitment in USD (PricingUnit = USD) | 
| ListCost | $52.40 | $1.00 × 52.40 USD | 
| ConsumedQuantity | null | **No resource consumed** | 
| CommitmentDiscountQuantity | 52.40 | Commitment wasted | 
| CommitmentDiscountStatus | Unused | Commitment not utilized | 
| ResourceId | auraweb:flexspend::123456789012:flexspendplan/fsp-abc123def456 | must match CommitmentDiscountId (no resource used) | 
| ResourceName | Compute Flexible Spend Plan | Carried from Purchase row (no resource consumed) | 
| ResourceType | Commitment | Carried from Purchase row (no resource consumed) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | must match Purchase row (no resource consumed) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | must match Purchase row | 

For spend-based unused rows, PricingUnit is USD and PricingQuantity is the hourly commitment amount. ListCost = ListUnitPrice ($1.00) × PricingQuantity, which equals the wasted commitment dollars per hour.

## 8.2.10 Aura Web Flexible Spend Plan - All Upfront - 50% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | All Upfront | 
| Commitment Discount Category | Spend | 
| Utilization | 50% | 
| Hours Generated | 24 | 
| Annual Commitment | $693,003.60 | 
| List Unit Price | $118.67/hour | 

### 8.2.10.1 Scenario Description

This example shows an **Aura Web Flexible Spend Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **underutilization** at 50% where only 12 of 24 commitment hours are consumed. The remaining 12 hours appear as 'Unused' rows with CommitmentDiscountStatus='Unused'. These unused rows still have EffectiveCost to reflect the wasted commitment value.

### 8.2.10.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $693,003.60 | $0.00 | 
| Usage (Used) | 12 | $0.00 | $949.32 | 
| Usage (Unused) | 12 | $0.00 | $949.32 | 
| **Total** | 25 | **$693,003.60** | **$1,898.64** | 

### 8.2.10.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.10.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 79.11 (USD) | 

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $79.11/hour commitment, this value is $79.11.

#### 8.2.10.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $118.67 | 
| **ContractedUnitPrice** | Negotiated unit price | $118.67 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.10.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $693,003.60 | $0.00 | $693,003.60 | 
| **Used Row** | $0.00 | $79.11 | $118.67 | 
| **Unused Row** | $0.00 | $79.11 | $79.11 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.
- **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.

### 8.2.10.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | One-Time | One-time upfront payment | 
| BilledCost | $693,003.60 | Full annual commitment payment | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 693,003.60 | Total commitment in USD (PricingUnit = USD) | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 693,003.60 | Full annual commitment ($79.11/hr × 8,760 hrs) | 
| CommitmentDiscountUnit | USD | Unit of commitment capacity (spend-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase | 

### 8.2.10.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $79.11 | Amortized cost (annual / hours) | 
| ListCost | $118.67 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 79.11 | Hourly commitment spend applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | auraweb:flexspend::123456789012:flexspendplan/fsp-... | Links usage to purchase | 
| SkuId | AURAWEB-USEAST1-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

### 8.2.10.6 Unused Commitment Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Represents commitment capacity | 
| BilledCost | $0.00 | No additional billing (already paid at purchase) | 
| EffectiveCost | $79.11 | **Wasted value** - lost commitment | 
| PricingQuantity | 79.11 | Hourly commitment in USD (PricingUnit = USD) | 
| ListCost | $79.11 | $1.00 × 79.11 USD | 
| ConsumedQuantity | null | **No resource consumed** | 
| CommitmentDiscountQuantity | 79.11 | Commitment wasted | 
| CommitmentDiscountStatus | Unused | Commitment not utilized | 
| ResourceId | auraweb:flexspend::123456789012:flexspendplan/fsp-abc123def456 | must match CommitmentDiscountId (no resource used) | 
| ResourceName | Compute Flexible Spend Plan | Carried from Purchase row (no resource consumed) | 
| ResourceType | Commitment | Carried from Purchase row (no resource consumed) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | must match Purchase row (no resource consumed) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | must match Purchase row | 

For spend-based unused rows, PricingUnit is USD and PricingQuantity is the hourly commitment amount. ListCost = ListUnitPrice ($1.00) × PricingQuantity, which equals the wasted commitment dollars per hour.

## 8.2.11 Aura Web Flexible Spend Plan - All Upfront - 0% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | All Upfront | 
| Commitment Discount Category | Spend | 
| Utilization | 0% | 
| Hours Generated | 24 | 
| Annual Commitment | $353,028.00 | 
| List Unit Price | $60.45/hour | 

### 8.2.11.1 Scenario Description

This example shows an **Aura Web Flexible Spend Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **zero utilization** where the commitment is purchased but no resources are consumed. All usage rows have CommitmentDiscountStatus='Unused', representing wasted commitment capacity. The EffectiveCost on these rows reflects the cost of unused commitment that cannot be recovered.

### 8.2.11.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $353,028.00 | $0.00 | 
| Usage (Unused) | 24 | $0.00 | $967.20 | 
| **Total** | 25 | **$353,028.00** | **$967.20** | 

### 8.2.11.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.11.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 40.30 (USD, hourly rate) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 40.30 (USD) | 

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For this commitment, the value equals the hourly dollar commitment.

#### 8.2.11.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $1.00 | 
| **ContractedUnitPrice** | Negotiated unit price | $1.00 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices. For spend-based purchase and unused rows, PricingUnit is USD and ListUnitPrice is $1.00, because you are fundamentally purchasing a block of dollars.

#### 8.2.11.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $353,028.00 | $0.00 | $353,028.00 | 
| **Unused Row** | $0.00 | $40.30 | $40.30 | 

This scenario has no Used or Standard rows because utilization is 0% and no resources were consumed.

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.

### 8.2.11.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | One-Time | One-time upfront payment | 
| BilledCost | $353,028.00 | Full annual commitment payment | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 353,028.00 | Total commitment in USD (PricingUnit = USD) | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 353,028.00 | Full annual commitment ($40.30/hr × 8,760 hrs) | 
| CommitmentDiscountUnit | USD | Unit of commitment capacity (spend-based) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase | 

### 8.2.11.5 Unused Commitment Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Represents commitment capacity | 
| BilledCost | $0.00 | No additional billing (already paid at purchase) | 
| EffectiveCost | $40.30 | **Wasted value** - lost commitment | 
| PricingQuantity | 40.30 | Hourly commitment in USD (PricingUnit = USD) | 
| ListCost | $40.30 | $1.00 × 40.30 USD | 
| ConsumedQuantity | null | **No resource consumed** | 
| CommitmentDiscountQuantity | 40.30 | Commitment wasted | 
| CommitmentDiscountStatus | Unused | Commitment not utilized | 
| ResourceId | auraweb:flexspend::123456789012:flexspendplan/fsp-abc123def456 | must match CommitmentDiscountId (no resource used) | 
| ResourceName | Compute Flexible Spend Plan | Carried from Purchase row (no resource consumed) | 
| ResourceType | Commitment | Carried from Purchase row (no resource consumed) | 
| SkuId | AURAWEB-USEAST1-COMPUTE-PURCHASE | must match Purchase row (no resource consumed) | 
| SkuPriceId | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | must match Purchase row (no resource consumed) | 

For spend-based unused rows, PricingUnit is USD and PricingQuantity is the hourly commitment amount. ListCost = ListUnitPrice ($1.00) × PricingQuantity, which equals the wasted commitment dollars per hour.

## 8.2.12 CrestNode Resource Reservation - All Upfront - 100% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | All Upfront | 
| Commitment Discount Category | Usage | 
| Utilization | 100% | 
| Hours Generated | 24 | 
| Annual Commitment | $358,021.20 | 
| List Unit Price | $61.31/hour | 

### 8.2.12.1 Scenario Description

This example shows a **CrestNode Resource Reservation**, which is a commitment (with a Commitment Discount Category of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

### 8.2.12.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $358,021.20 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $980.88 | 
| **Total** | 25 | **$358,021.20** | **$980.88** | 

### 8.2.12.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.12.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 1 (commitment units) | 

**For usage-based commitments:** CommitmentDiscountQuantity represents the quantity of resources (e.g., instance hours), not a dollar amount. For a 1-hour reservation, CommitmentDiscountQuantity = 1.

#### 8.2.12.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $61.31 | 
| **ContractedUnitPrice** | Negotiated unit price | $61.31 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.12.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $358,021.20 | $0.00 | $358,021.20 | 
| **Used Row** | $0.00 | $40.87 | $61.31 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

### 8.2.12.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | One-Time | One-time upfront payment | 
| BilledCost | $358,021.20 | Full annual commitment payment | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 1 | One commitment unit purchased | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 8760.00 | Total commitment capacity for the 1-year term (1 instance-hr/hr × 8,760 hrs/yr) | 
| CommitmentDiscountUnit | Hours | Unit of commitment capacity (usage-based) | 
| SkuId | CRESTNODE-EASTUS-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | CRESTNODE-EASTUS-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase | 

### 8.2.12.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $40.87 | Amortized cost (annual / hours) | 
| ListCost | $61.31 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 1 | Commitment units applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | crestnode:compute:eastus:f0e9d8c7-b6a5-4321-0987-654321... | Links usage to purchase | 
| SkuId | CRESTNODE-EASTUS-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | CRESTNODE-EASTUS-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

## 8.2.13 CrestNode Resource Reservation - No Upfront - 100% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | No Upfront | 
| Commitment Discount Category | Usage | 
| Utilization | 100% | 
| Hours Generated | 24 | 
| Annual Commitment | $664,008.00 | 
| List Unit Price | $113.70/hour | 

### 8.2.13.1 Scenario Description

This example shows a **CrestNode Resource Reservation**, which is a commitment (with a Commitment Discount Category of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **No Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

### 8.2.13.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $55,334.00 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $1,819.20 | 
| **Total** | 25 | **$55,334.00** | **$1,819.20** | 

### 8.2.13.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.13.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 1 (commitment units) | 

**For usage-based commitments:** CommitmentDiscountQuantity represents the quantity of resources (e.g., instance hours), not a dollar amount. For a 1-hour reservation, CommitmentDiscountQuantity = 1.

#### 8.2.13.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $113.70 | 
| **ContractedUnitPrice** | Negotiated unit price | $113.70 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.13.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $55,334.00 | $0.00 | $55,334.00 | 
| **Used Row** | $0.00 | $75.80 | $113.70 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

### 8.2.13.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | Recurring | Monthly recurring fee | 
| BilledCost | $55,334.00 | Monthly recurring payment (annual / 12) | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 1 | One commitment unit purchased | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 672.00 | Commitment capacity for Feb (1 instance-hr/hr × 672 hrs) | 
| CommitmentDiscountUnit | Hours | Unit of commitment capacity (usage-based) | 
| SkuId | CRESTNODE-EASTUS-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | CRESTNODE-EASTUS-COMPUTE-PURCHASE-MONTHLY | Price point for recurring purchase | 

### 8.2.13.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $75.80 | Amortized cost (annual / hours) | 
| ListCost | $113.70 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 1 | Commitment units applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | crestnode:compute:eastus:f0e9d8c7-b6a5-4321-0987-654321... | Links usage to purchase | 
| SkuId | CRESTNODE-EASTUS-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | CRESTNODE-EASTUS-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

## 8.2.14 CrestNode Flexible Spend Plan - All Upfront - 100% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | All Upfront | 
| Commitment Discount Category | Spend | 
| Utilization | 100% | 
| Hours Generated | 24 | 
| Annual Commitment | $462,002.40 | 
| List Unit Price | $79.11/hour | 

### 8.2.14.1 Scenario Description

This example shows a **CrestNode Flexible Spend Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

### 8.2.14.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $462,002.40 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $1,265.76 | 
| **Total** | 25 | **$462,002.40** | **$1,265.76** | 

### 8.2.14.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.14.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 52.74 (USD) | 

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $52.74/hour commitment, this value is $52.74.

#### 8.2.14.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $79.11 | 
| **ContractedUnitPrice** | Negotiated unit price | $79.11 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.14.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $462,002.40 | $0.00 | $462,002.40 | 
| **Used Row** | $0.00 | $52.74 | $79.11 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

### 8.2.14.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | One-Time | One-time upfront payment | 
| BilledCost | $462,002.40 | Full annual commitment payment | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 462,002.40 | Total commitment in USD (PricingUnit = USD) | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 462,002.40 | Full annual commitment ($52.74/hr × 8,760 hrs) | 
| CommitmentDiscountUnit | USD | Unit of commitment capacity (spend-based) | 
| SkuId | CRESTNODE-EASTUS-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | CRESTNODE-EASTUS-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase | 

### 8.2.14.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $52.74 | Amortized cost (annual / hours) | 
| ListCost | $79.11 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 52.74 | Hourly commitment spend applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | crestnode:compute:eastus:f0e9d8c7-b6a5-4321-0987-654321... | Links usage to purchase | 
| SkuId | CRESTNODE-EASTUS-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | CRESTNODE-EASTUS-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

## 8.2.15 LatticeScale Resource Reservation - No Upfront - 100% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | No Upfront | 
| Commitment Discount Category | Usage | 
| Utilization | 100% | 
| Hours Generated | 24 | 
| Annual Commitment | $257,982.00 | 
| List Unit Price | $44.18/hour | 

### 8.2.15.1 Scenario Description

This example shows a **LatticeScale Resource Reservation**, which is a commitment (with a Commitment Discount Category of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **No Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. LatticeScale commitments are billed monthly with no upfront payment option. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

### 8.2.15.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $19,790.40 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $706.80 | 
| **Total** | 25 | **$19,790.40** | **$706.80** | 

### 8.2.15.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.15.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 1 (commitment units) | 

**For usage-based commitments:** CommitmentDiscountQuantity represents the quantity of resources (e.g., instance hours), not a dollar amount. For a 1-hour reservation, CommitmentDiscountQuantity = 1.

#### 8.2.15.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $44.18 | 
| **ContractedUnitPrice** | Negotiated unit price | $44.18 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.15.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $19,790.40 | $0.00 | $19,790.40 | 
| **Used Row** | $0.00 | $29.45 | $44.18 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

### 8.2.15.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | Recurring | Monthly recurring fee | 
| BilledCost | $19,790.40 | Monthly fee (hourly rate × 672 hours in Feb) | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 1 | One commitment unit purchased | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 672.00 | Commitment capacity for Feb (1 instance-hr/hr × 672 hrs) | 
| CommitmentDiscountUnit | Hours | Unit of commitment capacity (usage-based) | 
| SkuId | LATTICESCALE-USCENTRAL1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | LATTICESCALE-USCENTRAL1-COMPUTE-PURCHASE-MONTHLY | Price point for recurring purchase | 

### 8.2.15.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $29.45 | Amortized cost (annual / hours) | 
| ListCost | $44.18 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 1 | Commitment units applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | latticescale:compute:us-central1:proj-123456:commitment-dis... | Links usage to purchase | 
| SkuId | LATTICESCALE-USCENTRAL1-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | LATTICESCALE-USCENTRAL1-COMPUTE-USAGE-COMMITTED | Price point for committed usage | 

## 8.2.16 LatticeScale Dynamic Compute Commitment - No Upfront - 100% Utilization

| Parameter | Value | 
|---|---|
| Scenario Type | commitment | 
| Payment Model | No Upfront | 
| Commitment Discount Category | Spend | 
| Utilization | 100% | 
| Hours Generated | 24 | 
| Annual Commitment | $553,018.80 | 
| List Unit Price | $94.70/hour | 

### 8.2.16.1 Scenario Description

This example shows a **LatticeScale Dynamic Compute Commitment**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **No Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. LatticeScale commitments are billed monthly with no upfront payment option. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

### 8.2.16.2 Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type | Count | BilledCost | EffectiveCost | 
|---|---|---|---|
| Purchase | 1 | $42,423.36 | $0.00 | 
| Usage (Used) | 24 | $0.00 | $1,515.12 | 
| **Total** | 25 | **$42,423.36** | **$1,515.12** | 

### 8.2.16.3 Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

#### 8.2.16.3.1 Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column | Purpose | When Populated | Typical Value | 
|---|---|---|---|
| **PricingQuantity** | Quantity used for pricing calculation | All priced rows | 1 (per hour/unit) | 
| **ConsumedQuantity** | Actual resource consumption | Usage rows with resources | 1 (hours consumed) | 
| **CommitmentDiscountQuantity** | Commitment capacity applied | Rows with commitment discount | 63.13 (USD) | 

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $63.13/hour commitment, this value is $63.13.

#### 8.2.16.3.2 Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column | Purpose | Commitment-Covered | 
|---|---|---|
| **ListUnitPrice** | List (public) unit price | $94.70 | 
| **ContractedUnitPrice** | Negotiated unit price | $94.70 | 

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

#### 8.2.16.3.3 Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario | BilledCost | EffectiveCost | ListCost | 
|---|---|---|---|
| **Purchase Row** | $42,423.36 | $0.00 | $42,423.36 | 
| **Used Row** | $0.00 | $63.13 | $94.70 | 

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

### 8.2.16.4 Purchase Row Details

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Purchase | Commitment purchase transaction | 
| ChargeFrequency | Recurring | Monthly recurring fee | 
| BilledCost | $42,423.36 | Monthly fee (hourly rate × 672 hours in Feb) | 
| EffectiveCost | $0.00 | **must be 0** - cost is amortized to usage rows | 
| PricingQuantity | 42,423.36 | Total commitment in USD (PricingUnit = USD) | 
| CommitmentDiscountStatus | null | Status only applies to usage rows | 
| CommitmentDiscountQuantity | 42,423.36 | Commitment capacity for Feb ($63.13/hr × 672 hrs) | 
| CommitmentDiscountUnit | USD | Unit of commitment capacity (spend-based) | 
| SkuId | LATTICESCALE-USCENTRAL1-COMPUTE-PURCHASE | Commitment purchase SKU | 
| SkuPriceId | LATTICESCALE-USCENTRAL1-COMPUTE-PURCHASE-MONTHLY | Price point for recurring purchase | 

### 8.2.16.5 Usage Row Details (Commitment-Covered)

| Column | Value | Explanation | 
|---|---|---|
| ChargeCategory | Usage | Compute resource consumption | 
| PricingCategory | Committed | Priced under commitment discount | 
| BilledCost | $0.00 | **must be 0** - covered by commitment | 
| EffectiveCost | $63.13 | Amortized cost (annual / hours) | 
| ListCost | $94.70 | What you would have paid at list price | 
| PricingQuantity | 1 | Units priced | 
| ConsumedQuantity | 1 | Hours used | 
| CommitmentDiscountQuantity | 63.13 | Hourly commitment spend applied | 
| CommitmentDiscountStatus | Used | Commitment applied | 
| CommitmentDiscountId | latticescale:compute:us-central1:proj-123456:commitment-dis... | Links usage to purchase | 
| SkuId | LATTICESCALE-USCENTRAL1-COMPUTE-USAGE | Resource usage SKU (differs from Purchase) | 
| SkuPriceId | LATTICESCALE-USCENTRAL1-COMPUTE-USAGE-COMMITTED | Price point for committed usage |