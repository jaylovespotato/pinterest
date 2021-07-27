from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from .decorator import profile_ownership_required
from .forms import ProfileCreationForm
from .models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})

    # 프로필 만들 때 주인 id 가져오기 용

    def form_valid(self, form):
        ### 여기서부터

        # 이거는 우리가 실제 DB에 안넣고 서버단에서 임시저장하는 부분
        # form 은 위에서 받아온 저 form임
        # commit=False로 해서 임시 역할
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()

        ### 여기까지는 우리가 customizing 하는 부분
        return super().form_valid(form)


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})
