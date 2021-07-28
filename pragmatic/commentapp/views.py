from django.shortcuts import render
from django.urls import reverse

from django.views.generic import CreateView

from .forms import CommentCreationForm
from .models import Comment
from articleapp.models import Article


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        ### 여기서부터

        # 이거는 우리가 실제 DB에 안넣고 서버단에서 임시저장하는 부분
        # form 은 위에서 받아온 저 form임
        # commit = False로 해서 임시역할
        temp_comment = form.save(commit=False)
        # temp_comment.article = self.request.user
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()

        ### 여기까지는 우리가 customizing 하는 부분
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
