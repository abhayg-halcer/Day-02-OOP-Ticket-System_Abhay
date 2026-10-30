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


def test_full_ticket_pipeline(tmp_path):
    # Load and clean dataset
    raw_tickets = load_tickets("data/tickets.csv")
    valid_tickets, quality_report = clean_tickets(raw_tickets)

    # Generate analytics
    summary = generate_summary(valid_tickets)
    sla_results = analyze_sla_breaches(valid_tickets)

    # Export reports to temporary directory
    quality_file = tmp_path / "quality_report.csv"
    summary_file = tmp_path / "summary_metrics.csv"
    sla_file = tmp_path / "sla_report.csv"

    export_report(quality_report, quality_file)
    export_summary(summary, summary_file)
    export_report(sla_results, sla_file)

    # Verify pipeline results
    assert len(raw_tickets) == 40
    assert len(valid_tickets) == 32
    assert len(quality_report) == 9

    assert summary["total_tickets"] == 32
    assert len(sla_results) == 4

    assert quality_file.exists()
    assert summary_file.exists()
    assert sla_file.exists()


def test_pipeline_exports_all_reports(tmp_path):
    raw_tickets = load_tickets("data/tickets.csv")
    valid_tickets, quality_report = clean_tickets(raw_tickets)

    summary = generate_summary(valid_tickets)
    sla_results = analyze_sla_breaches(valid_tickets)

    export_report(quality_report, tmp_path / "quality.csv")
    export_summary(summary, tmp_path / "summary.csv")
    export_report(sla_results, tmp_path / "sla.csv")

    assert len(list(tmp_path.glob("*.csv"))) == 3