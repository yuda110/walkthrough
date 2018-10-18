# celery beat 셋업

### django settings.py 수정
- **Celery Timezone** 추가(혹은 `celery.py` 에 추가해도 됨)

        CELERY_TIMEZONE = 'Asia/Seoul'
        CELERY_ENABLE_UTC=False


- **CELERY_BEAT_SCHEDULE** 추가

        CELERY_BEAT_SCHEDULE = {
            'create-every-sunday-morning': {
                'task': 'util.tasks.create_homework',
                'schedule': crontab(),
                'args': ()
            },
        }

### ubuntu에서 celery 실행
- venv 실행

        $ source /home/venv/platform_env/bin/activate

- 스케쥴 추가(--detach)

        $ celery beat -A {project_name} --detach

- celery 확인 

        $ celery -A {project_name} worker -l info

- celery stop

        $ ps aux|grep 'celery worker'   - celery의 경우
        $ ps aux|grep 'celery beat'     - celery beat의 경우
        $ sudo kill process_id