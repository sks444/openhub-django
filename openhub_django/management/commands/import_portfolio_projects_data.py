from django.core.management.base import BaseCommand

from openhub_django.data import get_data
from openhub_django.portfolio_projects import import_data


class Command(BaseCommand):
    help = 'Import PortfolioProjects data'

    COLLECTIONS = 'projects'
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        projects = get_data(self.COLLECTIONS)
        self.IMPORT_DATA(projects)
