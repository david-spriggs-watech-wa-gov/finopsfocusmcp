---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/metadata/schema/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2010-04-05"
fingerprint: f0f96b01b4f663e5
---
# 5.4 Schema

The schema metadata object and its content provide information about the structure of the data provided.

## 5.4.1 Requirements

Schema adheres to the following requirements:

- Schema MUST be present in the Metadata.
- Schema MUST be structured as a collection of objects.
- Schema MUST NOT be null.
- Schema collection MUST contain at least one object for every DatasetInstance object.
- Schema collection MUST NOT contain null objects.
- Schema collection object MUST be associated with one and only one DatasetInstance object.
- Schema collection object MUST be added to the collection whenever the structure of the *dataset instance artifacts* changes (including, but not limited to, additions or removals of columns, modifications to any ColumnDefinition, or updates to the FOCUSVersion or DataGeneratorVersion).
- Schema collection object MUST be referenced by *dataset instance artifacts* that conform to the structure defined by that Schema collection object.
- Schema collection object MUST define the exact structure of the *dataset instance artifacts* that reference it.
- Schema collection object MUST be retrievable independently from the *dataset instance artifacts* that conform to the structure defined by that Schema collection object.
- Schema collection object SHOULD be provided separately from the *dataset instance artifacts* that conform to the structure defined by that Schema collection object.
- Schema collection object MAY be provided through the structure and/or schema of the delivery mechanism (e.g., database tables).

## 5.4.2 Examples

There are many scenarios that would result in an update to the Schema metadata. These scenarios include but are not limited to:

For an example of the FOCUS schema metadata, please refer to: Schema Metadata Example.

## 5.4.3 Metadata ID

Schema

## 5.4.4 Metadata Name

Schema

## 5.4.5 Version Introduced

1.0

## 5.4.6 Schema ID

The Schema ID provides the reference item to associate which Schema was used for the generation of a *FOCUS dataset*.

SchemaId adheres to the following requirements:

- SchemaId MUST be present in an object within the Schema collection.
- SchemaId MUST be of type String.
- SchemaID MUST NOT be null.
- SchemaId SHOULD be a Globally Unique Identifier (GUID).

### 5.4.6.1 Metadata ID

SchemaId

### 5.4.6.2 Metadata Name

Schema ID

### 5.4.6.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Mandatory | 
| Allows nulls | False | 
| Data type | String | 
| Value format | GUID (recommended) | 

### 5.4.6.4 Version Introduced

1.0

## 5.4.7 Creation Date

Date the schema was created.

CreationDate adheres to the following requirements:

- CreationDate MUST be present in an object within the Schema collection.
- CreationDate MUST be of type Date/Time.
- CreationDate MUST conform to DateTimeFormat.
- CreationDate MUST NOT be null.

### 5.4.7.1 Metadata ID

CreationDate

### 5.4.7.2 Metadata Name

Creation Date

### 5.4.7.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Mandatory | 
| Allows nulls | False | 
| Data type | Date/Time | 
| Value format | Date/Time Format | 

### 5.4.7.4 Version Introduced

1.0

## 5.4.8 FOCUS Version

The version of FOCUS utilized for building the dataset.

FocusVersion adheres to the following requirements:

- FocusVersion MUST be present in an object within the Schema collection.
- FocusVersion MUST be of type String.
- FocusVersion MUST NOT be null.
- FocusVersion MUST match one of the published versions of the FOCUS specification.
- FocusVersion MUST match the version of the FOCUS specification that the *dataset instance artifact* conforms to.

### 5.4.8.1 Metadata ID

FocusVersion

### 5.4.8.2 Metadata Name

FOCUS Version

### 5.4.8.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Mandatory | 
| Allows nulls | False | 
| Data type | String | 
| Value format | \<not specified> | 

### 5.4.8.4 Version Introduced

1.0

## 5.4.9 Data Generator Version

The DataGeneratorVersion may be supplied to declare the version of logic by which the *dataset instance artifact* was generated and is separate from FOCUS Version. DataGeneratorVersion allows for the provider to specify changes that may not result in a structural change in the data. It is suggested that the DataGeneratorVersion use a versioning approach such as SemVer version.

DataGeneratorVersion adheres to the following requirements:

- DataGeneratorVersion MAY be present in an object within the Schema collection.
- DataGeneratorVersion MUST be of type String.
- DataGeneratorVersion MUST conform to StringHandling requirements.
- DataGeneratorVersion MUST NOT be null.
- DataGeneratorVersion MUST be changed when FocusVersion is changed.
- Data generators MUST document what changes are present in the DataGeneratorVersion.

