from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Answer
from django.utils import timezone


def index(request):
    question_list = Question.objects.order_by('-create_date')  # '-' 넣으면 내림차순, 안 넣으면 오름차순
    context = {'question_list': question_list}  # 왼쪽은 키, 오른쪽은 값
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)  # 없는 페이지 입력시 not found
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)