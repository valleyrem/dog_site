"""Delete old contact-form messages (GDPR storage limitation).

The Privacy Policy promises that messages are kept for up to 12 months. Run
it from cron, e.g. monthly:

    python manage.py purge_contact_messages --days 365 --dry-run
    python manage.py purge_contact_messages --days 365
"""

from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from woof.models import ContactMessage


class Command(BaseCommand):
    help = "Delete contact messages older than the retention period."

    def add_arguments(self, parser):
        parser.add_argument(
            "--days",
            type=int,
            default=365,
            help="Keep messages younger than this many days (default 365).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Only report how many messages would be deleted.",
        )

    def handle(self, *args, **options):
        cutoff = timezone.now() - timedelta(days=options["days"])
        expired = ContactMessage.objects.filter(created_at__lt=cutoff)
        count = expired.count()

        if options["dry_run"]:
            self.stdout.write(
                self.style.WARNING(
                    f"{count} messages older than {options['days']} days "
                    f"(before {cutoff:%Y-%m-%d}) — dry run, nothing deleted"
                )
            )
            return

        deleted, _ = expired.delete()
        self.stdout.write(
            self.style.SUCCESS(
                f"deleted {deleted} messages older than {options['days']} days "
                f"(before {cutoff:%Y-%m-%d})"
            )
        )
