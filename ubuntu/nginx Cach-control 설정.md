# nginx Cache-control

nginx의 sites-available에 있는 파일을 열고,

    $ cd /etc/nginx/sites-available
    $ sudo vi default


다음을 추가해준다.


        location ~* \.(?:jpg|jpeg|gif|png|ico|cur|gz|svg|svgz|mp4|ogg|ogv|webm|htc)$ {
          expires 1M;
          add_header Cache-Control "public";
        }
    
        location ~* \.(?:)$ {
          expires 30d;
          add_header Cache-Control "public";
        }
        
이렇게 하면 저 확장자에 대한 캐쉬를 30일동안 보관한다.