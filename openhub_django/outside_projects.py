from openhub_django.variables import ORG_NAME
from openhub_django.models import OutsideProject
from openhub_django.checker import data_checker


def get_outside_projects_data(json_object):
    """
    :param json_object: json data of outside projects
    :return: a list of outside projects dict
    """
    data = json_object['response']['result'
                                   ]['outside_projects']['project']
    data = data_checker(data)
    return data


def import_data(projects):
    outside_project_objects_list = []
    for project in projects:
        project['org'] = ORG_NAME
        outside_project_objects_list.append(OutsideProject(**project))
    OutsideProject.objects.bulk_create(outside_project_objects_list)
