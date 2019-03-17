# module 'pip' has no attribute 'main'

Django 프로젝트를 시작하려는데 Django 모듈을 받자 다음과 같은 에러가 발생했다.

> module 'pip' has no attribute 'main'

아마 PyCharm과 pip 버전이 맞지 않아 생기는 문제같다.
이럴 땐 pip 버전을 다운그레이드 해주면 된다.

    pip install --upgrade pip==9.0.3
