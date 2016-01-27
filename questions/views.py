# from django.http import HttpResponse
# from django.views.generic import ListView, DetailView
# from django.views.generic import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
# from .models import Question

# # Create your views here.

# class QuestionList(ListView):
    # model = Question
# class QuestionDetail(DetailView):
    # model = Question
# class QuestionCreate(CreateView):
    # model = Question
    # fields = ['title', 'description'] 
# class QuestionUpdate(UpdateView):
    # model = Question
    # fields = ['title', 'description']
# class QuestionDelete(DeleteView):
    # model = Question
    # success_url = reverse_lazy('question_list') 
from .models import Question
from django.http import Http404

from .serializer import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class QuestionList(APIView):

    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class QuestionDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        question = QuestionSerializer(question)
        return Response(question.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    