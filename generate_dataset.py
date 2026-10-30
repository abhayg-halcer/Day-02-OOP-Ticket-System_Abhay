
import csv
from pathlib import Path

OUTPUT_FILE = Path("data/tickets.csv")

headers = [
    "ticket_id",
    "customer_id",
    "category",
    "priority",
    "status",
    "created_at",
    "resolution_time_hours",
    "customer_rating",
    "description",
]

priorities = (
    ["Low"] * 10
    + ["Medium"] * 10
    + ["High"] * 10
    + ["Critical"] * 10
)

statuses = (
    ["Open"] * 10
    + ["In Progress"] * 10
    + ["Resolved"] * 15
    + ["Closed"] * 5
)

categories = ["Billing", "Technical", "Account", "Delivery", "Product"]

rows = []

for i in range(40):
    priority = priorities[i]
    status = statuses[i]

    resolution_time = ""
    if status in ("Resolved", "Closed"):
        resolution_time = str((i % 12) + 2)

    rating = str((i % 5) + 1) if i % 7 != 0 else ""

    rows.append({
        "ticket_id": f"TKT{i + 1:03d}",
        "customer_id": f"C{i + 1:03d}",
        "category": categories[i % 5],
        "priority": priority,
        "status": status,
        "created_at": f"2026-10-{(i % 28) + 1:02d}T10:00:00",
        "resolution_time_hours": resolution_time,
        "customer_rating": rating,
        "description": f"Synthetic support ticket number {i + 1}",
    })


# Intentional data-quality anomalies
rows[38]["category"] = ""                          # Missing category
rows[37]["priority"] = "Unknown"                   # Invalid priority
rows[36]["status"] = "Waiting"                     # Invalid status
rows[35]["created_at"] = "invalid-date"            # Invalid date
rows[34]["resolution_time_hours"] = "-2"           # Negative duration
rows[33]["customer_rating"] = "6"                  # Invalid rating
rows[32]["description"] = ""                       # Blank description

# Final row: duplicate ticket ID
rows[39]["ticket_id"] = rows[0]["ticket_id"]
rows[39]["customer_id"] = "C999"
rows[39]["description"] = "Duplicate ticket ID test"

# Separate missing ticket ID anomaly
rows[30]["ticket_id"] = ""


OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

print(f"Dataset generated: {OUTPUT_FILE}")
print(f"Total records: {len(rows)}")
print("Dataset generation complete.")
