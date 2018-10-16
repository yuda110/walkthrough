유저 모델을 커스터마이징 했는데, request.user 가 AnonymousUser로 받아질 경우,

`settings.py`에 다음 추가

        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework.authentication.BasicAuthentication',
                'rest_framework.authentication.SessionAuthentication',
                'rest_framework.authentication.TokenAuthentication',
            )
        }