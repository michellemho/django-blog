from django.shortcuts import render
from django.http import Http404
from polling.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

# def list_view(request):
# 	context = {'polls': Poll.objects.all()}
# 	return render(request, 'polling/list.html', context)

class PollListView(ListView):
	model = Poll
	template_name = 'polling/list.html'

class PollDetailView(DetailView):
	model = Poll
	template_name = 'polling/detail.html'
	
	# need to be able to do one more thing, post votes... add method here.
	def post(self, request, *args, **kwargs):
		poll = self.get_object() # retrieve ID of indicated poll
		if request.POST.get("vote") == "Yes":
			poll.score += 1
		else:
			poll.score -= 1
		context = {'object': poll} #context variable named object... generic
		return render(request, 'polling/detail.html', context)

# def detail_view(request, poll_id):
# 	try:
# 		poll = Poll.objects.get(pk=poll_id)
# 	except Poll.DoesNotExist:
# 		raise Http404
# 	if request.method == "POST":
# 		if request.POST.get("vote") == "Yes":
# 			poll.score += 1
# 		else:
# 			poll.score -= 1
# 		poll.save()
# 	context = {'poll': poll}
# 	return render(request, 'polling/detail.html', context)
