---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/appendix/saas-examples/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "2760547a44a373e1"
---
# 8.11 Examples: SaaS

The following section contains examples of how SaaS data generators may implement the FOCUS specification. SaaS data generator implementations will vary on the level of detail available in their data, contract terms, purchasing options, and other factors.

## 8.11.1 Simple SaaS Agreements

Many SaaS providers provide simple contract terms, therefore don't need to support complex scenarios like spend commitments or pricing strategies in their billing data.

The scenarios described below illustrate how a Cost and Usage *FOCUS dataset* should look for simple SaaS agreement scenarios (these scenarios may not be specific to SaaS agreements only).

### 8.11.1.1 Scenario A1: Invoice Up-Front for a Purchase of a Service

PipelCRM allows its customers to purchase their service for a term (in this case, a year) for a $10,000. PipelCRM provides Acme Corp with a single invoice for their usage. PipelCRM does not provide detailed cost and usage reports to Acme Corp throughout the Charge Period after the initial purchase.

Given that PipelCRM does not charge based on or track usage, its usage details are irrelevant to this scenario.

Note the following details in the example dataset:

- The Charge Period is April 1st 2025 - April 1st 2026. The Billing Period is the month of April 2025 (when the licenses were ordered) and therefore will appear in the April invoice.
- A single charge representing the total payment for the 12-month agreement ($10,000) is charged in the first invoice. BilledCost and EffectiveCost are realized in the same record since detailed usage records will not be provided during the 12-month period to realize amortized portions of this up-front payment.
- The single charge record does not include a List Unit Price, Pricing Quantity, or SKU-related information. Alternatively, the Pricing Quantity could have been set to 1, and the List Unit Price could be the same as the total charge.

### 8.11.1.2 Scenario A2: Invoice Up-Front for a Quantity of a Service

PipelCRM offers its customer the ability to purchase a fixed quantity of licenses for their service. PipelCRM provides Acme Corp with a single invoice for their usage. PipelCRM does not provide detailed cost and usage reports to Acme Corp throughout the Charge Period after the initial purchase.

On April 1st, 2025, PipelCRM executes a contract and invoices Acme Corp $50,000 (Billed Cost) for a Charge Period of April 1st 2025 to April 1st 2026. As there is no negotiated discount, List Cost of the purchase is also $50,000.

Note the following details in the example dataset:

- The Charge Period is April 1st 2025 to April 1st 2026. The Billing Period is the month of April 2025 (when the licenses were ordered) and therefore will appear in the April invoice.
- A single charge representing the total payment for the 12-month agreement is charged in the first invoice. Billed Cost and Effective Cost are both realized in the same record since detailed usage records will not be provided during the 12-month period to realize amortized portions of this up-front payment.
- The single charge provided includes a ListUnitPrice for the licenses and a Pricing Quantity.

### 8.11.1.3 Scenario A3: Additional Purchase Records Provided in the SaaS Data Generator's FOCUS Dataset

On June 1st 2025 PipelCRM provides the following records due to Acme Corp's $1,000 mid-contract purchase of an additional 10 licenses for the same Charge Period (April 1st 2025 to April 1st 2026).

Note the following additional details in the example dataset:

- The Charge Period is still April 1st 2025 to April 1st 2026. The Billing Period is now the month of June 2025 (when the additional licenses were ordered) and therefore will appear in the June 2025 invoice.

### 8.11.1.4 Scenario B: Billed in Arrears for a Quantity of a Service

Similar to Scenario A above, PipelCRM offers its customer the ability to purchase their service with a fixed quantity of licenses. However, in Scenario B, PipelCRM issues the invoice at the end of the usage period.

On April 1st, 2026, PipelCRM invoices Acme Corp $50,000 (Billed Cost) for the Charge Period of April 1st 2025 to April 1st 2026. As there is no negotiated discount, List Cost of the purchase is also $50,000.

Note the following additional details in the example dataset:

- The Charge Period is April 1st 2025 to April 1st 2026. The Billing Period is now the month of March 2026 (since this charge is invoiced as of the last month of the Charge Period).

### 8.11.1.5 Scenario C: Simple SaaS Agreement with Monthly Billing

Like Scenario A2 above, PipelCRM offers its customers the ability to purchase their service with a fixed quantity of licenses. However, in Scenario C, PipelCRM issues invoices at the end of each month (usage period). For this scenario, contract terms additionally include the following terms:

- PipelCRM charges users monthly for the licenses that were consumed in that Billing Period
- The licenses are charged at $20 per license per month

Acme Corp's consumption looks like this:

- In April 2025, Acme Corp uses 505 licenses
- In May 2025, Acme Corp uses 650 licenses
- In June 2025, Acme Corp uses 635 licenses

Note the following additional details in the example dataset:

- The Charge Period and Billing Period are April 1st, 2025, to May 1st, 2025, for the first month. Subsequent months increment the Charge Period and Billing Period by one month to match the month the charges are incurred.
- Billed Cost and Effective Cost are the same value since there is no up-front payment to amortize

## 8.11.2 SaaS Spend Agreements

Many SaaS service providers support billing models that allow (or in some cases require) consumers to agree to an amount to spend over a period. In some cases, customers receive a negotiated discount for usage during that period in exchange for the spend agreement. Spend agreements can have different payment models like billing in arrears or pre-paid contracts and may impose minimum spend requirements for parts of the agreement.

The scenarios described below illustrate how a Cost and Usage *FOCUS dataset* should look for various spend agreement scenarios.

### 8.11.2.1 Baseline Scenario

The following baseline conditions apply to the scenarios described below:

