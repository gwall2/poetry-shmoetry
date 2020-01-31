from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

import boto3
client = boto3.client('comprehend')

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



@csrf_exempt
@api_view(['POST'])
def anal_text(request):
    print('fuck off')
    response = client.detect_key_phrases(
        Text=request.data.get('text'),
        LanguageCode='en'
    )
    import pdb; pdb.set_trace()
    return Response(PoemSerializer(poems,many=True).data, 200)