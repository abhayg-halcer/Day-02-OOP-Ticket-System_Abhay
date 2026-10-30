# Customer Support Ticket Data Pipeline

## Project Overview

This project implements a Python-based customer support ticket data pipeline using Object-Oriented Programming (OOP) and reusable modules.

It processes synthetic customer support ticket records, validates data quality, cleans invalid records, generates analytics, performs SLA breach analysis, and exports reports in CSV format.

## Project Features

- Load customer support ticket data from CSV files.
- Validate ticket fields and identify invalid records.
- Detect duplicate ticket IDs.
- Handle invalid customer ratings by normalizing them to `None`.
- Use a `SupportTicket` dataclass to represent ticket records.
- Generate ticket summary metrics.
- Analyze SLA breaches by priority.
- Export data-quality, summary, and SLA reports.
- Run unit and integration tests using pytest.

## Project Structure

```text
Day_02_OOP__Ticket_System/
├── data/
│   └── tickets.csv
├── src/
│   ├── models/
│   │   └── support_ticket.py
│   ├── services/
│   │   ├── csv_loader.py
│   │   ├── ticket_validator.py
│   │   ├── ticket_cleaner.py
│   │   ├── ticket_analytics.py
│   │   └── report_exporter.py
│   └── main.py
├── tests/
├── outputs/
├── evidence/
├── generate_dataset.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or later
- pytest

## Setup

Clone or download the project and navigate to its root directory.

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Pipeline

From the project root directory:

```bash
python -m src.main
```

## Run Tests

Run the complete test suite:

```bash
pytest -v
```

## Output Reports

The pipeline generates three CSV reports inside the `outputs/` directory:

| Report | Description |
|---|---|
| `data_quality_report.csv` | Validation issues, duplicates, and rejected records |
| `summary_metrics.csv` | Overall ticket summary metrics |
| `sla_breach_by_priority.csv` | SLA analysis grouped by priority |

## SLA Thresholds

| Priority | SLA Limit |
|---|---:|
| Critical | 4 hours |
| High | 8 hours |
| Medium | 24 hours |
| Low | 72 hours |

Resolved or closed tickets exceeding their priority threshold are counted as SLA breaches. Unresolved tickets are reported separately.

## Test Results

The project currently includes **17 unit and integration tests**, all passing successfully.

```text
17 passed
```

Python compilation was also verified successfully using:

```bash
python -m compileall src tests
```

## Technologies Used

- Python
- Object-Oriented Programming
- Dataclasses
- CSV module
- pathlib
- pytest
- Git