- Acme Corp has signed an agreement with SaaS service provider StoreStack to use their database services
- On April 1 2025, Acme Corp agrees to spend $1200 (post-discounts) in the upcoming 12-months
- Acme Corp receives a 20% negotiated discount in return for the commitment
- StoreStack calculates the spend counted against the agreements after discounts (like the negotiated discounts). Other service providers may use the cost after discounts i.e., using List Cost for calculating the spend commitment.

### 8.11.2.2 Scenario A: Billed in Arrears

For this scenario A, contract includes the following terms in addition to the baseline scenario mentioned above:

- All charges will be billed in arrears at a monthly frequency

#### 8.11.2.2.1 Scenario A1: Billed in Arrears with No Minimum Spend Requirement Per Month

For this scenario, contract additionally includes the following terms:

- Committed spend can be used anytime within the 1-year commitment period.

Acme Corp's consumption looks like this:

- In the first month, Acme Corp uses $48 of services (4 server hours). This usage has a List Cost of $60 (before discounts)
- In the following 2 months, Acme Corp has some more usage
- For the final 9 months, Acme Corp does not use StoreStack services

Note the following details in the example dataset:

- A single charge representing the total unused amount from the 12-month agreement is charged during the final month of the 12-month commitment period

#### 8.11.2.2.2 Scenario A2: Billed in Arrears with a Minimum Spend Requirement Per Month

The spend agreement with StoreStack requires the customer to spend a minimum amount in each Billing Period (monthly). Unused fees are charged per Billing Period when the consumption is below this level (use-it or lose-it). For this scenario, contract additionally includes the following terms:

- A minimum of $60 needs to be spent each month

Acme Corp's consumption looks like this:

- In the first month, Acme Corp uses $48 of services (4 server hours). This usage has a List Cost of $60 (before discounts). For this month, StoreStack charges $12 (ListCost of $15) for not meeting the monthly minimum
- In the following 2 months, Acme Corp has usage at or above the minimum requirement
- For the final 9 months, Acme Corp does not use StoreStack services

Note the following details in the example dataset:

- A monthly charge representing the unused minimum monthly amount is charged during months 4 through 11 of the 12-month commitment period
- The final month has a charge that captures the overall unmet spend requirement for the 12-month contract. Alternatively, this could be provided as two charges, one for the unused portion of the final month, and one to capture the overall unmet spend requirement.

### 8.11.2.3 Scenario B: Prepaid Contract

For this scenario B, contract includes the following terms in addition to the baseline scenario mentioned above:

- The charges will be billed in arrears using monthly invoices

#### 8.11.2.3.1 Scenario B1: Prepaid with No Minimum Spend Requirement Per Month

Scenario B1 is similar to scenario A1 with the difference being that it's a pre-paid contract.

Note the following details in the example dataset:

- A purchase record for the initial $1200 payment is present representing List, Billed, and Contracted cost of the purchase
- The charge for the unused amount has a $0 BilledCost (since the total amount was billed with the prepayment). However, the charge captures the unused portion as an EffectiveCost.
- The unused charge rows apply to the entire Charge Period the contract was signed for.
- This scenario shows List Cost and Contracted Cost column double counting dynamic (described here in ListCost and ContractedCost) where either the ChargeCategory Purchase or Usage rows need to be excluded depending on the reporting scenario.

#### 8.11.2.3.2 Scenario B2: Prepaid with a Minimum Spend Requirement Per Month

Scenario B2 is similar to A2 with the difference being that it's a pre-paid contract.

Note the following details in the example dataset:

- A purchase record for the initial $1200 payment is present representing List, Billed, and Contracted cost of the purchase
- The monthly charge for the unused amount has a $0 BilledCost (since the total amount was billed with the prepayment). However, the charge captures the unused portion as an EffectiveCost.
- The final month has a charge that captures the overall unmet spend requirement for the 12-month contract. Alternatively, this could be provided as two charges, one for the unused portion of the final month, and one to capture the overall unmet spend requirement.
- This scenario shows List Cost and Contracted Cost column double counting dynamic (described here in ListCost and ContractedCost) where either the Purchase or Usage rows need to be excluded depending on the reporting scenario.

## 8.11.3 Virtual Currency Pricing Model

Many SaaS service providers support pricing models that utilize virtual currencies such as credits, tokens, or points. Charges may be provided using a virtual currency, which can subsequently be converted to a national currency such as USD or EUR at an advertised or agreed-upon conversion rate.

The scenarios described below illustrate how a Cost and Usage *FOCUS dataset* should look for various scenarios where a provider utilizes this pricing model.

### 8.11.3.1 Baseline Scenario

The following baseline conditions apply to the scenarios described below:

- Acme Corp has signed an agreement with SaaS service provider OmniQuery to use their services.
- OmniQuery offers a virtual currency pricing model for their services and requires a purchase of virtual currency in advance of usage. Their denomination of virtual currency is called "tokens".
- OmniQuery requires purchase of additional tokens in the event of usage exceeding purchased tokens.
- OmniQuery publicly lists the cost of their tokens at $2 per token.
- OmniQuery treats token purchases as resources; therefore, charges for token purchases include values for ResourceId, ResourceName, and ResourceType.
- OmniQuery publicly lists their usage to token rates. These rates are as follows:
  - 1 Q Widget Execution = 1 token
  - 1 Z Widget Execution = 2 tokens
  - 1 Workflow Operation = 3 tokens

### 8.11.3.2 Scenario A: Virtual Currency Not Offered at a Discount

For this scenario, contract terms include the following terms in addition to the baseline scenario mentioned above:

