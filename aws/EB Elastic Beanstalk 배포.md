# EB Elastic Beanstalk 배포

### 애플리케이션 생성
EB 서비스 페이지에서 '새 애플리케이션 생성' 클릭한 뒤 생성

### 환경 생성
1. '웹 서버 환경' 클릭
2. 환경 이름 입력 (ex. staging-env, prod-env)
3. 플랫폼에서 Python 선택

---

### Django 배포

[자습서 참고](https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-setup-venv)

(Django 리퍼지토리가 있다는 가정 하에)

1. 기본 환경 구성
    - 가상환경 활성화
    - requirements.txt 파일 생
2. eb 환경 구성
    - .ebextensions이라는 디렉터리 생성
   ```
   $ mkdir .ebextensions
   ```
3. .ebextensions 내 django.config라는 구성 파일 추가
    ```
    option_settings:
      aws:elasticbeanstalk:container:python:
        WSGIPath: config/wsgi.py
    container_commands:
      01_wsgipass:
        command: 'echo "WSGIPassAuthorization On" >> ../wsgi.conf'
    ```
4. .ebextensions 내 db-migrate.config라는 구성 파일 추가
    ```
    container_commands:
      01_migrate:
        command: "python manage.py migrate"
        leader_only: true
    option_settings:
      aws:elasticbeanstalk:application:environment:
        DJANGO_SETTINGS_MODULE: config.settings.staging
    ```
    * DJANGO_SETTINGS_MODULE은 staging일 경우, production일 경우 구분해서 입력해야 함
5. EB 환경 적용
    - Django 프로젝트 디렉토리 아래서 eb init 후 생성한 애플리케이션, 환경 차례로 선택
    ```
    $ eb init
    ```
6. 자동으로 생성된 .elasticbeanstalk 아래 config.yml 적절히 수정
    ```
    branch-defaults:
      master:
        environment: master-env
      develop:
        environment: development-env
    global:
      application_name: my-application-name
      branch: null
      default_ec2_keyname: null
      default_platform: Python 3.6
      default_region: ap-northeast-2
      include_git_submodules: true
      instance_profile: null
      platform_name: null
      platform_version: null
      profile: eb-cli
      repository: null
      sc: git
      workspace_type: Application
    ```
7. 배포
    ```
    $ eb deploy
    ```

---

### 주의

- 배포된 URL로 들어가면 당연히 `Not Found`가 뜬다. 유효한 URL로 체크하도록.

