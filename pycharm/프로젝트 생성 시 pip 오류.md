# Django 프로젝트 생성 시 pip 오류

> module 'pip' has no attribute 'main'

Virtual Environment 기반 프로젝트 생성 시 위와 같은 오류가 나타난다면 일단 local python을 참조하고,

setting에서 virtual env 생성 뒤, 

그 폴더에 들어가 pip 다운로드
    
    $ pip install pip==9.0.3