### 5.4.9.1 Metadata ID

DataGeneratorVersion

### 5.4.9.2 Metadata Name

Data Generator Version

### 5.4.9.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Optional | 
| Allows nulls | False | 
| Data type | String | 
| Value format | \<not specified> | 

### 5.4.9.4 Version Introduced

1.1

## 5.4.10 Dataset Instance ID

The Dataset Instance ID is a unique identifier for the specific dataset instance provided by the data generator. It identifies the dataset instance that this schema and the corresponding dataset artifacts are aligned with.

DatasetInstanceId adheres to the following requirements:

- DatasetInstanceId MUST be present in an object within the Schema collection.
- DatasetInstanceID MUST be of type String.
- DatasetInstanceID MUST NOT be null.
- DatasetInstanceID MUST be a unique identifier within a data generator.

### 5.4.10.1 Metadata ID

DatasetInstanceId

### 5.4.10.2 Metadata Name

Dataset Instance ID

### 5.4.10.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Mandatory | 
| Allows nulls | False | 
| Data type | String | 
| Value format | GUID (recommended) | 

### 5.4.10.4 Version Introduced

1.3

## 5.4.11 Column Definition

The FOCUS metadata schema column definition provides a list of the columns present in the *dataset instance artifact* along with metadata about the columns.

### 5.4.11.1 Requirements

ColumnDefinition adheres to the following requirements:

- ColumnDefinition MUST be present in an object within the Schema collection.
- ColumnDefinition MUST be structured as a collection of objects.
- ColumnDefinition MUST NOT be null.
- ColumnDefinition collection MUST contain one and only one object for every column provided in *dataset instance artifacts* that reference the parent Schema object.
- ColumnDefinition collection MUST NOT contain null objects.

### 5.4.11.2 Metadata ID

ColumnDefinition

### 5.4.11.3 Metadata Name

Column Definition

### 5.4.11.4 Version Introduced

1.0

### 5.4.11.5 Column Name

The name of the column provided in the *FOCUS dataset*.

ColumnName adheres to the following requirements:

- ColumnName MUST be present in an object within the ColumnDefinition collection.
- ColumnName MUST be of type String.
- ColumnName MUST NOT be null.

#### 5.4.11.5.1 Metadata ID

ColumnName

#### 5.4.11.5.2 Metadata Name

Column Name

#### 5.4.11.5.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Mandatory | 
| Allows nulls | False | 
| Data type | String | 
| Value format | \<not specified> | 

#### 5.4.11.5.4 Version Introduced

1.0

### 5.4.11.6 Data Type

The data type of the column provided in the *FOCUS dataset*.

DataType adheres to the following requirements:

- DataType MUST be present in an object within the ColumnDefinition collection.
- DataType MUST be of type String.
- DataType MUST NOT contain null values.

#### 5.4.11.6.1 Metadata ID

DataType

#### 5.4.11.6.2 Metadata Name

Data Type

#### 5.4.11.6.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Mandatory | 
| Allows nulls | False | 
| Data type | String | 
| Value format | \<not specified> | 

#### 5.4.11.6.4 Version Introduced

1.0

### 5.4.11.7 Deprecated

The deprecation status of a column in a Dataset Instance.

Deprecated adheres to the following requirements:

- Deprecated MUST be present in an object within the ColumnDefinition collection when the column is planned for removal.
- Deprecated MUST be of type Boolean.
- Deprecated MUST NOT contain null values.
- Deprecated SHOULD only be "true" when the column is deprecated.
- Deprecated MUST be "true" when the data generator removes a column at a future date, or the column has been identified for deprecation for the FOCUS version identified in the schema definition.

#### 5.4.11.7.1 Metadata ID

Deprecated

#### 5.4.11.7.2 Metadata Name

Deprecated

#### 5.4.11.7.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Conditional | 
| Allows nulls | False | 
| Data type | Boolean | 
| Value format | \<not specified> | 

#### 5.4.11.7.4 Version Introduced

1.2

### 5.4.11.8 Numeric Precision

Numeric Precision is the maximum number of digits for the values in the column.

NumericPrecision adheres to the following requirements:

- NumericPrecision SHOULD be present in an object within the ColumnDefinition collection when the column is of Decimal data type.
- NumericPrecision MUST be of type Integer.
- NumericPrecision MUST NOT contain null values.

