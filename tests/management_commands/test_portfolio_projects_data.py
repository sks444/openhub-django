import unittest

from django.core.management import call_command
from django.test import TestCase

from openhub_django.models import PortfolioProject
from openhub_django.variables import ORG_NAME


class ImportPortfolioProjectDataTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        call_command('import_portfolio_projects_data')

    def test_command_import_portfolio_projects_data(self):
        p_projects = PortfolioProject.objects.all()
        if not p_projects:
            raise unittest.SkipTest(
                'No record of portfolio projects from openhub')
        self.assertIn(ORG_NAME,
                      [p_project.name for p_project in p_projects])
