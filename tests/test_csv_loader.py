import pytest

from src.services.csv_loader import load_tickets


def test_load_tickets_returns_40_records():
    tickets = load_tickets("data/tickets.csv")

    assert len(tickets) == 40
    assert isinstance(tickets[0], dict)
    assert tickets[0]["ticket_id"] == "TKT001"


def test_missing_csv_file_raises_error():
    with pytest.raises(FileNotFoundError):
        load_tickets("data/missing.csv")