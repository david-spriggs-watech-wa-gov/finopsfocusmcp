---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/attributes/unit-format/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: "67b368db3ca620b4"
---
# 4.15 Unit Format

Billing data frequently captures data measured in units related to data size, count, time, and other *dimensions*. The Unit Format attribute provides a standard for expressing units of measure in columns appearing in a *FOCUS dataset*.

## 4.15.1 Requirements

Column conforming to UnitFormat attribute MUST adhere to the following requirements:

- *FOCUS dataset column* MUST adhere to the following base unit requirements:
  - *FOCUS dataset column* MUST include at least one base unit.
  - *FOCUS dataset column* MUST use one of the allowed data size unit abbreviations listed below for data size base units.
  - *FOCUS dataset column* MUST use the allowed data size unit abbreviations in the same form for both singular and plural units.
  - *FOCUS dataset column* MUST use the allowed abbreviation for exabit, exabyte, exbibit, or exbibyte when representing values exceeding 10^18.
  - *FOCUS dataset column* MUST use the allowed abbreviation for bit or byte when representing values smaller than one byte.
  - *FOCUS dataset column* MUST use one of the allowed time-based unit names listed below for time-based base units.
  - *FOCUS dataset column* SHOULD use one of the recommended count-based unit names listed below for count-based base units.
  - *FOCUS dataset column* SHOULD use capitalized nouns for base units that do not correspond to any of the allowed base unit names listed below.
  - *FOCUS dataset column* MAY include a count-based base unit that is not listed as one of the allowed values.
- *FOCUS dataset column* MAY include a unit quantity expressed as a positive integer.
- *FOCUS dataset column* expressing a compound unit MUST use a hyphen (`-`) to separate base units (e.g., `GB-Hours`).
- *FOCUS dataset column* expressing a compound unit SHOULD use the `<singular-base-unit>-<plural-base-unit>` format (e.g., `GB-Hours`, `MB-Days`, `Request-Tokens`).
- *FOCUS dataset column* expressing a ratio unit MUST use a slash (`/`) to separate the numerator and denominator (e.g., `GB/Hour` to signify gigabytes per hour).
- *FOCUS dataset column* expressing a ratio unit MAY include a denominator quantity expressed as a positive integer.
- *FOCUS dataset column* expressing a ratio unit and including a denominator quantity SHOULD use the `<plural-units>/<denominator-quantity> <plural-time-units>` format (e.g., `Units/3 Months`).
- *FOCUS dataset column* expressing a ratio unit with a compound unit numerator SHOULD use the `<compound-unit>/<singular-time-unit>` format (e.g., `Core-Hours/Day`).
- *FOCUS dataset column* expressing a ratio unit with a time denominator SHOULD use the `<plural-units>/<singular-time-unit>` format (e.g., `GB/Hour`, `PB/Day`).
- *FOCUS dataset column* expressing a simple unit SHOULD use the `<plural-units>` format (e.g., `GB`, `Seconds`).
- *FOCUS dataset column* including a unit quantity SHOULD use the `<unit-quantity> <plural-units>` format (e.g., `1000 Tokens`, `1000 Characters`).

## 4.15.2 Definitions

The normative requirements above refer to the following definitions.

### 4.15.2.1 Measurement Unit

A standardized expression that describes how quantities in a *FOCUS dataset* are denominated (e.g., `GB`, `Seconds`, `GB-Hours`, `10 GB/Hour`, `Units/3 Months`).

### 4.15.2.2 Base Unit

An atomic unit that serves as a building block for all measurement units; can be a data size unit, time-based unit, or count-based unit (e.g., `GB`, `Hour`, `Token`).

### 4.15.2.3 Simple Unit

A measurement unit that contains exactly one base unit, optionally preceded by a unit quantity (e.g., `GB`, `Seconds`, `1000 Tokens`).

### 4.15.2.4 Compound Unit

