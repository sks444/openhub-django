from django.core.management.base import BaseCommand

from openhub_django.data import get_data
from openhub_django.outside_projects import import_data


class Command(BaseCommand):
    help = 'Import OutsideProject data'

    COLLECTIONS = 'outside_projects'
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        outside_projects = get_data(self.COLLECTIONS)
        self.IMPORT_DATA(outside_projects)
