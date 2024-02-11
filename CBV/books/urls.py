from django.urls import path 
# from .views import  IndexDetail 
from .views import BookDetail, IndexDetail, ListBookView , TagView, AddBookView, BookEditView


app_name = 'book'

urlpatterns = [
    # path('', IndexDetail.as_view(), name='index'),
    path('', ListBookView.as_view(), name='index'),
    path('add/', AddBookView.as_view(), name='index'),
    # path('<slug:slug>/', BookDetail.as_view(), name='book-detail')  ,
    # path('<slug:slug>/edit/', BookEditView.as_view(), name='book-detail')  ,
    path('<int:pk>/', BookDetail.as_view(), name='book-detail')  ,
    path('<int:pk>/edit/', BookEditView.as_view(), name='book-detail')  ,  
    
    path('g/<str:genre>/', TagView.as_view())  ,
]


