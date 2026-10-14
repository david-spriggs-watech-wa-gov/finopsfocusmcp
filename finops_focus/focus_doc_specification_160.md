---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/glossary/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: b69811fb26b3b1c5
---
1. Specification
2. v1.4
3. Glossary

# 7 Glossary

73 terms

## A

- Accrual-Based Accounting
- An accounting method used in technology cost management to record costs in the period when resources are utilized, services are delivered, or entitlements are available for or actually consumed (including unused or expired entitlements). This approach ensures that expenses are recognized in the same timeframe as the value they provide, independent of when charges are invoiced.
- Adjustment
- A charge representing a modification to billing data to account for certain events or circumstances not previously captured, or captured incorrectly. Examples include billing errors, service disruptions, or pricing changes.
- Allocated Charge
- The charge that was created as the result of an allocation operation. This is used in the context of Data Generator-Calculated Split Cost Allocation to identify the charges that were created from the origin charge resulting from the application of Data Generator-Calculated Split Cost Allocation.
- Allocated Method
- The process or formula by which cost is being allocated from an origin charge to produce allocated charges. This is used in the context of Data Generator-Calculated Split Cost Allocation which requires documentation of the method to be provided for any and all allocated methods used. May also be colloquially referred to as allocation method.
- Amortization
- The distribution of upfront costs over time to accurately reflect the consumption or benefit derived from the associated resources or services. Amortization is valuable when the commitment *period* extends beyond the granularity of the source report.
- Availability Zone
- A collection of geographically separated locations containing a data center or cluster of data centers. Each availability zone (AZ) should have its own power, cooling, and networking, to provide redundancy and fault tolerance.

## B

- Billing Account
- A container for resources and/or services that are billed together in an invoice. A billing account may have sub accounts, all of whose costs are consolidated and invoiced to the billing account.
- Billing Currency
- An identifier that represents the currency that a charge for resources and/or services was billed in.
- Billing Period
- The time window that an organization receives an invoice for, inclusive of the start date and exclusive of the end date. It is independent of the time of usage and consumption of resources and services.
- Block Pricing
- A pricing approach where the cost of a particular resource or service is determined based on predefined quantities or tiers of usage. In these scenarios, the Pricing Unit and the corresponding Pricing Quantity can be different from the Consumed Unit and Consumed Quantity.

## C

- Cash-Based Accounting
- An accounting method used in technology cost management to record costs in the period when charges are invoiced. This approach aligns expenses with billing cycles, independent of when resources are utilized, services are delivered, or entitlements are available for or actually consumed (including unused or expired entitlements).
- Capacity Reservation
- A capacity reservation is an agreement that secures a dedicated amount of resources or services for a specified period. This ensures the reserved capacity is always available and accessible, even if it's not fully utilized. Customers are typically charged for the reserved capacity, regardless of actual consumption.
- Charge
- A row in a FOCUS-compatible cost and usage dataset.
- Charge Period
- The time window for which a charge is effective, inclusive of the start date and exclusive of the end date. The charge period for continuous usage should match the time granularity of the *dataset instance* (e.g., 1 hour for hourly, 1 day for daily). The charge period for a non-usage charge with time boundaries should match the period of eligibility.
- Closed Billing Period
- A *billing period* with Billing Period Status set to "Closed". The period has been financially closed after all anticipated invoices for the period have been *issued* by designated *invoice issuers* and no additional invoices will be associated with this period. Exceptionally, additional invoices may be associated with a closed billing period if explicitly requested or approved by the customer.
- Cloud Service Provider (CSP)
- A company or organization that provides remote access to computing resources, infrastructure, or applications for a fee.
- Commitment
- A customer's agreement to either spend a defined monetary amount or consume a specific quantity of resources or services over a specified *period*.
- Commitment Discount
- A publicly available *contract commitment* that provides discounted pricing on preselected SKUs in exchange for a commitment to specific spend or usage goals over a specified *period*, based on publicly disclosed standard terms and pricing. Committed spend or usage is evenly distributed across predefined Contract Commitment Fulfillment Intervals (e.g., hourly), and unused benefits cannot be carried over to subsequent Intervals. Only one commitment discount may be applied to a single charge at a time, and it may overlap with one or more *negotiated discounts*.
This term has been used in the past by FinOps teams managing Public Cloud to refer to specific *contract commitments* (including Reserved Instances, Savings Plans and Committed Use Discounts) offered by cloud providers, and is defined here to maintain consistency with the terms of that subset of *contract commitments*.
Commitment discounts are classified with the following designations: 
  - Contract Commitment Offer Category: "Public"
  - Contract Commitment Benefit Category: "Discount"
  - Contract Commitment Model: "Continuous"
  - Unused benefits cannot be carried over to subsequent Contract Commitment Fulfillment Intervals
