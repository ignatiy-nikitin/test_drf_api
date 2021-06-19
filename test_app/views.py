from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view()
def first_view(request):
    return Response({"message": "First View"})
