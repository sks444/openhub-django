"""
Community URL configuration.
"""

from django_distill import distill_url
from django.conf.urls.static import static
from django.conf import settings

from .views import index as openhub_django_index
from .models import (
    PortfolioProject,
    OutsideCommitter,
    AffiliatedCommitter,
    OutsideProject,
    Organization,
    )
from .views import (
    PortfolioProjectListView,
    PortfolioProjectDetailView,
    AffiliatedCommitterListView,
    AffiliatedCommitterDetailView,
    OrganizationListView,
    OrganizationDetailView,
    OutsideProjectListView,
    OutsideProjectDetailView,
    OutsideCommitterListView,
    OutsideCommitterDetailView,
    )


def get_index():
    # The index URI regex, ^$, contains no parameters, named or otherwise.
    # You can simply just return nothing here.
    return None


def get_all_portfolioprojects():
    for portfolioproject in PortfolioProject.objects.all():
        yield {'pk': portfolioproject.id}


def get_all_outsidecommitters():
    for outsidecommitter in OutsideCommitter.objects.all():
        yield {'pk': outsidecommitter.id}


def get_all_outsideprojects():
    for outsideproject in OutsideProject.objects.all():
        yield {'pk': outsideproject.id}


def get_all_affiliatedcommitters():
    for affiliatedcommitter in AffiliatedCommitter.objects.all():
        yield {'pk': affiliatedcommitter.id}


def get_organization():
    for organization in Organization.objects.all():
        yield {'pk': organization.id}


urlpatterns = [
    distill_url(
        r'openhub/$', openhub_django_index,
        name='community-openhub',
        distill_func=get_index,
    ),
    distill_url(
        r'openhub/outside_committers/$',
        OutsideCommitterListView.as_view(),
        name='outsidecommitters',
        distill_func=get_index,
    ),
    distill_url(
        r'openhub/outside_committer/(?P<pk>\d+)/$',
        OutsideCommitterDetailView.as_view(),
        name='outsidecommitter-detail',
        distill_func=get_all_outsidecommitters,
    ),
    distill_url(
        r'openhub/outside_projects/$',
        OutsideProjectListView.as_view(),
        name='outsideprojects',
        distill_func=get_index,
    ),
    distill_url(
        r'openhub/outside_project/(?P<pk>\d+)/$',
        OutsideProjectDetailView.as_view(),
        name='outsideproject-detail',
        distill_func=get_all_outsideprojects,
    ),
    distill_url(
        r'openhub/affiliated_committers/$',
        AffiliatedCommitterListView.as_view(),
        name='affiliatedcommitters',
        distill_func=get_index,
    ),
    distill_url(
        r'openhub/affiliated_committer/(?P<pk>\d+)/$',
        AffiliatedCommitterDetailView.as_view(),
        name='affiliatedcommitter-detail',
        distill_func=get_all_affiliatedcommitters,
    ),
    distill_url(
        r'openhub/portfolio_projects/$',
        PortfolioProjectListView.as_view(),
        name='portfolioprojects',
        distill_func=get_index,
    ),
    distill_url(
        r'openhub/portfolio_project/(?P<pk>\d+)/$',
        PortfolioProjectDetailView.as_view(),
        name='portfolioproject-detail',
        distill_func=get_all_portfolioprojects,
    ),
    distill_url(
        r'openhub/organization/$',
        OrganizationListView.as_view(),
        name='organization',
        distill_func=get_index,
    ),
    distill_url(
        r'openhub/org/(?P<pk>\d+)/$',
        OrganizationDetailView.as_view(),
        name='org-detail',
        distill_func=get_organization,
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
