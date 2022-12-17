from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    return Response({"message": "Hello, world!"})


@api_view(['GET'])
def results(request, result_id):
    return Response(f'Hello, world. You\'re at the scraper result {result_id}')


@api_view(['GET'])
def vote(request, vote_id):
    return Response(f'Hello, world. You\'re at the scraper vote {vote_id}')
