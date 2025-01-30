from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @api_view(['GET'])
# def index (request):
#     return Response({
#         "name":"sandra",
#         "phone":1234567890
#     })

@api_view(['GET','POST'])
def index (request):
    if request.method=='GET':
        return Response({
            "name":"sandra",
            "phone":1234567890
    })
    elif request .method=='POST':
        return Response({
            "hellooooooooo"
        })
        