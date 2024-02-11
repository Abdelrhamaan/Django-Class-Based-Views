from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from post.models import Post
from django.db.models import F



class MyView(TemplateView):
    template_name = 'ex2.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = Post.objects.get(id=1)
        context['name'] = Post.objects.get(id=1).name
        return context


class PostPreLoad(RedirectView):
    pattern_name = 'post:single_post' # which page will he redirect to (single post)

    #  evey time anyone got post url increase count by one 
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        post = Post.objects.filter(pk=kwargs['pk']) 
        post.update(count=F('count') + 1)   

        return super().get_redirect_url(*args, **kwargs)


class SinglePost(TemplateView):
    template_name = 'ex3.html' # which page will be rendered

    # override get_context_data which responsible of get context data
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = get_object_or_404(Post, pk = kwargs['pk']) 
        
        
        return context
