from typing import Any
from django.db.models.query import QuerySet
from django.utils import timezone
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import  DetailView
from django.views.generic.list import  ListView
from django.views.generic.edit import  FormView, CreateView, UpdateView
from .models import Book
from .forms import AddForm
from django.db.models import F


class IndexDetail(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()

        return context
    

# class BookDetail(DetailView):
#     model = Book


class BookDetail(DetailView):
    model = Book
    template_name = 'book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Book.objects.filter(slug=self.kwargs['slug'])
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()

        return context
    


class ListBookView(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'
    paginate_by = 1
    # paginate_by = 2  
    # queryset = Book.objects.all()[:2] ---> this equal to override  get_queryset function 

    # def get_queryset(self) -> QuerySet[Any]:
    #     return Book.objects.all()[:2]
    


class TagView(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'
    paginate_by = 1

    def get_queryset(self, *args, **kwargs) -> QuerySet[Any]:
        return Book.objects.filter(genre__icontains=self.kwargs.get('genre'))
    

# class AddBookView(FormView):
#     template_name = 'add.html'
#     success_url = '/books/'
#     form_class = AddForm

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)



class AddBookView(CreateView):
    model = Book
    template_name = 'add.html'
    success_url = '/books/'
    # fields = ['title']
    form_class = AddForm

    def get_initial(self, *args, **kwargs) -> dict[str, Any]:
        intial = super().get_initial( **kwargs)
        intial['title'] = 'Enter Title'

        return intial
    


class BookEditView(UpdateView):
    model = Book
    template_name = 'add.html'
    success_url = '/books/'
    # fields = ['title']
    form_class = AddForm