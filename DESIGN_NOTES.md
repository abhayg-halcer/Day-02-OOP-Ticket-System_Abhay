# Design Notes — Customer Support Ticket Data Pipeline

## 1. Design Approach

The project follows a modular design using Object-Oriented Programming (OOP) principles.

Each module has a specific responsibility. This separation makes the code easier to understand, test, maintain, and reuse.

## 2. Data Model

### SupportTicket

**File:** `src/models/support_ticket.py`

The `SupportTicket` class is implemented using Python's `dataclass`.

It represents an individual customer support ticket and stores:

- Ticket ID
- Customer ID
- Category
- Priority
- Status
- Creation timestamp
- Resolution time
- Customer rating
- Description

The class uses `frozen=True` to prevent modification after object creation.

The `__post_init__()` method validates the ticket fields and enforces data rules.

The class also implements `__str__()` and `__repr__()` for readable object representations.

## 3. Service Modules

### CSV Loader

**File:** `src/services/csv_loader.py`

- Reads ticket records from CSV files.
- Uses `csv.DictReader`.
- Returns records as a list of dictionaries.
- Raises `FileNotFoundError` when the input file does not exist.

### Ticket Validator

**File:** `src/services/ticket_validator.py`

- Checks required fields.
- Validates categories, priorities, and statuses.
- Validates creation timestamps.
- Checks resolution duration and customer ratings.
- Returns a list of detected data-quality issues.

### Ticket Cleaner

**File:** `src/services/ticket_cleaner.py`

- Processes raw CSV records.
- Rejects duplicate ticket IDs.
- Rejects records containing blocking validation errors.
- Normalizes invalid optional customer ratings to `None`.
- Converts valid rows into `SupportTicket` objects.
- Produces a data-quality report.

### Ticket Analytics

**File:** `src/services/ticket_analytics.py`

Provides two main functions:

1. `generate_summary()` calculates total tickets, status counts, priority counts, and average resolution time.
2. `analyze_sla_breaches()` calculates SLA performance grouped by priority.

SLA thresholds:

| Priority | Threshold |
|---|---:|
| Critical | 4 hours |
| High | 8 hours |
| Medium | 24 hours |
| Low | 72 hours |

Unresolved tickets are counted separately and are not included in resolved-ticket breach percentages.

### Report Exporter

**File:** `src/services/report_exporter.py`

- Exports lists of dictionaries to CSV files.
- Creates output directories when necessary.
- Exports summary metrics in a two-column format.

## 4. Pipeline Execution

**File:** `src/main.py`

The main module coordinates the complete workflow:

1. Load raw ticket records.
2. Validate and clean the records.
3. Generate summary metrics.
4. Analyze SLA breaches.
5. Export CSV reports.
6. Display processing results in the terminal.

The `main()` function acts as the entry point of the application.

## 5. Error Handling

The project handles common data-quality problems, including:

- Missing ticket IDs.
- Duplicate ticket IDs.
- Invalid categories, priorities, and statuses.
- Invalid timestamps.
- Negative or invalid resolution durations.
- Invalid customer ratings.
- Blank descriptions.

Invalid optional ratings are normalized to `None`; records with blocking errors are rejected.

## 6. Testing Strategy

The project uses pytest for unit and integration testing.

Tests cover:

- SupportTicket object creation.
- CSV loading.
- Ticket validation.
- Ticket cleaning.
- Summary and SLA analytics.
- CSV report exporting.
- End-to-end pipeline execution.

Current test result: **17 passed**.

## 7. Design Benefits

- **Modularity:** Each component has a focused responsibility.
- **Reusability:** Service functions can be reused independently.
- **Maintainability:** Changes can be made within individual modules.
- **Testability:** Components can be tested separately and together.
- **Data integrity:** Validation and cleaning help prevent invalid records from entering analytics.

## 8. Future Improvements

- Add configurable SLA thresholds.
- Add more advanced data-quality checks.
- Support additional export formats.
- Add logging instead of relying only on print statements.
- Add command-line arguments for input and output paths.

- ## 9. Design comparison

### Design A — one processor class
A single `TicketProcessor` would load the CSV, validate, clean, analyse, and export.
That is simpler to start, but every change (new SLA rule, new export) touches the same class.
Tests become large and coupled. This is a god object.

### Design B — small modules composed by `main()` (chosen)
- `csv_loader` only reads rows
- `ticket_validator` only finds field issues
- `ticket_cleaner` only decides keep / reject / normalise
- `ticket_analytics` only computes metrics
- `report_exporter` only writes CSV
- `SupportTicket` only represents one valid ticket
- `main()` wires them in order

**Why B:** lower coupling, each module has one job, SLA analysis was added as a new function without changing loading or validation. Composition here means `main` uses these pieces; there is no inheritance, because nothing needed an “is-a” relationship.

## 10. Review of a messy design (what we avoided)

A messy version would look like:

- one class holding the file path, all rows, valid tickets, reports, and SLA limits
- methods like `run()`, `fix()`, `stats()`, `save()` on the same class
- class-level `tickets = []` shared by every instance
- validation mixed with print statements and file writes

Issues: many reasons to change, hard to test without real files, easy to mutate shared class state, invalid tickets can leak into analytics.

We avoided that by keeping validation on the model, cleaning in one function, and analytics as pure functions of a ticket list.

## 11. Class vs instance state in this project

- **Instance state:** each `SupportTicket` has its own `ticket_id`, `priority`, `status`, and so on.
- **Module-level constants:** `ALLOWED_PRIORITIES`, `SLA_LIMITS` are shared rules, not per-ticket data.
- **Not used:** a mutable class attribute like `SupportTicket.seen_ids = []`. If two pipelines ran, they would share and corrupt that list. Duplicate tracking is a local `seen_ticket_ids` set inside `clean_tickets()` instead.
