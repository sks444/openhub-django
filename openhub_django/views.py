# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	PortfolioProjectActivity,
	PortfolioProject,
	OutsideProject,
	ContributonsToPortfolioProject,
	OutsideCommitter,
	MostCommit,
	MostRecentCommit,
	AffiliatedCommitter,
	InfographicDetail,
	Organization,
)


class PortfolioProjectActivityCreateView(CreateView):

    model = PortfolioProjectActivity


class PortfolioProjectActivityDeleteView(DeleteView):

    model = PortfolioProjectActivity


class PortfolioProjectActivityDetailView(DetailView):

    model = PortfolioProjectActivity


class PortfolioProjectActivityUpdateView(UpdateView):

    model = PortfolioProjectActivity


class PortfolioProjectActivityListView(ListView):

    model = PortfolioProjectActivity


class PortfolioProjectCreateView(CreateView):

    model = PortfolioProject


class PortfolioProjectDeleteView(DeleteView):

    model = PortfolioProject


class PortfolioProjectDetailView(DetailView):

    model = PortfolioProject


class PortfolioProjectUpdateView(UpdateView):

    model = PortfolioProject


class PortfolioProjectListView(ListView):

    model = PortfolioProject


class OutsideProjectCreateView(CreateView):

    model = OutsideProject


class OutsideProjectDeleteView(DeleteView):

    model = OutsideProject


class OutsideProjectDetailView(DetailView):

    model = OutsideProject


class OutsideProjectUpdateView(UpdateView):

    model = OutsideProject


class OutsideProjectListView(ListView):

    model = OutsideProject


class ContributonsToPortfolioProjectCreateView(CreateView):

    model = ContributonsToPortfolioProject


class ContributonsToPortfolioProjectDeleteView(DeleteView):

    model = ContributonsToPortfolioProject


class ContributonsToPortfolioProjectDetailView(DetailView):

    model = ContributonsToPortfolioProject


class ContributonsToPortfolioProjectUpdateView(UpdateView):

    model = ContributonsToPortfolioProject


class ContributonsToPortfolioProjectListView(ListView):

    model = ContributonsToPortfolioProject


class OutsideCommitterCreateView(CreateView):

    model = OutsideCommitter


class OutsideCommitterDeleteView(DeleteView):

    model = OutsideCommitter


class OutsideCommitterDetailView(DetailView):

    model = OutsideCommitter


class OutsideCommitterUpdateView(UpdateView):

    model = OutsideCommitter


class OutsideCommitterListView(ListView):

    model = OutsideCommitter


class MostCommitCreateView(CreateView):

    model = MostCommit


class MostCommitDeleteView(DeleteView):

    model = MostCommit


class MostCommitDetailView(DetailView):

    model = MostCommit


class MostCommitUpdateView(UpdateView):

    model = MostCommit


class MostCommitListView(ListView):

    model = MostCommit


class MostRecentCommitCreateView(CreateView):

    model = MostRecentCommit


class MostRecentCommitDeleteView(DeleteView):

    model = MostRecentCommit


class MostRecentCommitDetailView(DetailView):

    model = MostRecentCommit


class MostRecentCommitUpdateView(UpdateView):

    model = MostRecentCommit


class MostRecentCommitListView(ListView):

    model = MostRecentCommit


class AffiliatedCommitterCreateView(CreateView):

    model = AffiliatedCommitter


class AffiliatedCommitterDeleteView(DeleteView):

    model = AffiliatedCommitter


class AffiliatedCommitterDetailView(DetailView):

    model = AffiliatedCommitter


class AffiliatedCommitterUpdateView(UpdateView):

    model = AffiliatedCommitter


class AffiliatedCommitterListView(ListView):

    model = AffiliatedCommitter


class InfographicDetailCreateView(CreateView):

    model = InfographicDetail


class InfographicDetailDeleteView(DeleteView):

    model = InfographicDetail


class InfographicDetailDetailView(DetailView):

    model = InfographicDetail


class InfographicDetailUpdateView(UpdateView):

    model = InfographicDetail


class InfographicDetailListView(ListView):

    model = InfographicDetail


class OrganizationCreateView(CreateView):

    model = Organization


class OrganizationDeleteView(DeleteView):

    model = Organization


class OrganizationDetailView(DetailView):

    model = Organization


class OrganizationUpdateView(UpdateView):

    model = Organization


class OrganizationListView(ListView):

    model = Organization

