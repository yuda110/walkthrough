# postfix

###mailutils 설치
    $ sudo apt-get install mailutils

그럼 postfix도 함께 받아질텐데,
 
- General type of mail configuration: **Internet Site** 선택

- System mail name: 만약 `mars.example.com` 이라면 **example.com** 입력

### conf 파일 수정
    $ sudo vi /etc/postfix/main.cf
//

    # inet_interfaces = all
    inet_interfaces = loopback-only


### 재시작
    $ sudo service postfix restart

### 테스트
    $ echo "This is message line" | mail -s "This is the subject line" aydha0110@gmail.com

----
###에러 로그
    $tail -f /var/log/syslog | grep postfix