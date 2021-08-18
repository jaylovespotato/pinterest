from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from .models import Subscription
from projectapp.models import Project

from articleapp.models import Article


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
        # 플젝 디테잂 페이지에서 구독을 누를 수 있게 할 것임.
        # 차이점은.. 아래 거는, 해당하는 주인의 pk를 가져 왔다면, 여기서는 project_pk를 get 방식으로 받아서 이 pk를 가지고 있는 페이지로 되돌아 가는 것.
        # return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})

    def get(self, request, *args, **kwargs):

        # Project_pk 를 가지고 있는 Project를 찾는데, 없으면 404에러
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        # 위 두 정보로 subscription 찾는다
        subscription = Subscription.objects.filter(user=user, project=project)

        # 토글 형식
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list