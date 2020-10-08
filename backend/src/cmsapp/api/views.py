from rest_framework.generics import ListAPIView, RetrieveAPIView
from cmsapp.models import Quiz
from .serializers import QuizSerializer

class QuizListView(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetailView(RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

