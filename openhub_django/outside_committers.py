from openhub_django.variables import ORG_NAME
from openhub_django.models import (
    OutsideCommitter,
    ContributionsToPortfolioProject,
)
from openhub_django.checker import data_checker


def get_outside_committers_data(json_object):
    """
    :param json_object: json data of outside committers
    :return: a list of outside committers dict
    """
    data = json_object['response']['result'
                                   ]['outside_committers']['contributor']
    data = data_checker(data)
    return data


def import_data(contributors):
    outside_committer_objects_list = []
    for contributor in contributors:
        ctpp, created = ContributionsToPortfolioProject.objects.get_or_create(
            **contributor['contributions_to_portfolio_projects'])
        contributor['contributions_to_portfolio_projects'] = ctpp
        contributor['org'] = ORG_NAME
        outside_committer_objects_list.append(OutsideCommitter(**contributor))
    OutsideCommitter.objects.bulk_create(outside_committer_objects_list)
