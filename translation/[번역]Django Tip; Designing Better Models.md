# Django Tip; Designing Better Models

_이 문서는 [Designing Better Models](https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html)
를 번역한 것입니다._

이 글에서는, 더 나은 Django 모델을 디자인 하기 위한 몇 가지 팁을 공유하려 합니다.
이중 명명법에 관련된 팁이 많은 비중을 차지하는데, 이는 당신의 코드를 훨씬 읽기 쉽게 만들어 줄 것입니다.

[PEP8](https://www.python.org/dev/peps/pep-0008/)은 파이썬 생태계에서 널리 쓰이고 있죠. 
따라서 당신이 프로젝트를 진행할 때엔 이를 따르는 것이 좋습니다.

PEP8 외에도 전 Django를 개발하는 사람들을 위한 [Django's Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/) 또한 선호합니다.

우리가 살펴볼 항목들은 이렇습니다.
- [Model 이름 짓기](#item1)
- [Model 정렬](#item2)
- [역관계](#item3)
- [Blank와 Null 필드](#item4)

---

<a name="item1"></a> 
## Model 이름 짓기 
모델은 클래스로 정의되므로 항상 **CapWords**를 (_ 없이) 사용해야 합니다.
`User`, `Permission`, `ContentType`처럼요.

모델의 어트리뷰트에는 `first_name`, `last_name`과 같은 **snake_case**를 사용합니다.

예시:

    from django.db import models
    
    class Company(models.Model):
        name = models.CharField(max_length=30)
        vat_identification_number = models.CharField(max_length=20)
        
---

<a name="item2"></a> 
## Model 이름 짓기 

Django Coding Style은 내부 클래스, 함수, 어트리뷰트에 대해 다음과 같은 순서를 추천합니다.

- 만약 고정된 모델 필드를 위한 **choices**가 있다면, 모든 선택사항들을 tuple 내 tuple로 정의합니다.
모든 선택사항의 이름은 