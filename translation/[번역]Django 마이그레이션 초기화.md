# Django 마이그레이션 초기화

_이 문서는 [How to Reset Migrations](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)
를 번역한 것입니다._

Django 마이그레이션 시스템은 많은 수의 마이그레이션들을 작업하는 데에 최적화되어 있습니다. 
따라서 일반적인 경우, 당신은 코드상에서 많은 양의 모델 마이그레이션을 신경쓸 필요가 없습니다.
물론 이는 때때로, 테스트를 돌리는 데에 많은 시간을 소요하는 등 원하지 않는 결과를 초래하긴 하죠. 
하지만 이 경우 당신은 마이그레이션을 간단하게 비활성화시킬 수 있습니다.(비록 지금은 내장 옵션이 없지만요.)

아무튼, 당신이 마이그레이션을 초기화하길 바란다면 이 튜토리얼에 제시된 몇 가지 옵션들을 참고하길 바랍니다.

---
### 시나리오 1
- 프로젝트가 아직 개발 환경에 남아있고, 이것을 전부 초기화하길 바랄 경우
- 데이터베이스를 전부 날려도 되는 경우

#### 1. 프로젝트에 있는 모든 마이그레이션 파일을 삭제합니다.
프로젝트 내 앱들의 마이그레이션 폴더를 각각 열어 `__init__.py` 파일을 제외한 모든 파일들을 삭제합니다.

혹 당신이 unix 계열의 OS를 사용하고 있다면 다음 명령어를 실행해도 됩니다.(프로젝트 폴더 내에서 실행)
    
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete

#### 2. 현재 데이터베이스를 드랍합니다. 만약 sqlite를 사용하고 있다면 `db.sqlite3`를 삭제합니다.

#### 3. 첫 마이그레이션을 생성한 뒤 데이터베이스 스키마를 만듭니다.

    python manage.py makemigrations
    python manage.py migrate

---
### 시나리오 2
- 모든 마이그레이션 기록을 지우고 싶지만 데이터베이스는 유지하고 싶은 경우

#### 1. 당신의 모델이 현재 데이터베이스 스키마에 맞는지 확인합니다.
가장 쉬운 방법은 새로운 마이그레이션을 만들어 보는 것입니다.

    python manage.py makemigrations
      
대기중인 마이그레이션이 있다면, 일단 그것들을 먼저 적용하세요.

만약 아래 메시지가 나타난다면 다음 단계를 진행해도 좋습니다.

    No changes detected
    
#### 2. 각각의 앱에서 마이그레이션 기록을 삭제합니다.
이제 각각의 앱에서 마이그레이션 기록을 삭제해야 합니다.

먼저 현재 상황을 추적할 수 있도록 `showmigrations` 명령어를 실행하세요.

    $ python manage.py showmigrations
    

결과:

    admin
     [X] 0001_initial
     [X] 0002_logentry_remove_auto_add
    auth
     [X] 0001_initial
     [X] 0002_alter_permission_name_max_length
     [X] 0003_alter_user_email_max_length
     [X] 0004_alter_user_username_opts
     [X] 0005_alter_user_last_login_null
     [X] 0006_require_contenttypes_0002
     [X] 0007_alter_validators_add_error_messages
    contenttypes
     [X] 0001_initial
     [X] 0002_remove_content_type_name
    core
     [X] 0001_initial
     [X] 0002_remove_mymodel_i
     [X] 0003_mymodel_bio
    sessions
     [X] 0001_initial
     
이제 마이그레이션 기록을 삭제합니다.(**core**가 앱 이름임을 참고해주세요.)

    $ python manage.py migrate --fake core zero
    
실행한 결과가 이렇게 나올 것입니다.

    Operations to perform:
      Unapply all migrations: core
    Running migrations:
      Rendering model states... DONE
      Unapplying core.0003_mymodel_bio... FAKED
      Unapplying core.0002_remove_mymodel_i... FAKED
      Unapplying core.0001_initial... FAKED
      
이제 `showmigrations` 커맨드를 다시 실행해봅시다.

    $ python manage.py showmigrations
    
결과:

    admin
     [X] 0001_initial
     [X] 0002_logentry_remove_auto_add
    auth
     [X] 0001_initial
     [X] 0002_alter_permission_name_max_length
     [X] 0003_alter_user_email_max_length
     [X] 0004_alter_user_username_opts
     [X] 0005_alter_user_last_login_null
     [X] 0006_require_contenttypes_0002
     [X] 0007_alter_validators_add_error_messages
    contenttypes
     [X] 0001_initial
     [X] 0002_remove_content_type_name
    core
     [ ] 0001_initial
     [ ] 0002_remove_mymodel_i
     [ ] 0003_mymodel_bio
    sessions
     [X] 0001_initial
     
마이그레이션 기록 초기화를 하고 싶은 모든 앱에 대해 이 과정을 거쳐야 합니다.

#### 3. 실제 마이그레이션 파일 삭제
프로젝트 내 앱들의 마이그레이션 폴더를 각각 열어 `__init__.py` 파일을 제외한 모든 파일들을 삭제합니다.

혹 당신이 unix 계열의 OS를 사용하고 있다면 다음 명령어를 실행해도 됩니다.(프로젝트 폴더 내에서 실행)
    
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete
    
> PS: 위의 명령어는 당신 프로젝트 내의 모든 마이그레이션 파일을 지웁니다.

`showmigrations`를 다시 실행해봅시다.

결과:

    admin
     [X] 0001_initial
     [X] 0002_logentry_remove_auto_add
    auth
     [X] 0001_initial
     [X] 0002_alter_permission_name_max_length
     [X] 0003_alter_user_email_max_length
     [X] 0004_alter_user_username_opts
     [X] 0005_alter_user_last_login_null
     [X] 0006_require_contenttypes_0002
     [X] 0007_alter_validators_add_error_messages
    contenttypes
     [X] 0001_initial
     [X] 0002_remove_content_type_name
    core
     (no migrations)
    sessions
     [X] 0001_initial
     
#### 4. 첫 마이그레이션을 생성합니다.

    $ python manage.py makemigrations
    
결과:

    Migrations for 'core':
      0001_initial.py:
        - Create model MyModel
        
#### 5. 첫 마이그레이션을 페이크합니다.
데이터베이스가 이미 존재하기 때문에 첫 마이그레이션을 마이그레이트하지 않습니다. 대신 우리는 이 마이그레이션을 가짜로 마이그레이트할 겁니다.

    $ python manage.py migrate --fake-initial
    
결과:

    Operations to perform:
      Apply all migrations: admin, core, contenttypes, auth, sessions
    Running migrations:
      Rendering model states... DONE
      Applying core.0001_initial... FAKED
      
`showmigrations`를 다시 실행해봅시다.

    admin
     [X] 0001_initial
     [X] 0002_logentry_remove_auto_add
    auth
     [X] 0001_initial
     [X] 0002_alter_permission_name_max_length
     [X] 0003_alter_user_email_max_length
     [X] 0004_alter_user_username_opts
     [X] 0005_alter_user_last_login_null
     [X] 0006_require_contenttypes_0002
     [X] 0007_alter_validators_add_error_messages
    contenttypes
     [X] 0001_initial
     [X] 0002_remove_content_type_name
    core
     [X] 0001_initial
    sessions
     [X] 0001_initial
     
     
모든 준비가 끝났습니다. :-)