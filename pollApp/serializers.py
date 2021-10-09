from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.db.models import Q
from .models import Poll,Answer,Choice,Question

#all surveys which we have
class PollSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Poll

# anser choices we have
class ChoicesSerializer(ModelSerializer):
    class Meta:
        fields = ("id","choiceText")
        model = Choice

#all questions we have
class QuestionsSerializer(ModelSerializer):
    class Meta:
        fields = ("id",'question_text','question_type','poll')
        model = Question

#all answers we have
class AnswersSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer

#Questions with all answer from the user
class AllQuestionsListSerializer(ModelSerializer):
    answers = serializers.SerializerMethodField("obtain_answers")
    class Meta:
        fields = ['question_text','answers']
        model = Question
    # I used obtain_answer function in order to get all anwers matched to the answer
    def obtain_answers(self,question):
        author_id = self.context.get('request').user.id
        answers = Answer.objects.filter(
            Q(question=question) & Q(author__id = author_id)
        )
        serializer = AnswersSerializer(instance=answers,many=True)
        return serializer.data

#All polls with both questions and answers
class UserPollSerializer(ModelSerializer):
    questions = AllQuestionsListSerializer(read_only=True,many=True)

    class Meta:
        fields = '__all__'
        model = Poll

class UserFilterField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        question_id = self.context.get('request').parser_context['kwargs'][
            'question_pk']
        request = self.context.get('request', None)
        queryset = super(UserFilterField,
                         self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(question_id=question_id)

#Answers with the text answer
class AnswerTextAnswerSerializer(ModelSerializer):
    class Meta:
        fields = ['text_answer']
        model = Answer

#Single choice answer serializer class
class AnswerSingleAnswer(ModelSerializer):
    single_answer = UserFilterField(
        many = False,
        queryset = Choice.objects.all()
    )

    class Meta:
        fields = ['single_answer']
        model = Answer

#Multiple answers allowing in this serializer class
class AnswerMultipleAnswer(ModelSerializer):
    multiple_answer = UserFilterField(
        many = True,
        queryset = Choice.objects.all()
    )

    class Meta:
        fields = ['multiple_answer']
        model = Answer
