from django.core.management.base import BaseCommand

from openhub_django.data import get_data
from openhub_django.affiliated_committers import import_data


class Command(BaseCommand):
    help = 'Import AffiliatorCommitters data'

    COLLECTIONS = 'affiliated_committers'
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        affiliators = get_data(self.COLLECTIONS)
        self.IMPORT_DATA(affiliators)
