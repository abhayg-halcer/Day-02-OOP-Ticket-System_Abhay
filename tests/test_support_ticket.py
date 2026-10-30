import pytest
from datetime import datetime

from src.models.support_ticket import SupportTicket


def test_valid_ticket_creation():
    ticket = SupportTicket(
        ticket_id="TKT001",
        customer_id="C001",
        category="Technical",
        priority="High",
        status="Resolved",
        created_at=datetime(2026, 10, 1, 10, 0),
        resolution_time_hours=5.0,
        customer_rating=4,
        description="Login issue resolved",
    )

    assert ticket.ticket_id == "TKT001"
    assert ticket.priority == "High"
    assert ticket.resolution_time_hours == 5.0


def test_invalid_priority_rejected():
    with pytest.raises(ValueError, match="Invalid priority"):
        SupportTicket(
            ticket_id="TKT002",
            customer_id="C002",
            category="Technical",
            priority="Urgent",
            status="Open",
            created_at=datetime(2026, 10, 1, 10, 0),
            resolution_time_hours=None,
            customer_rating=None,
            description="Test ticket",
        )


def test_empty_ticket_id_rejected():
    with pytest.raises(ValueError, match="Ticket ID cannot be empty"):
        SupportTicket(
            ticket_id="   ",
            customer_id="C001",
            category="Technical",
            priority="High",
            status="Open",
            created_at=datetime(2026, 10, 1, 10, 0),
            resolution_time_hours=None,
            customer_rating=None,
            description="Test ticket",
        )


def test_resolved_ticket_requires_resolution_time():
    with pytest.raises(ValueError, match="need a resolution time"):
        SupportTicket(
            ticket_id="TKT003",
            customer_id="C001",
            category="Technical",
            priority="High",
            status="Resolved",
            created_at=datetime(2026, 10, 1, 10, 0),
            resolution_time_hours=None,
            customer_rating=4,
            description="Resolved without duration",
        )


def test_open_ticket_cannot_have_resolution_time():
    with pytest.raises(ValueError, match="Unresolved tickets cannot have a resolution time"):
        SupportTicket(
            ticket_id="TKT004",
            customer_id="C001",
            category="Technical",
            priority="High",
            status="Open",
            created_at=datetime(2026, 10, 1, 10, 0),
            resolution_time_hours=3.0,
            customer_rating=None,
            description="Open with duration",
        )


def test_frozen_ticket_cannot_be_changed():
    ticket = SupportTicket(
        ticket_id="TKT005",
        customer_id="C001",
        category="Technical",
        priority="High",
        status="Open",
        created_at=datetime(2026, 10, 1, 10, 0),
        resolution_time_hours=None,
        customer_rating=None,
        description="Immutable ticket",
    )
    with pytest.raises(Exception):
        ticket.status = "Closed"
