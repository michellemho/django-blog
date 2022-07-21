from django.urls import path
from polling.views import PollListView, PollDetailView #, list_view, detail_view

urlpatterns = [
	# path('', list_view, name='poll_index'),
	path("", PollListView.as_view(), name='poll_index'),
	# path('polls/<int:poll_id>/', detail_view, name='poll_detail'),
	path("polls/<int:pk>/", PollDetailView.as_view(), name='poll_detail') # pk for primary key
]
