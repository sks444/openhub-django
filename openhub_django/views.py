from django.shortcuts import render
from django.views import generic

from openhub_django.models import (
    PortfolioProject,
    OutsideProject,
    OutsideCommitter,
    AffiliatedCommitter,
    Organization,
    )


def index(request):
    args = {
        'portfolioprojects': 'portfolio_projects',
        'outsidecommitters': 'outside_committers',
        'affiliatedcommitters': 'affiliated_committers',
        'outsideprojects': 'outside_projects',
        'organization': 'organization',
        }
    return render(request, 'openhub_django/index.html', args)


class PortfolioProjectListView(generic.ListView):
    model = PortfolioProject
    context_object_name = 'portfolio_project_list'
    template_name = 'openhub_django/portfolioproject_list.html'


class PortfolioProjectDetailView(generic.DetailView):
    model = PortfolioProject
    template_name = 'openhub_django/portfolioproject_detail.html'


class OutsideProjectListView(generic.ListView):
    model = OutsideProject
    context_object_name = 'outside_project_list'
    template_name = 'openhub_django/outsideproject_list.html'


class OutsideProjectDetailView(generic.DetailView):
    model = OutsideProject
    template_name = 'openhub_django/outsideproject_detail.html'


class OutsideCommitterListView(generic.ListView):
    model = OutsideCommitter
    context_object_name = 'outside_committer_list'
    template_name = 'openhub_django/outsidecommitter_list.html'


class OutsideCommitterDetailView(generic.DetailView):
    model = OutsideCommitter
    template_name = 'openhub_django/outsidecommitter_detail.html'


class AffiliatedCommitterListView(generic.ListView):
    model = AffiliatedCommitter
    context_object_name = 'affiliated_committer_list'
    template_name = 'openhub_django/affiliatedcommitter_list.html'


class AffiliatedCommitterDetailView(generic.DetailView):
    model = AffiliatedCommitter
    template_name = 'openhub_django/affiliatedcommitter_detail.html'


class OrganizationListView(generic.ListView):
    model = Organization
    context_object_name = 'organization_list'
    template_name = 'openhub_django/organization_list.html'


class OrganizationDetailView(generic.DetailView):
    model = Organization
    template_name = 'openhub_django/organization_detail.html'