#### 5.4.11.8.1 Metadata ID

NumericPrecision

#### 5.4.11.8.2 Metadata Name

Numeric Precision

#### 5.4.11.8.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Recommended | 
| Allows nulls | False | 
| Data type | Integer | 
| Value format | Numeric Format | 

#### 5.4.11.8.4 Version Introduced

1.0

### 5.4.11.9 Number Scale

The number scale of the data provides the maximum number of digits after the decimal point in decimal numbers.

NumberScale adheres to the following requirements:

- NumberScale SHOULD be present in an object within the ColumnDefinition collection when the column is of Decimal data type.
- NumberScale MUST be of type Integer.
- NumberScale MUST conform to NumericFormat requirements.
- NumberScale MUST NOT be null.

#### 5.4.11.9.1 Metadata ID

NumberScale

#### 5.4.11.9.2 Metadata Name

Number Scale

#### 5.4.11.9.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Recommended | 
| Allows nulls | False | 
| Data type | Integer | 
| Value format | Numeric Format | 

#### 5.4.11.9.4 Version Introduced

1.0

### 5.4.11.10 PreviousColumnName

The PreviousColumnName field indicates that on that schema the column where the key is included was renamed.

PreviousColumnName adheres to the following requirements:

- PreviousColumnName MUST be present in an object within the ColumnDefinition collection when the column was renamed.
- When PreviousColumnName is present, PreviousColumnName adheres to the following normative requirements:
  - PreviousColumnName MUST be of type String.
  - PreviousColumnName MUST not be null.
  - PreviousColumnName MUST be the name used in previous versions of the schema.
  - PreviousColumnName MUST NOT be present in schema versions created after the rename.

#### 5.4.11.10.1 Metadata ID

PreviousColumnName

#### 5.4.11.10.2 Metadata Name

Previous Column Name

#### 5.4.11.10.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Conditional | 
| Allows nulls | False | 
| Data type | String | 
| Value format | \<not specified> | 

#### 5.4.11.10.4 Version Introduced

1.2

### 5.4.11.11 Provider Tag Prefixes

The Provider Tag Prefixes define the list of prefixes used in the tag name of provider-defined tags. This metadata is useful for the consumer to identify which tags are provider-defined vs user-defined.

ProviderTagPrefixes adheres to the following requirements:

- ProviderTagPrefixes MUST be present in an object within the ColumnDefinition collection when ColumnName is "Tags".
- ProviderTagPrefixes MUST be of type Collection of Strings.
- ProviderTagPrefixes SHOULD be easily associated with the data generator who generated the *dataset instance* and the corresponding *dataset instance artifacts*.

#### 5.4.11.11.1 Metadata ID

ProviderTagPrefixes

#### 5.4.11.11.2 Metadata Name

Provider Tag Prefixes

#### 5.4.11.11.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Conditional | 
| Allows nulls | False | 
| Data type | Collection of Strings | 
| Value format | \<not specified> | 

#### 5.4.11.11.4 Version Introduced

1.0

### 5.4.11.12 String Encoding

The string encoding scheme of the column provided in the *FOCUS dataset*.

StringEncoding adheres to the following requirements:

- StringEncoding MUST be present in an object within the ColumnDefinition collection when this information is required in order to successfully read the data.
- StringEncoding MUST be of type String.
- StringEncoding MUST NOT be null.

#### 5.4.11.12.1 Metadata ID

StringEncoding

#### 5.4.11.12.2 Metadata Name

StringEncoding

#### 5.4.11.12.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Conditional | 
| Allows nulls | False | 
| Data type | String | 
| Value format | \<not specified> | 

#### 5.4.11.12.4 Version Introduced

1.0

### 5.4.11.13 String Max Length

The string max length of the data that can be stored in the column.

StringMaxLength adheres to the following requirements:

- StringMaxLength SHOULD be present in an object within the ColumnDefinition collection when the column is of String data type.
- StringMaxLength MUST be of type Integer.
- StringMaxLength MUST NOT be null.

#### 5.4.11.13.1 Metadata ID

StringMaxLength

#### 5.4.11.13.2 Metadata Name

String Max Length

#### 5.4.11.13.3 Content Constraints

| Constraint | Value | 
|---|---|
| Feature level | Recommended | 
| Allows nulls | False | 
| Data type | Integer | 
| Value format | Numeric Format | 

#### 5.4.11.13.4 Version Introduced

1.0