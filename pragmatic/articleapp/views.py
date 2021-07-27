from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .decorator import article_ownership_required
from .form import ArticleCreationForm
from .models import Article


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

    # article 만들 때 주인 id 가져오기 용

    def form_valid(self, form):
        ### 여기서부터

        # 이거는 우리가 실제 DB에 안넣고 서버단에서 임시저장하는 부분
        # form 은 위에서 받아온 저 form임
        # commit = False로 해서 임시역할
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()

        ### 여기까지는 우리가 customizing 하는 부분
        return super().form_valid(form)


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'
