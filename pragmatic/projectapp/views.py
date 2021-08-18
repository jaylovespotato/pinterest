from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from .form import ProjectCreationForm
from .models import Project
from articleapp.models import Article

from subscribeapp.models import Subscription


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


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = "target_project"
    template_name = "projectapp/detail.html"

    paginate_by = 25

    def get_context_data(self, **kwargs):

        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None

        # obj_list에다가
        # 현재 프로젝트의 오브젝트와 같은 프로젝트를 가진 아티클을 모두 필터링
        object_list = Article.objects.filter(project=self.get_object())

        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                               **kwargs)
