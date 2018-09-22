from django.shortcuts import render

#클래스형 제네릭 뷰를 위해 TemplateView, ListView, DetailView 클래스 임포트
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

#테이블 조회를 위해 모델클래스들 임포트
from books.models import Book, Author, Publisher


#Book 어플리케이션의 첫 화면을 보여주기 위한 뷰다 템플릿만 렌더링하는 경우에는 TemplateView 제네릭 뷰를 상속받는다.
class BooksModelView(TemplateView):
	#TemplateView 를 상속받는경우 필수적으로 template_name 클래스를 오버라이딩해 지정해야한다.
	template_name = 'books/index.html'
	
	#템플릿 시스템으로 넘겨줄 컨텍스트 변수가 있는경우 get_context_data() 메소드를 오버라이딩한다.
	def get_context_data(self, **kwargs):
		
		#get_context_data 를 사용하면 맨 첫번째줄에 super() 메소드를 호출해야한다.
		context = super().get_context_data(**kwargs)
		
		#books 애플리케이션 화면에 테이블 리스트를 보여주기 위해 model_list 에 담아 템플릿을 호출한다.
		context['model_list'] = ['Book', 'Author', 'Publisher']
		
		#get_context_data 를 사용하면 return 도 필수다
		return context


#--LIST VIEW
# ListView 를 상속받는 경우 
# 객체가 들어있는 리스트를 구성해 이를 컨텍스트 변수로 템플릿 시스템에 넘겨주면 된다.
# 모든 레코드를 가져와 구상하는 경우는 테이블명 즉 모델명만 지정해주면 된다.

# 명시적으로 지정하지 않아도 장고에서는 디폴트로 지정해주는 속성이 2가지가 있다.
# 1. 컨텍스트 변수로 objext_list를 사용하는 것
# 2. 템플릿 파일을 모델명 소문자_list.html 형식으로 지정하는것
class BookList(ListView):
	model = Book
	
class AuthorList(ListView):
	model = Author

class PublisherList(ListView):
	model = Publisher




#--DETAIL VIEW	
# DetailView를 상속받는 경우
# 특정객체 하나를 컨텍스트 변수에 담아서 템플릿 시스템에 넘겨주면 된다.
# 만약 테이블에서 Primary Key 로 조회하여 특정 객체를 가저오는경우는 모델클래스만 지정해주면 된다.
# 조회시 사용한 Primary Key 값은 URLconf에서 추출한 값으로 사용.

# 명시적으로 지정하지 않아도 장고에서는 디폴트로 지정해주는 속성이 2가지가 있다.
# 1. 컨텍스트 변수로 objext를 사용하는 것
# 2. 템플릿 파일을 모델명 소문자_detail.html 형식으로 지정하는것
class BookDetail(DetailView):
	model = Book
	
class AuthorDetail(DetailView):
	model = Author

class PublisherDetail(DetailView):
	model = Publisher 
	
