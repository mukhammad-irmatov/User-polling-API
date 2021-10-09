from pollApp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("polls",views.PollViewSet,basename="all_polls")
router.register("polls/<int:pk>/questions",views.QuestionViewSet,basename='all_questions')
router.register("polls/<int:pk>/questions/<int:pk>/choices",views.ChoiceViewSet,basename="all_choices")
router.register("activePolls",views.ActivePollsListViewSet,basename="active_polls")
router.register("polls/<int:pk>/questions/<int:pk>/answers",views.AnswerCreateViewSet,basename="all_answers")
router.register('my_polls',views.UserPollListView,basename="userPoll")

urlpatterns = router.urls


