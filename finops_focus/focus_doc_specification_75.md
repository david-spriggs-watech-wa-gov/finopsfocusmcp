---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/changelog/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "8308653a8062fe63"
---
1. Specification
2. v1.4
3. Changelog

# Changelog

What changed from 1.3 to 1.4

Columns:
                                            +47
                                                                -2
                                                                \~14

Attributes:
                                            +6
                                                                -3

Features:
                                            +2
                                                                                    \~21

Conditions:

Glossary:
                                            +18
                                                                -2
                                                                \~15

## Columns

### RemovedRemoved Columns (2)

Provider - DEPRECATED

Publisher - DEPRECATED

### ChangedChanged Columns (14)

Contract Commitment Period EndDescription Short: The \*exclusive end bound\* of a \*contract commitment period\*.The \*exclusive end bound\* of a contract commitment period.

Contract Commitment Period StartDescription Short: The \*inclusive start bound\* of a \*contract commitment period\*.The \*inclusive start bound\* of a contract commitment period.

Contract Period EndDescription Short: The \*exclusive end bound\* of a \*contract period\*.The \*exclusive end bound\* of a contract period.

Contract Period StartDescription Short: The \*inclusive start bound\* of a \*contract period\*.The \*inclusive start bound\* of a contract period.

Allocated Method DetailsColumn Type: DimensionDimension / Metric

Billed CostDescription Short: A \*charge\* serving as the basis for invoicing, inclusive of…Cost of a \*charge\* as invoiced by the \[\*invoice issuer\*\](#glossary:invoice-issuer)…

Charge ClassDescription Short: Indicates whether the \*row\* represents a correction to a previously…Indicates whether a \*charge\* represents a correction to a previously…

Contract AppliedDescription Short: A set of properties that associate a charge with one…A set of properties that associate a \*charge\* with one…Column Type: Dimension and MetricDimension / Metric

Effective CostDescription Short: The \*amortized\* cost of the \*charge\* after applying all reduced…Cost of a \*charge\* based on the \*resources\* used, \*services\*…

Host Provider NameDescription Short: The name of the entity whose \*resources\* are used by…The name of the entity whose \*resources\* are used by…

Invoice IDFeature Level: RecommendedConditional

Pricing CurrencyDescription Short: The national or virtual currency denomination that a \*resource\* or…The \*national\* or \*virtual currency\* denomination that a \*resource\* or…

Pricing Currency Effective CostDescription Short: The cost of the \*charge\* after applying all reduced rates,…The PricingCurrency-denominated equivalent of Effective Cost, representing the cost of…

Service Provider NameVersion Introduced: 1.3 Introduced as a replacement for \[ProviderName\](#providername)1.3 Introduced as a replacement for the removed ProviderName column

## Attributes

### AddedNew Attributes (6)

### RemovedRemoved Attributes (3)

Column Handling

Discount Handling

Invoice Handling

## Features

### AddedNew Features (2)

### ChangedChanged Features (21)

Account StructuresVersion Introduced: 0.5

Billed Cost and Invoice AlignmentVersion Introduced: 0.5

Charge CategorizationVersion Introduced: 1.0

Commit Usage and Under UsageVersion Introduced: 1.0

Contract CommitmentsVersion Introduced: 1.3

Cost and Usage AttributionVersion Introduced: 1.0

Cost ComparisonVersion Introduced: 0.5

Custom ColumnsVersion Introduced: 0.5

Data Generator-Calculated Split Cost AllocationVersion Introduced: 1.3

Data GranularityVersion Introduced: 0.5

Dataset Instance MetadataVersion Introduced: 1.3

Effective Cost AnalysisVersion Introduced: 0.5

LocationVersion Introduced: 1.0

Marketplace PurchasesVersion Introduced: 1.0

Participating Entity IdentificationVersion Introduced: 1.1

Recency MetadataVersion Introduced: 1.3

Resource UsageVersion Introduced: 1.0

Schema MetadataVersion Introduced: 1.1

Service CategorizationVersion Introduced: 1.1

Service Provider ServicesVersion Introduced: 0.5

Verification, Comparison, and Fluctuation Tracking of Unit PricesVersion Introduced: 1.0

## Conditions

## Glossary

### RemovedRemoved Terms (2)

Billed Cost

Effective Cost

### ChangedChanged Terms (15)

FOCUS DatasetDefinition Md: A structured collection of columns that conforms to the BCP14…A structured collection of columns that conforms to the BCP14…

Allocated ChargeDefinition Md: The \[charge\](#glossary:charge) that was created as the result of an…The \[charge\](#glossary:charge) that was created as the result of an…

Allocated MethodDefinition Md: The process or formula by which cost is being allocated…The process or formula by which cost is being allocated…

Charge PeriodDefinition Md: The time window for which a charge is effective, inclusive…The time window for which a charge is effective, inclusive…

Commitment DiscountDefinition Md: A billing discount model that offers reduced rates on preselected…A publicly available \[\*contract commitment\*\](#glossary:contract-commitment) that provides discounted pricing on…

Contracted Unit PriceDefinition Md: The agreed-upon unit price for a single \[Pricing Unit\](#pricingunit) of…The agreed-upon unit price for a single \[Pricing Unit\](#datasets.costandusage.pricingunit) of…

CorrectionDefinition Md: A charge to correct cost or usage data in a…Any modification (including updates, additions, or omissions) to previously delivered…

Dataset InstanceDefinition Md: A specific implementation of a \[\*FOCUS dataset\*\](#glossary:FOCUS-dataset) provided by a…A specific implementation of a \[\*FOCUS dataset\*\](#glossary:FOCUS-dataset) provided by a…

Dataset Instance ArtifactDefinition Md: A physical representation of a specific \[\*dataset instance\*\](#glossary:dataset-instance) delivered by…A physical representation of a specific \[\*dataset instance\*\](#glossary:dataset-instance) delivered by…

List Unit PriceDefinition Md: The suggested service-provider-published unit price for a single \[Pricing Unit\](#pricingunit)…The suggested service-provider-published unit price for a single \[Pricing Unit\](#datasets.costandusage.pricingunit)…

Negotiated DiscountDefinition Md: A contractual agreement where a customer commits to specific spend…A privately agreed \[\*contract commitment\*\](#glossary:contract-commitment) that provides discounted pricing in…

Origin ChargeDefinition Md: The \[charge\](#glossary:charge) that existed prior to an operation. This is…The \[charge\](#glossary:charge) that existed prior to an operation. This is…

ServiceDefinition Md: An offering that can be purchased from a service provider,…An offering that can be purchased from a service provider,…

SKU PriceDefinition Md: A pricing construct that encompasses SKU properties (e.g., functionality and…A pricing construct that encompasses SKU properties (e.g., functionality and…

TermDefinition Md: An agreement specified on a \[\*contract\*\](#glossary:contract).An agreement specified on a \[\*contract\*\](#glossary:contract) or \[\*invoice\*\](#glossary:invoice).