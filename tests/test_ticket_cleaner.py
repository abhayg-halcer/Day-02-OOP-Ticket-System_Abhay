from src.services.csv_loader import load_tickets
from src.services.ticket_cleaner import clean_tickets


def test_cleaner_returns_valid_ticket_objects():
    rows = load_tickets("data/tickets.csv")

    valid_tickets, quality_report = clean_tickets(rows)

    assert len(valid_tickets) > 0
    assert all(ticket.ticket_id for ticket in valid_tickets)
    assert all(ticket.priority in {"Low", "Medium", "High", "Critical"}
               for ticket in valid_tickets)


def test_duplicate_ticket_is_rejected():
    rows = load_tickets("data/tickets.csv")

    valid_tickets, quality_report = clean_tickets(rows)

    duplicate_issues = [
        issue for issue in quality_report
        if issue["issue"] == "duplicate_ticket_id"
    ]

    assert len(duplicate_issues) == 1
    assert duplicate_issues[0]["ticket_id"] == "TKT001"


def test_invalid_rating_is_normalized():
    rows = load_tickets("data/tickets.csv")

    valid_tickets, quality_report = clean_tickets(rows)

    normalized_issues = [
        issue for issue in quality_report
        if issue["issue"] == "invalid_rating"
    ]

    assert len(normalized_issues) == 1
    assert any(
        ticket.ticket_id == "TKT034" and ticket.customer_rating is None
        for ticket in valid_tickets
    )