- Acme Corp offers no discount for purchased tokens.

### 8.11.3.3 Scenario A1: Purchase of Virtual Currency Without a Discount

For this scenario, the initial purchase of virtual currency is executed as follows:

- On April 1, 2025, Acme Corp agrees to purchase 100,000 tokens at $2 per token for a total spend $200,000. These tokens are only valid for 12 months.

Note the following details in the example dataset:

- The Charge Period is April 1st 2025 - April 1st 2026. The Billing Period is the month of April 2025 (when the tokens were purchased) and therefore will appear in the April invoice.
- Because OmniQuery uses a virtual currency pricing model for usage and publishes their token price in terms of dollars and their usage cost in terms of tokens, their Cost and Usage *FOCUS dataset* includes the columns PricingCurrency, PricingCurrencyContractedUnitPrice, PricingCurrencyEffectiveCost, and PricingCurrencyListUnitPrice.
- A single charge representing the total payment for the initial token purchase agreement ($200,000) is charged in the first invoice.
  - ListCost, BilledCost, and ContractedCost of the purchase are all represented in this charge, however EffectiveCost is zero since the tokens are not yet consumed.
- PricingQuantity is set to the total tokens purchased.
- Because Acme Corp is paying the list price, ListUnitPrice and ContractedUnitPrice are all set to the same value of $2.

### 8.11.3.4 Scenario A2: Usage of Virtual Currency Purchased Without a Discount

Acme Corp uses OmniQuery's services consuming tokens as follows in the first day:

- 245 executions of Q Widget
- 5 executions of Z Widget
- 120 operations of Workflow

Note the following details in the example dataset:

- The Charge Period is April 1st 2025 - April 2nd 2025. The Billing Period is the month of April 2025.
- PricingCurrency for these usage charges reflects the per usage token price of the particular usage.
- PricingQuantity reflects the amount of usage of the PricingUnit for each charge and is equivalent to ConsumedQuantity. While relevant to this example, there are scenarios including tiered pricing where ConsumedQuantity and PricingQuantity may not be the same.
- Because Acme Corp's usage includes no discount on usage to token rates, PricingCurrencyContractedUnitPrice and PricingCurrencyListUnitPrice are equivalent.

### 8.11.3.5 Scenario B: Virtual Currency Offered at a Discount

For this scenario, contract terms include the following terms in addition to the baseline scenario mentioned above:

- Acme Corp offers a discount for purchased tokens.

### 8.11.3.6 Scenario B1: Purchase of Virtual Currency at a Discount

For this scenario, the initial purchase of virtual currency is executed as follows:

- On April 1, 2025, Acme Corp agrees to purchase 100,000 tokens at discounted cost of $1 per token for a total spend $100,000. These tokens are only valid for 12 months.

Note the following details in the example dataset:

- The Charge Period is April 1st 2025 - April 1st 2026. The Billing Period is the month of April 2025 (when the tokens were purchased) and therefore will appear in the April invoice.
- Because OmniQuery uses a virtual currency pricing model for usage and publishes their token price in terms of dollars and their usage cost in terms of tokens, their *FOCUS dataset* includes the columns PricingCurrency, PricingCurrencyContractedUnitPrice, PricingCurrencyEffectiveCost, and PricingCurrencyListUnitPrice.
- A single charge representing the total payment for the initial token purchase agreement ($100,000) is charged in the first invoice.
  - ListCost, BilledCost, and ContractedCost of the purchase are all represented in this charge, however EffectiveCost is zero, as required for prepaid purchases.
- PricingQuantity is set to the total tokens purchased.
- Because Acme Corp is receiving a discount on the token price, the ListUnitPrice is set to $2 and the ContractedUnitPrice is set to $1. A ListCost of ($200,000) and ContractedCost ($100,000) reflect the cost of the tokens at the list price and contracted price respectively. The BilledCost is set to $100,000 since this is the amount that Acme Corp will be charged for the purchase of tokens.

### 8.11.3.7 Scenario B2: Usage of Virtual Currency Purchased at a Discount

Acme Corp uses OmniQuery's services, consuming tokens as follows in the first day:

- 245 executions of Q Widget
- 5 executions of Z Widget
- 120 operations of Workflow

Note the following details in the example dataset:

- PricingQuantity reflects the amount of usage of the PricingUnit for each charge and is equivalent to ConsumedQuantity. While relevant to this example, there are scenarios including tiered pricing where ConsumedQuantity and PricingQuantity may not be the same.
- Because Acme Corp's usage includes no discount on usage to token rates, PricingCurrencyContractedUnitPrice and PricingCurrencyListUnitPrice are equivalent.

### 8.11.3.8 Scenario B3: Usage of Virtual Currency at a Modified Rate

Acme Corp uses OmniQuery's services consuming tokens as follows in the first day:

- 245 executions of Q Widget
- 5 executions of Z Widget
- 120 operations of Workflow

Additionally, OmniQuery offers a modified usage to token ratio for one of their services as follows:

- 1 Workflow Operation = 2 tokens

Note the following details in the example dataset:

- Because of the modified rate for Workflow Operations, the PricingCurrencyContractedUnitPrice and PricingCurrencyListUnitPrice are different for this charge. The ContractedUnitPrice is set to $1 and the ListUnitPrice is set to $2.
- The PricingCurrencyEffectiveCost is 240 tokens for this charge, which is less than example B2 above due to the modified rate.
- ListCost reflects the cost of the charge at both the list cost of the tokens and the list rate for which the usage consumes tokens.

### 8.11.3.9 Scenario C: Handling Virtual Currency Usage Overages

