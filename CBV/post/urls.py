from django.urls import path
from django.views.generic.base import TemplateView, RedirectView
from .views import MyView, PostPreLoad, SinglePost


app_name = 'post'

urlpatterns = [
    path('ex1/', TemplateView.as_view(template_name='ex1.html', extra_context={'title':'hello world'})),
    path('ex2/', MyView.as_view() ),
    path('rdt/', RedirectView.as_view(url='https://www.google.com'), name='go to Google'), 
    path('ex3/<int:pk>', PostPreLoad.as_view(), name='preload'), 
    path('ex4/<int:pk>', SinglePost.as_view(), name='single_post'), 
]
