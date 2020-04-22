from django.db import models

# Create your models here.
class Todo(models.Model):  #models.Model 클래스를 상속
    task = models.CharField(max_length=200, null=False, help_text="할 일을 채워주세요!")
    is_done = models.BooleanField(default=False)

    def __str__(self):  
        return self.task  
        #자기 task를 돌려준다. : '할일'의 내용을 표시해주기 위한 메써드 / 이 메써드 없으면 'object 1'같이 표시됨.
        #메써드엔 self 쓴다. self자리에 인스턴스가 들어갈 거임
        # __str__ : ?