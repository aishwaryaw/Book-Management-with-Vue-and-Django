from django.urls import path,include
from .views import BookViewSet, post_image

urlpatterns = [
    path('books/', BookViewSet.as_view({
        'get' : 'listBooks',
        'post' : 'createBook',
    })),

    path('book/<str:pk>/', BookViewSet.as_view({
        'get' : 'singleBook',
        'put' : 'updateBook',
        'delete' : 'deleteBook'
    })),
    path('book_image/', post_image)

]
