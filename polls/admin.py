from django.contrib import admin

#models.py 에서 등록한 정보를 가져와서 어드민페이지에 임포트 하겠다는 내용
from polls.models import Question, Choice

#class ChoiceInline(admin.StackedInline):										# 한 화면에서 변경하기
class ChoiceInline(admin.TabularInline):										# 테이블 형식으로 보여주기
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text']										# 필드 순서 변경하기
	fieldsets = [																# 각 필드 분리하기
		('Question Statment', {'fields': ['question_text']}),
		#('Date Information', {'fields': ['pub_date']}),						
		('Date Information',{'fields': ['pub_date'], 'classes': ['collapse']}),	# 필드 접기 
	]
	inlines = [ChoiceInline]													# 위에서 선언한 Choice 모델 같이 사용하기			
	list_display = ['question_text', 'pub_date']								# 리스트형식으로 변경
	list_filter = ['pub_date']													# 옆에 필터추가
	search_fields = ['question_text']											# 검색 추가



#클래스를 임포트하고 admin.site.register() 함수를 사용하여 Admin페이지에 등록
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