For this scenario, Acme Corp has exceeded their purchased tokens on October 1st 2025 by 1,500 tokens and OmniQuery has charged them for the overage. The following conditions apply:

- OmniQuery has charged Acme Corp for the cost of tokens at the list price of $2 per token, and this purchase is effective from April 1st 2025 to the date of the purchase, October 1st 2025.
- Acme Corp purchases an additional 25,000 tokens to facilitate usage to the end of their contract. These tokens are valid from October 1st 2025 to April 1st 2026.

Note the following details in the example dataset:

- This example focuses on the purchases records only for the overage and additional purchases. Neither usage charges nor earlier purchases are not included in this example.
- The Charge Period for the Overage Purchase is April 1st 2025 - October 1st 2025. This is because the overage charge is to cover the period of time the overage token purchase is applicable to.
- The Charge Period for the Additional Purchase is October 1st 2025 - April 1st 2026. This is because the additional purchase is to cover the period of time to which the additional token purchase is applicable. Because end dates are exclusive, ChargePeriodEnd is April 1st 2026.

## 8.11.4 Billing Scenario Examples

The following examples illustrate how BilledCost and EffectiveCost behave across common software as a service (SaaS) and platform as a service (PaaS) billing models. Each scenario uses a fictional *service provider* with illustrative pricing and demonstrates a distinct billing pattern that SaaS or PaaS data generators may implement via the FOCUS specification.

Each example targets a specific billing pattern. All examples share a consistent column set; columns not applicable to a given scenario contain null values.

| Scenario | Service Provider | What You'll Learn | 
|---|---|---|
| Credit-Based Consumption | OmniQuery | Custom consumption units (Credits) with `ChargeFrequency` split between "Usage-Based" (compute) and "Recurring" (storage). No *commitment discount*; BilledCost = EffectiveCost on all rows. | 
| Host-Based SaaS Monitoring | StackLens | Multiple *services* billed on independent metrics (hosts vs. GB). "Recurring" for host-based charges, "Usage-Based" for log ingestion. No regional billing. | 
| Seat-Based SaaS Subscription | SprintCanvas | Upfront annual purchase amortized to monthly Usage rows. BilledCost vs. EffectiveCost divergence. Spend-based `CommitmentDiscountCategory`, One-Time `ChargeFrequency`. | 
| Multi-Unit PaaS Database | StoreStack | Three heterogeneous PricingUnit values (Hours, GB, GB) within one *service provider*. Region-specific billing with RegionId/RegionName populated. | 
| Flat-Rate SaaS Licensing | CollabChat | Fixed monthly subscription where PricingUnit is "Subscriptions" and PricingQuantity is 1, decoupled from underlying user count. | 
| Annual Commitment Billed Monthly | PipelCRM | Annual term contract with monthly billing where the billed rate equals list price. No *commitment discount* despite the annual obligation. | 
| Tiered Pricing with Committed Minimum | PulseMail | Plan fee as a usage-denominated *commitment discount* with Used/Unused split and overage pricing. `CommitmentDiscountCategory` = "Usage". Two billing periods showing under- and over-minimum scenarios. | 

### 8.11.4.1 Credit-Based Consumption: On-Demand Data Platform Usage

A data platform *service provider*, OmniQuery, uses a credit-based consumption model. Customers consume credits based on warehouse compute activity and pay a fixed per-credit rate determined by their service edition. Storage is billed separately on a per-terabyte basis.

The *service provider*'s on-demand pricing for this example:

| Service | SKU | Unit Price | Pricing Unit | Credits/Hour | 
|---|---|---|---|---|
| Virtual Warehouse Compute | XS Warehouse | $3.00 | Credits | 1 | 
| Virtual Warehouse Compute | Medium Warehouse | $3.00 | Credits | 4 | 
| Storage | Active Storage | $23.00 | TB | n/a | 

Credit consumption varies by warehouse size. An XS warehouse consumes 1 credit per hour. A Medium warehouse consumes 4 credits per hour.

A customer runs two warehouses in the US East region during January 2025:

- XS warehouse (analyst workload): 200 hours of runtime = 200 credits consumed
- Medium warehouse (ETL workload): 80 hours of runtime = 320 credits consumed (4 credits/hour)
- 5 TB of active storage

Three usage charges appear on the January invoice:

- XS Warehouse: `200 Credits x $3.00` = $600.00
- Medium Warehouse: `320 Credits x $3.00` = $960.00
- Active Storage: `5 TB x $23.00` = $115.00

Total BilledCost: $1,675.00

Here is how these charges appear in the data (relevant columns only):

| FOCUS Column | XS Warehouse | Medium Warehouse | Active Storage | 
|---|---|---|---|
| ChargeCategory | Usage | Usage | Usage | 
| ChargeFrequency | Usage-Based | Usage-Based | Recurring | 
| ConsumedQuantity | 200 | 320 | 5 | 
| ConsumedUnit | Credits | Credits | TB | 
| BilledCost | $600.00 | $960.00 | $115.00 | 
| EffectiveCost | $600.00 | $960.00 | $115.00 | 
| ListCost | $600.00 | $960.00 | $115.00 | 
| ContractedCost | $600.00 | $960.00 | $115.00 | 
| PricingUnit | Credits | Credits | TB | 
| PricingCategory | Standard | Standard | Standard | 

Key observations:

