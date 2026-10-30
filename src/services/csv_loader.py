import csv
from pathlib import Path
from typing import Any


def load_tickets(file_path: str | Path) -> list[dict[str, Any]]:
    """
    Read ticket records from a CSV file.

    Returns each row as a dictionary.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open("r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)