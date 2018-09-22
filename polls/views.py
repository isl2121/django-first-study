from django.shortcuts import get_object_or_404, render							#장고의 단축함수인 render() 함수 임포트
from django.http import HttpResponseRedirect, HttpResponse						#HttpRedirect 필요하여 추가
from django.urls import reverse
from polls.models import Choice, Question										#Question테이블을 가져오기 위해polls.models.question 클래스 임포트
from django import forms
from django.views.generic import View
from django.views import generic

import logging

logger = logging.getLogger(__name__)
	
def vote(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		#설문 투표폼을 다시보여준다.
		#파일을 찾지 못하였을경우 question과 함께 리다이렉트
		return render(request, 'polls/detail.html', {
			'question' : question,
			'error_message': "You didn't select a choice",
		});
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# POST 데이터를 정상적으로 처리했으면
		# 항상 HttpResponseRedirect로 번환처리함
		
		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
		  

	
class indexView(generic.ListView):
	logger.debug("vote().question_id: %s % question_id")
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self)	:
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
	
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

	
	

class NameForm(forms.Form):														# 클래스 함수
	your_name 	= forms.CharField(label='your name', max_length=5)				# your name 이라는 길이가 5글자 text폼을 생성
	subject		= forms.CharField(max_length=100)
	message		= forms.CharField(widget=forms.Textarea)
	sender 		= forms.EmailField()
	cc_myself	= forms.BooleanField(required=False)


		
		
		

def test(request):																# 실험적으로 만든 뷰
	
	if request.method == 'POST':												# 요청방식에 따라 GET 요청과 POST 요청이 된다. 폼에 데이터를
																				# 넣고 전송하면 POST 요청으로 도착한다.
		form = NameForm(request.POST)											# 입력받은 데이터를 다시 form에 채워둔다 이걸 바운드 폼이라 한다.
		
		if form.is_valid():														# 폼의 is_vaild를 호출하여 올바른 폼인지 판단하여 맞으면 TRUE 반환
		
			new_name = form.cleaned_data['name']								# cleaned_data 에 폼이 들어있으면 이 데이터를 처리
			
			return HttpResponseRedirect('/thanks/')
	
	else:																		# GET 요청이 들어오면 빈폼 객체를 생성하고 렌더링해 시스템으로 전달
		form = NameForm()														# 이부분은 처음으로 사용자가 들어올때 일어나는 동작이다.
	
	return render(request, 'polls/test.html', {'form':form.as_ul} )			# is_vaild에서 false일경우 다시 form 에 데이터를 담아 보낸다.
																				# render 함수는 템플릿코드 test.html 에 데이터를 담아 보낸다.
	