- Both warehouses share the same ListUnitPrice of $3.00 per credit. The credit price is determined by the service edition, not warehouse size.
- ConsumedUnit is "Credits" for compute and "TB" for storage. The credit is the *service provider*'s unit of compute consumption.
- ChargeFrequency is "Usage-Based" for compute (metered by credit consumption) and "Recurring" for storage (billed per TB per month).
- Storage has no ResourceId or ResourceName because it is an account-level charge, not tied to a specific *resource*.
- BilledCost and EffectiveCost are equal on all rows. These two columns diverge when a purchase *charge* covers future usage (as with a *commitment discount*), because the *cash-based* outflow is invoiced upfront while cost is recognized on an *accrual basis* over time. With no such purchase *charges* here, the two views produce the same cost per row.

### 8.11.4.2 Host-Based SaaS Monitoring: Monthly On-Demand Usage

A SaaS observability *service provider*, StackLens, offers multiple monitoring *services* billed on different units: host-based pricing for infrastructure and application performance monitoring, and volume-based pricing for log ingestion.

The *service provider*'s on-demand pricing for this example:

| Service | SKU | Unit Price | Pricing Unit | 
|---|---|---|---|
| Infrastructure Monitoring | Infra Pro | $18.00 | Hosts | 
| APM | APM Standard | $36.00 | Hosts | 
| Log Management | Log Ingestion | $0.10 | GB | 

A customer uses the *service provider*'s monitoring platform on a month-to-month basis with no annual commitment. During January 2025, the customer's usage is:

- 25 infrastructure hosts monitored
- 10 APM hosts monitored (a subset of the infrastructure hosts, billed independently)
- 150 GB of logs ingested

Three usage charges appear on the January invoice:

- Infrastructure Monitoring: `25 Hosts x $18.00` = $450.00
- APM: `10 Hosts x $36.00` = $360.00
- Log Management: `150 GB x $0.10` = $15.00

Total BilledCost: $825.00

Here is how these charges appear in the data (relevant columns only):

| FOCUS Column | Infra Monitoring | APM | Log Management | 
|---|---|---|---|
| ChargeCategory | Usage | Usage | Usage | 
| ChargeFrequency | Recurring | Recurring | Usage-Based | 
| ConsumedQuantity | 25 | 10 | 150 | 
| ConsumedUnit | Hosts | Hosts | GB | 
| BilledCost | $450.00 | $360.00 | $15.00 | 
| EffectiveCost | $450.00 | $360.00 | $15.00 | 
| ListCost | $450.00 | $360.00 | $15.00 | 
| ContractedCost | $450.00 | $360.00 | $15.00 | 
| PricingUnit | Hosts | Hosts | GB | 
| PricingCategory | Standard | Standard | Standard | 

Key observations:

- ChargeFrequency is "Recurring" for the host-based *services* (billed per host per month regardless of utilization within the month) and "Usage-Based" for log ingestion (billed on actual volume consumed).
- APM hosts are a subset of infrastructure hosts but each *service* is billed independently. The 10 APM hosts also appear in the 25 infrastructure host count.
- RegionId and RegionName are null. This *service provider* does not expose region in its billing. Some SaaS and PaaS *service providers* do bill by region, in which case these columns would be populated (see the Multi-Unit PaaS example below).
- ResourceId and ResourceName are null. The *service provider* bills at the *service* level (per host or per GB), not per individual monitored *resource*.
- All three *services* share the ServiceCategory "Management and Governance" per the FOCUS allowed values for logging, monitoring, and observability *services*.
- BilledCost and EffectiveCost are equal on all rows because there are no purchase *charges* covering future usage (see the Credit-Based Consumption example for a full explanation of when these columns diverge).

### 8.11.4.3 Seat-Based SaaS Subscription: Annual Upfront with Commitment Discount

This example illustrates an annual upfront SaaS subscription where the customer receives a discounted per-user rate by committing to a 12-month term. The discounted rate is only available with the annual commitment, making this a *commitment discount*.

The *service provider*, SprintCanvas, offers a project management platform with the following pricing for 50 users on the Standard plan:

| Billing Option | Unit Price | Monthly Cost (50 users) | Annual Cost | 
|---|---|---|---|
| Monthly | $9.05/user/month | $452.50 | $5,430.00 | 
| Annual | $7.58/user/month | $379.00 | $4,550.00 | 

The annual option represents a \~16% discount versus monthly billing.

A customer subscribes to the Standard plan for 50 users on April 1, 2025. They choose the annual billing option, paying $4,550.00 upfront for a 12-month term ending April 1, 2026. All 50 seats are occupied in the first month.

Two charges appear in the April 2025 *billing period*:

Here is how these charges appear in the data (relevant columns only):

| FOCUS Column | Purchase | Usage (April) | 
|---|---|---|
| ChargeCategory | Purchase | Usage | 
| ChargeFrequency | One-Time | Recurring | 
| CommitmentDiscountCategory | Spend | Spend | 
| CommitmentDiscountStatus | *(null)* | Used | 
| CommitmentDiscountQuantity | 4,550.00 | 379.00 | 
| CommitmentDiscountUnit | USD | USD | 
| ConsumedQuantity | *(null)* | 50 | 
| ConsumedUnit | *(null)* | Users | 
| BilledCost | $4,550.00 | $0.00 | 
| EffectiveCost | $0.00 | $379.00 | 
| ListCost | $5,430.00 | $452.50 | 
| ContractedCost | $5,430.00 | $452.50 | 
| PricingUnit | Count | Users | 
| PricingCategory | Standard | Committed | 

**Purchase Charge:** ChargeCategory is "Purchase" with ChargeFrequency "One-Time". The full annual amount is invoiced in a single payment.