- Commitment Discount Flexibility
- A feature of *commitment discounts* that may further transform the predetermined amount of usage purchased or consumed based on additional, service-provider-specific requirements.
- Commitment Program
- A service-provider offering that allows a customer to enter into a *commitment*. Commitment programs include *commitment discounts*, *capacity reservations*, and other constructs that require advance spend or usage agreements.
- Contract
- A collection of agreed terms between a service provider and a customer.
- Contract Commitment
- A specific term within a *contract* that defines a measurable obligation agreed upon by a provider and a customer, such as a minimum spend or usage over an agreed period of time.
- Contracted Unit Price
- The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of negotiated discounts, if present, and exclusive of any other discounts. This price is denominated in the Billing Currency.
- Correction
- Any modification (including updates, additions, or omissions) to previously delivered records within a defined *delivery scope* (e.g., temporal grouping such as a *billing period* or non-temporal, logical grouping such as a *contract*).
A correction (lowercase) may consist of one or more simultaneous changes, including updates to or omission of previously delivered records, or the addition of new records that supplement previously delivered data within the affected *delivery scope*. This concept applies across all FOCUS datasets.
In contrast to the broader concept of correction (lowercase), the term "Correction" (capitalized) refers to a specific allowed value in the Charge Class column in Cost and Usage datasets. It designates *charges* used to correct cost or usage data from a previously *closed billing period*.
- Covered Charge
- A *charge* whose Billed Cost is fully or partially absorbed by a corresponding *covering charge*. Common examples include usage charges applied against *commitment discounts*, or consumption of SaaS offerings drawn from a prepayment, such as marketplace purchases.
- Covering Charge
- A purchase *charge* whose cost is applied against one or more *covered charges*, offsetting their Billed Cost. Common examples include *commitment discount* purchases, prepayment charges, and marketplace purchases that cover consumption-based usage.
- Credit
- A financial incentive or allowance granted by a service provider unrelated to other past/current/future charges.
- Custom Column
- A column not defined by FOCUS and included in a *FOCUS dataset*. Custom columns are prefixed with `x_` and provide additional context from *native datasets* beyond what is captured in FOCUS columns. See Dataset Completeness for inclusion requirements.

## D

- Dataset Artifact
- An abbreviated term for *dataset instance artifact*.
- Dataset Instance
- A specific implementation of a *FOCUS dataset* provided by a data generator. A Data Generator may provide multiple dataset instances of the same *FOCUS dataset*, each with different properties such as time granularity or differing custom column inclusions. For example, the same 'FOCUS Cost and Usage' *FOCUS dataset* may be provided at an hourly or daily time granularity by a Data Generator. Each would be a distinct Dataset Instance.
- Dataset Instance Artifact
- A physical representation of a specific *dataset instance* delivered by a data generator.
- Delivery Scope
- A dataset-specific boundary or set of boundaries that determines which records are included in a *dataset artifact* delivery. Scopes can be temporal (e.g., a *billing period*) or non-temporal (e.g., a *contract* or other logical grouping), and multiple scopes may be applicable for a single dataset depending on use case or delivery configuration. Scopes determine how Overwrite and Append *dataset artifact* deliveries, as well as corrections, are applied.
- Dimension
- A specification-defined categorical attribute that provides context or categorization to billing data.

## E

- Exclusive End Bound
- A Date/Time Format value that is not contained within the ending bound of a time period.

## F

- Finalized Tag
- A tag with one tag value chosen from a set of possible tag values after being processed by a set of service-provider-defined or user-defined rules.
- FinOps Cost and Usage Specification (FOCUS)
- An open-source specification that defines requirements for billing data.
- FOCUS Column
- A column defined by FOCUS and included in a *FOCUS dataset*. See the Columns section of each dataset for definitions.
- FOCUS Dataset
- A structured collection of columns that conforms to the BCP14 criteria established by FOCUS. All columns included must be defined in the FOCUS Columns section of the specification. In addition to these standardized columns, data generators include *custom columns* to capture information from *native datasets* that is not represented by *FOCUS columns*. If custom columns introduce record-splitting (i.e., a single original charge results in multiple rows), the data generator is responsible for ensuring that all cost and quantity metrics still meet the aggregation and consistency rules required by the specification.
The collection of datasets are designed to provide billing insight, additional context, metadata, mapping, or enrichment information that enhances the interpretability or completeness. See also: *Native Dataset*.
- FOCUS Dataset Column
- A column included in a *FOCUS dataset*. A FOCUS dataset column is either a *FOCUS column* or a *custom column*.

## I

- Inclusive Start Bound
- A Date/Time Format value that is contained within the beginning bound of a time period.
- Interruptible
- A category of compute resources that can be paused or terminated by the CSP within certain criteria, often advertised at reduced unit pricing when compared to the equivalent non-interruptible resource.
- Invoice
- A document that summarizes the charges for resources or services consumed by a customer.
- Invoice Issuer
- An entity responsible for issuing payable *invoices* for the *resources* or *services* consumed. Common examples include *cloud service providers*, *managed service providers*, or marketplace operators.
- Invoice Reconciliation
- The process of verifying that the costs, quantities, and applied adjustments on an *invoice* are equal to the underlying usage records and contracted rates for a specific *billing period*.
In the context of FOCUS, this process ensures consistency by reconciling cost and usage data across the invoice, the Invoice Detail dataset, and the Cost and Usage dataset to identify and resolve any discrepancies.
- Issued Invoice
- An *invoice* that has been formally *reconciled* and issued by the designated *invoice issuer* (Invoice Issue Status set to "Issued"). Once issued, the invoice becomes the authoritative financial document and is considered finalized. The financial data presented on the invoice is not expected to change.

