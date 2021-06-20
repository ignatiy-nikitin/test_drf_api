from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view()
def first_view(request):
    return Response({"message": "First View"})


class FirstApiView(APIView):
    def get(self, request, format=None):
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        return Response({'message': 'get from FirstApiView'})

    def post(self, request, format=None):
        return Response({'message': 'post from FirstApiView'})


class MainApiView(APIView):
    def get(self, request, format=None):
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        return Response({'message': 'get from MainApiView'})

    def post(self, request, format=None):
        return Response({'message': 'post from MainApiView'})