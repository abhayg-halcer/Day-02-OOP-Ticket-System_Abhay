# Study Notes — Day 2: Object-Oriented Python & Reusable Modules

## 1. Object-Oriented Programming (OOP)

OOP is a programming approach that organizes code using classes and objects.

### Class

A class is a blueprint used to create objects.

In this project, `SupportTicket` is a class representing customer support tickets.

### Object

An object is an instance of a class.

Each valid CSV record is converted into a `SupportTicket` object.

### Dataclass

Python's `dataclass` decorator reduces boilerplate code when creating classes that primarily store data.

Example:

```python
from dataclasses import dataclass

@dataclass
class Customer:
    customer_id: str
    name: str
```

In this project, `SupportTicket` uses `@dataclass`.

### Frozen Dataclass

Using `frozen=True` prevents attributes from being reassigned after object creation.

```python
@dataclass(frozen=True)
class SupportTicket:
    ticket_id: str
```

This helps protect ticket data from accidental modification.

### Post Initialization

The `__post_init__()` method runs automatically after a dataclass object is initialized.

It is useful for applying additional validation rules.

In this project, it checks ticket IDs, categories, priorities, statuses, ratings, and resolution times.

## 2. Special Methods

### `__str__()`

Returns a readable string representation of an object.

### `__repr__()`

Returns a developer-oriented representation of an object.

Both methods are implemented in the `SupportTicket` class.

## 3. Python Modules and Packages

A module is a Python file containing reusable code.

A package is a directory containing related Python modules.

This project separates code into:

- `models/` — data models.
- `services/` — reusable processing functions.
- `tests/` — automated tests.

The `__init__.py` files identify package directories.

Imports allow one module to reuse code from another.

## 4. Type Hints

Type hints describe the expected types of variables, parameters, and return values.

Examples used in this project:

```python
def load_tickets(file_path: str) -> list[dict]:
    ...
```

Optional values can be represented using `Optional`.

```python
from typing import Optional

customer_rating: Optional[int]
```

Type hints improve code readability and help developers understand function interfaces.

## 5. CSV File Handling

Python provides the built-in `csv` module for reading and writing CSV files.

### DictReader

`csv.DictReader` reads CSV rows as dictionaries using column headers as keys.

### DictWriter

`csv.DictWriter` writes dictionaries into CSV files.

These are used for loading ticket records and exporting reports.

## 6. pathlib

The `pathlib` module provides an object-oriented way to work with filesystem paths.

Examples from the project:

```python
from pathlib import Path

path = Path("data/tickets.csv")

if path.exists():
    print("File exists")
```

It is used for file checks, reading files, and creating output directories.

## 7. Exception Handling

Exception handling prevents unexpected errors from crashing an application without useful context.

Example:

```python
try:
    value = float("invalid")
except ValueError:
    print("Invalid numeric value")
```

The project handles exceptions such as:

- `FileNotFoundError`
- `ValueError`
- `TypeError`

## 8. Data Validation and Cleaning

Validation checks whether input data follows defined rules.

Cleaning handles invalid or inconsistent data.

In this project:

- Duplicate ticket IDs are rejected.
- Invalid required fields cause records to be rejected.
- Invalid optional customer ratings are normalized to `None`.
- Valid rows are converted into `SupportTicket` objects.

## 9. Collections and Analytics

### List

Stores multiple ticket objects or records.

### Dictionary

Stores key-value pairs, such as summary metrics.

### Set

Stores unique values and is used to track previously encountered ticket IDs.

### Counter

`collections.Counter` counts occurrences of values.

It is used to calculate ticket counts by status and priority.

## 10. Testing with pytest

pytest is a Python testing framework.

Tests are written as functions whose names begin with `test_`.

### Assertions

Assertions verify expected results.

```python
assert len(valid_tickets) == 32
```

### Fixtures: `tmp_path`

pytest provides the `tmp_path` fixture for temporary directories.

It is used in integration tests to export reports without modifying the project's actual output files.

### Unit Testing

Tests individual functions or components independently.

### Integration Testing

Tests how multiple components work together.

This project currently contains 17 passing unit and integration tests.

## 11. Important Project Commands

Run the application:

```bash
python -m src.main
```

Run all tests:

```bash
pytest -v
```

Compile-check the source and tests:

```bash
python -m compileall src tests
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 12. Key Learnings

Through this project, I practised:

- Designing classes and creating objects.
- Using dataclasses and frozen objects.
- Applying validation through `__post_init__()`.
- Organizing reusable Python modules.
- Reading and writing CSV files.
- Handling invalid data and exceptions.
- Generating analytics using collections.
- Writing unit and integration tests.
- Building a complete data-processing pipeline.

