import csv

from src.services.report_exporter import (
    export_report,
    export_summary,
)


def test_export_report_creates_csv(tmp_path):
    records = [
        {"priority": "High", "count": 5},
        {"priority": "Low", "count": 3},
    ]

    output_file = tmp_path / "reports" / "test_report.csv"

    export_report(records, output_file)

    assert output_file.exists()

    with output_file.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 2
    assert rows[0]["priority"] == "High"


def test_export_summary_creates_csv(tmp_path):
    summary = {
        "total_tickets": 3,
        "average_resolution_hours": 5.5,
        "status_counts": {"Resolved": 2, "Open": 1},
        "priority_counts": {"High": 2, "Low": 1},
    }

    output_file = tmp_path / "summary.csv"

    export_summary(summary, output_file)

    with output_file.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    metrics = {row["metric"]: row["value"] for row in rows}

    assert metrics["total_tickets"] == "3"
    assert metrics["average_resolution_hours"] == "5.5"
    assert metrics["status_Resolved"] == "2"