- The *charge period* spans the entire commitment term: April 1, 2025 through April 1, 2026.
- BilledCost is $4,550.00. This is the *cash-based* invoiced amount for the annual subscription.
- EffectiveCost is $0.00. The purchase covers future usage. Cost is recognized on an *accrual basis* as usage occurs.
- ListCost is $5,430.00 (`50 users x $9.05/user/month x 12 months`). This represents the cost without the annual discount.
- ContractedCost is $5,430.00, equal to ListCost. Because no *negotiated discounts* apply (the annual rate is a published *commitment discount*, not a bilateral negotiation), ContractedUnitPrice defaults to ListUnitPrice per the spec. The difference between ContractedCost ($5,430.00) and BilledCost ($4,550.00) represents the $880.00 in *commitment discount* savings at the point of purchase.
- ResourceId equals CommitmentDiscountId. The *commitment discount* itself is the *resource* being purchased.
- CommitmentDiscountCategory is "Spend" because the commitment is denominated in dollars, not usage units.
- CommitmentDiscountQuantity is 4,550.00 CommitmentDiscountUnit (USD). This is the total spend eligible for consumption over the term.
- PricingCategory is "Standard". The purchase of the *commitment discount* is at the agreed-upon rate.

**Usage Charge (April 2025):** ChargeCategory is "Usage" with PricingCategory "Committed". The usage is covered by the annual purchase.

