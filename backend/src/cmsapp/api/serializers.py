from rest_framework import serializers
from cmsapp.models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'content')