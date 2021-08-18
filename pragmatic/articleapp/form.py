from django import forms
from django.forms import ModelForm

from .models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):

    content = forms.CharField(widget = forms.Textarea(attrs={'class':'editable text-left',
                                                             'style':'height: auto;'
                                                             }))
    
    #이거 foreign key 사용하는 필드. queryset은 필수
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)


    class Meta:
        model = Article
        #writer는 서버내에서 설정. 왜냐? 남의 article을 만들 수 있으니까.
        fields = ['title', 'image', 'project','content']


