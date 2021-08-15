from django.forms import ModelForm

from .models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        #writer는 서버내에서 설정. 왜냐? 남의 article을 만들 수 있으니까.
        fields = ['title', 'image', 'project','content']


