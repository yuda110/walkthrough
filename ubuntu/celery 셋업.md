# celery 셋업 과정

## 설치
- 일단 RabbitMQ 받는다. celery를 이용하기 위해서는 RabbitMQ라는 메시지 브로커 소프트웨어(오픈소스)가 있어야 한다. 
    
    
    $ sudo apt-get install rabbitmq-server


- celery 받는다(venv를 사용할 경우, venv에다 받을 것)


    $ pip install celery
    

- 프로젝트 아래에서 시험 삼아 돌려본다.


    $ celery -A {{project_name}} worker --loglevel=info
    
    
## Daemonization
celery를 daemon으로 돌리고 싶다면, 이 [블로그](https://pythad.github.io/articles/2016-12/how-to-run-celery-as-a-daemon-in-production)를 따라한다.
- /etc/init.d/celeryd 파일을 만들고, [celery github](https://github.com/celery/celery/blob/master/extra/generic-init.d/celeryd)를 참조하여 내용을 복붙한다.


    $ sudo touch /etc/init.d/celeryd
    
- 그리고 파일 권한을 설정해준다.


    $ sudo chmod 755 /etc/init.d/celeryd
    $ sudo chown root:root /etc/init.d/celeryd
    
    
- /etc/default/celeryd 파일을 만들어야 한다.


    $ sudo touch /etc/default/celeryd
    
    
    
## celery 관련 명령어
- celery 시작/종료/재시작


    $ /etc/init.d/celeryd {start|stop|restart}


- celery  


    $ celery -A {project_name} worker -l info

- 실행되고 있는 celery 확인


    $ ps aux|grep 'celery worker'   // celery의 경우
    $ ps aux|grep 'celery beat'     // celery beat의 경우

    
## 버그 리포트
- 만약 다음과 같은 에러가 발생한다면,
> AttributeError async

> KeyError async

kombu와 celery의 버전이 충돌하는 것이니, celery 버전을 4.2.1로 받아준다. [celery github에 올라온 이슈](https://github.com/celery/kombu/issues/870)