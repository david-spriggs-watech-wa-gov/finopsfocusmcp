---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/appendix/metadata-examples/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2010-09-08"
fingerprint: b9e9733d64b4e1ed
---
# 8.9 Examples: Metadata

The following sections contain examples of metadata provided by a hypothetical FOCUS data generator called CrestNode to supply the required reference between the *FOCUS dataset artifacts* and the Metadata. Data Generator implementations will vary on how the metadata is disseminated; however, the data generator's chosen metadata delivery approach should be able to support the structure represented in this example.

In this example, the data generator supports delivery of FOCUS data via file export to a data storage system. It uses JSON as the format for providing the metadata. The data generator delivers data every 12 hours into a path structure described below:

| Type of data | Path | 
|---|---|
| Export location | `/FOCUS` | 
| Metadata location | `/FOCUS/metadata` | 
| Cost data location | `/FOCUS/data` | 

Here are some metadata examples for various scenarios:

## 8.9.1 Data Generator Metadata

### 8.9.1.1 Scenario

CrestNode provides metadata about the data generator as a part of their FOCUS data export. They provide the relevant data via the Data Generator schema object.

### 8.9.1.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/data_generator.json`.

The updated Data Generator-related metadata could look like this:

```
{
    "DataGenerator": "CrestNode"
}
```
## 8.9.2 Dataset Metadata Example

### 8.9.2.1 Scenario

CrestNode provides two FOCUS datasets: Cost and Usage and Contract. Each Schema metadata object includes the Dataset metadata to indicate which FOCUS Dataset the Schema conforms to.

### 8.9.2.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-1234-abcde-12345-abcde-12345.json`.

The schema for the data artifact conforming to the dataset FOCUS Cost and Usage.

```
{
  "SchemaId": "1234-abcde-12345-abcde-12345",
  "FocusVersion": "1.0",
  "CreationDate": "2024-01-01T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
          {
                "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["crestnode", "cn"]
          }
      ]
}
```
The schema for the data artifact conforming to the dataset FOCUS Contracts.

```
{
  "SchemaId": "1234-abcde-12345-abcde-12345",
  "FocusVersion": "1.0",
  "CreationDate": "2024-01-01T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-246811",
  "ColumnDefinition": [
          {
                "ColumnName": "ContractId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
              "ColumnName": "OverColumnName",
              "DataType": "STRING",
              "StringMaxLength": 64,
              "StringEncoding": "UTF-8"
          }
      ]
}
```
## 8.9.3 Deprecating Columns

### 8.9.3.1 Scenario

CrestNode has decided to deprecate columns prior to removal from their FOCUS data export. The column for deprecation is x\_awesome\_column3. The data generator creates a new Schema object to represent the new schema, with a unique SchemaId.

### 8.9.3.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-34567-abcde-34567-abcde-34567.json`.

The updated schema-related metadata could look like this:

```
{
  "SchemaId": "34567-abcde-34567-abcde-34567",
  "FocusVersion": "1.0",
  "CreationDate": "2024-03-02T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["crestnode", "cn"]
          },
          {
                "ColumnName": "x_awesome_column1",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "x_awesome_column2",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "x_awesome_column3",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8",
                "Deprecated": true
            }
      ]
}
```
For an example of how CrestNode ensures the schema metadata reference requirement is met see: Schema Metadata to FOCUS Data Reference

## 8.9.4 Renaming Columns

### 8.9.4.1 Scenario

CrestNode has decided to rename a column in their FOCUS data export. The column for rename is x\_awesome\_column1 and will be renamed to x\_awesome\_column\_one. The data generator creates a new Schema object to represent the new schema, with a unique SchemaId. After this schema definition is created if the data generator creates another schema, the PreviousColumnName is removed.

### 8.9.4.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-34567-abcde-34567-abcde-34567.json`.

The updated schema related metadata for the schema where the rename took place could look like this:

```
 {
  "SchemaId": "34567-abcde-34567-abcde-34567",
  "FocusVersion": "1.0",
  "CreationDate": "2024-03-02T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["crestnode", "cn"]
          },
          {
                "ColumnName": "x_awesome_column_one",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8",
                "PreviousColumnName": "x_awesome_column1"
          },
          {
                "ColumnName": "x_awesome_column2",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "x_awesome_column3",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8",
                "Deprecated": true
            }
      ]
}
```
The subsequent new schema metadata after the rename could look like this:

