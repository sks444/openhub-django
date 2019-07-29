from django.core.management.base import BaseCommand

from openhub_django.data import get_data
from openhub_django.outside_committers import import_data


class Command(BaseCommand):
    help = 'Import OutsideCommitters data'

    COLLECTIONS = 'outside_committers'
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        outside_committers = get_data(self.COLLECTIONS)
        self.IMPORT_DATA(outside_committers)
