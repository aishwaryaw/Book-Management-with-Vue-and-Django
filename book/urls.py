from django.urls import path,include
from .views import BookViewSet

urlpatterns = [
    path('books/', BookViewSet.as_view({
        'get' : 'listBooks',
        'post' : 'createBook',
    })),

    path('book/<str:pk>/', BookViewSet.as_view({
        'get' : 'singleBook',
        'put' : 'updateBook',
        'delete' : 'deleteBook'
    }))

]