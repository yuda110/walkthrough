# nginx + gunicorn 셋업

- gunicorn 인스톨

        $ pip install Django gunicorn

- venv 켠 상태로
 
        $ source venv/bin/activate

- static 폴더 생성(settings.py에 STATIC_ROOT = os.path.join(BASE_DIR, 'static/') 있어야 함)

        $ python manage.py collectstatic

- nginx 설정 파일 수정

        $ cd /etc/nginx/sites-available
        $ sudo vi default
        
        
        // /etc/nginx/sites-available/default
        

        location /api/ {
            proxy_pass http://localhost:8001;
        }
        
        // certbot을 했다면 아랫부분에 또 적어줘야 함!
        
        location /api/ {
            proxy_pass http://localhost:8001;
        }


- epollo_backend 아래 가서

        $ cd epollo_backend
        $ gunicorn {project_name}.wsgi --bind=localhost:8001 --daemon
        

##추가 팁
- 안 되면 gunicorn 실행되고 있는지 확인

        $ ps -A

- gunicorn 끄고 싶으면

        $ kill {port}

- 포트 돌아가는 거 보려면

        $ sudo netstat -peanut

- nginx 다시 시작하려면

        $ sudo service nginx restart