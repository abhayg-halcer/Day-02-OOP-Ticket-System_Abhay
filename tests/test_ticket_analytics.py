from datetime import datetime

from src.models.support_ticket import SupportTicket
from src.services.ticket_analytics import (
    generate_summary,
    analyze_sla_breaches,
)


def create_ticket(ticket_id, priority, duration):
    return SupportTicket(
        ticket_id=ticket_id,
        customer_id="C001",
        category="Technical",
        priority=priority,
        status="Resolved" if duration is not None else "Open",
        created_at=datetime(2026, 10, 1, 10, 0),
        resolution_time_hours=duration,
        customer_rating=4,
        description="Test ticket",
    )


def test_generate_summary():
    tickets = [
        create_ticket("TKT001", "Critical", 5),
        create_ticket("TKT002", "High", 6),
        create_ticket("TKT003", "Low", None),
    ]

    summary = generate_summary(tickets)

    assert summary["total_tickets"] == 3
    assert summary["priority_counts"]["Critical"] == 1
    assert summary["status_counts"]["Resolved"] == 2
    assert summary["average_resolution_hours"] == 5.5


def test_sla_breach_analysis():
    tickets = [
        create_ticket("TKT001", "Critical", 5),
        create_ticket("TKT002", "Critical", 4),
        create_ticket("TKT003", "High", 6),
        create_ticket("TKT004", "Low", None),
    ]

    results = analyze_sla_breaches(tickets)

    critical = next(
        item for item in results
        if item["priority"] == "Critical"
    )

    assert critical["total_tickets"] == 2
    assert critical["breached_tickets"] == 1
    assert critical["within_sla_tickets"] == 1
    assert critical["breach_percentage"] == 50.0


def test_unresolved_tickets_are_not_counted_as_breaches():
    tickets = [
        create_ticket("TKT001", "High", None),
    ]

    results = analyze_sla_breaches(tickets)

    high = next(
        item for item in results
        if item["priority"] == "High"
    )

    assert high["unresolved_tickets"] == 1
    assert high["breached_tickets"] == 0