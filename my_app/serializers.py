from django.contrib.auth.models import *
from rest_framework import serializers
from my_app.models import *


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'
