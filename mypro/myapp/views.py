from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import TodoSerializer
# Create your views here.
# @api_view(['GET'])
# def index (request):
#     return Response({
#         "name":"sandra",
#         "phone":1234567890
#     })

# @api_view(['GET','POST'])
# def index (request):
#     if request.method=='GET':
#         return Response({
#             "name":"sandra",
#             "phone":1234567890
#     })
#     elif request .method=='POST':
#         return Response({
#             "hellooooooooo"
#         })

@api_view(['POST'])
def add_todo(request):
    if request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_todos(request):
    if request.method=='GET':
        todos=Todo.objects.all()
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_todo(request,id):
    try:
        todo=Todo.objects.get(pk=id)
        todo.delete()
        return Response(
            {'message': 'Todo deleted successfully'},
            status=status.HTTP_204_NO_CONTENT

        )
    except Todo.DoesNotExist:
        return Response(
            {'error':'Todo not found'},
            status=status.HTTP_404_NOT_FOUND
        )