from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView

from .form import ProjectCreationForm
from .models import Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "projectapp/create.html"

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectListView(ListView):
    model = Project
    context_object_name = "project_list"
    template_name = "projectapp/list.html"
    paginate_by = 25


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "target_project"
    template_name = "projectapp/detail.html"