## J

- JSON
- A common acronym for JavaScript Object Notation, a data format codified in ECMA-404 as a standard for human-readable, serializable data objects. This data format is used in FOCUS to communicate multiple pieces of information about a charge (tags, properties, etc.) in a single column.

## L

- List Unit Price
- The suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts. This price is denominated in the Billing Currency.

## M

- Managed Service Provider (MSP)
- A company or organization that provides outsourced management and support of a range of IT services, such as network infrastructure, cybersecurity, cloud computing, and more.
- Metric
- A FOCUS-defined column that provides numeric values, allowing for aggregation operations such as arithmetic operations (sum, multiplication, averaging etc.) and statistical operations.

## N

- National Currency
- A government-issued currency (e.g., US dollars, Euros).
- Native Dataset
- A dataset provided by a *data generator* in a format other than FOCUS. For *service providers*, this typically refers to their proprietary data exports (e.g., billing exports, contract details, or other FinOps-related datasets). For FinOps tool vendors, this refers to any non-FOCUS dataset they offer to *practitioners*. See also: *FOCUS Dataset*.
- Negotiated Discount
- A privately agreed *contract commitment* that provides discounted pricing in exchange for a commitment to specific spend or usage goals over a specified *period*, with terms and pricing specifically modified from standard. Multiple negotiated discounts may be applied to a single charge at a time, and they may overlap with a *commitment discount*.
Negotiated discounts are classified with the following designations: 
  - Contract Commitment Offer Category: "Negotiated"
  - Contract Commitment Benefit Category: "Discount"

## O

- On-Demand
- A service that is available and provided immediately or as needed, without requiring a pre-scheduled appointment or prior arrangement. In cloud computing, virtual machines can be created and terminated as needed, i.e., on demand.
- Open Billing Period
- A *billing period* with Billing Period Status set to "Open". Billing activities are ongoing, and the period remains subject to updates until formally closed.
- Origin Charge
- The charge that existed prior to an operation. This is used in the context of Data Generator-Calculated Split Cost Allocation to identify the charge that existed prior to the application of Data Generator-Calculated Split Cost Allocation to produce allocated charges.

## P

- Pascal Case
- Pascal Case (PascalCase, also known as UpperCamelCase) is a format for identifiers which contain one or more words meaning the words are concatenated together with no delimiter and the first letter of each word is capitalized.
- Period
- A time window, with a specifically defined start and end date/time.
- Potato
- A long and often painful conversation had by the FOCUS contributors. Sometimes the name of a thing that we could not yet name. No starchy root vegetables were harmed during the production of this specification. We thank potato for its contribution in the creation of this specification.
- Practitioner
- An individual who performs FinOps within an organization to maximize the business value of using cloud and cloud-like services.
- Price List
- A comprehensive list of prices offered by a service provider.

## R

- Refund
- A return of funds that have previously been charged.
- Resource
- A unique component that incurs a charge.
- Row
- A row in a FOCUS-compatible cost and usage dataset.

## S

- Service
- An offering that can be purchased from a service provider, and can include many types of usage or other charges; e.g., a cloud database service may include compute, storage, and networking charges.
- SKU
- A construct composed of the common properties of a product offering associated with one or many SKU Prices.
- SKU Price
- A pricing construct that encompasses SKU properties (e.g., functionality and technical specifications), along with core stable pricing details for a particular SKU, while excluding dynamic or negotiable pricing elements such as unit price amounts; currency (and related exchange rates); temporal validity (e.g., effective dates); and contract- or negotiation-specific factors (e.g., contract or account identifiers and negotiable discounts).
- Sub Account
- A sub account is an optional service-provider-supported construct for organizing resources and/or services connected to a billing account. Sub accounts must be associated with a billing account as they do not receive invoices.

## T

- Tag
- A metadata label assigned to a resource to provide information about it or to categorize it for organizational and management purposes.
- Tag Scheme
- A distinct framework for assigning metadata to charges, resources, or other assets. Different metadata types within a single provider (e.g., "tags" vs. "labels") are considered separate schemes. They can be user-defined (i.e., allowing user input) or provider-defined (i.e., controlled by the service provider).
- Tag Source
- A Resource or Service-Provider-defined construct for grouping resources and/or other Service-Provider-defined construct that a Tag can be assigned to.

## V

- Virtual Currency
- A proprietary currency (e.g., credits, tokens) issued by service providers and independent of government regulation.