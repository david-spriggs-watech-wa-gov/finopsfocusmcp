---
title: FOCUS Specification
url: https://focus.finops.org/docs/specification/v1-4/sections/schemas/
hostname: finops.org
description: View the FinOps Open Cost and Usage Specification (FOCUS) which introduces common taxonomy, terminology, and metrics for billing datasets produced by technology vendors.
sitename: FOCUS Specification 1.4
date: "2026-01-01"
fingerprint: a1d6a58a487a768
---
# 6 Schemas

This section provides machine-readable JSON Schema definitions for validating the structure and content of JSON-formatted columns in FOCUS datasets.

## 6.1 Contract Commitment

### 6.1.1 Contract Commitment Applicability Object Schema

The Contract Commitment Applicability Object Schema defines the structure for the Contract Commitment Applicability column.

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://focus.finops.org/schemas/contractcommitmentapplicabilityobject.json",
  "title": "Contract Commitment Applicability Object",
  "description": "Schema for validating the Contract Commitment Applicability column JSON object structure in FOCUS datasets",
  "type": "object",
  "$defs": {
    "ApplicabilityObject": {
      "type": "object",
      "properties": {
        "Cost": {
          "type": "number",
          "description": "Percentage applicable to ContractCommitmentCost",
          "minimum": 0.0,
          "maximum": 1.0,
          "default": 1.0
        },
        "Usage": {
          "type": "number",
          "description": "Percentage applicable to ContractCommitmentQuantity",
          "minimum": 0.0,
          "maximum": 1.0,
          "default": 1.0
        }
      },
      "additionalProperties": false
    },
    "ApplicabilityRule": {
      "type": "object",
      "required": [
        "Dimension",
        "Operator",
        "Values"
      ],
      "properties": {
        "Dimension": {
          "type": "string",
          "description": "A valid FOCUS Column Name"
        },
        "Operator": {
          "type": "string",
          "description": "The comparison logic to apply",
          "enum": [
            "In",
            "NotIn",
            "StartsWith",
            "NotStartsWith",
            "Contains",
            "NotContains",
            "EndsWith",
            "Exists",
            "DoesNotExist"
          ]
        },
        "Values": {
          "type": "array",
          "description": "List of strings to compare",
          "items": {
            "type": "string"
          },
          "minItems": 1
        },
        "Applicability": {
          "$ref": "#/$defs/ApplicabilityObject",
          "description": "Optional rule-level applicability that overrides top-level"
        }
      },
      "allOf": [
        {
          "description": "Wildcard constraint: If '*' is used, it must be the only value and Operator must be compatible.",
          "if": {
            "properties": {
              "Values": {
                "contains": {
                  "const": "*"
                }
              }
            }
          },
          "then": {
            "properties": {
              "Values": {
                "maxItems": 1
              },
              "Operator": {
                "enum": [
                  "In",
                  "Contains",
                  "Exists",
                  "DoesNotExist"
                ]
              }
            }
          }
        },
        {
          "description": "Existence Logic: Exists/DoesNotExist operators require the specific wildcard value.",
          "if": {
            "properties": {
              "Operator": {
                "enum": [
                  "Exists",
                  "DoesNotExist"
                ]
              }
            }
          },
          "then": {
            "properties": {
              "Values": {
                "items": {
                  "const": "*"
                },
                "maxItems": 1
              }
            }
          }
        }
      ],
      "additionalProperties": false
    }
  },
  "properties": {
    "IsGlobalScope": {
      "type": "boolean",
      "description": "If true, commitment applies to all entities",
      "default": false
    },
    "IsComplexScope": {
      "type": "boolean",
      "description": "If true, applicability logic exceeds schema capabilities",
      "default": false
    },
    "Applicability": {
      "$ref": "#/$defs/ApplicabilityObject",
      "description": "Top-level fractional mapping for metrics"
    },
    "InclusionOperator": {
      "type": "string",
      "description": "Logical operator for Inclusions array",
      "enum": [
        "And",
        "Or"
      ]
    },
    "Inclusions": {
      "type": "array",
      "description": "List of rules defining the applicability boundary",
      "items": {
        "$ref": "#/$defs/ApplicabilityRule"
      }
    },
    "ExclusionOperator": {
      "type": "string",
      "description": "Logical operator for Exclusions array",
      "enum": [
        "And",
        "Or"
      ]
    },
    "Exclusions": {
      "type": "array",
      "description": "List of rules defining entities to exclude",
      "items": {
        "$ref": "#/$defs/ApplicabilityRule"
      },
      "minItems": 1
    }
  },
  "allOf": [
    {
      "description": "IsGlobalScope and IsComplexScope cannot both be true simultaneously.",
      "not": {
        "required": [
          "IsGlobalScope",
          "IsComplexScope"
        ],
        "properties": {
          "IsGlobalScope": {
            "const": true
          },
          "IsComplexScope": {
            "const": true
          }
        }
      }
    },
    {
      "description": "If IsGlobalScope is true, Inclusions must be empty or omitted.",
      "if": {
        "properties": {
          "IsGlobalScope": {
            "const": true
          }
        },
        "required": [
          "IsGlobalScope"
        ]
      },
      "then": {
        "properties": {
          "Inclusions": {
            "maxItems": 0
          },
          "InclusionOperator": false
        }
      }
    },
    {
      "description": "If IsComplexScope is true, Inclusions must be empty or omitted.",
      "if": {
        "properties": {
          "IsComplexScope": {
            "const": true
          }
        },
        "required": [
          "IsComplexScope"
        ]
      },
      "then": {
        "properties": {
          "Inclusions": {
            "maxItems": 0
          },
          "InclusionOperator": false
        }
      }
    },
    {
      "description": "If neither Global nor Complex scope is active, Inclusions and InclusionOperator are required.",
      "if": {
        "not": {
          "anyOf": [
            {
              "properties": {
                "IsGlobalScope": {
                  "const": true
                }
              },
              "required": [
                "IsGlobalScope"
              ]
            },
            {
              "properties": {
                "IsComplexScope": {
                  "const": true
                }
              },
              "required": [
                "IsComplexScope"
              ]
            }
          ]
        }
      },
      "then": {
        "required": [
          "InclusionOperator",
          "Inclusions"
        ],
        "properties": {
          "Inclusions": {
            "minItems": 1
          }
        }
      }
    },
    {
      "description": "If Exclusions are present, ExclusionOperator is required.",
      "if": {
        "required": [
          "Exclusions"
        ]
      },
      "then": {
        "required": [
          "ExclusionOperator"
        ]
      }
    }
  ],
  "patternProperties": {
    "^x_[A-Z][a-zA-Z0-9]*$": {
      "description": "Custom data generator-defined properties prefixed with x_ in PascalCase format"
    }
  },
  "additionalProperties": false
}
```
## 6.2 Cost and Usage

### 6.2.1 Allocated Method Details Object Schema

The Allocated Method Details Object Schema defines the structure for the Allocated Method Details column.

```
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://focus.finops.org/schemas/allocatedmethoddetailsobject.json",
    "title": "Allocated Method Details Object",
    "description": "Schema for validating the Allocated Method Details column JSON object structure in FOCUS datasets",
    "type": "object",
    "required": [
        "Elements"
    ],
    "properties": {
        "Elements": {
            "type": "array",
            "description": "Array containing one or more objects describing allocation properties",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": [
                    "AllocatedRatio"
                ],
                "properties": {
                    "AllocatedRatio": {
                        "type": "number",
                        "description": "Percentage of overall cost derived from corresponding method and metric",
                        "minimum": 0,
                        "maximum": 1
                    },
                    "UsageUnit": {
                        "type": [
                            "string",
                            "null"
                        ],
                        "description": "Unit being measured used to calculate allocation"
                    },
                    "UsageQuantity": {
                        "type": [
                            "number",
                            "null"
                        ],
                        "description": "Volume of UsageUnit consumed or used"
                    }
                },
                "anyOf": [
                    {
                        "description": "Scenario 1: UsageQuantity is absent or explicitly null. UsageUnit can be anything (or absent).",
                        "properties": {
                            "UsageQuantity": {
                                "type": "null"
                            }
                        }
                    },
                    {
                        "description": "Scenario 2: UsageQuantity is provided and is a number. UsageUnit MUST be provided and MUST be a string.",
                        "required": [
                            "UsageQuantity",
                            "UsageUnit"
                        ],
                        "properties": {
                            "UsageQuantity": {
                                "type": "number"
                            },
                            "UsageUnit": {
                                "type": "string"
                            }
                        }
                    }
                ],
                "patternProperties": {
                    "^x_[A-Z][a-zA-Z0-9]*$": {
                        "description": "Custom data generator-defined properties prefixed with x_ in PascalCase format"
                    }
                },
                "additionalProperties": false
            }
        }
    },
    "patternProperties": {
        "^x_[A-Z][a-zA-Z0-9]*$": {
            "description": "Custom data generator-defined top-level properties prefixed with x_ in PascalCase format"
        }
    },
    "additionalProperties": false
}
```
### 6.2.2 Commitment Program Eligibility Details Object Schema

The Commitment Program Eligibility Details Object Schema defines the structure for the Commitment Program Eligibility Details column.

```
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://focus.finops.org/schemas/commitmentprogrameligibilitydetailsobject.json",
    "title": "Commitment Program Eligibility Details Object",
    "description": "Schema for validating the Commitment Program Eligibility Details column JSON object structure in FOCUS datasets",
    "type": "object",
    "required": [
        "CommitmentPrograms"
    ],
    "properties": {
        "CommitmentPrograms": {
            "type": "array",
            "description": "Array of objects identifying commitment programs for which the usage is eligible.",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": [
                    "ProgramType"
                ],
                "properties": {
                    "ProgramType": {
                        "type": "string",
                        "description": "The specific type of commitment program (e.g., discount or capacity reservation) available for this usage."
                    }
                },
                "patternProperties": {
                    "^x_[A-Z][a-zA-Z0-9]*$": {
                        "description": "Custom data generator-defined properties prefixed with x_ in PascalCase format"
                    }
                },
                "additionalProperties": false
            }
        }
    },
    "patternProperties": {
        "^x_[A-Z][a-zA-Z0-9]*$": {
            "description": "Custom data generator-defined top-level properties prefixed with x_ in PascalCase format"
        }
    },
    "additionalProperties": false
}
```
### 6.2.3 Contract Applied Object Schema

The Contract Applied Object Schema defines the structure for the Contract Applied column.

```
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://focus.finops.org/schemas/contractappliedobject.json",
    "title": "Contract Applied Object",
    "description": "Schema for validating the Contract Applied column JSON object structure in FOCUS datasets",
    "type": "object",
    "required": [
        "Elements"
    ],
    "properties": {
        "Elements": {
            "type": "array",
            "description": "Array containing one or more objects describing contract commitments applied to the charge",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": [
                    "ContractId",
                    "ContractCommitmentId"
                ],
                "properties": {
                    "ContractId": {
                        "type": "string",
                        "description": "Unique identifier for the contract"
                    },
                    "ContractCommitmentId": {
                        "type": "string",
                        "description": "Unique identifier for the contract commitment term"
                    },
                    "ContractCommitmentAppliedCost": {
                        "type": [
                            "number",
                            "null"
                        ],
                        "description": "Cost value of the charge applied to the contract commitment"
                    },
                    "ContractCommitmentAppliedQuantity": {
                        "type": [
                            "number",
                            "null"
                        ],
                        "description": "Quantity of usage applied to the contract commitment"
                    },
                    "ContractCommitmentAppliedUnit": {
                        "type": [
                            "string",
                            "null"
                        ],
                        "description": "Unit of measure for the applied quantity"
                    }
                },
                "oneOf": [
                    {
                        "description": "Scenario 1: Cost has a value. Quantity and Unit MUST be absent or explicitly null.",
                        "required": [
                            "ContractCommitmentAppliedCost"
                        ],
                        "properties": {
                            "ContractCommitmentAppliedCost": {
                                "type": "number"
                            },
                            "ContractCommitmentAppliedQuantity": {
                                "type": "null"
                            },
                            "ContractCommitmentAppliedUnit": {
                                "type": "null"
                            }
                        }
                    },
                    {
                        "description": "Scenario 2: Quantity and Unit have values. Cost MUST be absent or explicitly null.",
                        "required": [
                            "ContractCommitmentAppliedQuantity",
                            "ContractCommitmentAppliedUnit"
                        ],
                        "properties": {
                            "ContractCommitmentAppliedCost": {
                                "type": "null"
                            },
                            "ContractCommitmentAppliedQuantity": {
                                "type": "number"
                            },
                            "ContractCommitmentAppliedUnit": {
                                "type": "string"
                            }
                        }
                    }
                ],
                "patternProperties": {
                    "^x_[A-Z][a-zA-Z0-9]*$": {
                        "description": "Custom data generator-defined properties prefixed with x_ in PascalCase format"
                    }
                },
                "additionalProperties": false
            }
        }
    },
    "patternProperties": {
        "^x_[A-Z][a-zA-Z0-9]*$": {
            "description": "Custom data generator-defined top-level properties prefixed with x_ in PascalCase format"
        }
    },
    "additionalProperties": false
}
```