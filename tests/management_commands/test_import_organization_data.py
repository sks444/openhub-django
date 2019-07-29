from django.core.management import call_command
from django.test import TestCase

from openhub_django.models import Organization
from openhub_django.variables import ORG_NAME


class ImportOrganizationDataTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        call_command('import_organization_data')

    def test_command_import_organization_data(self):
        org = Organization.objects.get(name=ORG_NAME)
        self.assertIsNotNone(org)
