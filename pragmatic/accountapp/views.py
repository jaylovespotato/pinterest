from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .accountupdateform import AccountUpdateForm
from .models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get("hello_world_input")

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


# 로그인 로그아웃 view는 지정해야할 것이 많지 않음. 그냥 url에서 바로 해줌.

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    # 템플릿에서 사용하는 유저 객체의 이름을 다르게 설정.
    # 이 페이지의 주인임. 접속한 사람은 user이고.
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    # form_class = UserCreationForm
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