```
 {
  "SchemaId": "34567-abcde-34567-abcde-34567",
  "FocusVersion": "1.0",
  "CreationDate": "2024-03-02T12:01:03.083z",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["crestnode", "cn"]
          },
          {
                "ColumnName": "x_awesome_column_one",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "x_awesome_column2",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "x_awesome_column3",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8",
                "Deprecated": true
            }
      ]
}
```
For an example of how CrestNode ensures the schema metadata reference requirement is met see: Schema Metadata to FOCUS Data Reference

## 8.9.5 Schema Metadata

### 8.9.5.1 Scenario

CrestNode has only provided one Schema for their FOCUS data export. CrestNode provides a directory of schemas and each schema is a single file. CrestNode provides a file representing the schema for the data they provide.

### 8.9.5.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-1234-abcde-12345-abcde-12345.json`.

The updated schema-related metadata could look like this:

```
{
  "SchemaId": "1234-abcde-12345-abcde-12345",
  "FocusVersion": "1.0",
  "CreationDate": "2024-01-01T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["crestnode", "cn"]
          }
      ]
}
```
## 8.9.6 Schema Metadata to FOCUS Data Reference

### 8.9.6.1 Scenario

CrestNode makes a change to the Schema of their data exports. For each FOCUS data export, CrestNode includes a metadata reference to the schema object. Because multiple files are provided in each export, CrestNode has elected to include a metadata file in each export folder that includes the FOCUS schema reference that applies to the data export files within that folder. When the schema changes, they include the new Schema ID in their export metadata file of the new folder.

### 8.9.6.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/data/export1-metadata.json`

The export metadata could look like this:

```
{
  "SchemaId":"1234-abcde-12345-abcde-12345",
  "data_location":
  [
    {
      "filepath": "/FOCUS/data/export1/export1-part1.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export1/export1-part2.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export1/export1-part3.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export1/export1-part4.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    }
  ]
}
```
New metadata can be provided at a location such as `/FOCUS/data/export2-metadata.json`.

The new export metadata could look like this:

```
{
  "SchemaId":"23456-abcde-23456-abcde-23456",
  "data_location":
  [
    {
      "filepath": "/FOCUS/data/export2/export2-part1.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export2/export2-part2.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export2/export2-part3.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export2/export2-part4.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    }
  ]
}
```
## 8.9.7 Data Changed by Data Generator Using Data Generator Version

### 8.9.7.1 Scenario

CrestNode specifies the optional metadata property Data Generator Version in their Schema object. They made a change to the Cost and Usage *FOCUS dataset* they produce that does not adopt a new FOCUS Version, nor does it make a change to the included columns, but does impact values in the data. This example illustrates that Data Generator Version changes are independent of column changes, however data generator version changes may include column changes.

The data generator creates a new schema object to represent the new schema. The data generator includes both the FOCUS Version and Data Generator Version in the schema object.

### 8.9.7.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-56789-abcde-56789-abcde-56789.json`.

The updated schema-related metadata could look like this:

```
 {
  "SchemaId": "56789-abcde-56789-abcde-56789",
  "FocusVersion": "1.1",
  "DataGeneratorVersion": "2.4",
  "CreationDate": "2024-05-02T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "DataGeneratorTagPrefixes": ["crestnode", "cn"]
          },
          {
                "ColumnName": "x_awesome_column1",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "x_awesome_column2",
                "DataType": "DATETIME"
          }
      ]
}
```
For an example of how CrestNode ensures the schema metadata reference requirement is met see: Schema Metadata to FOCUS Data Reference

## 8.9.8 Adding New Columns

### 8.9.8.1 Scenario

CrestNode has decided to add additional columns to their FOCUS data export. The new columns are x\_awesome\_column1, x\_awesome\_column2, and x\_awesome\_column3. The data generator creates a new Schema object to represent the new schema, this schema object has a unique SchemaId. The subsequent data exports that use the new schema include the new schema's id as a reference to their corresponding schema object.

### 8.9.8.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-23456-abcde-23456-abcde-23456.json`.

The updated schema-related metadata could look like this:

```
 {
  "SchemaId": "23456-abcde-23456-abcde-23456",
  "FocusVersion": "1.0",
  "CreationDate": "2024-02-02T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
          {
                "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["crestnode", "cn"]
          },
          {
                "ColumnName": "x_awesome_column1",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "x_awesome_column2",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "x_awesome_column3",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          }
      ]
}
```
For an example of how CrestNode ensures the schema metadata reference requirement is met see: Schema Metadata to FOCUS Data Reference

