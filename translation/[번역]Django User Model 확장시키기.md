# Django User Model 확장시키기

_이 문서는 [How to Extend Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
를 번역한 것입니다._

Django는 훌륭한 내장 인증 시스템을 가지고 있습니다.
대부분의 경우, 우리는 별 다른 설정이나 설치 없이 이 기능을 사용하여 개발/테스팅에 들이는 노력을 아낄 수 있습니다.
이는 거의 모든 상황에 적합하며 매우 안전합니다. 
하지만 우리는 가끔 각자의 웹 어플리케이션에 맞는 수정을 필요로 하죠.

흔히 유저와 관련된 정보를 추가로 저장할 때가 그렇습니다. 
만약 당신의 웹 어플리케이션이 SNS와 같은 성격을 지니고 있다면, 유저의 상태와 위치, 그리고 기타 정보들을 저장해야 할 겁니다.

이 튜토리얼에서는 Django User Model을 (처음부터 설정할 필요 없이) 간단히 확장할 수 있는 방법을 소개하겠습니다.

---
### 기존 User Model을 확장하는 방법들

일반적으로 이미 존재하는 User Model을 확장시키는 방법은 4가지입니다. 왜, 그리고 언제 이 방법들을 써야 하는지 읽어주세요.


#### **Option 1:** Proxy Model 사용하기
##### Proxy Model이란?
Proxy Model은 데이터베이스에 새로운 테이블을 생성할 필요가 없는 모델 상속입니다. 
이는 기존 데이터베이스 구조에 영향을 주지 않고 이미 존재하는 모델의 행동을 바꿀 때(ex. 기본 정렬, 새로운 메소드 추가 등) 사용합니다.

##### 언제 사용하나요?
데이터베이스에 추가 정보를 저장하지 않는 상태에서 메소드를 추가하거나 해당 모델의 Query Manager를 변경할 때 사용합니다.

이 경우, [다음 지시](#option1)를 따릅니다.


#### **Option 2:** User Model에 일대일(One-To-One) 관계 적용하기
##### 일대일 관계란?
일대일 관계는 자체 데이터베이스 테이블을 가지고 있는 Django 고정 모델입니다. 
이는 `OneToOneField`를 통해 이미 존재하는 User Model과 일대일 관계를 유지합니다.

##### 언제 사용하나요?
이미 존재하는 User Model에 추가 정보를 저장해야 할 경우, 그리고 그 정보가 인증 절차에 관련이 없을 경우 일대일 관계를 사용합니다. 
이를 보통 User Profile이라 부르죠.

이 경우, [다음 지시]()를 따릅니다.


#### **Option 3:** AbstractBaseUser를 상속하여 커스텀 User Model 만들기
##### AbstractBaseUser를 상속한 커스텀 User Model이란?
이는 `AbstractBaseUser`를 상속받은 완전히 새로운 User Model입니다. 
이 모델은 특별한 관리를 필요로 하며 `settings.py`를 통해 몇 가지 레퍼런스를 업데이트 해주어야 합니다.
이는 데이터베이스 스키마에 극단적인 변화를 주기 때문에 프로젝트를 시작할 때 설정해주는 것이 좋습니다.
또 실행하는 동안 추가적인 관리가 필요하죠.

##### 언제 사용하나요?
커스텀 User Model은 당신의 어플리케이션이 인증 절차에 대해 특정 요구사항을 가지고 있을 때 사용합니다.
예를 들어 어떤 경우에서는, 유저 이름보다 이메일 주소를 인증 토큰으로 사용하는 것이 더 합리적이겠죠.

이 경우, [다음 지시]()를 따릅니다.


#### **Option 4:** AbstractUser를 상속하여 커스텀 User Model 만들기
##### AbstractUser를 상속한 커스텀 User Model이란?
이는 `AbstractUser`를 상속받은 새로운 User Model입니다. 이하 설명은 Option 3와 같습니다.

#### 언제 사용하나요?
이는 AbstractBaseUser와 달리, 당신이 Django 인증 프로세스를 그대로 받아들이고 싶을 때,
그리고 이와 동시에 추가적인 클래스 생성 없이 기존 User Model에 추가 정보를 저장하고 싶을 때 사용합니다.(**Option 2**처럼 말이죠.)

이 경우, [다음 지시]()를 따릅니다.
 
---
 
### Proxy Model을 사용하여 User Model 확장하기<a name="option1"></a>
이는 User Model을 간단하게 확장하는 방법입니다.
아무런 문제도 일어나지 않을 테지만, 매우 한정적이죠.
 

    from django.contrib.auth.models import User
    from .managers import PersonManager
    
    class Person(User):
       objects = PersonManager()
    
       class Meta:
           proxy = True
           ordering = ('first_name', )
    
       def do_something(self):
           ...
            
위의 예시에서는 `Person`이라는 Proxy Model을 정의합니다.
Meta 클래스 내에서 `proxy = True`를 적어 Django에게 이 모델이 Proxy Model이라고 알려줍니다.

이 경우 우리는 기본 정렬을 재정의할 수 있고, 모델에 커스텀 `Manager`를 할당할 수 있습니다. 
또 `do_something`과 같은 새로운 메소드도 정의할 수 있습니다.

여기서 `User.objects.all()`과 `Person.objects.all()`이 동일한 데이터베이스 테이블을 참조한다는 것에 주목해야 합니다. 
이 둘의 유일한 차이는 Proxy Model 내에 정의된 것들뿐입니다.

---
