from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('I hate Ethan')

from django.contrib.auth.models import *
from rest_framework import viewsets
from my_app.serializers import *

@csrf_exempt
@api_view(['GET'])
def get_poems(request):
	print('fuck off')
	poems = Poem.objects.all()
	return Response(PoemSerializer(poems,many=True).data, 200)
