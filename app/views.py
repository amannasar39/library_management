from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import bookserializer
from .models import book

# Create your views here.
#create book
class bookcreate(APIView):
    def post(self,request):
        serializer_instance=bookserializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#list book
class booklist(APIView):
    def get(self,request):
        qs=book.objects.all()
        serializer_instance=bookserializer(qs,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

#retrieve all book
class booklist(APIView):
    def get(self,request):
        qs=book.objects.all()
        serializer_instance=bookserializer(qs,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)


#retrieve book using id
class bookretrieve(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(book,id=pk)
        serializer_instance=bookserializer(qs)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

#update book
class bookupdate(APIView):
    def put(self,request,pk):
        qs=book.objects.get(id=pk)
        serializer_instance=bookserializer(qs,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


#partial update book
class bookpartialupdate(APIView):
    def patch(self,request,pk):
        qs=book.objects.get(id=pk)
        serializer_instance=bookserializer(qs,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



#delete book
class bookdelete(APIView):
    def delete(self,request,pk):
        qs=book.objects.get(id=pk)
        qs.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
    


    