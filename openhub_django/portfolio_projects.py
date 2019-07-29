from openhub_django.variables import ORG_NAME
from openhub_django.models import (
    PortfolioProject,
    PortfolioProjectActivity,
)
from openhub_django.checker import data_checker


def get_portfolio_projects_data(json_object):
    """
    :param json_object: json data of portfolio projects
    :return: a list of portfolio projects dict
    """
    data = json_object['response']['result'
                                   ]['portfolio_projects']['project']
    data = data_checker(data)
    return data


def import_data(projects):
    portfolio_project_objects_list = []
    for project in projects:
        ppa, created = PortfolioProjectActivity.objects.get_or_create(
            **project['twelve_mo_activity_and_year_on_year_change'])
        project['twelve_mo_activity_and_year_on_year_change'] = ppa
        project['org'] = ORG_NAME
        portfolio_project_objects_list.append(PortfolioProject(**project))
    PortfolioProject.objects.bulk_create(portfolio_project_objects_list)