A measurement unit that combines two base units using a hyphen (`-`), optionally preceded by a unit quantity (e.g., `GB-Hours`, `MB-Days`, `Request-Tokens`).

### 4.15.2.5 Ratio Unit

A measurement unit that expresses one base unit or compound unit per another using a slash (`/`), optionally including a denominator quantity (e.g., `GB/Hour`, `Units/3 Months`, `Core-Hours/Day`).

### 4.15.2.6 Unit Quantity

A positive integer included in a measurement unit, indicating the granularity (e.g., `1000` in `1000 Tokens`).

### 4.15.2.7 Denominator Quantity

A positive integer included in the denominator of a ratio unit, indicating the granularity of the denominator (e.g., `3` in `Units/3 Months`).

## 4.15.3 Base Unit Names

### 4.15.3.1 Allowed Data Size Unit Abbreviations

Data size units are nouns representing data size measured in bits or bytes, expressed using standard abbreviations. Each abbreviation can be used for both the singular and plural form of the unit.

For example:

- `GB` represents both the singular and plural form of a gigabyte.
- `TB` is a valid base unit name, while `TBs` and `terabyte` are considered invalid.

Values larger than 10^18 must use the abbreviation for exabit, exabyte, exbibit, or exbibyte. Values smaller than a byte must use the abbreviation for bit or byte.

The table below lists the valid abbreviations for data size units from a single bit or byte to 10^18 bits or bytes.

| Data size in bits | Data size in bytes | 
|---|---|
| b (bit = 10^0) | B (byte = 10^0) | 
| Kb (kilobit = 10^3) | KB (kilobyte = 10^3) | 
| Mb (megabit = 10^6) | MB (megabyte = 10^6) | 
| Gb (gigabit = 10^9) | GB (gigabyte = 10^9) | 
| Tb (terabit = 10^12) | TB (terabyte = 10^12) | 
| Pb (petabit = 10^15) | PB (petabyte = 10^15) | 
| Eb (exabit = 10^18) | EB (exabyte = 10^18) | 
| Kib (kibibit = 2^10) | KiB (kibibyte = 2^10) | 
| Mib (mebibit = 2^20) | MiB (mebibyte = 2^20) | 
| Gib (gibibit = 2^30) | GiB (gibibyte = 2^30) | 
| Tib (tebibit = 2^40) | TiB (tebibyte = 2^40) | 
| Pib (pebibit = 2^50) | PiB (pebibyte = 2^50) | 
| Eib (exbibit = 2^60) | EiB (exbibyte = 2^60) | 

### 4.15.3.2 Allowed Time-Based Unit Names

Time-based units are nouns representing a discrete time period. They can be used alone to indicate duration, combined with another unit to form a compound unit (e.g., `GB-Hours`), or a per-time ratio unit (e.g., `GB/Hour`).

The table below lists allowed time-based base units.

| Time-based Unit (Singular) | Time-based Unit (Plural) | 
|---|---|
| Year | Years | 
| Month | Months | 
| Day | Days | 
| Hour | Hours | 
| Minute | Minutes | 
| Second | Seconds | 
| Millisecond | Milliseconds | 
| Microsecond | Microseconds | 

### 4.15.3.3 Recommended Count-Based Unit Names

A count-based unit is a noun representing a discrete number of items, events, or actions. For example, a count-based unit can represent the number of requests, instances, tokens, or connections.

The table below lists recommended names for count-based base units.

| Count-based Unit (Singular) | Count-based Unit (Plural) | 
|---|---|
| Count | Counts | 
| Unit | Units | 
| Request | Requests | 
| Token | Tokens | 
| Connection | Connections | 
| Certificate | Certificates | 
| Domain | Domains | 
| Core | Cores | 

*Note: When a count-based base unit is not covered by the recommended values, a new value can be used as long as it is capitalized.*

## 4.15.6 Description

Indicates standards for expressing measurement units in columns appearing in a *FOCUS dataset*.