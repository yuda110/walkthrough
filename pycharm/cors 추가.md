# cors 추가

웹에서 127.0.0.1:8000 으로 불러온 api 가 안 될 때
> Failed to load http://127.0.0.1:8000/api/...../: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://localhost:8090' is therefore not allowed access.


**django-cors-headers**를 인스톨한 뒤,

- settings.py MIDDLEWARE 에 'corsheaders.middleware.CorsMiddleware' 추가

        MIDDLEWARE_CLASSES = (
            ...
            'corsheaders.middleware.CorsMiddleware',
            ...
        )

- INSTALLED_APPS 에도 'corsheaders' 추가

        INSTALLED_APPS = (
            'django.contrib.admin',
            'django.contrib.auth',
            ...
            'corsheaders',    # 'django-cors-headers' package
        )