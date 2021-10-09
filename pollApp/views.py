from rest_framework import viewsets,mixins,permissions
from .serializers import (PollSerializer,ChoicesSerializer,QuestionsSerializer,
                          AnswersSerializer,AllQuestionsListSerializer,UserPollSerializer,
                          AnswerMultipleAnswer,AnswerSingleAnswer,AnswerTextAnswerSerializer)
from .models import Poll,Question,Answer,Choice
from rest_framework.generics import get_object_or_404
from datetime import datetime
from django.db.models import Q
# Create your views here.

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAdminUser,)

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionsSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        poll = get_object_or_404(Poll, id=self.kwargs['id'])
        return poll.questions.all()

    def perform_create(self, serializer):
        poll = get_object_or_404(Poll, pk=self.kwargs['id'])
        serializer.save(poll=poll)

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoicesSerializer
    permission_classes = (permissions.IsAdminUser,)

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            pk = self.kwargs['question_pk'],
            poll__id = self.kwargs['id']
        )
        serializer.save(question=question)

    def get_queryset(self):
        question = get_object_or_404(Question, id=self.kwargs['question_pk'])
        return question.choices.all()

class AnswerCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ActivePollsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.AllowAny,)


class UserPollListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserPollSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Poll.objects.exclude(~Q(questions__answers__author__id=user_id))
        return queryset