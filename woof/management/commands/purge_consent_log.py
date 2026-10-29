"""Delete old cookie-consent records (GDPR storage limitation).

The consent register keeps one row per visitor decision. It is evidence, not
analytics, so it does not need to live forever: after a year the record adds
nothing to what the banner already tells the visitor. Run it from cron, e.g.
monthly:

    python manage.py purge_consent_log --days 365 --dry-run
    python manage.py purge_consent_log --days 365
"""

from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from woof.models import ConsentLog


class Command(BaseCommand):
    help = "Delete consent-log entries older than the retention period."

    def add_arguments(self, parser):
        parser.add_argument(
            "--days",
            type=int,
            default=365,
            help="Keep entries younger than this many days (default 365).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Only report how many entries would be deleted.",
        )

    def handle(self, *args, **options):
        cutoff = timezone.now() - timedelta(days=options["days"])
        expired = ConsentLog.objects.filter(created_at__lt=cutoff)
        count = expired.count()

        if options["dry_run"]:
            self.stdout.write(
                self.style.WARNING(
                    f"{count} entries older than {options['days']} days "
                    f"(before {cutoff:%Y-%m-%d}) — dry run, nothing deleted"
                )
            )
            return

        deleted, _ = expired.delete()
        self.stdout.write(
            self.style.SUCCESS(
                f"deleted {deleted} entries older than {options['days']} days "
                f"(before {cutoff:%Y-%m-%d})"
            )
        )
