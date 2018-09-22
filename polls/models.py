from django.db import models

class Question(models.Model): # 컬럼명은 Question
	#id = models.ForeignKey(autoincrement) id는 자동으로 장고에서 만들어준다.
	# 속성은 not null 과 자동증가
	
	#컬럼명 = question_text 타입은 varchar (200)
	#장고에서 클래스 변수는 question_text
	question_text = models.CharField(max_length=200)
	
	#컬럼명 = pub_date  타입은 datetime
	#장고에서 클래스 변수는 datetime
	#date published 는 pub_date 에 대한 레이블 문구.
	pub_date = models.DateTimeField('date published')
	
	# str 메소드는 객체를 문자열로 표현할떄 사용하는 함수이다 나중에 Admin 사이트나 장고 쉘등에 테이블을 보여주는데
	# 메소드를 정의하지 않으면 테이블명이 제대로 나오지 않는다.
	def __str__(self):
		return self.question_text
		
class Choice(models.Model):
	
	#id = models.ForeignKey(autoincrement) id는 자동으로 장고에서 만들어준다.
	# 속성은 not null 과 자동증가

	#컬럼명 = question_id 타입 = integer
	#장고의 클래스 변수 = question
	#FK(ForeignKey) 는 다른테이블 PK에 연결되므로 question 클래스의 id 변수까지 지정할 필요없이 question 클래스만 지정
	#실제 테이블에서는 FK로 지정된 컬럼은 뒤에 _id가 붙는다.
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	
	#컬럼명 = choice_text 타입 varchar(200)
	#장고의 클래스변수 = choide_text
	choice_text = models.CharField(max_length=200)
	
	#컬럼명 votes 타입 integer
	#클래스변수 = votes
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.choice_text
