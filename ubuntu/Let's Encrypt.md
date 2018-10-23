# Let's Encrypt

**HTTPS**를 웹에서 쓰려면 **CA**(Certificate Authority)에서 받은 인증서가 필요하다.

**Let's Encrypt**라는 사이트에서 SSL 인증서를 발급해주는데, 이는 **Certbot**이라는 프로그램을 통해 받을 수 있다. 



### DNS 설정 
godaddy에서 dns관리에서 유형 A (Alias)의 값을 Redirection Server의 ip로 변경하여 저장한다.

> 유형 CNAME 이름 ftp 값 @


### ubuntu

    $ sudo certbot --nginx -d example.com

이렇게 해서 `fullchain.pem`과 `privkey.pem`를 생성한다.

그리고 `/etc/nginx/conf.d` 아래 `example.com.conf` 파일 만들어서 아래 내용 삽입한다.

    server {
        listen       80;
        listen       443 ssl;
        
        server_name  mysite.com;
        return 301 $scheme://www.mysite.com$request_uri;
        ssl_certificate /etc/letsencrypt/live/mysite.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/mysite.com/privkey.pem;
    }

그 뒤, nginx 재시작

    $ sudo systemctl restart nginx