## 8.9.9 Removing Columns

### 8.9.9.1 Scenario

CrestNode has decided to remove columns from their FOCUS data export. The column removed is x\_awesome\_column3. The data generator creates a new Schema object to represent the new schema, with a unique SchemaId.

### 8.9.9.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-34567-abcde-34567-abcde-34567.json`.

The updated schema related metadata could look like this:

```
 {
  "SchemaId": "34567-abcde-34567-abcde-34567",
  "FocusVersion": "1.0",
  "CreationDate": "2024-03-02T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["crestnode", "cn"]
          },
          {
                "ColumnName": "x_awesome_column1",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "x_awesome_column2",
                "DataType": "DATETIME"
          }
      ]
}
```
For an example of how CrestNode ensures the schema metadata reference requirement is met see: Schema Metadata to FOCUS Data Reference

## 8.9.10 Changing Column Metadata

### 8.9.10.1 Scenario

CrestNode has decided to change the datatype of column x\_awesome\_column1 from a string to a number. CrestNode creates a new Schema object with the modification to x\_awesome\_column2.

### 8.9.10.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-67891-abcde-67891-abcde-67891.json`.

The updated schema-related metadata could look like this:

```
 {
  "SchemaId": "67891-abcde-67891-abcde-67891",
  "FocusVersion": "1.0",
  "CreationDate": "2024-06-02T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["crestnode", "cn"]
          },
          {
                "ColumnName": "x_awesome_column1",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "x_awesome_column2",
                "DataType": "DATETIME"
          }
      ]
}
```
For an example of how CrestNode ensures the schema metadata reference requirement is met see: Schema Metadata to FOCUS Data Reference

## 8.9.11 Data Generator Metadata Error Correction

### 8.9.11.1 Scenario

CrestNode has discovered that while their export includes the column x\_awesome\_column3, the Schema metadata does not include this column. In this case, the data generator fixes the metadata in the existing schema object and does not need to create a new schema object. Reference metadata remains the same.

### 8.9.11.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-34567-abcde-34567-abcde-34567.json`.

The updated schema-related metadata could look like this:

```
 {
  "SchemaId": "34567-abcde-34567-abcde-34567",
  "FocusVersion": "1.0",
  "CreationDate": "2024-03-02T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["crestnode", "cn"]
          },
          {
                "ColumnName": "x_awesome_column1",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "x_awesome_column2",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          }
      ]
}
```
## 8.9.12 FOCUS Version Changed

### 8.9.12.1 Scenario

CrestNode's previous exports used FOCUS version 1.0. They are now going to adopt FOCUS version 1.1. It is required that they create a new schema metadata object which specifies the new FOCUS version via the FOCUS Version property—regardless of schema changes. In this example, the new FOCUS version adoption doesn't include columns changes. This is to illustrate that FOCUS version changes are independent of column changes, however, this scenario is unlikely.

### 8.9.12.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-45678-abcde-45678-abcde-45678.json`.

The updated schema-related metadata could look like this:

```
 {
  "SchemaId": "45678-abcde-45678-abcde-45678",
  "FocusVersion": "1.1",
  "CreationDate": "2024-04-02T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["crestnode", "cn"]
          },
          {
                "ColumnName": "x_awesome_column1",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "x_awesome_column2",
                "DataType": "DATETIME"
          }
      ]
}
```
For an example of how CrestNode ensures the schema metadata reference requirement is met see: Schema Metadata to FOCUS Data Reference

## 8.9.13 FOCUS Version Changed by Data Generator Using Data Generator Version

### 8.9.13.1 Scenario

CrestNode specifies the optional metadata property Data Generator Version in their Schema object. Their data generator version 2.2 supported FOCUS version 1.0. They are now going to adopt FOCUS Version 1.1 which requires that they update their Data Generator Version when updating the FOCUS Version. They create a new schema object designating that both properties have changed. In this example, the adoption of the new FOCUS version doesn't include additional columns. This is to illustrate that Data Generator Version can change independent of column changes; however, this scenario is unlikely.

The data generator creates a new schema object to represent the new schema. The data generator includes both the new FOCUS Version and Data Generator Version in the schema object.

### 8.9.13.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-45678-abcde-45678-abcde-45678.json`.

The updated schema-related metadata could look like this:

