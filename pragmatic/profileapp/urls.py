from django.urls import path

from .views import ProfileCreateView, ProfileUpdateView

app_name='profileapp'

urlpatterns=[
    # path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),

]