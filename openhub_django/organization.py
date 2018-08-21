import json

import requests
import xmltodict

from openhub_django.variables import ORG_NAME, OH_TOKEN
from openhub_django.models import InfographicDetail, Organization


def get_organization_data():
    import_url = ('https://www.openhub.net/orgs/'
                  + ORG_NAME + '.xml?api_key=' + OH_TOKEN)
    resp = requests.get(import_url)
    jsonString = json.dumps(xmltodict.parse(resp.content), indent=4)
    json_object = json.loads(jsonString)
    jdict = json_object['response']['result']['org']
    data = json.dumps(jdict)
    org = json.loads(data)

    return org


def import_data(org):
    (cr, create) = InfographicDetail.objects.get_or_create(
        **org['infographic_details']
        )
    org['infographic_details'] = cr
    org['org_type'] = org.pop('type')
    org.pop('portfolio_projects')
    org.pop('vanity_url')
    Organization.objects.get_or_create(**org)