```
 {
  "SchemaId": "45678-abcde-45678-abcde-45678",
  "FocusVersion": "1.1",
  "DataGeneratorVersion": "2.3",
  "name": "New Columns",
  "CreationDate": "2024-04-02T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
      "DataType": "STRING",
      "StringMaxLength": 64,
      "StringEncoding": "UTF-8"
    },
    {
      "ColumnName": "BillingAccountName",
      "DataType": "STRING",
      "StringMaxLength": 64,
      "StringEncoding": "UTF-8"
    },
    {
      "ColumnName": "ChargePeriodStart",
      "DataType": "DATETIME"
    },
    {
      "ColumnName": "ChargePeriodEnd",
      "DataType": "DATETIME"
    },
    {
      "ColumnName": "BilledCost",
      "DataType": "DECIMAL",
      "NumericPrecision": 20,
      "NumberScale": 10
    },
    {
      "ColumnName": "EffectiveCost",
      "DataType": "DECIMAL",
      "NumericPrecision": 20,
      "NumberScale": 10
    },
    {
      "ColumnName": "Tags",
      "DataType": "JSON",
      "ProviderTagPrefixes": ["crestnode", "cn"]
    },
    {
      "ColumnName": "x_awesome_column1",
      "DataType": "STRING",
      "StringMaxLength": 64,
      "StringEncoding": "UTF-8"
    },
    {
      "ColumnName": "x_awesome_column2",
      "DataType": "DATETIME"
    }
  ]
}
```
For reference, the prior schema object looked like this:

```
 {
  "SchemaId": "34567-abcde-34567-abcde-34567",
  "FocusVersion": "1.0",
  "DataGeneratorVersion": "2.2",
  "CreationDate": "2024-04-02T12:01:03.083z",
  "Dataset": "FOCUS Cost and Usage",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
      "DataType": "STRING",
      "StringMaxLength": 64,
      "StringEncoding": "UTF-8"
    },
    {
      "ColumnName": "BillingAccountName",
      "DataType": "STRING",
      "StringMaxLength": 64,
      "StringEncoding": "UTF-8"
    },
    {
      "ColumnName": "ChargePeriodStart",
      "DataType": "DATETIME"
    },
    {
      "ColumnName": "ChargePeriodEnd",
      "DataType": "DATETIME"
    },
    {
      "ColumnName": "BilledCost",
      "DataType": "DECIMAL",
      "NumericPrecision": 20,
      "NumberScale": 10
    },
    {
      "ColumnName": "EffectiveCost",
      "DataType": "DECIMAL",
      "NumericPrecision": 20,
      "NumberScale": 10
    },
    {
      "ColumnName": "Tags",
      "DataType": "JSON",
      "ProviderTagPrefixes": ["crestnode", "cn"]
    },
    {
      "ColumnName": "x_awesome_column1",
      "DataType": "STRING",
      "StringMaxLength": 64,
      "StringEncoding": "UTF-8"
    },
    {
      "ColumnName": "x_awesome_column2",
      "DataType": "DATETIME"
    }
  ]
}
```
For an example of how CrestNode ensures the schema metadata reference requirement is met see: Schema Metadata to FOCUS Data Reference

## 8.9.14 Dataset Instance Metadata

### 8.9.14.1 Scenario

CrestNode provides three dataset instances: "Cost and Usage Daily," "Cost and Usage Hourly," and "Contract Commitments," corresponding to the FOCUS datasets Cost and Usage and Contract Commitment. CrestNode also provides a metadata directory containing a single file with metadata for each dataset instance.

### 8.9.14.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/dataset_instances.json`.

The updated schema-related metadata could look like this:

```
[
  {
    "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-246811",
    "DatasetInstanceName": "Contract Commitments Report",
    "FocusDatasetId": "ContractCommitment"
  },
  {
    "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
    "DatasetInstanceName": "Cost and Usage Daily",
    "FocusDatasetId": "CostAndUsage"
  },
  {
    "DatasetInstanceId": "178151-ja23h1287-387151-dbad145e-134657",
    "DatasetInstanceName": "Cost and Usage Hourly",
    "FocusDatasetId": "CostAndUsage"
  }
]
```
## 8.9.15 Recency Metadata

### 8.9.15.1 Scenario

CrestNode has elected to add recency metadata to its FOCUS data export. CrestNode provides a directory of recency metadata for each dataset they provide and each recency object is a single file.

### 8.9.15.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/recency/recency-1234-abcde-12345-abcde-12345.json`.

The provided recency metadata for a time series dataset could look like this:

