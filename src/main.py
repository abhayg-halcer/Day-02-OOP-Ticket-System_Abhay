from src.services.csv_loader import load_tickets
from src.services.ticket_cleaner import clean_tickets
from src.services.ticket_analytics import (
    generate_summary,
    analyze_sla_breaches,
)
from src.services.report_exporter import (
    export_report,
    export_summary,
)


def main():
    input_file = "data/tickets.csv"
    output_dir = "outputs"

    print("Starting ticket processing pipeline...")

    # 1. Load raw CSV records
    raw_tickets = load_tickets(input_file)
    print(f"Raw records loaded: {len(raw_tickets)}")

    # 2. Validate and clean records
    valid_tickets, quality_report = clean_tickets(raw_tickets)
    print(f"Valid tickets: {len(valid_tickets)}")
    print(f"Quality issues found: {len(quality_report)}")

    # 3. Generate analytics
    summary = generate_summary(valid_tickets)
    sla_results = analyze_sla_breaches(valid_tickets)

    # 4. Export reports
    export_report(
        quality_report,
        f"{output_dir}/data_quality_report.csv",
    )

    export_summary(
        summary,
        f"{output_dir}/summary_metrics.csv",
    )

    export_report(
        sla_results,
        f"{output_dir}/sla_breach_by_priority.csv",
    )

    # 5. Display results
    print("\n--- Ticket Summary ---")
    print(f"Total valid tickets: {summary['total_tickets']}")
    print(f"Average resolution time: {summary['average_resolution_hours']} hours")

    print("\n--- SLA Breach Analysis ---")
    for result in sla_results:
        print(
            f"{result['priority']}: "
            f"{result['breached_tickets']} breached / "
            f"{result['resolved_tickets']} resolved "
            f"({result['breach_percentage']}%)"
        )

    print("\nReports exported successfully:")
    print(f"- {output_dir}/data_quality_report.csv")
    print(f"- {output_dir}/summary_metrics.csv")
    print(f"- {output_dir}/sla_breach_by_priority.csv")


if __name__ == "__main__":
    main()