- BilledCost is $0.00. No additional invoiced amount. The usage is covered by the purchase charge.
- EffectiveCost is $379.00. This is the *accrual-based* recognized portion of the annual commitment: `$7.58/user x 50 users`.
- ListCost is $452.50 (`50 users x $9.05/user`). The monthly list cost without the annual discount.
- ContractedCost is $452.50, equal to ListCost. No *negotiated discounts* apply, so ContractedUnitPrice defaults to ListUnitPrice.
- The *commitment discount* savings appear in the difference between ContractedCost ($452.50) and EffectiveCost ($379.00): $73.50 per month.
- CommitmentDiscountStatus is "Used". All 50 seats are occupied.
- CommitmentDiscountQuantity is 379.00 USD. This is the amount of spend consumed from the commitment in this *charge period*.
- ResourceId is the actual *resource* (the customer's project management site), not the *commitment discount*.

**Rounding Note:** The per-user rate of $7.58 is derived from `$4,550 / 12 months / 50 users` = $7.5833, rounded to two decimal places. This means `$7.58 x 50 users x 12 months` = $4,548.00, which is $2.00 less than the $4,550.00 purchase. In a full 12-month dataset, the final month's charge would include a true-up to ensure the sum of EffectiveCost across all usage rows equals the BilledCost of the purchase row.

### 8.11.4.4 Multi-Unit Usage-Based PaaS: Database-as-a-Service

A PaaS database *service provider*, StoreStack, bills different resource types on different units. The *service provider* offers dedicated database clusters with separate charges for compute, storage, and data transfer.

The *service provider*'s on-demand pricing for this example:

| Service | SKU | Unit Price | Pricing Unit | 
|---|---|---|---|
| StoreStack Clusters | M10 Cluster | $0.08 | Hours | 
| StoreStack Clusters | M30 Cluster | $0.54 | Hours | 
| StoreStack Storage | SSD Storage | $0.25 | GB | 
| StoreStack Data Transfer | Data Transfer Out | $0.01 | GB | 

A customer runs two dedicated database clusters in the US East region for the full month of January 2025 (744 hours). They also consume 100 GB of SSD storage and 50 GB of outbound data transfer.

- 1x M10 cluster (analytics workload): 744 hours at $0.08/hour
- 1x M30 cluster (production workload): 744 hours at $0.54/hour
- 100 GB of SSD storage
- 50 GB of outbound data transfer

Four usage charges appear on the January invoice:

- M10 Cluster: `744 Hours x $0.08` = $59.52
- M30 Cluster: `744 Hours x $0.54` = $401.76
- SSD Storage: `100 GB x $0.25` = $25.00
- Data Transfer Out: `50 GB x $0.01` = $0.50

Total BilledCost: $486.78

Here is how these charges appear in the data (relevant columns only):

| FOCUS Column | M10 Cluster | M30 Cluster | SSD Storage | Data Transfer Out | 
|---|---|---|---|---|
| ChargeCategory | Usage | Usage | Usage | Usage | 
| ChargeFrequency | Usage-Based | Usage-Based | Recurring | Usage-Based | 
| ConsumedQuantity | 744 | 744 | 100 | 50 | 
| ConsumedUnit | Hours | Hours | GB | GB | 
| BilledCost | $59.52 | $401.76 | $25.00 | $0.50 | 
| EffectiveCost | $59.52 | $401.76 | $25.00 | $0.50 | 
| ListCost | $59.52 | $401.76 | $25.00 | $0.50 | 
| ContractedCost | $59.52 | $401.76 | $25.00 | $0.50 | 
| PricingUnit | Hours | Hours | GB | GB | 
| PricingCategory | Standard | Standard | Standard | Standard | 
| RegionId | us-east-1 | us-east-1 | us-east-1 | us-east-1 | 

Key observations:

- Three different PricingUnit values appear within a single *service provider*: Hours (compute), GB (storage), and GB (data transfer). This heterogeneity is typical for PaaS database *services*.
- ChargeFrequency varies by resource type. Compute clusters are "Usage-Based" (metered hourly). Storage is "Recurring" (billed per GB provisioned per month regardless of access patterns). Data transfer is "Usage-Based" (billed on actual volume transferred).
- Compute clusters have ResourceId and ResourceName values because each cluster is a distinct *resource*. Storage and data transfer are account-level charges with no specific *resource*, so these columns are null.
- All four charges share the ServiceCategory "Databases" but are split across three distinct ServiceName values: StoreStack Clusters, StoreStack Storage, and StoreStack Data Transfer.
- RegionId and RegionName are populated. This *service provider* deploys database clusters to specific regions, and pricing varies by region.
- BilledCost and EffectiveCost are equal on all rows because there are no purchase *charges* covering future usage (see the Credit-Based Consumption example for a full explanation of when these columns diverge).

### 8.11.4.5 Flat-Rate SaaS Licensing: Fixed Monthly Subscription

A team communications *service provider*, CollabChat, offers both per-user and flat-rate subscription tiers. This example uses the flat-rate option, where all features and unlimited users are included for a fixed monthly fee with no per-user pricing.

The *service provider*'s pricing for this example:

| Service | SKU | Unit Price | Pricing Unit | 
|---|---|---|---|
| CollabChat | Pro Unlimited | $349.00 | Subscriptions | 

The *service provider* also offers an annual billing option at $299.00 per month (billed annually). This example uses the month-to-month option with no annual commitment.

A customer subscribes to the Pro Unlimited plan on a month-to-month basis. During January 2025, the customer's team of 35 people uses the platform.

One charge appears on the January invoice:

- Pro Unlimited: `1 Subscription x $349.00` = $349.00

Total BilledCost: $349.00

Here is how this charge appears in the data (relevant columns only):

| FOCUS Column | Pro Unlimited | 
|---|---|
| ChargeCategory | Usage | 
| ChargeFrequency | Recurring | 
| ConsumedQuantity | 1 | 
| ConsumedUnit | Subscriptions | 
| BilledCost | $349.00 | 
| EffectiveCost | $349.00 | 
| ListCost | $349.00 | 
| ContractedCost | $349.00 | 
| PricingUnit | Subscriptions | 
| PricingQuantity | 1 | 
| PricingCategory | Standard | 

Key observations:

- ChargeFrequency is "Recurring". The subscription is a fixed monthly fee regardless of usage activity or user count within the *billing period*.
- PricingUnit is "Subscriptions" and PricingQuantity is 1. Unlike per-seat or per-unit models, the entire platform is a single billable unit.
- There is no relationship between ConsumedQuantity and the number of users. The 35-person team does not affect the charge.
- If the customer chose the annual billing option ($299.00/month billed annually), this would follow a *commitment discount* pattern similar to the Seat-Based SaaS Subscription example above, with a Purchase row for the annual payment and monthly Usage rows for amortized EffectiveCost.
- BilledCost and EffectiveCost are equal because there are no purchase *charges* covering future usage (see the Credit-Based Consumption example for a full explanation of when these columns diverge).

### 8.11.4.6 Annual Commitment Billed Monthly: Seat-Based CRM

A CRM *service provider*, PipelCRM, offers a seat-based sales platform requiring an annual commitment. Unlike prepaid annual subscriptions, one billing option charges monthly throughout the contract term. The monthly billed rate equals the list price, so no *commitment discount* is applied in FOCUS terms.

The *service provider*'s pricing for this example (Professional plan, 10 users):

| Billing Option | Unit Price | Monthly Cost (10 users) | Annual Cost | 
|---|---|---|---|
| Annual (pay upfront) | $90.00/user/month | $900.00 | $10,800.00 | 
| Annual (billed monthly) | $100.00/user/month | $1,000.00 | $12,000.00 | 

A customer subscribes to the Professional plan for 10 users, choosing the annual commitment with monthly billing. They pay $100.00 per user per month with no upfront payment.

One charge appears on the January 2025 invoice:

- Sales Platform Professional: `10 Users x $100.00` = $1,000.00

Total BilledCost: $1,000.00

Here is how this charge appears in the data (relevant columns only):

| FOCUS Column | Sales Platform Professional | 
|---|---|
| ChargeCategory | Usage | 
| ChargeFrequency | Recurring | 
| ConsumedQuantity | 10 | 
| ConsumedUnit | Users | 
| BilledCost | $1,000.00 | 
| EffectiveCost | $1,000.00 | 
| ListCost | $1,000.00 | 
| ContractedCost | $1,000.00 | 
| PricingUnit | Users | 
| PricingCategory | Standard | 

Key observations:

- BilledCost, EffectiveCost, ListCost, and ContractedCost are all equal at $1,000.00. Monthly billing on an annual contract produces no divergence between *cash-based* and *accrual-based* costs because there is no upfront payment to amortize.
- PricingCategory is "Standard" because the billed rate equals the ListUnitPrice. The annual contract is a term commitment, not a pricing discount. No *commitment discount* columns are populated.
- ChargeFrequency is "Recurring" because the charge recurs monthly at a fixed per-seat rate regardless of usage activity within the *billing period*.
- If the customer chose the annual pay-upfront option ($90.00/user/month), the $10.00 per-seat discount would qualify as a *commitment discount*, following the pattern in the Seat-Based SaaS Subscription example with a Purchase row and amortized EffectiveCost.
- This scenario demonstrates that an annual contract does not automatically produce a *commitment discount* in FOCUS. The distinguishing factor is whether the commitment provides a price reduction from the standard rate.

### 8.11.4.7 Tiered Pricing with Committed Minimum: Email API Platform

A SaaS email API *service provider*, PulseMail, offers tiered plans that include a monthly email allowance. Emails sent within the allowance are covered by the plan fee. Emails exceeding the allowance are billed at a per-email overage rate. The plan minimum functions as a usage-denominated *commitment discount* because the customer pays a fixed fee for a quantity of usage units.

The *service provider*'s pricing for this example (Essentials 50K plan):

| Component | Rate | Unit | 
|---|---|---|
| Plan fee (includes 50,000 emails) | $19.95 | Count | 
| Overage | $0.00133 | Emails | 

This example covers two billing periods to show both under-minimum and over-minimum scenarios:

- **January 2025:** The customer sends 30,000 emails, below the 50,000 email allowance. 20,000 emails go unused.
- **February 2025:** The customer sends 65,000 emails, exceeding the allowance by 15,000.

**January charges (under minimum):**

The monthly plan fee of $19.95 appears as a Purchase charge. Two Usage charges split the commitment between used and unused portions:

- Purchase: $19.95 (plan fee covering 50,000 emails)
- Used: 30,000 emails, EffectiveCost = $11.97 (`30,000 / 50,000 x $19.95`)
- Unused: 20,000 emails, EffectiveCost = $7.98 (`20,000 / 50,000 x $19.95`)

Total BilledCost: $19.95

Here is how the January charges appear in the data (relevant columns only):

| FOCUS Column | Purchase | Usage (Used) | Usage (Unused) | 
|---|---|---|---|
| ChargeCategory | Purchase | Usage | Usage | 
| ChargeFrequency | Recurring | Usage-Based | Usage-Based | 
| CommitmentDiscountCategory | Usage | Usage | Usage | 
| CommitmentDiscountStatus | *(null)* | Used | Unused | 
| CommitmentDiscountQuantity | 50,000 | 30,000 | 20,000 | 
| CommitmentDiscountUnit | Emails | Emails | Emails | 
| ConsumedQuantity | *(null)* | 30,000 | *(null)* | 
| ConsumedUnit | *(null)* | Emails | *(null)* | 
| BilledCost | $19.95 | $0.00 | $0.00 | 
| EffectiveCost | $0.00 | $11.97 | $7.98 | 
| ListCost | $19.95 | $39.90 | $26.60 | 
| ContractedCost | $19.95 | $39.90 | $26.60 | 
| PricingUnit | Count | Emails | Emails | 
| PricingCategory | Standard | Committed | Committed | 

**February charges (over minimum):**

The customer uses all 50,000 plan emails plus 15,000 overage emails:

- Purchase: $19.95 (plan fee covering 50,000 emails)
- Used: 50,000 emails, EffectiveCost = $19.95 (full allowance consumed)
- Overage: 15,000 emails at $0.00133 = $19.95 (standard pricing, not part of commitment)

Total BilledCost: $39.90

Here is how the February charges appear in the data (relevant columns only):

| FOCUS Column | Purchase | Usage (Used) | Usage (Overage) | 
|---|---|---|---|
| ChargeCategory | Purchase | Usage | Usage | 
| ChargeFrequency | Recurring | Usage-Based | Usage-Based | 
| CommitmentDiscountCategory | Usage | Usage | *(null)* | 
| CommitmentDiscountStatus | *(null)* | Used | *(null)* | 
| CommitmentDiscountQuantity | 50,000 | 50,000 | *(null)* | 
| CommitmentDiscountUnit | Emails | Emails | *(null)* | 
| ConsumedQuantity | *(null)* | 50,000 | 15,000 | 
| ConsumedUnit | *(null)* | Emails | Emails | 
| BilledCost | $19.95 | $0.00 | $19.95 | 
| EffectiveCost | $0.00 | $19.95 | $19.95 | 
| ListCost | $19.95 | $66.50 | $19.95 | 
| ContractedCost | $19.95 | $66.50 | $19.95 | 
| PricingUnit | Count | Emails | Emails | 
| PricingCategory | Standard | Committed | Standard | 

Key observations:

- CommitmentDiscountCategory is "Usage" on all commitment-related rows. The plan minimum is denominated in email quantity (50,000 emails), not a dollar amount. This distinguishes it from the "Spend" category in the Seat-Based SaaS Subscription example.
- CommitmentDiscountStatus shows "Used" and "Unused" on Usage rows. In January, the customer only consumed 30,000 of 50,000 emails, so the remaining 20,000 generate an "Unused" row. The Unused row has BilledCost of $0.00 but EffectiveCost of $7.98, representing waste from the commitment.
- The Purchase row has BilledCost of $19.95 and EffectiveCost of $0.00. This follows the same pattern as the Seat-Based SaaS Subscription: the purchase captures the *cash-based* cost, while *accrual-based* cost is recognized on the Usage rows.
- The overage row in February has no *commitment discount* columns populated. Overage emails are billed at the standard per-email rate and are not part of the commitment.
- ContractedUnitPrice and ListUnitPrice are both $0.00133 on all Usage rows. Because no *negotiated discounts* apply, ContractedUnitPrice defaults to ListUnitPrice per the spec. The *commitment discount* savings are reflected in the difference between ContractedCost and EffectiveCost, not in ContractedUnitPrice.
- ListCost and ContractedCost on Usage rows represent the market value of those emails at the per-email rate: `$0.00133 x 30,000` = $39.90 for the January Used row. These values exceed BilledCost ($0.00) because the usage is covered by the plan fee, not billed individually. The gap between ListCost and EffectiveCost shows the *commitment discount* benefit per row.
- PricingUnit is "Count" on the Purchase row because the plan fee is a single monthly purchase, not denominated in the usage unit (emails). On Usage rows, PricingUnit is "Emails" because those rows are priced per email.
- ChargeFrequency is "Recurring" on the Purchase rows (the plan fee recurs monthly). On the Usage rows, ChargeFrequency is "Usage-Based" for both Used and Unused rows because the amounts vary based on actual email consumption each period.