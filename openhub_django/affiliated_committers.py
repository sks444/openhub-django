from openhub_django.variables import ORG_NAME
from openhub_django.models import (
    MostCommit,
    MostRecentCommit,
    AffiliatedCommitter,
)
from openhub_django.checker import data_checker


def get_affiliated_committers_data(json_object):
    """
    :param json_object: json data of affiliated committers
    :return: a list of affiliated committers dict
    """
    data = json_object['response']['result'
                                   ]['affiliated_committers']['affiliator']
    data = data_checker(data)
    return data


def import_data(affiliators):
    affiliated_committer_objects_list = []
    for affiliator in affiliators:
        most_commits, created = MostCommit.objects.get_or_create(
            **affiliator['most_commits']
            )
        most_recent_commit, created = MostRecentCommit.objects.get_or_create(
            **affiliator['most_recent_commit']
            )
        affiliator['most_commits'] = most_commits
        affiliator['most_recent_commit'] = most_recent_commit
        affiliator['org'] = ORG_NAME
        affiliated_committer_objects_list.append(
            AffiliatedCommitter(**affiliator))
    AffiliatedCommitter.objects.bulk_create(affiliated_committer_objects_list)
