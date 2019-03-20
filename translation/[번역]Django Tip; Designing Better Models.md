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
        
모델명은 항상 단수형으로 작성합니다. `Companies` 대신 `Company`를 사용하세요. 
모델을 정의하는 것은 하나의 오브젝트(이 경우엔 하나의 company)에 대한 표현이지 companies의 콜렉션을 가리키는 것이 아닙니다.

한편 이는 가끔 혼돈을 야기하곤 합니다. 왜냐하면 모델은 데이터베이스 테이블로 간주되는 경향이 있기 때문입니다.
하나의 모델은 결국 하나의 테이블로 옮겨지니까요. 
테이블은 오브젝트의 콜렉션을 나타내기 때문에 복수형을 사용하여 명명하는 것이 좋습니다.

Django 모델에서는 `Company.objects`를 통해 오브젝트에 접근할 수 있는데, 
이때 `models.Manager`를 통해 `objects`를 다르게 이름지을 수 있습니다.

    from django.db import models
    
    class Company(models.Model):
        # ...
        companies = models.Manager()
        
이로써 우리는 `Company.companies.filter(name='Google')`과 같은 식으로 companies의 콜렉션에 접근할 수 있습니다.
하지만 나는 일관성을 위해 `objects` 어트리뷰트를 유지하는 것을 선호하기에 이 방법은 거의 쓰지 않습니다.

---

<a name="item2"></a> 
## Model 정렬

Django Coding Style은 내부 클래스, 함수, 어트리뷰트에 대해 다음과 같은 정렬 방법을 추천합니다.

- 만약 고정된 모델 필드를 위한 **choices**가 있다면, 모든 선택사항들을 **tuple of tuples**로 정의합니다.
모든 선택사항의 이름은 클래스명과 같이 대문자여야 합니다.
- 모든 데이터베이스 필드들
- 커스텀 manager 어트리뷰트들
- `class Meta`
- def \_\_str__()
- def save()
- def get_absolute_url()
- 커스텀 메소드들

Example:

    from django.db import models
    from django.urls import reverse
    
    class Company(models.Model):
        # CHOICES
        PUBLIC_LIMITED_COMPANY = 'PLC'
        PRIVATE_COMPANY_LIMITED = 'LTD'
        LIMITED_LIABILITY_PARTNERSHIP = 'LLP'
        COMPANY_TYPE_CHOICES = (
            (PUBLIC_LIMITED_COMPANY, 'Public limited company'),
            (PRIVATE_COMPANY_LIMITED, 'Private company limited by shares'),
            (LIMITED_LIABILITY_PARTNERSHIP, 'Limited liability partnership'),
        )
    
        # DATABASE FIELDS
        name = models.CharField('name', max_length=30)
        vat_identification_number = models.CharField('VAT', max_length=20)
        company_type = models.CharField('type', max_length=3, choices=COMPANY_TYPE_CHOICES)
    
        # MANAGERS
        objects = models.Manager()
        limited_companies = LimitedCompanyManager()
    
        # META CLASS
        class Meta:
            verbose_name = 'company'
            verbose_name_plural = 'companies'
    
        # TO STRING METHOD
        def __str__(self):
            return self.name
    
        # SAVE METHOD
        def save(self, *args, **kwargs):
            do_something()
            super().save(*args, **kwargs)  # Call the "real" save() method.
            do_something_else()
    
        # ABSOLUTE URL METHOD
        def get_absolute_url(self):
            return reverse('company_details', kwargs={'pk': self.id})
    
        # OTHER METHODS
        def process_invoices(self):
            do_something()
            
<a name="item3"></a> 
## 역관계

#### related_name

`ForeignKey` 필드 내의 `related_name` 어트리뷰트는 굉장히 유용합니다.
역관계에 있는 모델에 대해 의미 있는 명명을 할 수 있기 때문입니다. 

경험을 바탕으로 말하건대, 만약 무엇이 `related_name`가 될지 확실치 않다면 `ForeignKey`를 갖고 있는 모델의 복수형을 쓰세요.

    class Company:
        name = models.CharField(max_length=30)
    
    class Employee:
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

이는 `Company` 모델이 `employees`라는 특별한 어트리뷰트를 가진다는 것을 의미합니다.
그리고 이 `employees`는 company와 관련된 모든 employees의 쿼리셋을 반환하죠.

    google = Company.objects.get(name='Google')
    google.employees.all()
    
또한 역관계를 사용하여 `Employee` 인스턴스의 `company` 필드를 수정할 수도 있습니다.

    vitor = Employee.objects.get(first_name='Vitor')
    google = Company.objects.get(name='Google')
    google.employees.add(vitor)
    
    
#### related_query_name

이러한 관계는 쿼리 필터링에도 사용될 수 있습니다. 
예를 들어 'Vitor'라는 이름의 employ가 있는 companies를 리스트로 보고 싶다면 이렇게 하면 됩니다.

    companies = Company.objects.filter(employee__first_name='Vitor')
    
이 관계의 이름을 커스터마이징하고 싶다면 다음과 같이 하면 됩니다.

    class Employee:
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        company = models.ForeignKey(
            Company,
            on_delete=models.CASCADE,
            related_name='employees',
            related_query_name='person'
        )
        
그럼 이렇게 사용할 수 있죠.

    companies = Company.objects.filter(person__first_name='Vitor')

일관된 사용을 위해 `related_name`은 복수형으로, `related_query_name`은 단수형으로 짓는 것이 좋습니다.

<a name="item4"></a> 
## Blank와 Null 필드

나는 전에 [Blank와 Null의 차이점](https://simpleisbetterthancomplex.com/tips/2016/07/25/django-tip-8-blank-or-null.html)에 대한 글을 올린 적 있지만
여기서 간단히 요약하려 합니다.

- **Null**: database-related. 해당 데이터베이스 칼럼이 null 값을 받아들일지 말 것인지를 결정.
- **Blank**: validation-related. 

필수가 아닌 텍스트 기반 필드에는 `null=True`를 사용하지 마세요.
그게 아니면 해당 필드는 "데이터 없음"에 대해 **None**과 **빈 문자열**, 이렇게 두 개의 값을 가질 겁니다.
"데이터 없음"에 대해 가능한 값이 두 개라는 건 중복입니다.
Django는 NULL이 아닌 빈 문자열을 사용합니다.

Example:

    # The default values of `null` and `blank` are `False`.
    class Person(models.Model):
        name = models.CharField(max_length=255)  # Mandatory
        bio = models.TextField(max_length=500, blank=True)  # Optional (don't put null=True)
        birth_date = models.DateField(null=True, blank=True) # Optional (here you may add null=True)

## 더 읽을거리

모델 정의는 Django 어플리케이션에서 가장 중요한 부분 중 하나입니다.
필드 유형을 적절하게 정의함으로써 
[Django models field types](https://docs.djangoproject.com/en/2.0/ref/models/fields/#model-field-types)
을 검토하여 옵션들을 확인하세요. 필드 타입을 커스터마이징할 수도 있습니다.

만약 코드 규약에 관심이 있다면, [Django’s Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
을 둘러보는 것을 추천합니다. 또한 제가 전에 올렸던 [flake8 library](https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html)
튜토리얼은 당신이 PEP8을 따르는 데 도움될 것입니다.