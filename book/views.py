from django.shortcuts import render
from rest_framework import viewsets, permissions,serializers
from .models import Book
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND
from .serializers import BookSerializer
import os
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class BookViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    # Get all books belonging to current logged in user 
    def listBooks(self,request):
        books = Book.objects.filter(user=request.user)
        bookSerializer = BookSerializer(books,many=True)
        return Response(bookSerializer.data, status=HTTP_200_OK)

    # Add a new book
    def createBook(self, request,*args,**kwargs):
        try:
            serializer = BookSerializer(data= request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=HTTP_201_CREATED)
        
        except serializers.ValidationError:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(status=HTTP_400_BAD_REQUEST)
            
    # Get details of requested book 
    def singleBook(self,request,pk=None):
        try:
            requiredBook = Book.objects.get(id=pk)
            if requiredBook.user == request.user:
                bookSerializer = BookSerializer(requiredBook)
                return Response(bookSerializer.data, status=HTTP_200_OK)
            else:
                return Response({"message":"This book does not belong to you"}, status=HTTP_404_NOT_FOUND)
            
        except:
            return Response({"message":"Id does not exist"}, status=HTTP_404_NOT_FOUND)

    # Update the requested book  
    def updateBook(self, request, pk=None):
        try:
            book = Book.objects.get(id=pk)
            url = os.environ.get('url')
            serializer = BookSerializer(instance=book, data=request.data)
            if 'poster_image' in request.data and f'{url}/uploads/' in request.data['poster_image']:
                # book.poster_image = request.data['poster_image'].replace(f'{url}/uploads/','uploads/')
                # book.save()
                serializer.initial_data.pop('poster_image')
                if serializer.is_valid(raise_exception = True):
                    serializer.save()
            else:
                if serializer.is_valid(raise_exception=True):
                    if 'poster_image' not in serializer.validated_data:
                        book.poster_image.delete(save=True)
                        book.save()
                    serializer.save()
            return Response(serializer.data, status = HTTP_202_ACCEPTED)

        except serializers.ValidationError:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(status=HTTP_400_BAD_REQUEST)
    

    # Delete the requested book
    def deleteBook(self, request, pk = None):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except:
            return Response({"message":"Id does not exist"}, status=HTTP_404_NOT_FOUND)





