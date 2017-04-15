from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
def index(request):
    latestQuestionList = Question.objects.order_by('-datePublished')[:5]
    context = {
        'latestQuestionList' : latestQuestionList,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})
    
def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)
    
def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)