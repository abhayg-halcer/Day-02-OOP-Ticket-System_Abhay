# Daily Report — Day 02

## Topics learned
- Classes, instances, `self`, dataclasses, `__post_init__`, `__str__`, `__repr__`
- Encapsulation, composition vs inheritance, single responsibility
- Class vs instance state and why mutable class attributes are risky
- Splitting load, validate, clean, analytics, and export into separate modules

## What I can explain without notes
- Why `SupportTicket` validates in `__post_init__` and is frozen
- Why CSV loading, validation, cleaning, and analytics are separate
- How SLA analysis was added without changing summary generation
- How I would test a module that reads a file (inject a path / use `tmp_path`)

## Implementation completed
- `SupportTicket` model with field validation
- CSV loader, validator, cleaner, analytics, report exporter
- SLA breach analysis by priority as a new analytics operation
- Unit and integration tests (17 passing)
- Pipeline run on `data/tickets.csv` (40 raw → 32 valid)

## Tests/experiment results
- `pytest -v` → 17 passed (see `evidence/test_results.txt`)
- `python -m src.main` → reports in `outputs/` (see `evidence/pipeline_execution.txt`)

## One bug or challenge and its root cause
Invalid customer ratings were being treated like required-field errors, so good tickets were dropped.
Root cause: optional vs blocking validation was mixed together.
Fix: flag `invalid_rating`, set rating to `None`, keep the ticket if nothing else is wrong.

## One design decision and why
I used composition of small modules (functions + one dataclass) instead of one ticket-processor class or an inheritance tree.
Reason: each piece can be tested alone, and SLA analysis could be added without touching the loader or model.

## Blocker and what I tried
No remaining blocker. Early confusion was resolved vs open tickets having/missing resolution time; the model now rejects both inconsistent states.

## Tomorrow's plan
- Day 03 topics as assigned
- Optional: configurable SLA limits and a shared constants module
