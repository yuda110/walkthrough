Django X PostgreSQL 연결
---

psycopg2 모듈 설치
```shell
pip install psycopg2
```


DATABASE 세팅

`settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_database',
        'USER': 'my_name',
        'PASSWORD': '1234567890',
        'HOST': '127.0.0.1',
    }
}
```

OperationalError
> 윈도우에서는 psycopg2 가 안 돌아감! 이건 리눅스 환경에서만 동작한다.
따라서 psycopg2-binary 모듈을 받아야 한다.

> USER에게 권한 주면 됨(pgadmin에서 유저 속성에서 Privileges 수정)