```
{
  "DatasetInstanceId": "1234-abcde-12345-abcde-12345",
  "RecencyLastUpdateDate": "2025-01-291T12:01:03.083z",
  "TimeSectors": [
    {
      "TimeSectorStart": "2025-01-27T0:00:00z",
      "TimeSectorEnd" : "2025-01-27T1:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T1:00:00z",
      "TimeSectorEnd" : "2025-01-27T2:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T2:00:00z",
      "TimeSectorEnd" : "2025-01-27T3:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T3:00:00z",
      "TimeSectorEnd" : "2025-01-27T4:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T4:00:00z",
      "TimeSectorEnd" : "2025-01-27T5:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T5:00:00z",
      "TimeSectorEnd" : "2025-01-27T6:00:00z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T6:00:00z",
      "TimeSectorEnd" : "2025-01-27T7:00:00z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    }
  ]
}
```
The provided recency metadata for non-time series dataset could look like this:

```
{
  "DatasetInstanceId": "54321-abcde-12345-abcde-12345",
  "RecencyLastUpdateDate": "2025-01-291T12:01:03.083z",
  "DatasetInstanceLastUpdated" : "2025-01-29T04:00:00z",
  "DatasetInstanceComplete" : true
}
```
## 8.9.16 Recency Metadata Update (Non Time Series)

### 8.9.16.1 Scenario

CrestNode provides recency metadata to accompany their FOCUS data export. CrestNode updates their FOCUS Contracts dataset, a non time-series dataset, every day. In this case, the most recent update to the recency data indicates the dataset and associated data artifact has been updated and is considered complete.

### 8.9.16.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/recency/recency-54321-abcde-12345-abcde-12345.json`.

The provided recency metadata for non-time series dataset could look like this:

```
{
  "DatasetInstanceId": "54321-abcde-12345-abcde-12345",
  "RecencyLastUpdate": "2025-01-291T15:01:03.083z",
  "DatasetInstanceLastUpdated" : "2025-01-29T010:00:00z",
  "DatasetInstanceComplete" : true
}
```
## 8.9.17 Recency Metadata Update (Time Series)

### 8.9.17.1 Scenario

CrestNode provides recency metadata to accompany its FOCUS data export. CrestNode updates its FOCUS Cost and Usage dataset (time series) every hour; however, the data lags by two days. Here, the most recent update to the recency data indicates the previous time sectors are now TimeSectorComplete. It also indicates that previous time sectors have been updated in the dataset. New time sectors have also been added.

### 8.9.17.2 Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/recency/recency-1234-abcde-12345-abcde-12345.json`.

The provided recency metadata for time series dataset could look like this:

```
{
  "DatasetInstanceId": "1234-abcde-12345-abcde-12345",
  "RecencyLastUpdateDate": "2025-01-291T12:01:03.083z",
  "TimeSectors": [
    {
      "TimeSectorStart": "2025-01-27T0:00:00z",
      "TimeSectorEnd" : "2025-01-27T1:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T1:00:00z",
      "TimeSectorEnd" : "2025-01-27T2:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T2:00:00z",
      "TimeSectorEnd" : "2025-01-27T3:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T3:00:00z",
      "TimeSectorEnd" : "2025-01-27T4:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T4:00:00z",
      "TimeSectorEnd" : "2025-01-27T5:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T5:00:00z",
      "TimeSectorEnd" : "2025-01-27T6:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T6:00:00z",
      "TimeSectorEnd" : "2025-01-27T7:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T11:15:24z"
    },
    {
      "TimeSectorStart": "2025-01-27T7:00:00z",
      "TimeSectorEnd" : "2025-01-27T8:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T11:15:24z"
    },
    {
      "TimeSectorStart": "2025-01-27T8:00:00z",
      "TimeSectorEnd" : "2025-01-27T9:00:00z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T9:00:00z",
      "TimeSectorEnd" : "2025-01-27T10:00:00z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T10:23:10z"
    },
    {
      "TimeSectorStart": "2025-01-27T10:00:00z",
      "TimeSectorEnd" : "2025-01-27T11:00:00z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T11:15:24z"
    }
  ]
}
```
The provided recency metadata for non-time series dataset could look like this:

```
{
  "Dataset": "1234-abcde-12345-abcde-12345",
  "RecencyLastUpdateDate": "2025-01-291T12:01:03.083z",
  "DatasetInstanceLastUpdated" : "2025-01-29T04:00:00z",
  "DatasetInstanceComplete" : true
}
```