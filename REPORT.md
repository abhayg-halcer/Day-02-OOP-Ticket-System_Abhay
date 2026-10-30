# Project Report — Customer Support Ticket Data Pipeline

## Submission Details

- **Developer:** Abhay Gour
- **Assignment:** Day 02 — Object-Oriented Python & Reusable Modules
- **Date:** 2026-10-30
- **Repository URL:** https://github.com/abhayg-halcer/Day-02-OOP-Ticket-System_Abhay
- **Latest commit hash:** `60a64df`
- **Pull Request:** N/A — no pull request created

---

## 1. Project Title

**Customer Support Ticket Data Pipeline using Object-Oriented Python and Reusable Modules**

## 2. Objective

The objective of this project is to develop a modular Python application that processes customer support ticket data, identifies data-quality issues, generates analytical insights, and exports structured CSV reports.

The project demonstrates Object-Oriented Programming, reusable modules, data validation, exception handling, and automated testing.

## 3. Dataset Description

The project uses a synthetic dataset containing 40 customer support ticket records.

Each record includes:

- Ticket ID
- Customer ID
- Category
- Priority
- Status
- Creation timestamp
- Resolution time in hours
- Customer rating
- Description

The dataset includes intentionally introduced data-quality issues to test validation and cleaning functionality.

## 4. Methodology

The pipeline follows these processing stages:

1. **Data Loading:** Read ticket records using Python's CSV module.
2. **Validation:** Check required fields, allowed values, timestamps, durations, and ratings.
3. **Cleaning:** Reject invalid records, identify duplicates, and normalize invalid optional ratings.
4. **Object Creation:** Convert valid records into `SupportTicket` dataclass objects.
5. **Analytics:** Calculate summary metrics and SLA breach statistics.
6. **Export:** Generate CSV reports for data quality, summary metrics, and SLA analysis.

## 5. Object-Oriented Design

The project uses a `SupportTicket` dataclass to represent individual tickets.

The class includes:

- Data attributes for ticket information.
- `__post_init__()` for validation.
- `__str__()` for readable output.
- `__repr__()` for developer-friendly representation.
- `frozen=True` to prevent accidental modification.

The application is divided into reusable model and service modules.

## 6. SLA Analysis

The project uses the following SLA thresholds:

| Priority | SLA Threshold |
|---|---:|
| Critical | 4 hours |
| High | 8 hours |
| Medium | 24 hours |
| Low | 72 hours |

Resolved or closed tickets exceeding their priority threshold are classified as breached.

Unresolved tickets are counted separately.

## 7. Implementation Results

The pipeline successfully processed the synthetic dataset.

| Metric | Result |
|---|---:|
| Raw records loaded | 40 |
| Valid tickets | 32 |
| Data-quality issues | 9 |
| Average resolution time | 7.75 hours |
| Unit and integration tests passed | 17 |

### SLA Breach Results

| Priority | Breached | Resolved | Breach % |
|---|---:|---:|---:|
| Critical | 2 | 2 | 100% |
| High | 4 | 10 | 40% |
| Medium | 0 | 0 | 0% |
| Low | 0 | 0 | 0% |

*Note: Medium and Low priorities had no resolved tickets in the cleaned dataset, so their breach percentages are reported as 0%.*

## 8. Generated Reports

The application generates three CSV reports:

1. `data_quality_report.csv` — records detected data-quality issues and actions.
2. `summary_metrics.csv` — stores overall ticket metrics.
3. `sla_breach_by_priority.csv` — provides SLA statistics grouped by priority.

All reports are saved in the `outputs/` directory.

## 9. Testing and Verification

The project includes unit and integration tests using pytest.

**Test execution:**

```bash
pytest -v
```

**Result:**

```text
17 passed in 0.04s
```

Python compilation was also verified:

```bash
python -m compileall src tests
```

No compilation errors were reported.

## 10. Challenges Addressed

- Handling missing and invalid CSV values.
- Detecting duplicate ticket IDs.
- Separating blocking validation errors from optional-field issues.
- Normalizing invalid customer ratings.
- Maintaining data integrity while creating ticket objects.
- Calculating SLA breaches by priority.
- Testing the complete processing workflow.

## 11. Conclusion

The project successfully demonstrates how Object-Oriented Python and reusable modules can be used to build a structured data-processing pipeline.

It combines CSV processing, validation, cleaning, analytics, report generation, and automated testing into a single application.

The successful execution of all 17 tests confirms that the implemented functionality works as expected for the current synthetic dataset and test cases.

## 12. Future Scope

- Add configurable SLA thresholds.
- Support additional input and output formats.
- Introduce structured logging.
- Add command-line configuration.
- Expand validation and test coverage.
- Add visual dashboards for ticket analytics.
