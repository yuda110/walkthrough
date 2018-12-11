# nginx로 EC2 서버 올리고 도메인 설정하기

## 사전 준비
- 일단 EC2 인스턴스 생성
- puttygen으로 키 생성
- putty로 EC2 실행


- git 프로젝트 clone


## nginx 설치 및 셋업
- nginx 설치

        $ sudo apt-get update
        $ sudo apt-get install nginx

- nginx 설정파일 수정
 
        /etc/nginx/sites-available 에서 default든 뭐든.
        
        # root /var/www;
        root /home/ubuntu/{프로젝트 이름};

- nginx 재시작

        $ sudo service nginx restart


## 도메인 관리
- 퍼블릭 DNS **ec2-11-111-111.us-east-2.compute.amazonaws.com** 이런 주소로 되는지 확인

- godaddy의 DNS 설정으로 가서 레코드 수정한 뒤 도메인으로(http) 접속되는지 확인

    - 유형: CNAME
    -  이름: @
    - 값: ec2-11-111-111.us-east-2.compute.amazonaws.com
    - TTL: 1시간


- certbot 설정

        $ sudo apt-get update
        $ sudo apt-get install software-properties-common
        $ sudo add-apt-repository ppa:certbot/certbot
        $ sudo apt-get update
        $ sudo apt-get install python-certbot-nginx 

    그리고

        $ sudo certbot --nginx
        
    > No names were found in your configuration files. Please enter in your domain
    name(s) (comma and/or space separated)  (Enter 'c' to cancel): 이런 게 뜨면, 도메인 입력(ex. mysite.com)
    
    > Redirect 할거냐 말거냐 물어보면 '한다' 선택