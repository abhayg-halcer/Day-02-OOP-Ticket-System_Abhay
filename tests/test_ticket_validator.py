import pytest

from src.services.csv_loader import load_tickets
from src.services.ticket_validator import validate_ticket_row


def test_invalid_priority_is_detected():
    row = {
        "ticket_id": "TKT001",
        "customer_id": "C001",
        "category": "Technical",
        "priority": "Unknown",
        "status": "Open",
        "created_at": "2026-10-01T10:00:00",
        "resolution_time_hours": "",
        "customer_rating": "",
        "description": "Test ticket",
    }

    issues = validate_ticket_row(row)

    assert {"field": "priority", "issue": "invalid_priority"} in issues


def test_invalid_date_is_detected():
    row = {
        "ticket_id": "TKT002",
        "customer_id": "C002",
        "category": "Billing",
        "priority": "High",
        "status": "Open",
        "created_at": "invalid-date",
        "resolution_time_hours": "",
        "customer_rating": "",
        "description": "Test ticket",
    }

    issues = validate_ticket_row(row)

    assert {"field": "created_at", "issue": "invalid_date"} in issues


def test_dataset_contains_expected_anomalies():
    rows = load_tickets("data/tickets.csv")

    all_issues = [
        issue
        for row in rows
        for issue in validate_ticket_row(row)
    ]

    issue_types = {issue["issue"] for issue in all_issues}

    assert "invalid_priority" in issue_types
    assert "invalid_status" in issue_types
    assert "invalid_date" in issue_types
    assert "negative_duration" in issue_types
    assert "invalid_rating" in issue_types